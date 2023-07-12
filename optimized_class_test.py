from optimized_class import ClassifyObject
import cv2 as cv
from tflite_runtime.interpreter import Interpreter
import time
from motion_sensor import MotionSensor
from motors import Motor
# import threading

model_path = 'model2.tflite'
label_path = 'labels.txt'
top_k_results = 3

cap = cv.VideoCapture(0)
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
motor = Motor([35, 36, 37, 38])
classifier = ClassifyObject(interpreter, cap, motor)
motion_detect = MotionSensor(cap, classifier, motor)
motion_detect.start()