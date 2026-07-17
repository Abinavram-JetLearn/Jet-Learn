import cv2
import os
from PIL import Image
os.chdir("C:/Users/abina/OneDrive/Documents/Jet Learn/4. Open CV with Python/lesson 5/images")
path = 'C:/Users/abina/OneDrive/Documents/Jet Learn/4. Open CV with Python/lesson 5/images'
print(os.listdir('.'))
imgs = os.listdir('.')
mw = 0
mh = 0
w = 0
h = 0
for i in imgs:
    img = Image.open(os.path.join(path, i))
    w += img.size[0]
    h += img.size[1]
mw = w // 3
mh = h // 3
print(mw, mh)

for i in imgs:
    img = Image.open(os.path.join(path, i))
    imgR = img.resize((mw, mh))
    imgR.save(i,'JPEG', quality = 95)

video = "first_video.avi"
videos = cv2.VideoWriter(video, 0, 0.5, (mw, mh))
for i in imgs:
    videos.write(cv2.imread(os.path.join(path, i)))
# hi
videos.release()