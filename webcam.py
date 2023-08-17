import cv2
from threading import Thread
class webcamImageGetter:

    def __init__(self):
        self.currentFrame = None
        self.CAMERA_WIDTH = 512
        self.CAMERA_HEIGHT = 512
        self.CAMERA_NUM = 0

        self.capture = cv2.VideoCapture(0) #Put in correct capture number here
        #OpenCV by default gets a half resolution image so we manually set the correct resolution
    #Starts updating the images in a thread
    def start(self):
        Thread(target=self.updateFrame, args=()).start()

    #Continually updates the frame
    def updateFrame(self):
        while(True):
            ret, self.currentFrame = self.capture.read()
    def getFrame(self):
        return self.currentFrame
