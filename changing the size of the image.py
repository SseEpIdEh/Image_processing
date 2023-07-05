import cv2

pic = cv2.imread('D:/SEPIDEH/Flag_of_the_United_States.png')

cv2.namedWindow('image_AUTOSIZE',cv2.WINDOW_AUTOSIZE)
cv2.imshow('image_AUTOSIZE',pic)

cv2.namedWindow('image_WINDOW_NORMAL',cv2.WINDOW_NORMAL)
cv2.imshow('image_WINDOW_NORMAL',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
