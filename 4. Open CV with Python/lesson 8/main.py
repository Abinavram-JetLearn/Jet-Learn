import cv2
import os

video = cv2.VideoCapture(0)

data = "4. Open CV with Python/lesson 8/haarcascade_smile.xml"
face_detection = cv2.CascadeClassifier(data)

while(video.isOpened()):
    return_val, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 2, 10)
    print(faces)
    for x,y,w,h in faces:
        face_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (120, 120))
    cv2.imshow("YOU", img)
    k = cv2.waitKey(10)
    if k == 27:
        break