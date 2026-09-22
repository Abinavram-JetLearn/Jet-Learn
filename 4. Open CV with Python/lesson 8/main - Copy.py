import cv2
import os

video = cv2.VideoCapture("4. Open CV with Python/opencv-assets-main/cars.mp4")
car_data = "4. Open CV with Python/lesson 8/cars.xml"

face_detection = cv2.CascadeClassifier(car_data)

while(video.isOpened()):
    return_val, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.2, 2)
    print(faces)
    for x,y,w,h in faces:
        face_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        face = gray[y:y + h, x:x + w]
    cv2.imshow("YOU", img)
    k = cv2.waitKey(30)
    if k == 27:
        break