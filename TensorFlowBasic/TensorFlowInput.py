import tensorflow as tf 

x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.float32)
z = tf.placeholder(tf.string)

with tf.Session() as sess:
	output = sess.run(x,feed_dict={x:123, y:45.67, z:'Test String!'})
	print(output)
