from flask import render_template, Response
from app import app, config
from streamer import Streamer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    streamer = Streamer(config['username'], config['password'], config['url'])
    
    return Response(streamer.stream(), mimetype='multipart/x-mixed-replace; boundary=frame')
