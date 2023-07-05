import cv2
pic = cv2.imread('D:/SEPIDEH/Flag_of_the_United_States.png')
cv2.imwrite('D:/SEPIDEH/Flag_of_USA.jpg',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()