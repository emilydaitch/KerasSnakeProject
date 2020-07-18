import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
#tf.__version__

mnist = tf.keras.datasets.mnist # 28x28 images handwritten digits 0 - 9
                                # hello world dataset of machine learning

(x_train, y_train), (x_test, y_test) = mnist.load_data()
#plt.imshow(x_train[0], cmap = plt.cm.binary)
#plt.show()
x_train = tf.keras.utils.normalize(x_train, axis=1) # normalize 0-255 data
x_test = tf.keras.utils.normalize(x_test, axis=1)
#plt.imshow(x_train[0], cmap = plt.cm.binary)
#plt.show()

# Model Creation
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))   # relu - TODO
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) # number of classifications
                                                                # softmax probability distribution
# Parameters for training
model.compile(  optimizer='adam', # research stochastic gradient descent
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

#Epoch 1/3
#1875/1875 [==============================] - 6s 3ms/step - loss: 0.2651 - accuracy: 0.9222
#Epoch 2/3
#1875/1875 [==============================] - 5s 3ms/step - loss: 0.1104 - accuracy: 0.9658
#Epoch 3/3
#1875/1875 [==============================] - 5s 3ms/step - loss: 0.0760 - accuracy: 0.9760

# model memorizing samples vs. learning "what makes" a classification

# Test model
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)
# 0.0893695056438446 0.9725000262260437 -- My results differ from tutorial, but as expected, 
# test loss and accuracy are slightly worse than in-sample loss and accuracy, we are not over-fit

model.save('num_reader.model')
new_model = tf.keras.models.load_model('num_reader.model')

predictions = new_model.predict(x_test) # always takes a list
# TODO learn tf.argmax - 'sessioning'

print(np.argmax(predictions[0]))

