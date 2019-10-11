import tensorflow as tf

logits = [2.0,1.0,0.1]
softmax = tf.nn.softmax(logits)

with tf.Session() as sess:
	output = sess.run(softmax)
	print(output)
