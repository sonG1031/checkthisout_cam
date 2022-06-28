import cv2
import pyzbar.pyzbar as pyzbar
import requests

cap = cv2.VideoCapture(0)

if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
    exit()

SCALE = 10 # 크기
GREEN = (0, 255, 0)
RED = (0, 0, 255)
THICKNESS = 30 # 두께
PASS = 'PASS'
FAILED = 'FAILED'
FONT =  cv2.FONT_HERSHEY_SIMPLEX

while True:
    success, frame = cap.read()

    if not success:
        break

    for code in pyzbar.decode(frame):
        my_code = code.data.decode('utf-8')
        url = f'http://43.200.123.69:5000/image/cam/{my_code}'
        headers = {'camera_request': r"wY?a&KtTF;\S6so"}
        try:
            res = requests.get(url, headers=headers).json()
            if res['data'] == "success":
                cv2.putText(frame, PASS, (250, 450), FONT, SCALE, GREEN, THICKNESS)
            else:
                cv2.putText(frame, FAILED, (150, 450), FONT, SCALE, RED, THICKNESS)
        except:
            pass

    cv2.imshow('CAM', frame)
    if cv2.waitKey(1)&0xFF == 27:  # 사용자가 q를 입력하면
        break

cap.release()
cv2.destroyAllWindows()