#Simple Image Thresholding
#Used For Separating Object from Background
#Comparison of Predefined Image to a Threshold Value

import cv2
import numpy as np

img = cv2.imread('gradient.jpeg',0)
#_ implies ret which is True

#_, th1 = cv2.threshold(img, 127 , 255 ,cv2.THRESH_BINARY)


#Thresh Binary implies if pixel value is less than 127, then assign it 0, otherwise 255
#Therefore we have only two parts to the image

#_, th2 = cv2.threshold(img, 127 , 255 ,cv2.THRESH_BINARY_INV)

#Make the image inverse of binary
#that is, less than 127 will be given value 255, and more than 127 will be 0 pixel value


#_, th3 = cv2.threshold(img, 127 , 255 ,cv2.THRESH_TRUNC)

#Value less than 127 will not change, and after 127 , will remain 127 till the end


#_, th4 = cv2.threshold(img, 127 , 255 ,cv2.THRESH_TOZERO)

#Value less than 127 will be 0, and after 127 all the pixels will remain the same

, th5 = cv2.threshold(img, 127 , 255 ,cv2.THRESH_TOZERO_INV)

#value of pixels will be original but after 127 it will be 0

cv2.imshow("Image", img)
#cv2.imshow("TH1", th1 )
#cv2.imshow("TH2",th2)
#cv2.imshow("TH3",th3)
#cv2.imshow("TH4",th4)
cv2.imshow("TH5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
