import cv2
import os
import numpy as np
img = cv2.imread("4. Open CV with Python\lesson 3\Videocollage1.jpg")

line = cv2.line(img, (40,70), (1000, 1000), (250, 0, 250), 10)
cv2.imshow("screen", line)
cv2.waitKey(5000)

circle = cv2.circle(img, (500,500), 100, (255, 0, 255), -1)
cv2.imshow("screen", circle)
cv2.waitKey(5000)

rect = cv2.rectangle(img, (40,70), (1000, 1000), (250, 0, 250), 10)
cv2.imshow("screen", rect)
cv2.waitKey(5000)

text = cv2.putText(img, "Cool Fish", (500, 500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 5, (255, 0, 0), 1)
cv2.imshow("screen", text)
cv2.waitKey(5000)

polylist = [(500, 500),(300, 300),(300, 500),(500, 300)]
points = np.array(polylist, dtype=np.int32)
square = cv2.polylines(img, [points], True, (0,0,255), 10)
cv2.imshow("screen", square)
cv2.waitKey(5000)
