from tensorflow import keras
from keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import os
import cv2

data_dir = "animals/animals/"
model = load_model('models/AnimalClassification.h5', compile=False)
Classifications = os.listdir(data_dir)

def loadImage(path):
    img = cv2.imread(path)
    plt.imshow(img)
    resize = tf.image.resize(img, (255,255))
    plt.imshow(resize.numpy().astype(int))
    plt.show()
    return resize

def predictImage(path):
    resized_image = loadImage(path)
    yhat = model.predict(np.expand_dims(resized_image/254, 0))
    return yhat

for x in range(2, 7):
    yhat = predictImage(f'tester{x}.jpg')
    print(Classifications[yhat.argmax()])
    print(yhat[0, yhat.argmax()])