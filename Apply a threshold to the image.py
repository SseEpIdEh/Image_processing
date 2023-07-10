import cv2

img = cv2.imread('D:/SEPIDEH/Flag_of_USA.jpg', 0)
print(img.shape)

desired_width = 200
desired_height = 300
resized_img = cv2.resize(img, (desired_width, desired_height))
print(resized_img.shape)
cv2.imshow('resized_img',resized_img )
ret,thresh1 = cv2.threshold(resized_img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(resized_img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(resized_img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(resized_img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(resized_img,127,255,cv2.THRESH_TOZERO_INV)

#cv2.imshow('img1', thresh1)
#cv2.imshow('img2',thresh2 )
#cv2.imshow('img3',thresh3 )
cv2.imshow('img4',thresh3 )
cv2.imshow('img5',thresh3 )

cv2.waitKey(0)
cv2.destroyAllWindows()