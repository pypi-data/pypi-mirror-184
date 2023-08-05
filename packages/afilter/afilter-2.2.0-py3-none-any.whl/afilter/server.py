import io
import cv2
import sys
import grpc
import logging
import argparse
import numpy as np
from PIL import Image
from datetime import datetime
from functools import partial
from concurrent import futures
import tritonclient.grpc as grpcclient
import tritonclient.http as httpclient

from afilter.protos import afilter_pb2
from afilter.protos import afilter_pb2_grpc
from afilter.utils.transform import imnormalize, image_to_base64, base64_to_image, image_to_bytes
from afilter.utils.check_health import HealthServicer, _Watcher, _watcher_to_send_response_callback_adapter
from tritonclient.utils import InferenceServerException
from vspscripts.alignment.PyMatch import ICpair_Matching

try:
    from mmseg.datasets.vsp_cam import VSP_CAMDataset
    CLASSES = VSP_CAMDataset.CLASSES
except Exception as e:
    CLASSES = ('background', 'island', 'nick', 'open', 'protrusion', 'short')

if sys.version_info >= (3, 0):
    import queue
else:
    import Queue as queue

OK = True
NG = False

# Callback function used for async_stream_infer()
def completion_callback(user_data, result, error):
    # passing error raise and handling out
    user_data._completed_requests.put((result, error))

class UserData:

    def __init__(self):
        self._completed_requests = queue.Queue()

user_data = UserData()

def get_class_mask(defect, mod='bytes'):
    classes = np.array(CLASSES)

    class_mask = []
    for label, name in enumerate(classes):
        if label != 0 and name != '':
            table = [0]*256
            table[label] = 1
            mask = defect.point(table, '1')
            if mask.getextrema() != (0, 0):
                print('[{}]: {}'.format(label, name))
                if mod == 'bytes':
                    mask_data = image_to_bytes(mask)
                elif mod == 'base64':
                    mask_data = image_to_base64(mask)
                mask_Onemat = afilter_pb2.Onemat(rows=mask.size[1], cols=mask.size[0], \
                    d_type=mod, mat_data=mask_data)
                class_mask.append(afilter_pb2.Onedefect(name=name, mask=mask_Onemat))

    return class_mask

def get_concat(cam_data, cad_data, is_matched=True):
    # cam = Image.frombytes(mode="RGBA", size=(cam_data.rows,cam_data.cols), data=cam_data.mat_data, decoder_name="raw")
    # cam = Image.open(io.BytesIO(cam_data.mat_data))
    if cam_data.d_type == 'base64':
        cam = base64_to_image(cam_data.mat_data)
    elif cad_data.d_type == 'bytes':
        cam = Image.open(io.BytesIO(cam_data.mat_data))
    if is_matched:
        # cad = Image.open(io.BytesIO(cad_data.mat_data))
        if cad_data.d_type == 'base64':
            cad = base64_to_image(cad_data.mat_data)
        elif cad_data.d_type == 'bytes':
            cad = Image.open(io.BytesIO(cad_data.mat_data))
        cam, cad, _, M_Sim, score, (left_top, right_bottom) = ICpair_Matching(cam, cad, None, 600)
        # cam = cam / 255.0
        # cam = np.expand_dims(cam, axis=0)
        # cam = np.transpose(cam, axes=[0, 3, 1, 2])
        # cad = cad / 255.0
        # cad = np.expand_dims(cad, axis=0)
        # cad = np.expand_dims(cad, axis=0)
    else:
        if cad_data.d_type == 'base64':
            cad = base64_to_image(cad_data.mat_data).convert('L')
        elif cad_data.d_type == 'bytes':
            cad = Image.open(io.BytesIO(cad_data.mat_data)).convert('L')
        cam = cam.resize((600, 600), Image.ANTIALIAS)
        cam = cv2.cvtColor(np.asarray(cam), cv2.COLOR_RGB2BGR)
        cad = cad.resize((600, 600), Image.ANTIALIAS)
        cad = cv2.cvtColor(np.asarray(cad), cv2.COLOR_RGB2BGR)
    mean=[123.675, 116.28, 103.53]
    std=[58.395, 57.12, 57.375]
    to_rgb = True
    mean = np.array(mean, dtype=np.float32)
    std = np.array(std, dtype=np.float32)
    cam = imnormalize(cam, mean, std, to_rgb)
    # cam = cam.convert("RGB")
    # cam = np.asarray(cam)
    # cam = cam / 255.0
    if len(cad.shape) < 3:
        cad = np.expand_dims(cad, -1)
    cad = cad.transpose(2, 0, 1)
    cam = cam.transpose(2, 0, 1)
    # cam = np.transpose(cam, axes=[0, 3, 1, 2])
    # cam = cam.astype(np.float32)

    # cad = Image.frombytes(mode="RGBA", size=(cad_data.rows,cad_data.cols), data=cad_data.mat_data, decoder_name="raw").convert('L')
    # cad = np.asarray(cad)
    # cad = cad / 255.0
    # cad = np.expand_dims(cad, axis=0)
    # cam = np.expand_dims(cam, axis=0)
    cam_cad = np.append(cam, cad, axis = 0)
    cam_cad = np.expand_dims(cam_cad, axis=0)
    return cam_cad.astype(np.float32), (left_top, right_bottom)

