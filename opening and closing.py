import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Dots1.jpg")
width=400
height=300
img1 = cv2.resize(img, (width, height))
kernel=np.ones((11,11),np.uint8)    #the more kernel, the more zero we have(black)
opening=cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)
cv2.imshow("img1",img1)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()