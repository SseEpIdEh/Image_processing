import cv2
img1=cv2.imread("D:/SEPIDEH/Flag_of_USA.jpg")
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
#if you want to have access to other changing color functions

flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)






cv2.waitKey(0)
cv2.destroyAllWindows()