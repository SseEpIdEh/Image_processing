import cv2

import cv2
import numpy as np

img = cv2.imread("D:/SEPIDEH/dots.jpg",cv2.IMREAD_GRAYSCALE)
width = 400
height = 300
img1 = cv2.resize(img, (width, height))

# Apply adaptive thresholding to obtain a binary image
# In digital image processing, a binary image is commonly represented using a 2D matrix
# or array of pixels, where each pixel has a value of either 0 or 1. The value 0 typically represents the background,
# while the value 1 represents the foreground or the object of interest.
binary_image = cv2.adaptiveThreshold(img1, 255, cv2.THRESH_BINARY,cv2.ADAPTIVE_THRESH_MEAN_C, 11, 2)

# Define the structuring element for morphological operations
structuring_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
# Morphological operations (like getStructuringElement)primarily focus on the spatial arrangement of pixels
# Apply closing operation for noise removal and object connectivity
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, structuring_element)

# Apply distance transform
dist_transform = cv2.distanceTransform(closed_image, cv2.DIST_L2, 3)

# Threshold the distance transform to obtain markers
_, markers = cv2.threshold(dist_transform, 0.3 * dist_transform.max(), 255, cv2.THRESH_BINARY)
markers= markers.astype(np.uint8)
img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
# Apply watershed algorithm for object segmentation
markers = cv2.connectedComponents(markers)[1]
markers = cv2.watershed(img1, markers)
marked_image = cv2.cvtColor(markers.astype(np.uint8),cv2.COLOR_RGB2BGR)

# Display the original image, binary image, and segmented objects
cv2.imshow('Original Image', img1)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Segmented Objects', marked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
