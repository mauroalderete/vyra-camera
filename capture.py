import sys
from types import FrameType
import cv2
from enum import Enum

class CaptureState(Enum):
    INITED = 0
    CONNECTED = 1
    RUNNING = 2
    DISPOSED = 3

class Capture:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.state = CaptureState.INITED

    def connect(self):
        try:
            print("[capture::connect] Connecting to "+'http://'+self.username+':'+self.password+'@'+self.url)
            self.cap = cv2.VideoCapture('http://'+self.username+':'+self.password+'@'+self.url)
            self.state = CaptureState.CONNECTED
        except:
            print("[Capture::error] Capture Connection Error: ", sys.exc_info()[0])
            self.dispose()

    def capture(self):
        self.state = CaptureState.RUNNING
        ret, frame = self.cap.read()

        if ret == True:
            self.frame = frame
            return ret, self.frame
        else:
            print("[Capture::capture] return FALSE")
            return ret, None

    def wait(self):
        cv2.waitKey(1)

    def dispose(self):
        self.cap.release()
        self.state = CaptureState.DISPOSED
