#Detect BLue Object  using OpenCV LiveFeed

import numpy as np
import cv2

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

    blur = cv2.GaussianBlur(frame , (5,5), 0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    low_hue = cv2.getTrackbarPos("LH", "Tracking")
    low_saturation = cv2.getTrackbarPos("LS", "Tracking")
    low_value = cv2.getTrackbarPos("LV", "Tracking")

    upper_hue = cv2.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv2.getTrackbarPos("US", "Tracking")
    upper_value = cv2.getTrackbarPos("UV", "Tracking")
    
    
    low_blue = np.array([low_hue,low_saturation,low_value])
    high_blue = np.array([upper_hue,upper_saturation,upper_value])
    
    #got these values using trackbar
    #low_blue = np.array([108,73,75])
    #high_blue = np.array([121,255,255])
    mask = cv2.inRange(hsv,low_blue,high_blue)

    #Now Get Contours

    _, contours ,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for contour in contours :
        area = cv2.contourArea(contour)
        print(area) #to make the next statement

        if area > 800 : 
            cv2.drawContours(frame, contour, -1 , (0,255,0) , 3)
            cv2.putText(frame,"Blue Object", (10,20),cv2.FONT_HERSHEY_SIMPLEX,
                        1,(0,0,255),3)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)
    if key == 27 : 
        break

cap.release()
cv2.destroyAllWindows()
    
