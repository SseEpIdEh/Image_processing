
# Dilation: Dilation expands or thickens the boundaries of foreground regions in an image.
# It adds pixels to the boundaries,
# making objects larger and filling in gaps or holes within the objects.


import cv2
import numpy as np
img = cv2.imread('D:/SEPIDEH/football.jpg')
width=400
height=300
img1 = cv2.resize(img, (width, height))
kernel=np.ones((10,10),np.uint8)    #the more kernel, the more zero we have(black)
dilation=cv2.dilate(img1,kernel)
cv2.imshow("img1",img1)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()