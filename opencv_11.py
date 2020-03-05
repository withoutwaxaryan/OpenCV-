#Detect Geometric Shapes using OpenCV

import numpy as np
import cv2

img = cv2.imread('shapes.webp')
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgGrey,240,255,cv2.THRESH_BINARY)
_, contours, _=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours :
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    #Approximates the Polygonal curve
    cv2.drawContours(img,[approx],0,(0,0,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if (len(approx)== 3) :
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    elif (len(approx)== 4) :
        #To check for Rectangle and Square
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <=1.05 :
        #Due to Noise in Contouring
             cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
        else:
            cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    elif (len(approx)== 5) :
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
    if (len(approx) > 5) :
        if len(approx) <= 13 : #random number
            cv2.putText(img,"Polygon",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))
        else :
            cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,0))


cv2.imshow('Shapes',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
