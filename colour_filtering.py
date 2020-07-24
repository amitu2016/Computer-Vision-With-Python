import cv2
import numpy as np

cap = cv2.VideoCapture(0)

dark_blue = np.uint8([[[255,0,0]]]) #BGR
dark_blue = cv2.cvtColor(dark_blue,cv2.COLOR_BGR2HSV)

print(dark_blue)

# 120,255,255 (HSV)  LOWER = (H-10, 100, 100)   UPPER = (H+10, 255, 255)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("video", frame)
    cv2.imshow("video2", mask)
    cv2.imshow("video3", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()