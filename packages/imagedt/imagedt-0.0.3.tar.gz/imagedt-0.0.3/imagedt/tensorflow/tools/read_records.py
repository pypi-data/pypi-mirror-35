# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function


import tensorflow as tf


def read_records(tfrecords_file):  
    '''''read and decode tfrecord file, generate (image, label) batches 
    '''
    # make an input queue from the tfrecord file  
    filename_queue = tf.train.string_input_producer([tfrecords_file])  
    reader = tf.TFRecordReader()  
    #从文件中独处一个样例。也可以使用read_up_to函数一次性读取多个样例  
    _, serialized_example = reader.read(filename_queue)  
    #解析每一个元素。如果需要解析多个样例，可以用parse_example函数  
    img_features = tf.parse_single_example(  
        serialized_example,  
        features={  
            'image/class/label': tf.FixedLenFeature([], tf.int64),
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/encoded': tf.FixedLenFeature([], tf.string),  
        })
    #tf.decode_raw可以将字符串解析成图像对应的像素数组  
    # image = tf.decode_raw(img_features['image/encoded'], tf.uint8)  
    image = tf.image.decode_jpeg(img_features['image/encoded'], channels=3)
    label = tf.cast(img_features['image/class/label'], tf.int32)
    height = tf.cast(img_features['image/height'], tf.int32)
    width = tf.cast(img_features['image/width'], tf.int32)

    with tf.Session() as sess:
        # 启动多线程
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        # 因为我这里只有 2 张图片，所以下面循环 2 次
        for i in range(2):
            # 获取一张图片和其对应的类型
            images, labels, height, width = sess.run([image, label, height, width])
            #img = tf.reshape(img, [224, 224, 1])
            edge = max(height, width)
            Image.fromarray(np.reshape(images, [edge, edge, 3])).show()
            import pdb
            pdb.set_trace()

    return image, label


import numpy as np
import tensorflow as tf
from PIL import Image


def visual_records(tfrecords_path):  
    # make an input queue from the tfrecord file  
    filename_queue = tf.train.string_input_producer([tfrecords_path])  
    #创建一个reader来读取TFRecord文件  
    reader = tf.TFRecordReader()  
    #从文件中独处一个样例。也可以使用read_up_to函数一次性读取多个样例  
    _, serialized_example = reader.read(filename_queue)  
    #解析每一个元素。如果需要解析多个样例，可以用parse_example函数  
    img_features = tf.parse_single_example(  
        serialized_example,  
        features={  
            'image/class/label': tf.FixedLenFeature([], tf.int64),
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/encoded': tf.FixedLenFeature([], tf.string),  
        })  
    #tf.decode_raw可以将字符串解析成图像对应的像素数组  
    # image = tf.decode_raw(img_features['image/encoded'], tf.uint8)  
    image = tf.image.decode_jpeg(img_features['image/encoded'], channels=3)
    label = tf.cast(img_features['image/class/label'], tf.int32)
    height = tf.cast(img_features['image/height'], tf.int32)
    width = tf.cast(img_features['image/width'], tf.int32)

    with tf.Session() as sess:
      # 启动多线程
      coord = tf.train.Coordinator()
      threads = tf.train.start_queue_runners(sess=sess, coord=coord)
      for i in range(2):
        # 获取一张图片和其对应的类型
        images, labels, height, width = sess.run([image, label, height, width])
        Image.fromarray(np.reshape(images, [height, width, 3])).show()
        exit()
