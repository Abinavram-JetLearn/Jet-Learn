import cv2
import os
img = cv2.imread("4. Open CV with Python\lesson 4\Blobs.jpeg")
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 50
params.filterByCircularity = True
params.minCircularity = 0.5
params.maxCircularity = 0.8
params.filterByConvexity = True
params.minConvexity = 0.5
params.maxConvexity = 1
params.filterByInertia = True
params.minInertiaRatio = 0.01
params.maxInertiaRatio = 1
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(img)
print(keypoints)
for pts in keypoints:
    x, y = int(pts.pt[0]), int(pts.pt[1])
    cv2.drawMarker(img, (x, y), (255, 0, 255), cv2.MARKER_DIAMOND, 10, 3)
cv2.imshow("screen", img)
cv2.waitKey(5000)