import cv2
import numpy

# colour, greyscale, unchanged ----> 1, 0, -1

myimage = cv2.imread('DeepLearning.jpeg',0)
myimage2 = cv2.imread('DeepLearning.jpeg',-1)

cv2.line(myimage2,(100,100), (500,500), (0,0,0),10)  # DRAWING LINE ON IMAGE ##BGR
cv2.rectangle(myimage2,(100,100), (500,500), (0,0,255), 5)
cv2.circle(myimage2,(300,300), 200, (255,0,0), 10)

cv2.putText(myimage2,'The Future is Here',(600,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

print(myimage2.shape)

myimage3 = myimage2[100:550,300:700]
myimage2[0:450,0:400] = myimage3

cv2.imshow("image window",myimage)
cv2.imshow("image window2",myimage2)
cv2.imshow("image window3",myimage3)
#cv2.imwrite('DL2.jpeg',myimage3)


cv2.waitKey(0)
cv2.destroyAllWindows()