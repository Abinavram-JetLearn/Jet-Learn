import cv2
import os

name = input("What is your name?: ")
datasets = '4. Open CV with Python/lesson 7/data_sets'

path = os.path.join(datasets, name)

if not os.path.isdir(path):
    os.mkdir(path)

video = cv2.VideoCapture(0)

data = "4. Open CV with Python/lesson 7/haarcascade_frontalface_default.xml"
face_detection = cv2.CascadeClassifier(data)
count = 1

while(video.isOpened()):
    return_val, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for x,y,w,h in faces:
        face_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (120, 120))
        if count <= 30 :
            cv2.imwrite(f'{datasets}/{name}/{count}.png', face_resize)
            count +=1
        else:
            break
    cv2.imshow("YOU", img)
    k = cv2.waitKey(10)
    if k == 27:
        break