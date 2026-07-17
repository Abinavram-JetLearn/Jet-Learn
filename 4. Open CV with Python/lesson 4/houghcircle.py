import cv2
img = cv2.imread("4. Open CV with Python\lesson 4\Blobs.jpeg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(grey, cv2.HOUGH_GRADIENT, 1, 5, param1= 100, param2=45, minRadius=5, maxRadius=70)
print(circles)
for i in circles[0]:
    x, y, r = int(i[0]), int(i[1]), int(i[2])
    circle = cv2.circle(img, (x,y), r, (255, 0, 0), 5)

cv2.imshow("screen", img)
cv2.waitKey(5000)