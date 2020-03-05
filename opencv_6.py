#Object Detection and Tracking using Live Feed using HSV Color Space

#HSV (Hue,Saturation,Value)
#Known as the HexCone Model


import cv2
import numpy as np

def nothing(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")


#TrackBars
cv2.createTrackbar("LH", "Tracking", 0 ,255 ,nothing)
cv2.createTrackbar("LS", "Tracking", 0 ,255 ,nothing)
cv2.createTrackbar("LV", "Tracking", 0 ,255 ,nothing)
cv2.createTrackbar("UH", "Tracking", 255 ,255 ,nothing)
cv2.createTrackbar("US", "Tracking", 255,255 ,nothing)
cv2.createTrackbar("UV", "Tracking", 255 ,255 ,nothing)

while True :

    _, frame = cap.read()

    #Convert Image to HSV   
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    low_hue = cv2.getTrackbarPos("LH", "Tracking")
    low_saturation = cv2.getTrackbarPos("LS", "Tracking")
    low_value = cv2.getTrackbarPos("LV", "Tracking")

    upper_hue = cv2.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv2.getTrackbarPos("US", "Tracking")
    upper_value = cv2.getTrackbarPos("UV", "Tracking")
    
    
    low_blue = np.array([low_hue,low_saturation,low_value])
    high_blue = np.array([upper_hue,upper_saturation,upper_value])
    
    #Threshold the Image to get only blue colour
    mask = cv2.inRange(hsv,low_blue,high_blue)

    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27 :
        break
    
cap.release()
cv2.destroyAllWindows()
