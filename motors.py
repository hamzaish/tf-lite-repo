from adafruit_servokit import ServoKit
import Jetson.GPIO as GPIO
import time

class MotionSensor:
    kit = ServoKit(channels=16)
    pins = None

    def __init__(self, pins):
        self.kit.servo[0].angle = 0
        self.pins = pins
        GPIO.setmode(GPIO.BOARD)
        for i in pins:
            GPIO.setup(pins[i], GPIO.OUT)

    def open_servo(self):
        self.kit.servo[0].angle = 60

    def close_servo(self):
        self.kit.servo[0].angle = 0
    
    def recycle(self):
        GPIO.output(self.pins[0], GPIO.HIGH)
        time.sleep(3)
        GPIO.output([self.pins[0], self.pins[1]], (GPIO.LOW, GPIO.HIGH))
        time.sleep(2)
        GPIO.output(self.pins[1], GPIO.LOW)

    def trash(self):
        GPIO.output(self.pins[2], GPIO.HIGH)
        time.sleep(3)
        GPIO.output([self.pins[2], self.pins[3]], (GPIO.LOW, GPIO.HIGH))
        time.sleep(2)
        GPIO.output(self.pins[3], GPIO.LOW)