def get_defects(protocol, triton_client, model_name, requests, set_async):
    REQ_NUM = len(requests)
    inputs_data, crop_bboxes = [], []
    for request in requests:
        input_data, (left_top, right_bottom) = get_concat(request.cam_data, request.cad_data)
        inputs_data.append(input_data)
        crop_bboxes.append((left_top, right_bottom))
    outputs_data = []
    try:
        if protocol =='grpc':
            inputs = [[grpcclient.InferInput(f'input', [1, 4, 600, 600], "FP32")] for i in range(REQ_NUM)]
            [inputs[i][0].set_data_from_numpy(inputs_data[i]) for i in range(REQ_NUM)]
            outputs = [[grpcclient.InferRequestedOutput(f'output')] for i in range(REQ_NUM)]
            if set_async:
                [triton_client.async_infer(model_name=model_name,
                                            inputs=inputs[i],
                                            callback=partial(completion_callback, user_data),
                                            outputs=outputs[i]) for i in range(REQ_NUM)]
                # outputs_data=user_data._completed_requests.get()
                processed_count = 0
                while processed_count < REQ_NUM:
                    (response, error) = user_data._completed_requests.get()
                    processed_count += 1
                    if error is not None:
                        print("Triton gRCP inference failed: " + str(error))
                        sys.exit(1)
                    outputs_data.append(response)
                # results = [output_data.as_numpy('output') for output_data in outputs_data]
            else:
                outputs_data = [triton_client.infer(model_name=model_name,
                                                    inputs=inputs[i],
                                                    outputs=outputs[i]) for i in range(REQ_NUM)]
        else:
            inputs = [[httpclient.InferInput('input', [1, 4, 600, 600], "FP32")] for i in range(REQ_NUM)]
            [inputs[i][0].set_data_from_numpy(inputs_data[i], binary_data=True) for i in range(REQ_NUM)]
            outputs = [[httpclient.InferRequestedOutput('output', binary_data=True)] for i in range(REQ_NUM)]
            if set_async:
                async_outputs = [triton_client.async_infer(model_name=model_name,
                                                        inputs=inputs[i],
                                                        outputs=outputs[i]) for i in range(REQ_NUM)]
                [outputs_data.append(async_output.get_result()) for async_output in async_outputs]
            else:
                outputs_data = [triton_client.infer(model_name=model_name,
                                                    inputs=inputs[i],
                                                    outputs=outputs[i]) for i in range(REQ_NUM)]
        results = [output_data.as_numpy('output') for output_data in outputs_data]
    except InferenceServerException as e:
            print("inference failed: " + str(e))
            sys.exit(1)

    return [Image.fromarray(np.squeeze(result.astype('uint8')), mode='L') for result in results], crop_bboxes

def get_OKNG(defect, crop_bbox, mod='bytes'):
    class_mask = get_class_mask(defect, mod)
    crop_bbox = afilter_pb2.Bbox(left=int(crop_bbox[0][0]), top=int(crop_bbox[0][1]), \
                                 right=int(crop_bbox[1][0]), bottom=int(crop_bbox[1][1]))
    if isinstance(class_mask, list) and len(class_mask) == 0:
        return afilter_pb2.OneReply(ok_ng=OK, crop_bbox=crop_bbox)
    else:
        return afilter_pb2.OneReply(ok_ng=NG, crop_bbox=crop_bbox, defect=class_mask)

