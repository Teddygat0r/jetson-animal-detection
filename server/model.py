from tensorflow import keras
from keras.models import load_model
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import os
import cv2
import requests
import time
import base64
import datetime

cam = cv2.VideoCapture(0)
data_dir = "animals/animals/"
server = "http://localhost:5000/"
model = load_model('models/AnimalClassification2.h5', compile=False)
Classifications = os.listdir(data_dir)

def loadImage(image):
    resize = tf.image.resize(image, (255,255))
    plt.imshow(resize.numpy().astype(int))
    return resize

def predictImage(image):
    resized_image = loadImage(image)
    yhat = model.predict(np.expand_dims(resized_image/254, 0))
    return yhat

def imageDifference(image_1, image_2):
    if image_1.shape != image_2.shape:
        raise ValueError("Both images must have the same dimensions.")
    diff = cv2.absdiff(previousImage, currentImage)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    difference_percentage = np.mean(gray_diff) / 255.0 * 100.0  
    return difference_percentage

def sendToServer(image, species):
    retval, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    myimg = {
        "species": species,
        "timestamp": datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        "image": jpg_as_text.decode('UTF-8'),
    }
    requests.post(f"{server}/api/images/add", json=myimg)


previousImage = None
res, currentImage = cam.read()

while(True):
    previousImage = currentImage
    res, currentImage = cam.read()
    if(res):
        diff = imageDifference(previousImage, currentImage)
        if(diff > 5):
            yhat = predictImage(currentImage)
            print(diff)
            print(yhat[0, yhat.argmax()])
            print(Classifications[np.array(yhat).argmax()])

            if(yhat[0, yhat.argmax()] > 0.8 and Classifications[np.array(yhat).argmax()] != "nothing"):
                sendToServer(currentImage, Classifications[np.array(yhat).argmax()])
            elif(yhat[0, yhat.argmax()] > 0.6 and Classifications[np.array(yhat).argmax()] != "nothing"):
                sendToServer(currentImage, f"Unsure, {Classifications[np.array(yhat).argmax()]}")
            

    time.sleep(1)
cap.release()