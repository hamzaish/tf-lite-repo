from motion_sensor import MotionSensor
import cv2

cap = cv2.VideoCapture(0)
motion = MotionSensor(cap, None)
motion.changeDetect()
