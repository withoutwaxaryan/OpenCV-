#captures video from live feed/ video in computer 

import cv2

#Captures image from webcam ,you can change the number for multiple cams
cap=cv2.VideoCapture(0)



#Set Camera Parameters in OpenCV
#cap.set(3,720)
#cap.set(4,1280)
#print(cap.get(3))
#print(cap.get(4))


fourcc = cv2.VideoWriter_fourcc(*'XVID')#FOurcc code
out = cv2.VideoWriter('output.avi', fourcc , 20.0, (640,480)) #To save the video

#cap=cv2.VideoCapture('name.avi') #to capture frames from existing video

#while(True) :
print(cap.isOpened())
while(cap.isOpened()) :
    ret , frame = cap.read() #ret is TRue or False
                             #frame is the image read

    if ret == True : 
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts to grayscale

        cv2.imshow('frame', gray) #displays the image

        if cv2.waitKey(1)  & 0xFF == ord('q') : # press q to exit
            break
    else:
        break

cap.release() #releases the resources
out.release()
cv2.destroyAllWindows()
