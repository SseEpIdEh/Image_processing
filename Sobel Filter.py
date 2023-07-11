#Sobel Filter:
# Sobel filters are used for edge detection.
# They calculate the gradient of the image intensity at each pixel
# and highlight regions of significant intensity changes, which correspond to edges.
import cv2
import numpy as np
image = cv2.imread('football.jpg')#,cv2.IMREAD_GRAYSCALE)
width=400
height=300
img1 = cv2.resize(image, (width, height))

# Apply Sobel filter
gradient_x = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_magnitude = cv2.normalize(gradient_magnitude, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#we normalize while  enhance or highlight specific features like edges.
# Display the original and filtered images
cv2.imshow('Original Image', img1)
cv2.imshow('Sobel Filter', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
