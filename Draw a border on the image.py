from typing import Any

import cv2
from cv2 import UMat

img = cv2.imread("D:/SEPIDEH/football.jpg")
desired_width = 200
desired_height = 200
resized_img = cv2.resize(img, (desired_width, desired_height))
constant=cv2.copyMakeBorder(resized_img,20,20,20,20,cv2.BORDER_CONSTANT,value=(255,0,0))
REFLECT=cv2.copyMakeBorder(resized_img,30,30,20,20,cv2.BORDER_REFLECT)
WRAP=cv2.copyMakeBorder(resized_img,30,30,20,20,cv2.BORDER_WRAP)
REPLICATE=cv2.copyMakeBorder(resized_img,10,10,20,50,cv2.BORDER_REPLICATE)
cv2.imshow("constant",constant)
cv2.imshow("REFLECT",REFLECT)
cv2.imshow("WRAP",WRAP)
cv2.imshow("REPLICATE",REPLICATE)

cv2.waitKey(0)
cv2.destroyAllWindows()