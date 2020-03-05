#Draw geometric shapes on images

import numpy as np
import cv2
import datetime

#img = np.zeros([100,100,3],np.uint8)
#creating black image using numpy zeroes


#reading image through openCV
img = cv2.imread('chessboard.png',1)

#img = cv2.line(img, (0,255) , (255,0), (0,0,255), 5)
# Line Function ( Image, from, to ,BGR,thickness)

#img = cv2.arrowedLine(img, (0,0) , (255,255), (0,0,255), 5)
# ArrowLine Function ( Image, from, to ,BGR,thickness)

img = cv2.rectangle(img,(0,0),(210,210),(0,0,255),5)
#Rectangle Function(img,topleft coordinate,bottomright coordinate, BGR,thickness)


#img = cv2.rectangle(img,(0,0),(210,210),(0,0,255),-1)
#Since thickness is -1 , it will fill the rectangle with colour of the border

#img = cv2.circle(img,(105,105) , 50,(0,255,0),-1)
#Circle Function (img,center ,radius,BGR,thickness)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV', (10,50), font , 1 ,(255,0,0),5,cv2.LINE_AA)
#Puts Text(Image,text,coordinates,font,fontsize,fontcolor,thickness,linetype)

#To Add Current Date and Time
#datet=str(datetime.datetime.now())
#img = cv2.putText(img,datet, (10,50), font , 1 ,(255,0,0),5,cv2.LINE_AA)

cv2.imshow('chessboard_image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
