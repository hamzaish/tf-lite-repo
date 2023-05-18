from optimized_methods import getVideo, classify
import cv2 as cv
from tflite_runtime.interpreter import Interpreter
import time
# import threading

model_path = 'model2.tflite'
label_path = 'labels.txt'
top_k_results = 3

cap = cv.VideoCapture(0)
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()

while True:
    print(classify(interpreter, getVideo(cap)))
    time.sleep(5)