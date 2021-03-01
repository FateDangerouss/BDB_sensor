from picamera import PiCamera
from time import sleep

class camera:
    def __init__(self):
        self.cam = PiCamera()
    
    def get(self):
        self.cam.start_preview()
        sleep(2)
        self.cam.capture("object.jpg")
        self.cam.stop_(preview)