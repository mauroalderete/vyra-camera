# syntax=docker/dockerfile:1
FROM python:3.9.5

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY capture.py capture.py
COPY streamer.py streamer.py
COPY views.py views.py
COPY templates/index.html templates/index.html
COPY static/main.css static/main.css

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

