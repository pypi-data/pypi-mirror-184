# -*- coding: utf-8 -*-

from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
from werkzeug.utils import secure_filename
import os
import cv2
from PIL import Image
from tensorflow.keras.preprocessing import image
import numpy as np
# from flask_ngrok import run_with_ngrok
from flask import Flask,request,jsonify,render_template
from io import BufferedReader
import os
import cv2
import matplotlib.pyplot as plt
from File_attach import  file

def load_image(img_pa):
    try:
        img = Image.open(img_pa)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        resized_image = cv2.resize(gray, (124, 124))

        resized_image = resized_image.reshape(124, 124, 1)

        h1 = np.expand_dims(resized_image, axis=0)
        h1 = h1 / 255.0

        best_model = load_model('best_model.h5')

        pred = best_model.predict(h1)
        op = np.where(pred > 0.5, 'MEN', 'WOMEN')[0][0]
    except:
        op = 'Other'

    return op


