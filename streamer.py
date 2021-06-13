import cv2
from capture import Capture, CaptureState

class Streamer:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.capture = Capture(self.username, self.password, self.url)

    def stream(self):
        while True:
            if self.capture.state == CaptureState.DISPOSED:
                self.capture = Capture(self.username, self.password, self.url)

            if self.capture.state == CaptureState.INITED:
                self.capture.connect()

            while self.capture.state == CaptureState.CONNECTED or self.capture.state == CaptureState.RUNNING:
                ret, frame = self.capture.capture()

                if ret == False:
                    self.capture.dispose()
                    break;

                ret, buffer = cv2.imencode('.jpg', frame)

                if ret == False:
                    self.capture.dispose()
                    break;

                source = buffer.tobytes()

                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + source + b'\r\n')  # concat frame one by one and show result
