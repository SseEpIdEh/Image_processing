import cv2
import numpy as np
img = cv2.imread('football.jpg')
width=400
height=300
img1 = cv2.resize(img, (width, height))
bilateral=cv2.bilateralFilter(img1, 15,100,100)
cv2.imshow("img1",img1)
cv2.imshow("bilateral",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()