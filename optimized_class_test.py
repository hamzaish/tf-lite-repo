from optimized_class import ClassifyObject
import cv2 as cv
from tflite_runtime.interpreter import Interpreter
import time
from motion_sensor import MotionSensor
from motors import Motor
import board
# import threading

model_path = 'model2.tflite'
label_path = 'labels.txt'
top_k_results = 3

cap = cv.VideoCapture(0)
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
rec_up, rec_down, trash_up, trash_down = None, None, None, None
motor = Motor([rec_up, rec_down, trash_up, trash_down], [board.D19, board.D16, board.D26, board.D20])
motor.recycle()
motor.trash()
classifier = ClassifyObject(interpreter, cap, motor)
motion_detect = MotionSensor(cap, classifier, motor)
motion_detect.start()
