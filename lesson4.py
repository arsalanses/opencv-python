import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(frame, (100, 200), (200, 400), (0, 255, 0), 10)
    cv2.rectangle(frame, (100, 200), (200, 300), (0, 0, 255), 5)

    cv2.imshow('webCam', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
