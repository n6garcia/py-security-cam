import cv2
import requests
from datetime import datetime
from time import sleep

def sendImage(frame):
    imencoded = cv2.imencode(".jpg", frame)[1]

    now = datetime.now()
    seq = now.strftime("%Y%m%d%H%M%S")

    file = {'file': (seq, imencoded.tobytes(), 'image/jpeg')}

    #response = requests.post("https://noeldev.site/cam", files=file, timeout=5)
    #response = requests.post("http://localhost:3004/", files=file, timeout=5)
    try:
        response = requests.post("https://noeldev.site/cam", files=file, timeout=5)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response

def takeImage():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    print(sendImage(frame))
    cap.release()


while 1:
    takeImage()
    sleep(5)
