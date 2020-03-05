#Reads and Displays Image which has already been saved in computer

import cv2

#To Read Image
#in imread(), the first parameter is the image name
#Second Parameter is (-1,0,1) where 0 is grayscale and 1 is normal image
img = cv2.imread('chessboard.png',1)
#img = cv2.imread('aryan.jpeg',-1)

print(img) #prints the array in image

cv2.imshow('Image of Chessboard',img)#Displays image but for very small time.
#cv2.waitKey(5000)  #Delays the image from shutting down

#cv2.waitKey(0)  # Image window will only close after pressing close button

k= cv2.waitKey(0)

if k==27 :  #escape key
    cv2.destroyAllWindows() #Destroys image window
elif k == ord('s') #s key
    #cv2.imwrite('chessboard_copy.png',img) #writes image in the form of a file
    cv2.destroyAllWindows()
