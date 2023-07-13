from adafruit_servokit import ServoKit
import digitalio
import time
import board

class Motor:
    kit = ServoKit(channels=16)
    pins = None

    def __init__(self, pins, vals):
        self.kit.servo[0].angle = 180
        self.pins = pins
        for i in range(len(pins)):
            self.pins[i] = digitalio.DigitalInOut(vals[i])
            self.pins[i].direction = digitalio.Direction.OUTPUT

    def open_servo(self):
        self.kit.servo[0].angle = 180

    def close_servo(self):
        self.kit.servo[0].angle = 0
    
    def recycle(self):
        self.pins[0].value = True
        time.sleep(3)
        self.pins[0].value = False
        self.pins[1].value = True
        time.sleep(2)
        self.pins[1].value = False

    def trash(self):
        self.pins[2].value = True
        time.sleep(3)
        self.pins[2].value = False
        self.pins[3].value = True
        time.sleep(2)
        self.pins[3].value = False

