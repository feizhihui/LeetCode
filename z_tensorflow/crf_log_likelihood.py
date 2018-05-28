# encoding=utf-8

import tensorflow as tf
import math


class Model:
    def __init__(self):
        # self.logits = tf.get_variable('logits',[1,5,3],dtype=tf.float32)
        self.logits = tf.constant([[[0.3, 0.4, 0.3],
                                    [0.1, 0.9, 0.0],
                                    [0.2, 0.7, 0.1],
                                    [0.3, 0.2, 0.5],
                                    [0.6, 0.2, 0.2]]])

        self.trans_params = tf.fill([3, 3], 0.5, name='trans_params')
        self.labels = tf.constant([[0, 1, 2, 0, 1]])  # shape=[1,5]
        self.sequence_lengths = tf.constant([5])  # shape=[1,]
        with tf.variable_scope('log_likelihood1'):
            self.log_likelihood1, self.trans1 = tf.contrib.crf.crf_log_likelihood(
                self.logits, self.labels, self.sequence_lengths)
        with tf.variable_scope('log_likelihood2', reuse=False):
            self.log_likelihood2, self.trans2 = tf.contrib.crf.crf_log_likelihood(
                self.logits, self.labels, self.sequence_lengths)


with tf.Graph().as_default() as g:
    model = Model()
    initer = tf.global_variables_initializer()
sess = tf.Session(graph=g)

sess.run(initer)
log1, log2, trans1, trans2 = sess.run([model.log_likelihood1, model.log_likelihood2, model.trans1, model.trans2])
print('=' * 50)
print('log likelihood:', log1, 'probability', math.e ** log1)
print('log likelihood:', log2, 'probability', math.e ** log2)
print('=' * 50)
print(trans1)
print(trans2)
print(model.log_likelihood1.name)
print(model.log_likelihood2.name)
