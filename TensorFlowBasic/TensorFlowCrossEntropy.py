# Quiz Solution
# Note: You can't run code in this tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

# ToDo: Print cross entropy from session
cross_entropy = -tf.reduce_sum(tf.multiply(one_hot_data, tf.log(softmax_data)))

with tf.Session() as sess:
    print(sess.run(cross_entropy))
