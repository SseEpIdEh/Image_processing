import cv2

pic = cv2.imread('D:/SEPIDEH/Flag_of_the_United_States.png')
pic1 = cv2.imread('D:/SEPIDEH/Flag_of_the_United_States.png', 1)
pic2 = cv2.imread('D:/SEPIDEH/Flag_of_the_United_States.png', 0)

cv2.imshow("pic", pic)
cv2.imshow("pic1", pic1)
cv2.imshow("pic2", pic2)

cv2.waitKey(0)
cv2.destroyAllWindows()
