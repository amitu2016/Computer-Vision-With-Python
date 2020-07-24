import cv2
import numpy

# colour, greyscale, unchanged ----> 1, 0, -1

myimage = cv2.imread('DeepLearning.jpeg',0)
myimage2 = cv2.imread('DeepLearning.jpeg',-1)
cv2.imshow("image window",myimage)
cv2.imshow("image window2",myimage2)
cv2.imwrite('DL2.jpeg',myimage)


cv2.waitKey(0)
cv2.destroyAllWindows()