import cv2

img = cv2.imread("D:/SEPIDEH/football.jpg")
cv2.namedWindow('image_WINDOW_NORMAL', cv2.WINDOW_NORMAL)
cv2.imshow('image_WINDOW_NORMAL', img)
print(img.size)  # 53747712
print(img.shape)  # ((3124, 2835, 3)
# now we should guess where the ball place is??!
ball=img[2600:3000,100:550]
print(ball.shape)
#cv2.namedWindow('image_WINDOW_NORMAL', cv2.WINDOW_NORMAL)
#cv2.imshow('image_WINDOW_NORMAL', ball)
#cv2.imshow("ball",ball)
img[2600:3000,1500:1950]=ball
cv2.imshow("image_WINDOW_NORMAL",img)
img[2600:3000,2000:2450]=ball
cv2.imshow("image_WINDOW_NORMAL",img)
img[2600:3000,1000:1450]=ball
cv2.imshow("image_WINDOW_NORMAL",img)
img[2600:3000,550:1000]=ball
cv2.imshow("image_WINDOW_NORMAL",img)


cv2.waitKey(0)
cv2.destroyAllWindows()





















