import time
import cv2
from datetime import datetime
import imutils

#Create observer method to notify observer about changes in motion.

class MotionSensor:
    cap = None
    optimized = None
    initial = None
    detect = True
    motor = None
    
    def __init__(self, cap, optimized, motor):
        self.cap = cap
        self.optimized = optimized
        self.motor = motor
    
    def notify(self):
        self.changeDetect()
        self.motor.close_servo()
        self.optimized.classify()
        self.changeDetect()
        self.motor.open_servo()
        self.start()
    
    def changeDetect(self):
        self.detect = not self.detect

    def start(self):
        while self.detect:
            _, frame = self.cap.read()
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)
            if initial is None:  
                initial = gray_frame
                continue
            differ_frame = cv2.absdiff(initial, gray_frame)
            thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
            cont = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cont)
            self.initial = gray_frame
            for cur in cnts:  
                if cv2.contourArea(cur) < 100000:
                    continue
                else:
                    return self.notify()
            