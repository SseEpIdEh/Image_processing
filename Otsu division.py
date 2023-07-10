import cv2

img = cv2.imread("D:/SEPIDEH/Figure2.png",0)
#desired_width = 200
#desired_height = 300
#resized_img = cv2.resize(img, (desired_width, desired_height))
#print(img.shape)
ret1,th1= cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow('th1',th1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




img = cv2.imread("D:/SEPIDEH/Figure2.png")
cv2.imshow("img1",img)
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)  #MEANS DOUBLE IT EACH WAY
cv2.imshow("RES",res)
cv2.imshow("img",img)
res1=cv2.resize(img,None,fx=2,fy=2)
cv2.imshow("RES1",res1)

#TRANSLATION: means we are able to change the palce of the shape inside the image
row,col,_ = img.shape
M=np.float32([[1,0,100],[0,1,50]])      #move to right
dst=cv2.warpAffine(img,M,(col,row))
cv2.imshow("dst",dst)