# Draw Contours on an image

import numpy as np
import cv2

img = cv2.imread('opencv_logo.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray,127,255,0)

_, contours, _= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cv2.findContours(grayscale_image,method,approximation_to_apply)
print("Number of Contours : " + str(len(contours)))

cv2.drawContours(img,contours, -1,(0,255,0), 3)
# -1 implies draw all contours

#to find specific contours , type 0,1,2.. etc instead of -1
cv2.imshow('Image' ,img)
cv2.imshow('Image Gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
