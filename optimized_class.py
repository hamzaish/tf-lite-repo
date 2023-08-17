import cv2
import numpy as np
import base64
import asyncio
import requests
import board
import digitalio as io
import time
# import grequests
from webcam import webcamImageGetter

class ClassifyObject():
    interpreter = None
    cap = None
    motor = None
    api = None
    lights = None
    cam = webcamImageGetter()

    def __init__(self, interpreter, cap, motor, lights) -> None:
        self.interpreter = interpreter
        self.cap = cap
        self.motor = motor
        self.api = "https://twsasq43d3.execute-api.us-east-1.amazonaws.com/staging"
        self.lights = lights
        self.cam.start()

    def getVideo(self):
        _, frame = self.cap.read()
        return frame

    def sendPost(self, img):
        _, im_arr = cv2.imencode('.jpg', img)
        im_b64 = base64.b64encode(im_arr)
        data = {"image": im_b64.decode()}
        x = requests.post(self.api, json=data)
        print(im_b64)

    def classify(self, image= None):
        time.sleep(0.5)
        input_index = self.interpreter.get_input_details()[0]["index"]
        output_index = self.interpreter.get_output_details()[0]["index"]
        post = None
        if image == None:
            img = self.cam.getFrame()
            self.sendPost(img)
            #loop = asyncio.get_event_loop()
            #loop.run_until_complete(post)
            img = img/255
        else:
            self.sendPost(image)
            #loop = asyncio.get_event_loop()
            #loop.run_until_complete(post)
            img = image/255
        img = img.astype(np.float32)
        img = cv2.resize(img, (224, 224))
        test_image = np.expand_dims(img, axis=0)
        cv2.imwrite('image.jpg', test_image)
        self.interpreter.set_tensor(input_index, test_image)
        self.interpreter.invoke()
        prob = self.interpreter.get_tensor(output_index)
        print(prob[0])
        if prob[0][0] > 0.70:
            self.motor.recycle()
        else:
            self.motor.trash()
    
