import time

import cv2
import pyzbar.pyzbar as pyzbar
from playsound import playsound
import requests

cap = cv2.VideoCapture(0)

if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
    exit()

while True:
    success, frame = cap.read()

    if not success:
        break

    for code in pyzbar.decode(frame):
        my_code = code.data.decode('utf-8')

        print('인식 성공: ' + my_code)
        playsound("sound.mp3")
        time.sleep(1)

    cv2.imshow('CAM', frame)
    if cv2.waitKey(1) == ord('q'):  # 사용자가 q를 입력하면
        break

cap.release()
cv2.destroyAllWindows()



code = None
url = f'http://127.0.0.1:5000/image/cam/{code}'
headers = {'camera_request' : r"wY?a&KtTF;\S6so"}

res = requests.get(url, headers=headers)