import cv2
import numpy


myimage = cv2.imread('football.jpg', -1)

print(myimage.shape)

myimage2 = myimage[80:170,420:510]

myimage[70:160, 520:610] = myimage2
myimage[60:150, 620:710] = myimage2
myimage[50:140, 720:810] = myimage2
myimage[40:130, 820:910] = myimage2
myimage[30:120, 920:1010] = myimage2

cv2.imshow("image window",myimage)
cv2.imshow("image window22",myimage2)




cv2.waitKey(0)
cv2.destroyAllWindows()