import numpy as np
import cv2
import sys

img_name = sys.argv[1]

print 'Using file ' + img_name

img = cv2.imread(img_name, cv2.IMREAD_COLOR)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# blah blah blah

cv2.imwrite('result.jpg', img)
