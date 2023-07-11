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



#cv2.threshold:

**cv2.threshold is a simple global thresholding method where a fixed threshold value is applied to all pixels in the image.**
  
It takes the following parameters:
  
src: The input image.
  
thresh: The threshold value used for classification.
                                
maxval: The maximum value assigned to pixels that exceed the threshold.
  
type: The type of thresholding applied, such as binary, truncated, to zero, etc.
  
The function converts the input image into a binary image by comparing pixel intensities with the threshold value.
cv2.adaptiveThreshold:

#cv2.adaptiveThreshold is an adaptive thresholding method where the threshold value is calculated locally based on the image characteristics in the neighborhood of each pixel.
  
It takes the following parameters:
  
src: The input image.
  
maxval: The maximum value assigned to pixels that exceed the threshold.
  
adaptiveMethod: The method used to calculate the threshold value.
  
thresholdType: The type of thresholding applied, such as binary or inverted binary.
  
blockSize: The size of the neighborhood used for threshold calculation.
  
C: A constant subtracted from the mean or weighted mean.

The function divides the image into smaller regions (blocks) and calculates a threshold value for each block based on its local characteristics.
                                                                                             
This adaptive thresholding allows for better handling of varying lighting conditions or uneven illumination across the image.

                          
********In summary, cv2.threshold applies a fixed global threshold to the entire image, while cv2.adaptiveThreshold calculates a local threshold for each pixel based on its neighborhood. 
Thdaptive thresholding method is beneficial when dealing with images containing non-uniform lighting
conditions or when a single global threshold is not sufficient for accurate image segmentation or object extraction.*******
