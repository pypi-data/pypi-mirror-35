# coding: utf-8 or # -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
from py_common_util.tensorflow.tf_utils import TFUtils
"""
TensorFlow全新的数据读取方式：Dataset API入门教程  https://zhuanlan.zhihu.com/p/30751039
tensorflow入门：tfrecord 和tf.data.TFRecordDataset https://blog.csdn.net/yeqiustu/article/details/79793454
tensorflow中的dataset http://d0evi1.com/tensorflow/datasets/
"""


class TFRecordsUtils:

    @staticmethod
    def bytes_feature(value):
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

    @staticmethod
    def int64_feature(value):
        value = value if hasattr(value, "__len__") else [value]
        return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

    """
    e.g. values = [[1, 3],[2, 4],[3, 5]]
    """
    @staticmethod
    def int64_feature_list(values):
        return tf.train.FeatureList(feature=[tf.train.Feature(int64_list=tf.train.Int64List(value=values[i])) for i in range(len(values))])

    @staticmethod
    def float_feature(value):
        value = value if hasattr(value, "__len__") else [value]
        return tf.train.Feature(float_list=tf.train.FloatList(value=value))

    """
    e.g. values = [[1.1, 3.0],[-2.0, 4.1],[3.2, 5.6]]
    """
    @staticmethod
    def float_feature_list(values):
        return tf.train.FeatureList(feature=[tf.train.Feature(float_list=tf.train.FloatList(value=values[i])) for i in range(len(values))])

    """
    dict, e.g. {"feature": bytes_feature(b''), "label": int64_feature(10)}
    """
    @staticmethod
    def build_tf_example_string(dict):
        return tf.train.Example(features=tf.train.Features(feature=dict)).SerializeToString()

    @staticmethod
    def build_tf_sequence_example_string(context_dict, feature_lists_dict):
        return tf.train.SequenceExample(
            context=tf.train.Features(feature=context_dict),
            feature_lists=tf.train.FeatureLists(feature_list=feature_lists_dict)
        ).SerializeToString()

    """
    注意结束应调用writer.close()
    with get_writer(path) as writer:
        xxx
    """
    @staticmethod
    def get_writer(tfrecords_file_path):
        return tf.python_io.TFRecordWriter(tfrecords_file_path)

    @staticmethod
    def parse_dataset(tfrecords_files, parse_example_fn):
        return tf.data.TFRecordDataset(tfrecords_files).map(parse_example_fn)

    @staticmethod
    def write_summary(tfrecords_file_path, category='image', channels=1, height=0, width=0, total_count=0,
            train_count=0, valid_count=0, test_count=0, num_classes=0,
            should_use_labels=False, data_is_normalized=False,
            using_shuffle_batch=False, remark=''):
        with TFRecordsUtils.get_writer(tfrecords_file_path) as writer:
            summary_example = tf.train.Example(features=tf.train.Features(feature={
                'feature_info': TFRecordsUtils.bytes_feature(b'0:feature_info(string),1:category(string),2:channels(int),3:height(int),4:width(int),5:total_count(int),6:train_count(int),7:valid_count(int),8:test_count(int),9:num_classes(int),10:should_use_labels(int),11:data_is_normalized(int),12:using_shuffle_batch(int),13:remark(string)'),
                'category': TFRecordsUtils.bytes_feature(bytes(category, encoding="utf8")),
                'channels': TFRecordsUtils.int64_feature(channels),
                'height': TFRecordsUtils.int64_feature(height),
                'width': TFRecordsUtils.int64_feature(width),
                'total_count': TFRecordsUtils.int64_feature(total_count),
                'train_count': TFRecordsUtils.int64_feature(train_count),
                'valid_count': TFRecordsUtils.int64_feature(valid_count),
                'test_count': TFRecordsUtils.int64_feature(test_count),
                'num_classes': TFRecordsUtils.int64_feature(num_classes),
                'should_use_labels': TFRecordsUtils.int64_feature(1 if should_use_labels else 0),    # 是否使用多标签(e.g. [1,2])：true-1, false-0
                'data_is_normalized': TFRecordsUtils.int64_feature(1 if data_is_normalized else 0),  # 数据是否已被正则化：true-1, false-0
                'using_shuffle_batch': TFRecordsUtils.int64_feature(1 if using_shuffle_batch else 0),  # 训练模型时是否使用shuffle batch读tfrecords的数据
                'remark': TFRecordsUtils.bytes_feature(bytes(remark, encoding="utf8"))
            }))
            writer.write(summary_example.SerializeToString())

    @staticmethod
    def serialize_data_to_string(np_data_raw=[[0.0, 0.0], [0.0, 0.0]], labels=[1, 2]):
        record_example = tf.train.SequenceExample(
            context=tf.train.Features(feature={
                "feature_info": TFRecordsUtils.bytes_feature(b'data_raw_bytes([byte]),label(int),data_raw([[float]])'),
                'data_raw_bytes': TFRecordsUtils.bytes_feature(np_data_raw.tobytes()),
                "labels": TFRecordsUtils.int64_feature(labels)
            }),
            feature_lists=tf.train.FeatureLists(feature_list={
                "data_raw": TFRecordsUtils.float_feature_list([[0.0]])
            })
        )
        return record_example.SerializeToString()

    @staticmethod
    def read_summary(tfrecords_file_path):
        """
        :param tfrecords_file_path:
        :return:
        usage:
            tuple_summary = TFRecordsUtils.read_summary("xxx.tfrecords")
            print(tuple_summary[0]) # index 0 to feature_info
        """
        num_filename_queue = tf.train.string_input_producer([tfrecords_file_path])
        key, serialized_example = tf.TFRecordReader().read(num_filename_queue)
        features = tf.parse_single_example(serialized_example,
                                           features={
                                               'feature_info': tf.FixedLenFeature([], tf.string),
                                               'category': tf.FixedLenFeature([], tf.string),
                                               'channels': tf.FixedLenFeature([], tf.int64),
                                               'height': tf.FixedLenFeature([], tf.int64),
                                               'width': tf.FixedLenFeature([], tf.int64),
                                               'total_count': tf.FixedLenFeature([], tf.int64),
                                               'train_count': tf.FixedLenFeature([], tf.int64),
                                               'valid_count': tf.FixedLenFeature([], tf.int64),
                                               'test_count': tf.FixedLenFeature([], tf.int64),
                                               'num_classes': tf.FixedLenFeature([], tf.int64),
                                               'should_use_labels': tf.FixedLenFeature([], tf.int64),
                                               'data_is_normalized': tf.FixedLenFeature([], tf.int64),
                                               'using_shuffle_batch': tf.FixedLenFeature([], tf.int64),
                                               'remark': tf.FixedLenFeature([], tf.string)
                                           })
        with tf.Session() as sess:
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(coord=coord, sess=sess)
            try:
                tfrecord_feature_info, tfrecord_category, tfrecord_channels, tfrecord_height, tfrecord_width, \
                tfrecord_total_count, tfrecord_train_count, tfrecord_valid_count, tfrecord_test_count, tfrecord_num_classes, \
                tfrecords_should_use_labels, tfrecord_is_normalized, tfrecord_using_shuffle_batch, tfrecords_remark \
                    = sess.run([tf.cast(features['feature_info'], tf.string),
                                tf.cast(features['category'], tf.string),
                                tf.cast(features['channels'], tf.int64),
                                tf.cast(features['height'], tf.int64),
                                tf.cast(features['width'], tf.int64),
                                tf.cast(features['total_count'], tf.int64),
                                tf.cast(features['train_count'], tf.int64),
                                tf.cast(features['valid_count'], tf.int64),
                                tf.cast(features['test_count'], tf.int64),
                                tf.cast(features['num_classes'], tf.int64),
                                tf.cast(features['should_use_labels'], tf.int64),
                                tf.cast(features['data_is_normalized'], tf.int64),
                                tf.cast(features['using_shuffle_batch'], tf.int64),
                                tf.cast(features['remark'], tf.string)])
                return bytes.decode(tfrecord_feature_info), \
                       bytes.decode(tfrecord_category), \
                       tfrecord_channels, \
                       tfrecord_height, \
                       tfrecord_width, \
                       tfrecord_total_count, \
                       tfrecord_train_count, \
                       tfrecord_valid_count, \
                       tfrecord_test_count, \
                       tfrecord_num_classes, \
                       True if tfrecords_should_use_labels > 0 else False, \
                       True if tfrecord_is_normalized > 0 else False, \
                       True if tfrecord_using_shuffle_batch > 0 else False, \
                       bytes.decode(tfrecords_remark, 'utf-8')
            except tf.errors.OutOfRangeError:
                print('Error Occurred while reading summary records!')
            finally:
                coord.request_stop()
                coord.join(threads)
                sess.close()
            coord.should_stop()
        return '', 'image', 1, 1, 1, 1, 1, 1, 1, 1, False, False, False, ''

    @staticmethod
    def read_and_decode(tfrecords_file_path,
                        category='image',
                        batch_size=128,
                        height_width_channels_shape=[],
                        should_use_labels=False,
                        data_is_normalized=False,
                        using_shuffle_batch=True):
        """
        数据类型的不一致会引起下面的异常：
        tensorflow.python.framework.errors_impl.InvalidArgumentError: Input to reshape is a tensor with 1568 values, but the requested shape has 784
        处理办法：train_images = np.float32(train_images)
        """
        print("Begin read_and_decode %s ..." % tfrecords_file_path)
        filename_queue = tf.train.string_input_producer([tfrecords_file_path])
        key, serialized_example = tf.TFRecordReader().read(filename_queue)
        contexts, features = tf.parse_single_sequence_example(
            serialized_example,
            context_features={"feature_info": tf.FixedLenFeature([], tf.string),
                              "labels": tf.VarLenFeature(tf.int64) if should_use_labels else tf.FixedLenFeature([], tf.int64),
                              'data_raw_bytes': tf.FixedLenFeature([], dtype=tf.string, default_value='')},
            sequence_features={'data_raw': tf.FixedLenSequenceFeature([], dtype=tf.float32)})
        labels = tf.SparseTensor.from_value(contexts['labels']) if should_use_labels else tf.cast(contexts['labels'], tf.int64)
        data_raw = tf.decode_raw(contexts['data_raw_bytes'], tf.float32)
        data_raw = tf.reshape(data_raw, height_width_channels_shape)
        if not data_is_normalized:
            data_raw = TFUtils.l2_normalization(data_raw)
        if category == 'image':
            # Display the training data_raw in the TensorBoard visualizer.
            image_data = tf.expand_dims(data_raw, 0)  # add batch_size dim
            if len(image_data.shape) < 4:
                image_data = tf.expand_dims(image_data, 3)  # add channels dim
            tf.summary.image('data_raw', image_data)  # [batch_size, height, width, channels]
        min_after_dequeue = 1000
        capacity = min_after_dequeue + 3 * batch_size
        if using_shuffle_batch:
            _data_raw, _data_labels = tf.train.shuffle_batch([data_raw, labels],
                                                  batch_size=batch_size,
                                                  capacity=capacity,
                                                  min_after_dequeue=min_after_dequeue)
        else:
            _data_raw, _data_labels = tf.train.batch([data_raw, labels], batch_size=batch_size, capacity=capacity)
        return _data_raw, _data_labels

    @staticmethod
    def load_np_data(tfrecords_file_path,
                     num_total=0,
                     batch_size=128,
                     allow_smaller_final_batch=False,
                     category='image',
                     height_width_channels_shape=[],
                     should_use_labels=False,
                     data_is_normalized=True,
                     using_shuffle_batch=True):
        """
        :param tfrecords_file_path:
        :param num_total:
        :param batch_size:
        :param allow_smaller_final_batch:
        :param category:
        :param height_width_channels_shape:
        :param should_use_labels:
        :param data_is_normalized:
        :param using_shuffle_batch:
        :return:
        usage:
        np_data_labels = TFRecordsUtils.np_load_data(tfrecords_path + "/valid.tfrecords",
            num_total=tuple_summary[7],
            batch_size=128,
            allow_smaller_final_batch=False,
            category=category,
            height_width_channels_shape=[height, width],
            should_use_labels=False,
            data_is_normalized=True,
            using_shuffle_batch=True)
        ...
        batch_x, batch_y = np_data_labels[batch_index]
        """
        data_raw, labels = \
            TFRecordsUtils.read_and_decode(tfrecords_file_path=tfrecords_file_path,
                                                                category=category,
                                                                batch_size=batch_size,
                                                                height_width_channels_shape=height_width_channels_shape,
                                                                should_use_labels=should_use_labels,
                                                                data_is_normalized=data_is_normalized,
                                                                using_shuffle_batch=using_shuffle_batch)
        total_num_batch = TFUtils.total_num_batch(num_total, batch_size, allow_smaller_final_batch)
        data_labels = []
        with tf.Session() as sess:
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(coord=coord, sess=sess)
            try:
                for i_batch in range(total_num_batch):
                    if not coord.should_stop():
                        _data, _labels = sess.run([data_raw, labels])
                        data_labels.append((np.asarray(_data, dtype=np.float32), np.asarray(_labels, dtype=np.int64)))
            except:
                print('Error Occurred on reading tfrecods data!')
                import traceback
                traceback.print_exc()
            finally:
                coord.request_stop()
                coord.join(threads)
                sess.close()
            coord.should_stop()
        return data_labels


if __name__ == '__main__':
    tfrecords_path = "/Users/tony/myfiles/spark/share/python-projects/deep_trading/dataset/tf_records/mnist"
    tuple_summary = TFRecordsUtils.read_summary(tfrecords_path + "/summary.tfrecords")
    category = tuple_summary[1]
    height = tuple_summary[3]
    width = tuple_summary[4]
    num_total = tuple_summary[6]
    np_data_labels = TFRecordsUtils.load_np_data(tfrecords_path + "/valid.tfrecords",
                                                 num_total=tuple_summary[7],
                                                 batch_size=128,
                                                 allow_smaller_final_batch=False,
                                                 category=category,
                                                 height_width_channels_shape=[height, width],
                                                 should_use_labels=False,
                                                 data_is_normalized=True,
                                                 using_shuffle_batch=True)
    for batch_idx, (data, label) in enumerate(np_data_labels):
        print(batch_idx, len(data), len(label))


