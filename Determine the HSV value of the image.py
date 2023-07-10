import cv2
import numpy as np
green=np.uint8([[[0,255,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)     #[[[60 255  255]]]   [Hue range[0,179]   Saturation range [0,255]   value range[0,255]]

#with this code we realize that green in the HSV space ,which parameter has.