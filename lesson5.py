import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # cv2.line(frame, (100, 200), (200, 400), (0, 255, 0), 10)
    
    # cv2.rectangle(frame, (100, 200), (200, 300), (0, 0, 255), 5)

    # cv2.circle(frame, (200, 200), 70, (120, 0, 50), 3)

    # pts = np.array([[50, 100], [120, 200], [250, 100], [400, 20]])
    # cv2.polylines(frame, [pts], True, (60, 40 , 20), 5)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, 'arsalan', (100, 100), font, 1, (100, 0, 0), 5)

    cv2.imshow('webCam', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
