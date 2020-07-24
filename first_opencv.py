import cv2
import numpy


myimage = cv2.imread('DeepLearning.jpeg')
cv2.imshow("image window",myimage)

cv2.waitKey(0)
cv2.destroyAllWindows()