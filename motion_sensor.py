import time
import cv2
import pandas
from datetime import datetime
import imutils

#Create observer method to notify observer about changes in motion.

class MotionSensor:
    cap = None
    optimized = None
    initial = None
    detect = False
    
    def __init__(self, cap, optimized):
        self.cap = cap
        self.optimized = optimized
    
    def notify(self):
        self.changeDetect()
        self.optimized.classify()
        self.changeDetect()
    
    def changeDetect(self):
        detect = not detect

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
            for cur in cnts:  
                if cv2.contourArea(cur) < 100000:
                    continue  
                self.notify()
            initial = gray_frame