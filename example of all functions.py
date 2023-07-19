import cv2
import numpy as np
img = cv2.imread("D:/SEPIDEH/football.jpg",cv2.IMREAD_GRAYSCALE)
width=400
height=300
img1 = cv2.resize(img, (width, height))

# Apply binary thresholding to obtain a binary image
_, binary_image = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY)

# Define the structuring element for morphological operations
structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply dilation #to expand or thicken the foreground regions in the binary image.
dilated_image = cv2.dilate(binary_image, structuring_element, iterations=1)

# Apply erosion  #to shrink or thin the foreground regions.
eroded_image = cv2.erode(binary_image, structuring_element, iterations=1)

# Display the original, dilated, and eroded images
cv2.imshow('Original Image', img1)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
