import sys
from monitor import Monitor, MonitorState
from capture import Capture, CaptureState

if __name__ == "__main__":
    print("Monitor")
    print("")
    username = "admin"
    password = "123456"
    url = "192.168.0.240/media/?action=stream"
    window = "Test"
    capture = Capture(username, password, url)
    monitor = Monitor(window)
    frameCount = 0

    while True:
        if capture.state == CaptureState.DISPOSED:
            capture = Capture(username, password, url)

        if capture.state == CaptureState.INITED:
            capture.connect()

        if monitor.state == MonitorState.DISPOSED:
            monitor = Monitor(window)

        while (capture.state == CaptureState.CONNECTED or capture.state == CaptureState.RUNNING) and (monitor.state==MonitorState.INITED or monitor.state==MonitorState.RUNNING):
            
            ret, frame = capture.capture()

            if ret == False:
                capture.dispose()
                break;

            try:
                monitor.show(frame)
            except:
                print("[main::error] Show Frame Error: ", sys.exc_info()[0])
                capture.dispose()
                break

            try:
                capture.wait()
            except:
                print("[main::error] Wait Frame Error: ", sys.exc_info()[0])
                monitor.dispose()
                capture.dispose()
                break

            frameCount = frameCount + 1
            print('Frame #'+str(frameCount))
