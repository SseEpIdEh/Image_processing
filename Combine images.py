import cv2
img1 = cv2.imread("D:/SEPIDEH/football.jpg")
img2 = cv2.imread("D:/SEPIDEH/Flag_of_USA.jpg")
print(img2.shape)

desired_width = 1200
desired_height = 632
resized_img = cv2.resize(img1, (desired_width, desired_height))
print(resized_img.shape)
#for combining the images ,we need to have same shape in terms of width and height

#cv2.imshow("resized_img",resized_img)
#cv2.imshow("img2",img2)
img3=cv2.add(resized_img,img2)
cv2.imshow("img3",img3)

#now we want to combine two images with different size
img4=cv2.addWeighted(resized_img,0.7,img2,0.3,0)
cv2.imshow("img4",img4)

img5=cv2.addWeighted(img2,0.7,resized_img,0.3,0)
cv2.imshow("img5",img5)

cv2.waitKey(0)
cv2.destroyAllWindows()