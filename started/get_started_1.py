import tensorflow as tf
import numpy as np

X = np.random.rand(100).astype(np.float32)
Y = X * 0.1 + 0.3

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
P = W * X + b

loss = tf.reduce_mean(tf.square(P - Y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in xrange(101):
    sess.run(train)
    if step % 10 == 0:
        print(step, sess.run(W), sess.run(b))


