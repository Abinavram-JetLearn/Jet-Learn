import cv2, os, numpy
loc = "4. Open CV with Python/lesson 7/haarcascade_frontalface_default.xml"
dataset = "4. Open CV with Python/lesson 7/data_sets"
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(dataset):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dataset, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            labels.append(label)
            images.append(cv2.imread(path, 0))
        id += 1

(images, labels) = [numpy.array(lis) for lis in [images, labels]]
recogniser = cv2.face.LBPHFaceRecognizer_create()
webcam = cv2.VideoCapture(0)
facedetection = cv2.CascadeClassifier(loc)
recogniser.train(images, labels)
while(True):
    return_val, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetection.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for x,y,w,h in faces:
        face_rect = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (120, 120))
        prediction = recogniser.predict(face_resize)
        print('Confidence:', prediction[1])
        print(names[prediction[0]])
    cv2.imshow("YOU", img)
    k = cv2.waitKey(10)
    if k == 27:
        break