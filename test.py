import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000]))); from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())