import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import argparse
from PIL import Image

def getVideo(cap):
    _, frame = cap.read()
    return frame

def classify(interpreter, img):
    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]
    img = img/255
    img = cv2.imread('snapple.jpg')
    img = img/255
    img = img.astype(np.float32)
    img = cv2.resize(img, (224, 224))
    test_image = np.expand_dims(img, axis=0)
    cv2.imwrite('image.jpg', test_image)
    interpreter.set_tensor(input_index, test_image)
    interpreter.invoke()
    prob = interpreter.get_tensor(output_index)
    print(prob[0])
    if prob[0][0] > 0.85:
        return 'recycle'
    else:
        return 'trash'
