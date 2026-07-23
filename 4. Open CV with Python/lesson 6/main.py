import cv2
video = cv2.VideoCapture("red video.mp4")
while(video.isOpened()):
    return_val, img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("INVISIBLE MAN", hsv)
    k = cv2.waitKey(10)
    if k == 27:
        break