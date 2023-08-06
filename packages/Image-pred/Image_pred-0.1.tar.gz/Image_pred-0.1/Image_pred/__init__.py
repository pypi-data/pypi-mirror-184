# -*- coding: utf-8 -*-
from keras.models import load_model
from PIL import Image
import numpy as np
import cv2


def load_image(img_pa,model):
    try:
        img = Image.open(img_pa)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        resized_image = cv2.resize(gray, (124, 124))

        resized_image = resized_image.reshape(124, 124, 1)

        h1 = np.expand_dims(resized_image, axis=0)
        h1 = h1 / 255.0

        best_model = load_model(model)

        pred = best_model.predict(h1)
        op = np.where(pred > 0.5, 'MEN', 'WOMEN')[0][0]
    except:
        op = 'Other'

    return op


