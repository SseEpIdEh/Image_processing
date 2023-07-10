import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Figure2.png")
cv2.imshow("img1",img)
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)  #MEANS DOUBLE IT EACH WAY
cv2.imshow("RES",res)
res1=cv2.resize(img,None,fx=2,fy=2)    #just show they are the same(res and res1)
cv2.imshow("RES1",res1)

#TRANSLATION: means we are able to change the palce of the shape inside the image
row,col,_ = img.shape
M=np.float32([[1,0,100],[0,1,50]])      #move to right
dst=cv2.warpAffine(img,M,(col,row))
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

