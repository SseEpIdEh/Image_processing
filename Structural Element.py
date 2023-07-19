import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Dots1.jpg")
width=400
height=300
img1 = cv2.resize(img, (width, height))
import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Dots1.jpg")
width=400
height=300
img1 = cv2.resize(img, (width, height))
element1=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
element2=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
element3=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

print(element1)

#[[1 1 1 1 1],[1 1 1 1 1],[1 1 1 1 1],[1 1 1 1 1],[1 1 1 1 1]]
print(element2)
#[[0 0 1 0 0],[1 1 1 1 1],[1 1 1 1 1],[1 1 1 1 1],[0 0 1 0 0]]
print(element3)
#[[0 0 1 0 0],[0 0 1 0 0],[1 1 1 1 1],[0 0 1 0 0],[0 0 1 0 0]]


kernel=element2=cv2.getStructuringElement(cv2.MORPH_CROSS,(9,9))
erosion=cv2.erode(img1,kernel)
cv2.imshow("img1",img1)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()