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
        