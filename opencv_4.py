#Binding Trackbar to OpenCV Window

import numpy as np
import cv2

def nothing(x):
    print(x) #will print the value of change in trackbar
    
#Create a black image , a window
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image') 


#Creating Trackbar
#(nameof entity to be changed,the image,range_low,range_high,function to call)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)





while(1) :
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k == 27 :
        break

    #Assigning the Values of the Trackbar
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')

    #Giving values to the Image
    img[:] = [b,g,r]
    
cv2.destroyAllWindows()


