# coding: utf-8

import sys
import os
import cv2
import yaml
import caffe
import traceback
import numpy as np
from ast import literal_eval


class classification_net:
    def __init__(self, prototxt, caffemodel, classifyLabel, GPUID, mean_file, batchsize=16):
        self.LABELS = {}
        for line in open(classifyLabel):
            self.LABELS[line.strip().split("\t")[1].strip()] = line.strip()

        caffe.set_mode_gpu()
        caffe.set_device(GPUID)

        self.net = caffe.Net(str(prototxt), str(caffemodel), caffe.TEST)

        # create transformer for the input called 'data'
        # new_shape = (len(chunk),) + tuple(dims)
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2, 0, 1))  # move image channels to outermost dimension
        if mean_file is None:
            self.transformer.set_mean('data', np.array([104, 117, 124]))  # subtract the dataset-mean value in each channel
        elif mean_file is 'zero':
            self.transformer.set_mean('data', np.array([0, 0, 0]))
        else:
            blob = caffe.proto.caffe_pb2.BlobProto()

            data = open(mean_file, 'rb').read()
            blob.ParseFromString(data)
            arr = np.array(caffe.io.blobproto_to_array(blob))[0].mean(1).mean(1)
            self.transformer.set_mean('data', arr)

        print '\n\nLoaded network {:s}'.format(caffemodel)

    from imagedt.decorator import time_cost
    @time_cost
    def classify(self, images):
        # 图像识别
        try:
            classifcations = []
            for index, img in enumerate(images):
                self.net.blobs['data'].data[index] = self.transformer.preprocess('data', img)
            # perform classification
            self.net.forward()
            # multi batchsize
            infos = []
            for ite in range(len(images)):
                output_prob = self.net.blobs['softmax'].data[ite].flatten()# obtain the output probabilities
                top_ind = output_prob.argsort()[::-1][0] # argsort 从小到大排列
                infos.append([output_prob[top_ind]] + self.LABELS[str(top_ind)].split('\t'))
            return infos
        except:
            traceback.print_exc()


class Classifier(object):
    def __init__(self, model_name=None):
        super(Classifier, self).__init__()
        self._config_path = self._absolute_path('/ssd_data/model_config/mod_config.yaml')
        self.model_name = model_name or 'sku_classify'
        self._load()
        self.get_model()

    def _absolute_path(self, path):
        return os.path.join(os.path.dirname(__file__), path)

    def _load(self):
        with open(self._config_path, 'r') as f:
            self.model_conf = yaml.load(f)[self.model_name]

    def _join_path(self, root_dir, add_path):
        return os.path.join(root_dir, add_path)

    def _get_class(self, class_path):
        with open(class_path, 'r') as f:
            return literal_eval(f.read())

    def get_model(self):
        model_root = self.model_conf['root_dir']
        prototxt = os.path.join(model_root, self.model_conf['prototxt'])
        caffemodel = os.path.join(model_root, self.model_conf['caffemodel'])
        classesPath = os.path.join(model_root, self.model_conf['classes'])
        GPUID = self.model_conf['GPUID']
        self.classification_net_runner = classification_net(prototxt, caffemodel, classesPath, GPUID, None)
        print("<<<<<<<<<<<<< load classify model {0} >>>>>>>>>>>>>>".format(self.model_name))

    def classify(self, img):
        return self.classification_net_runner.classify(img)

