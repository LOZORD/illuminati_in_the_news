import numpy as np
import cv2
import sys
from time import sleep

# mad props to http://stackoverflow.com/questions/11424002/how-to-detect-simple-geometric-shapes-using-opencv

def confirm_illuminati (file_name):
  num_illuminati_found = 0
  dst = copy = img = cv2.imread(file_name, cv2.IMREAD_COLOR)
  grey_img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

  ret, thresh = cv2.threshold(grey_img, 127, 255, 1)

  contours, h = cv2.findContours(thresh, 1, 2)

  FIRST = 0
  RED = (0, 0, 255)
  THICKNESS = 3

  largest_contour = None

  for some_contour in contours:
    approx = cv2.approxPolyDP(some_contour, 0.01*cv2.arcLength(some_contour, True), True)
    l = len(approx)

    # if we find a triangle
    if l == 3:
      print 'ILLUMINATI CONFIRMED!'
      num_illuminati_found += 1
      if largest_contour is None or cv2.contourArea(some_contour) > cv2.contourArea(largest_contour):
        largest_contour = some_contour

  # then output the zoom-in and final image

  box_x, box_y, box_w, box_h = cv2.boundingRect(largest_contour)

  orig_h, orig_w = img.shape[:2]

  center = (box_x + (box_w/2), box_y + (box_h/2))

  for i in range(2,5):
    c_x = center[0]
    c_y = center[1]

    crop_x = int(box_x - orig_w/i)
    crop_y = int(box_y - orig_h/i)

    crop_w = int(box_w + orig_w/i)
    crop_h = int(box_h + orig_h/i)

    crop_image = img[crop_y:crop_h, crop_x:crop_w]

    dst = cv2.resize(crop_image, (orig_h, orig_w))

    #finally, write the new file
    cv2.imwrite(file_name[:-4]+'_zoom_'+str(i)+'.jpg', dst)

  cv2.drawContours(copy, [largest_contour], FIRST, RED, THICKNESS)
  cv2.imwrite(file_name[:-4] + '_result.jpg', copy)
  return num_illuminati_found

### MAIN PROGRAM BELOW ###

print '---> executing: hack illuminati'
sleep(1)
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

