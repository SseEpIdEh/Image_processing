import cv2
img = cv2.imread("D:/SEPIDEH/football.jpg")
# Define the desired width and height for the resized image
desired_width = 800
desired_height = 600
# Resize the image
resized_img = cv2.resize(img, (desired_width, desired_height))

#cv2.namedWindow('image_WINDOW_NORMAL', cv2.WINDOW_NORMAL)
#cv2.imshow('image_WINDOW_NORMAL', img)
b, g, r = cv2.split(resized_img)
#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)
img2=cv2.merge((b,r,g))
cv2.imshow("img2",img2)
img3=cv2.merge((b,g,r))
cv2.imshow("img3",img3)
resized_img[:, :, 2]=0     # [0:blue, 1:green,2: red]  #means whole red pixel should be zero
resized_img[:, :, 1]=0       #whole green pixel should be zero,
cv2.imshow("resized_img",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()