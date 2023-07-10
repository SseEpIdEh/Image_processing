#M = cv2.getRotationMatrix2D(center, angle, scale)

#center: This parameter specifies the center point of rotation.
# It is represented as a tuple (center_x, center_y). The rotation will be performed around this center point.

#angle: This parameter represents the angle of rotation in degrees.
# It specifies the amount and direction of rotation. Positive values indicate clockwise rotation,
# while negative values indicate counterclockwise rotation.

#scale: This parameter determines the scale factor of the output image.
# It allows you to resize the output image.
# A scale factor of 1 means the output image will have the same size as the input image.
# You can use values greater than 1 to enlarge the output image or values between 0 and 1 to shrink it.
# (col/2, col/2) is used as the center point, which means the image will rotate around its center.
#90 represents a clockwise rotation of 90 degrees.
#1: This parameter represents the scale factor. It determines the scale of the output image.
# A scale factor of 1 means the output image will have the same size as the input image.
#getRotationMatrix2D function from OpenCV to create a 2D rotation matrix for rotating an image.
import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/Figure2.png")
cv2.imshow("img1",img)
row,col,_ = img.shape
M=np.float32([[1,0,100],[0,1,50]])      #move to right
dst=cv2.warpAffine(img,M,(col,row))    #change the place of image(inside)
#cv2.imshow("dst",dst)
row,col,_ = img.shape
M=cv2.getRotationMatrix2D((col/2,col/2),90,1)
dst1=cv2.warpAffine(img,M,(row,col))
cv2.imshow("dst1",dst1)
pts1 =np.float32([[50,50],[200,50],[50,200]])
pts2 =np.float32([[10,100],[250,50],[100,250]])
M =cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(row,col))
cv2.imshow("dst",dst)





cv2.waitKey(0)
cv2.destroyAllWindows()
