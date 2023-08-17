from adafruit_blinka.board.nvidia.jetson_nano import *
import digitalio
import time

class PirSensor:
    optimized = None
    detect = True
    motor = None
    pir = None
    motion_usonic = None
    ultrasonic1 = None
    ultrasonic2 = None
    lights = None

    def __init__(self, optimized, motor, lights):
        self.optimized = optimized
        self.motor = motor
        self.pir = digitalio.DigitalInOut(D17)
        self.pir.direction = digitalio.Direction.INPUT
        self.ultrasonic1 = digitalio.DigitalInOut(D27)
        self.ultrasonic1.direction = digitalio.Direction.INPUT
        self.ultrasonic2 = digitalio.DigitalInOut(D22)
        self.ultrasonic2.direction = digitalio.Direction.INPUT
        self.lights = lights
        self.motion_usonic = digitalio.DigitalInOut(D12)
        self.motion_usonic.direction = digitalio.Direction.INPUT
    def notify(self):
        self.lights.value = True
        self.motor.close_servo()
        time.sleep(2.5)
        self.optimized.classify()
        self.lights.value = False
        self.motor.open_servo()
        time.sleep(1)
        self.initial = None
        self.detect = True
        self.start()

    def start(self):
        while self.detect and (self.ultrasonic1.value == False and self.ultrasonic2.value == False):
            if self.pir.value == True or self.motion_usonic.value == True:
                self.detect = False
                return self.notify()
        if self.ultrasonic1.value == True or self.ultrasonic2.value == True:
            self.motor.close_servo()
            self.lights.value = False
