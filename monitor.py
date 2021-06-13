import cv2
from enum import Enum

class MonitorState(Enum):
    INITED = 0
    RUNNING = 1
    DISPOSED = 2

class Monitor:
    def __init__(self, name):
        self.name = name
        self.state = MonitorState.INITED
    
    def show(self, frame):
        self.state = MonitorState.RUNNING
        cv2.imshow(self.name,frame)

    def dispose(self):
        cv2.destroyAllWindows()
        self.state = MonitorState.DISPOSED