import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Dots1.jpg")
width=400
height=300
img1 = cv2.resize(img, (width, height))
kernel=np.ones((15,15),np.uint8)    #the more kernel, the more zero we have(black)
gradient=cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("img1",img1)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()