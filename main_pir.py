from optimized_class import ClassifyObject
import cv2 as cv
from tflite_runtime.interpreter import Interpreter
import time
from pir_sensor import PirSensor
from motors import Motor
from adafruit_blinka.board.nvidia.jetson_nano import *
import digitalio as io

model_path = 'model2.tflite'
label_path = 'labels.txt'

cap = None
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()
rec_up, rec_down, trash_up, trash_down = None, None, None, None
motor = Motor([rec_up, rec_down, trash_up, trash_down], [D19, D26, D21, D16])
motor.recycle()
motor.trash()
lights = io.DigitalInOut(D8)
lights.direction = io.Direction.OUTPUT
lights.value = False
classifier = ClassifyObject(interpreter, cap, motor, lights)
motion_detect = PirSensor(classifier, motor, lights)
motion_detect.start()

