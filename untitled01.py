# -*- coding: utf-8 -*-
"""Untitled01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wbVJScN0Ajwk2kglr-KP0y9D0IpF4LwA
"""

# Commented out IPython magic to ensure Python compatibility.
# %env KERAS_BACKEND=tensorflow

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train[1234].shape

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

x_train[1234].shape

X = x_train[1234]

X = X.reshape(28, 28)

plt.imshow(X,  cmap='Greys')

y_train[1234]

from keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

y_train[1234]

x_train = x_train/255
x_test = x_test/255

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import SGD

model = Sequential()

model.add(Conv2D(4, (5, 5), padding='same', input_shape=(28, 28, 1)))
model.add(Activation('relu'))

model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(8, (5, 5), padding='same'))
model.add(Activation('relu'))

model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(16, (5, 5), padding='same'))
model.add(Activation('relu'))

model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(9))
model.add(Activation('relu'))

model.add(Dense(10))

model.add(Activation('softmax'))

model.compile(loss='mse', optimizer=SGD(lr=0.07), metrics=['accuracy'])

model.summary()



model.fit(x_train, y_train, batch_size=100, epochs=10)

score = model.evaluate(x_test, y_test)

print(f'測試資料的 loss: {score[0]:.5f}')
print(f'測試資料的正確率: {score[1]}')

from keras.models import load_model

model.save('myCNNmodel.h5')

del model

import numpy as np
import cv2

from google.colab import drive
drive.mount('/content/drive/')
import os
os.chdir('/content/drive/My Drive/')

img = cv2.imread('mytest.jpg')

img2 = cv2.imread('test3.png')

type(img2)

type(img)

img.shape

plt.imshow(img,  cmap='Greys')



imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(imggray.shape)

plt.imshow(imggray,  cmap='Greys')

imggray = 1 - imggray / 255.0

imggray.shape

plt.imshow(imggray,  cmap='Greys')

model = load_model('myCNNmodel.h5')

predicted = np.argmax(model.predict(x_test),axis=1)



pick = np.random.randint(1,9999, 5)

for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(x_test[pick[i]].reshape(28,28), cmap='Greys')
    plt.title(predicted[pick[i]])
    
    
    plt.axis("off")

predicted = np.argmax(model.predict(x_test),axis=1)
print(predicted[img2])