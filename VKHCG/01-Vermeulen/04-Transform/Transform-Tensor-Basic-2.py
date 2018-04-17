################################################################
# -*- coding: utf-8 -*-
################################################################
import tensorflow as tf
import numpy as np
################################################################
#–a=(b+c)∗(c+22) a=(b+c)∗(c+22).
################################################################
# first, create a TensorFlow constant
const = tf.constant(22.0, name="const")
    
# create TensorFlow variables
b = tf.placeholder(tf.float32, [None, 1], name='b')
c = tf.Variable(3.0, name='c')

################################################################
# now create some operations
d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# setup the variable initialisation
init_op = tf.global_variables_initializer()

################################################################
# start the session
with tf.Session() as sess:
    # initialise the variables
    sess.run(init_op)
    # compute the output of the graph
    a_out = sess.run(a, feed_dict={b: np.arange(-5, 5)[:, np.newaxis]})
    print("Variable a is {}".format(a_out))
################################################################
print('### Done!! ############################################')
################################################################