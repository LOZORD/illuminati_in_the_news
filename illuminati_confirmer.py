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

  big_box_w = min(box_w * 5, orig_w)
  big_box_h = min(box_h * 5, orig_h)

  for i in range(2,5):
    crop_x = box_x - int(box_x/i)
    crop_y = box_y - int(box_y/i)

    crop_w = box_x+box_w + int(box_x/i)
    crop_h = box_y+box_h + int(box_y/i)

    crop_image = img[crop_y:crop_h, crop_x:crop_w]

    #display_img(crop_image)

    dst = cv2.resize(crop_image, (orig_w, orig_h))

    #finally, write the new file
    cv2.imwrite(file_name[:-4]+'_zoom_'+str(i-1)+'.jpg', dst)

  cv2.drawContours(copy, [largest_contour], FIRST, RED, THICKNESS)

  global cage_mode_on
  global cage_image_name
  if cage_mode_on:
    # load the cage img
    if cage_image_name == 'BEES.png':
      cage_image = cv2.imread(cage_image_name, -1)
    else:
      cage_image = cv2.imread(cage_image_name)
    # re-scale it to fit in the triangle
    cage_image = cv2.resize(cage_image, (box_w, box_h))
    #offset_on_triangle = int(box_y + (box_h / 2))

    if cage_image_name == 'BEES.png':
      for c in range(0,3):
        img[box_y:box_y+cage_image.shape[0], box_x:box_x+cage_image.shape[1], c] = cage_image[:,:,c] * (cage_image[:,:,3]/255.0) + img[box_y:box_y+cage_image.shape[0], box_x:box_x+cage_image.shape[1], c] * (1.0 - cage_image[:,:,3]/255.0)
    else:
      '''
      cage_image = np.array(cage_image).flatten()
      print '***'
      print str(cage_image)
      '''
      cage_h = cage_image.shape[0]
      cage_w = cage_image.shape[1]
      img[box_y:box_y+cage_h, box_x:box_x+cage_w, ] = cage_image
  cv2.imwrite(file_name[:-4] + '_result.jpg', copy)
  return num_illuminati_found

def display_img (img):
  cv2.imshow('image',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

### MAIN PROGRAM BELOW ###

print '---> executing: hack illuminati'
sleep(1)
print 'running illuminati.exe'
sleep(1)
illuminati_count = 0

cage_mode_on = False
cage_image_name = None

if sys.argv[-1] == 'BEES?' or sys.argv[-1] == 'DECLARATION?':
  cage_mode_on = True
  cage_image_name = 'BEES.png' if sys.argv[-1] == 'BEES?' else 'DECLARATION.jpg'
  sys.argv = sys.argv[:-1]

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

