import cv2
import os
img = cv2.imread("4. Open CV with Python\lesson 2\people.jpeg")
import numpy 

# #Convert function
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("screen", grey)
# cv2.waitKey(5000)

# rgreyb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("screen", rgreyb)
# cv2.waitKey(5000)

# hsgrey = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("screen", hsgrey)
# cv2.waitKey(5000)

#Edge Detection

edges = cv2.Canny(img, 100, 500)
cv2.imshow("screen", edges)
cv2.waitKey(5000)