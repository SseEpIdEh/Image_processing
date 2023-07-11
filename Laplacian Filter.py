# Laplacian Filter: This filter enhances the edges in an image by computing the second derivative
# of the image intensity.
# It highlights areas of rapid intensity changes, making edges more pronounced.

import cv2
image = cv2.imread('football.jpg',cv2.IMREAD_GRAYSCALE)
width=400
height=300
img1 = cv2.resize(image, (width, height))

# Apply Laplacian filter
filtered_image = cv2.Laplacian(img1, cv2.CV_64F)

# Convert the filtered image to uint8
# After applying the Laplacian filter, the resulting image may have negative values.
# To visualize the filtered image correctly, we convert it to the uint8 data type using cv2.convertScaleAbs().
# This function takes the absolute value of the filtered image and scales it to the range of 0 to 255.
filtered_image = cv2.convertScaleAbs(filtered_image)

# Display the original and filtered images
cv2.imshow('Original Image', img1)
cv2.imshow('Laplacian Filter', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
