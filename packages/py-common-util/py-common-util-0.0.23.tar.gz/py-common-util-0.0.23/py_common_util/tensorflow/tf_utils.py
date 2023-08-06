# coding: utf-8 or # -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
# 解决Warning：Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"


class TFUtils:

    @staticmethod
    def total_num_batch(num_total, batch_size, allow_smaller_final_batch=False):
        num_batch = num_total // batch_size
        if allow_smaller_final_batch:
            if num_total > (num_batch * batch_size):
                return num_batch + 1
        else:
            # 舍去最后不能够成1批的剩余训练数据部分
            return num_batch

    @staticmethod
    def batchify_np_data_label(tuple_np_data_label, batch_size, allow_smaller_final_batch=False):
        """
        :param tuple_np_data_label:
        :param batch_size:
        :return:
        使用：
        ......
        batched_data_label = TFUtils.batchify_np_data_label(np_test_data, parser_args.eval_batch_size)
        for batch_idx, (data, label) in enumerate(batched_data_label):
            data, label = ......
        ......
        """
        data = tuple_np_data_label[0][0]
        label = tuple_np_data_label[0][1]
        num_batch = TFUtils.total_num_batch(data.shape[0], batch_size, allow_smaller_final_batch)
        data = data[:num_batch*batch_size]
        label = label[:num_batch*batch_size]
        batched_data = np.split(data, num_batch)
        batched_label = np.split(label, num_batch)
        return list(zip(batched_data, batched_label))

    @staticmethod
    def l2_normalization(x):
        axis = TFUtils.get_axis(x)
        return tf.nn.l2_normalize(x, dim=axis)

    @staticmethod
    def std_normalization(x):
        axis = TFUtils.get_axis(x)
        batch_mean, batch_var = tf.nn.moments(x, axis, name='moments')
        return tf.divide(tf.subtract(x, batch_mean), tf.sqrt(batch_var + TFUtils.get_small_epsilon()))

    @staticmethod
    def get_small_epsilon():
        return 1e-3

    @staticmethod
    def get_axis(x):
        return list(range(len(x.shape) - 1))

    @staticmethod
    def read_mnist_from_local(data_dir="../../dataset/MNIST_data/"):
        """e.g. data_dir=sys.path[0] + '/../../dataset/MNIST_data/'"""
        import tensorflow.examples.tutorials.mnist.input_data as mnist_input_data
        mnist = mnist_input_data.read_data_sets(data_dir, one_hot=True)
        print("MNIST loaded!")
        return mnist

    @staticmethod
    def tf_l2_normal_weight_biases(n_hidden, n_classes, num_hidden=1):
        weights = tf.Variable(tf.nn.l2_normalize(tf.random_normal([num_hidden*n_hidden, n_classes]), [0, 1]))
        biases = tf.Variable(tf.random_normal([n_classes]))
        return weights, biases

    @staticmethod
    def tf_random_normal_weight_biases(n_hidden, n_classes, num_hidden=1):
        weights = tf.Variable(tf.random_normal([num_hidden*n_hidden, n_classes]))
        biases = tf.Variable(tf.random_normal([n_classes]))
        return weights, biases

    @staticmethod
    def tf_truncate_normal_weight_biases(n_hidden, n_classes, num_hidden=1):
        weights = tf.Variable(tf.truncated_normal([num_hidden*n_hidden, n_classes], stddev=.075, seed=1234, name='final_weights'))
        biases = tf.Variable(tf.random_normal([n_classes]))
        return weights, biases

    @staticmethod
    def dense_to_one_hot(labels_dense, num_classes=10):
        """
        Convert class labels from scalars to one-hot vectors.
        labels_dense e.g. np.asarray([5, 0, 3, 2, 4, 9, 6, 7, 2, 1, 0, 0, 1, 4, 5, 2, 5, 6, 7, 8])
        as example: dense_to_one_hot(np.asarray([8]), 10)
        ref to: tensorflow/contrib/learn/python/learn/datasets/mnist.py#dense_to_one_hot()
        """
        num_labels = labels_dense.shape[0]
        index_offset = np.arange(num_labels) * num_classes
        labels_one_hot = np.zeros((num_labels, num_classes))
        labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
        return labels_one_hot

    @staticmethod
    def one_hot_to_dense(labels_dense_one_hot=[]):
        '''
        for example:
        one_hot_to_dense([ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.])
        result index is: [1], and the result shuld be: index+1
        one_hot_to_dense([ 0.  0.  0.  1.  0.  0.  0.  0.  0.  0.])
        result index is: [3], and the result shuld be: index+1
        '''
        if np.asarray(labels_dense_one_hot.shape).size <= 1:
            return labels_dense_one_hot
        with tf.Session() as sess:
            return sess.run(tf.argmax(labels_dense_one_hot, 1))

    @staticmethod
    def average(pixel):
        # #ref to :https://samarthbhargav.wordpress.com/2014/05/05/image-processing-with-python-rgb-to-grayscale-conversion/
        # #1.convert RGB image to gray image
        # return (pixel[0] + pixel[1] + pixel[2]) / 3
        # #2.using numpy average
        # #3.G = R*0.299 + G*0.587 + B*0.114
        return 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]

    @staticmethod
    def cycle(iterable):
        """
        e.g.
        from neural_networks.tf_utils import TFUtils
        ...
        iter = TFUtils.cycle([0,2,3,1])
        next(iter) -> 0,next(iter) -> 2,...
        :param iterable:
        :return:
        """
        from itertools import cycle
        return cycle(iterable)

    @staticmethod
    def datetime_to_int(datetime):
        import time
        return int(time.mktime(datetime.timetuple()))

    @staticmethod
    def int_to_datetime(datetime_int):
        from datetime import datetime
        return datetime.fromtimestamp(datetime_int)

    @staticmethod
    def str_to_datetime(datetime_str, format="%Y%m%d%H%M%S"):
        from datetime import datetime
        return datetime.strptime(datetime_str, format)

    @staticmethod
    def datetime_to_str(date_time, format="%Y%m%d%H%M%S"):
        from datetime import datetime
        return date_time.strftime(format)  # 转成字面整型字符串, e.g. date: 2009-12-08 16:34:00 -> '20091208163400'

    @staticmethod
    def datetime_now():
        from datetime import datetime
        return datetime.now()

    @staticmethod
    def print_tf_version():
        print("Current Tensorflow Version: " + tf.__version__)

    @staticmethod
    def np_to_tensor(np_data):
        return tf.convert_to_tensor(np_data)


    @staticmethod
    def cuda_is_available():
        return False