class FilterServicer(afilter_pb2_grpc.FilterServicer, HealthServicer):
    def __init__(self,
                 protocol,
                 url,
                 model_name,
                 set_async = True):
        self.protocol = protocol
        self.url = url
        self.model_name = model_name
        self.set_async = set_async
        try:
            if self.protocol.lower() == "grpc":
                self.triton_client = grpcclient.InferenceServerClient(url=self.url+':18001')
            else:
                self.triton_client = httpclient.InferenceServerClient(url=self.url+':18000',
                    concurrency=100 if self.set_async == True else 1)
        except Exception as e:
            print("context creation failed: " + str(e))
            sys.exit()

        super(FilterServicer, self).__init__()

    def FilterFunc(self, requests: afilter_pb2.FilterRequest, context) -> afilter_pb2.FilterReply:
        reply = []
        # REQ_NUM = len(requests.request)
        infer_start_time = str(datetime.now())
        defects, crop_bboxes = get_defects(self.protocol.lower(), self.triton_client, 
                                           self.model_name, requests.request, set_async = True)
        for defect, crop_bbox in zip(defects, crop_bboxes):
            reply.append(get_OKNG(defect, crop_bbox, mod=requests.request[0].cam_data.d_type))
        # REQ_NUM = len(requests.request)
        # res = Image.new('L', (600, 600), 255)
        # crop_bboxes = [((0,0),(600,600))]
        # defects = [res]*REQ_NUM
        # for defect, crop_bbox in zip(defects, crop_bboxes):
        #     crop_bbox = afilter_pb2.Bbox(left=int(crop_bbox[0][0]), top=int(crop_bbox[0][1]), \
        #                          right=int(crop_bbox[1][0]), bottom=int(crop_bbox[1][1]))
        #     reply.append(afilter_pb2.OneReply(ok_ng=OK, crop_bbox=crop_bbox))
        infer_end_time = str(datetime.now())
        info = afilter_pb2.Info(infer_start_time=infer_start_time,
                                infer_end_time=infer_end_time)
        return afilter_pb2.FilterReply(reply=reply, info=info)

    def FilterChat(self, requests_iterator, context):
        # infer_start_time = str(datetime.now())
        for request in requests_iterator:
            defects, crop_bboxes = get_defects(self.protocol.lower(), self.triton_client, 
                                               self.model_name, [request], set_async = True)
            for defect, crop_bbox in zip(defects, crop_bboxes):
                yield get_OKNG(defect, crop_bbox, mod=request.cam_data.d_type)
            # res = Image.new('L', (600, 600), 255)
            # crop_bboxes = [((0,0),(600,600))]
            # defects = [res]
            # for defect, crop_bbox in zip(defects, crop_bboxes):
            #     crop_bbox = afilter_pb2.Bbox(left=int(crop_bbox[0][0]), top=int(crop_bbox[0][1]), \
            #                      right=int(crop_bbox[1][0]), bottom=int(crop_bbox[1][1]))
            #     yield afilter_pb2.OneReply(ok_ng=OK, crop_bbox=crop_bbox)
        # infer_end_time = str(datetime.now())
        # info = afilter_pb2.Info(infer_start_time=infer_start_time,
        #                         infer_end_time=infer_end_time)
        # return 
            
    
    def FilterCheck(self, request, context):
        response = self.Check(request, context)
        if response.status == afilter_pb2.HealthCheckResponse.SERVING:
            server_live = self.triton_client.is_server_live()
            server_ready = self.triton_client.is_server_ready()
            model_ready = self.triton_client.is_model_ready(self.model_name)
            if server_live and server_ready and model_ready:
                return afilter_pb2.HealthCheckResponse(status=afilter_pb2.HealthCheckResponse.SERVING)
            else:
                return afilter_pb2.HealthCheckResponse(status=afilter_pb2.HealthCheckResponse.NOT_SERVING)
        else:
            return response

    def FilterWatch(self, request, context, send_response_callback=None):
        blocking_watcher = None
        if send_response_callback is None:
            # The server does not support the experimental_non_blocking
            # parameter. For backwards compatibility, return a blocking response
            # generator.
            blocking_watcher = _Watcher()
            send_response_callback = _watcher_to_send_response_callback_adapter(
                blocking_watcher)
        service = request.service
        with self._lock:
            status = self._server_status.get(service)
            if status is None:
                status = afilter_pb2.HealthCheckResponse.SERVICE_UNKNOWN  # pylint: disable=no-member
            elif status == afilter_pb2.HealthCheckResponse.SERVING:
                server_live = self.triton_client.is_server_live()
                server_ready = self.triton_client.is_server_ready()
                model_ready = self.triton_client.is_model_ready(self.model_name)
                if server_live and server_ready and model_ready:
                    status =afilter_pb2.HealthCheckResponse.SERVING
                else:
                    status =afilter_pb2.HealthCheckResponse.NOT_SERVING
            send_response_callback(
                afilter_pb2.HealthCheckResponse(status=status))
            if service not in self._send_response_callbacks:
                self._send_response_callbacks[service] = set()
            self._send_response_callbacks[service].add(send_response_callback)
            context.add_callback(
                self._on_close_callback(send_response_callback, service))
        return blocking_watcher

def aivs_serve(protocol, url, model_name):
    MAX_MESSAGE_LENGTH = 256*1024*1024 # 256MB
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
               ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
               ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
    afilter_pb2_grpc.add_FilterServicer_to_server(
        FilterServicer(protocol, url, model_name, set_async = True), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
        '--triton_url',
        type=str,
        required=False,
        default='localhost',
        help='Inference server URL. Default is localhost.')
    parser.add_argument('-i',
        '--protocol',
        type=str,
        required=False,
        default='gRPC',
        help='Protocol (HTTP/gRPC) used to communicate with ' +
        'the inference service. Default is HTTP.')
    parser.add_argument('-m',
        '--model_name',
        default='segformer-b4',
        help='The model name in the server')
    args = parser.parse_args()

    logging.basicConfig()
    aivs_serve(args.protocol, args.triton_url, args.model_name)
