#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append('/data/project/ImageDT/imagedt/caffe/lib')
import json
import cv2
import caffe
import numpy as np

from fast_rcnn.config import cfg
from fast_rcnn.nms_wrapper import nms
from fast_rcnn.test import im_detect
from nms.py_cpu_nms import py_cpu_nms


class detection_net:
    def __init__(self, prototxt, caffemodel, classes, CONF_THRESH, GPUID, image_scale=None, an_scale=None,
                 an_ratio=None, base_size=None, rpn_min_size=None, image_filter=True, nms=0.1):

        self.classes = classes
        self.CONF_THRESH = CONF_THRESH
        self.an_scale = an_scale
        self.an_ratio = an_ratio
        self.base_size = base_size
        self.rpn_min_size = rpn_min_size
        self.image_filter = image_filter
        self.nms = nms
        self.GPUID = GPUID

        cfg.TEST.HAS_RPN = True
        if image_scale is not None:
            SCALES = int(image_scale.split('#')[0])
            MAX_SIZE = int(image_scale.split('#')[1])
            cfg.TEST.SCALES = (SCALES,)
            cfg.TEST.MAX_SIZE = MAX_SIZE

        if an_scale is not None and an_ratio is not None:
            cfg.AN_SCALES = self.an_scale
            cfg.AN_RATIO = self.an_ratio
        if base_size is not None:
            cfg.BASE_SIZE = self.base_size
        if rpn_min_size is not None:
            cfg.TEST.RPN_MIN_SIZE = self.rpn_min_size

        cfg.GPU_ID = self.GPUID
        caffe.set_mode_gpu()
        caffe.set_device(self.GPUID)

        self.net = caffe.Net(prototxt, caffemodel, caffe.TEST)

        print '\n\nLoaded network {:s}'.format(caffemodel)

        # # Warmup on a dummy image
        im = 128 * np.ones((500, 800, 3), dtype=np.uint8)
        for i in xrange(2):
            _, _ = im_detect(self.net, im)

    def detector(self, cnn_net, image):
        times = (1.0, 1.0)
        # if needresize:
        #     image, times = resize(image)

        scores, boxes = im_detect(cnn_net, image)

        NMS_THRESH = self.nms
        score_keeps = np.where(scores[:, 1:] > self.CONF_THRESH)
        detections = {}
        for ind, box_ind in enumerate(score_keeps[0]):
            cls_ind = score_keeps[1][ind] + 1
            cls = self.classes[cls_ind]

            cls_box = boxes[box_ind, 4:8]
            cls_score = scores[box_ind, cls_ind]
            try:
                dets = np.hstack((cls_box, cls_score, float(cls)))
            except:
                dets = np.hstack((cls_box, cls_score, 0))
            detections.setdefault(cls, [])
            detections[cls].append(dets)
        for cls in detections:
            dets = detections[cls]
            if dets:
                dets = np.array(dets).astype(np.float32)
                keep = py_cpu_nms(dets, NMS_THRESH)
                if len(keep) > 0:
                    detections[cls] = dets[keep, :].tolist()
                else:
                    detections[cls] = dets.tolist()
        return detections, times

    def reco(self, image, image_scale=None):
        rst = []

        if image is None:
            print 'image error'
            return rst

        if self.image_filter:
            if image.shape[0] / float(image.shape[1]) > 6 or image.shape[0] / float(image.shape[1]) < 0.16 or \
                            image.shape[0] < 30 or image.shape[1] < 30:
                print 'shape error'
                return rst

        cfg.GPU_ID = self.GPUID
        caffe.set_mode_gpu()
        caffe.set_device(self.GPUID)

        # 调用Caffe
        detections, times = self.detector(self.net, image)

        # 转为JSON
        # outputList = []
        if detections is not None:
            for cls in detections:
                for box in detections[cls]:
                    if self.CONF_THRESH < box[4]:
                        if box[5] < 0:
                            continue
                        box[1] = int(box[1] * times[1])
                        box[3] = int(box[3] * times[1])
                        box[0] = int(box[0] * times[0])
                        box[2] = int(box[2] * times[0])
                        box[5] = int(box[5])
                        if box[4] == 6763:
                            box[4] = 6762
                        # box[4] = round(box[4], 4)
                        box.remove(box[4])
                        rst.append(box)
        return rst
