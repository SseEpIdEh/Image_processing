import cv2
img =cv2.imread("D:/SEPIDEH/Boom.jpg")
cv2.imshow("img",img)

#img.shape
print(img.shape)          #(640,841,3)
print(img.dtype)           #uint8

px=img[100,100]
print(px)

blue=img[150,150,0]          # [0:Blue,1:Green, 2:Red]  index
print(blue)

red=img[150,150,2]          # [0:Blue,1:Green, 2:Red]  index
print(red)

###changing the color of pixel

for i in range (100):
    img[i,i]=[0,0,0]
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()