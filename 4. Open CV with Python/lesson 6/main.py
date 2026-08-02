import cv2
import numpy as np
video = cv2.VideoCapture("red video.mp4")
for i in range(60):
    return_val, bg = video.read()

while(video.isOpened()):
    return_val, img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lr1 = np.array([100, 60, 40])
    ur1 = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lr1, ur1)
    lr2 = np.array([170, 60, 40])
    ur2 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv, lr2, ur2)
    mask = mask + mask1
    mask2 = cv2.bitwise_not(mask)
    result1 = cv2.bitwise_and(bg, bg, mask= mask)
    result2 = cv2.bitwise_and(img, img, mask= mask2)
    output = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("INVISIBLE MAN", output)
    k = cv2.waitKey(10)
    if k == 27:
        break