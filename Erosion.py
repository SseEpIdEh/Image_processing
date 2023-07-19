# Erosion: Erosion shrinks or thins the boundaries of foreground regions in an image.
# It removes pixels from the boundaries,
# making objects smaller and breaking thin connections between objects.

import cv2
import numpy as np
img = cv2.imread('D:/SEPIDEH/football.jpg')
width=400
height=300
img1 = cv2.resize(img, (width, height))
kernel=np.ones((10,10),np.uint8)    #the more kernel, the more zero we have(black)
erosion=cv2.erode(img1,kernel)
cv2.imshow("img1",img1)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()