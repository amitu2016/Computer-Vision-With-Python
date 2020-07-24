import cv2
import numpy

myimage = cv2.imread('bookpage.jpg', -1)
myimage2 = cv2.imread('bookpage.jpg', 0)

# 0(black) - 255(white)

retval , myimage3 = cv2.threshold(myimage,9,255,cv2.THRESH_BINARY)

cv2.imshow('image1',myimage)
cv2.imshow('image2',myimage2)
cv2.imshow('image3',myimage3)



cv2.waitKey(0)
cv2.destroyAllWindows()