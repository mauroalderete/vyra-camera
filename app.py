from flask import Flask, render_template, Response
from streamer import Streamer

username = "admin"
password = "123456"
url = "192.168.0.240/media/?action=stream"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    global username
    global password
    global url
    
    streamer = Streamer(username, password, url)
    return Response(streamer.stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
