# coding=utf-8
import os
import sys
import yaml
import numpy as np
from ast import literal_eval
from .detection_net import detection_net
from ..lib.fast_rcnn.test import vis_detections


class Detector(object):
    def __init__(self, model_name=None):
        super(Detector, self).__init__()
        self._config_path = self._absolute_path('/ssd_data/model_config/mod_config.yaml')
        self.model_name = model_name or 'ocr_detect'
        self._load()

    def _absolute_path(self, path):
        return os.path.join(os.path.dirname(__file__), path)

    def _load(self):
        with open(self._config_path, 'r') as f:
            self.model_conf = yaml.load(f)[self.model_name]

        root_dir = self.model_conf['root_dir']
        prototxt = self._join_path(root_dir, self.model_conf['prototxt'])
        caffemodel = self._join_path(root_dir, self.model_conf['caffemodel'])
        classes = self._get_class(self._join_path(root_dir, self.model_conf['classes']))
        # os.environ["CUDA_VISIBLE_DEVICES"] = str(self.model_conf['GPUID'])
        self.detection_net_runner = detection_net(prototxt, caffemodel, classes, self.model_conf['confThresh'],
                                             self.model_conf['GPUID'], self.model_conf['image_scale'],
                                             an_scale=self.model_conf['an_scale'], an_ratio=self.model_conf['an_ratio'])
        print("<<<<<<<<<<<<< load classify model {0} >>>>>>>>>>>>>>".format(self.model_name))

    def _join_path(self, root_dir, add_path):
        return os.path.join(root_dir, add_path)

    def _get_class(self, class_path):
        with open(class_path, 'r') as f:
            return literal_eval(f.read())

    def detect(self, image):
        return self.detection_net_runner.reco(image)
