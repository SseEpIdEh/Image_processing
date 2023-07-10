#Perspective Transformation
#we need a matrix 3*3

import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Figure2.png")
cv2.imshow("img1",img)

pts1 =np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 =np.float32([[0,0],[300,0],[0,300],[300,300]])
M =cv2.getPerspectiveTransform(pts1,pts2)
M =cv2.getPerspectiveTransform(pts1,pts2)
row,col ,ch =img.shape
dst=cv2.warpPerspective(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

