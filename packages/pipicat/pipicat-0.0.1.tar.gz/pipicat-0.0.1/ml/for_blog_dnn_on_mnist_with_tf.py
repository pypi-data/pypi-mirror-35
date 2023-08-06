# A tutorail code for learning TensorFlow
# Based on the tutorial provided by TensorFLow
# Use deep NN on MNIST datt
# Yi DING @ 01/05/18

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# ==================== First section, simple softmax model
# Load MNIST Data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# Note that here "mnist" is a lightweight class called "Datasets"

# Start TensorFlow InteractiveSession
sess = tf.InteractiveSession()

# Build placeholders
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

# Variables
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Initialize variables
sess.run(tf.global_variables_initializer())

# Build graph (model)
y = tf.matmul(x, W) + b

# Build loss function
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

# Train the model
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# Note that the return "train_step" is an "Operation"
# Hence training can be conducted by repeatedly run the "Operation"
for _ in range(1000):
    batch = mnist.train.next_batch(100)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})

# Evaluate the model (Build evaluation graph)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


# ==================== Second section, multilayer CNN
# Handy functions
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape = shape)
    return tf.Variable(initial)


# Convolution and pooling
def con2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
