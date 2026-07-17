import cv2
import os
img = cv2.imread("4. Open CV with Python\lesson 1\opencv.png")
cv2.imshow("screen", img)
cv2.waitKey(0)

bwimg = cv2.imread("4. Open CV with Python\lesson 1\opencv.png", 0)
cv2.imshow("screen", bwimg)
os.chdir("C:/Users/abina/OneDrive/Documents/Jet Learn/4. Open CV with Python/lesson 1")
cv2.imwrite("bw.png", bwimg)