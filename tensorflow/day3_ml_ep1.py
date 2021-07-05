# Machine Learning Foundations: Ep #1 What is ML?
# Example: The “Hello World” of ML → https://goo.gle/3dfRtD1
# Exercise 1 → https://goo.gle/2zdSPzm

import tensorflow as tf
from tensorflow import keras 
import numpy as np

#Sequence mentions how many layers, unit is how many neuron 
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))


