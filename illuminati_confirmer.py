import numpy as np
import cv2
import sys
from time import sleep

# mad props to http://stackoverflow.com/questions/11424002/how-to-detect-simple-geometric-shapes-using-opencv

def confirm_illuminati (file_name):
  num_illuminati_found = 0
  copy = img = cv2.imread(file_name, cv2.IMREAD_COLOR)
  grey_img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

  ret, thresh = cv2.threshold(grey_img, 127, 255, 1)

  contours, h = cv2.findContours(thresh, 1, 2)

  FIRST = 0
  RED = (0, 0, 255)
  THICKNESS = 3

  for some_contour in contours:
    approx = cv2.approxPolyDP(some_contour, 0.01*cv2.arcLength(some_contour, True), True)
    l = len(approx)

    if l == 3:
      print 'ILLUMINATI CONFIRMED!'
      num_illuminati_found += 1
      cv2.drawContours(copy, [some_contour], FIRST, RED, 3)

  cv2.imwrite(file_name[:-4] + '_result.jpg', copy)
  return num_illuminati_found

### MAIN PROGRAM BELOW ###

print '---> executing: hack illuminati'
sleep(3)
print 'running illuminati.exe'
sleep(1)
illuminati_count = 0

for file_index in range(1, len(sys.argv)):
  file_name = sys.argv[file_index]
  print 'Processing meme: ' + file_name
  illuminati_count += confirm_illuminati(file_name)

print 'Congratulation, you have rekt the Illuminate'
print 'You have identified ' + str(illuminati_count) + ' of [REDACTED] total Illuminati'
sleep(1)
print '---> exiting illuminati.exe'
sleep(1)
print 'Have a nice day!'

