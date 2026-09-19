import cv2
import os

video = cv2.VideoCapture(0)
face_data = "4. Open CV with Python/lesson 8/haarcascade_frontalface_default.xml"
eye_data = "4. Open CV with Python/lesson 8/haarcascade_eye.xml"
data = "4. Open CV with Python/lesson 8/haarcascade_smile.xml"
face_detection = cv2.CascadeClassifier(face_data)
smile_detection = cv2.CascadeClassifier(data)
eye_detection = cv2.CascadeClassifier(eye_data)

while(video.isOpened()):
    return_val, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 2, 5)
    print(faces)
    for x,y,w,h in faces:
        face_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        face = gray[y:y + h, x:x + w]
        smiles = smile_detection.detectMultiScale(face, 1.5, 20)
        eyes = eye_detection.detectMultiScale(face, 1.5, 15)
        for x1, y1, w1, h1 in smiles:
            smile = cv2.rectangle(img, (x + x1, y + y1), (x + x1 + w1, y + y1 + h1), (255, 255, 0), 5)
        for x2, y2, w2, h2 in eyes:
            eye = cv2.rectangle(img, (x + x2, y + y2), (x + x2 + w2, y + y2 + h2), (255, 0, 255), 5)
    cv2.imshow("YOU", img)
    k = cv2.waitKey(10)
    if k == 27:
        break