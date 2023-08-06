# A tutorail code for learning TensorFlow
# Based on the tutorial provided by TensorFLow
# Use softmax algorithm on digits data
# Recommend installing Anaconda and this code can run directly
# Yi DING @ 06/02/17

# Load data and import numpy libraries
from sklearn.datasets import load_digits
digits = load_digits()
import numpy as np
  
# Test models with each data set
X = digits.data
y = digits.target
total_num = np.shape(y)[0]
y = np.zeros((total_num,10))
for i in range(digits.target.shape[0]):
    y[i,digits.target[i]] = 1

# Divide into train data and test data
train_num = np.int(total_num * 0.9)
X_train = X[0:train_num,:]
y_train = y[0:train_num,:]
X_test = X[train_num:total_num,:]
y_test = y[train_num:total_num,:]

# Import TensorFlow libraries
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import sys
import tensorflow as tf
FLAGS = None

# The shuffle_data function shuffle the data randomly
# and return n tuples (X,y) back
def shuffle_data(X,y,n):
    import numpy as np
    X = np.array(X)
    y = np.array(y)
    rows,columns = X.shape
    if rows < n:
        print("ERROR: There is not enough rows in X.")
    rndInd = np.random.permutation(rows)
    return X[rndInd[0:n],:], y[rndInd[0:n],:]

# Main process
# Create the model
x = tf.placeholder(tf.float32,[None,64])
W = tf.Variable(tf.zeros([64,10])) 

# Here W is a n-by-K matrix where n is # of features and K is # of classes
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Create session
sess = tf.InteractiveSession()

# Initialize variables
tf.global_variables_initializer().run()

# Train model
for _ in range(1000):
    batch_xs, batch_ys = shuffle_data(X_train,y_train,100)
    sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})

# Test trained model
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(sess.run(accuracy,feed_dict={x: X_test,y_:y_test}))