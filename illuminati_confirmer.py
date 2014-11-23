import numpy as np
import cv2
import sys

# mad props to http://stackoverflow.com/questions/11424002/how-to-detect-simple-geometric-shapes-using-opencv

img_name = sys.argv[1]

print 'Using file ' + img_name

copy = img = cv2.imread(img_name, cv2.IMREAD_COLOR)
grey_img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(grey_img, 127, 255, 1)

contours, h = cv2.findContours(thresh, 1, 2)

FIRST = 0
RED = (0, 0, 255)
THICKNESS = 3

for some_contour in contours:
  approx = cv2.approxPolyDP(some_contour, 0.01*cv2.arcLength(some_contour, True), True)
  l = len(approx)

  if l == 3:
    print 'TRIANGLE FOUND!'
    cv2.drawContours(copy, [some_contour], FIRST, RED, 3)

cv2.imshow('result', copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('result.jpg', copy)
