import cv2
boom = cv2.imread("D:/SEPIDEH/Boom.jpg")
boom = cv2.line(boom, (0, 0), (200, 400), (255, 0, 0,), 5)
cv2.imshow("boom",boom)
boom=cv2.rectangle(boom,(100,50),(300,200),(0,255,0),3)
cv2.imshow("boom",boom)
boom=cv2.circle(boom,(300,300),60,(0,0,255),-1)
cv2.imshow("boom",boom)
boom=cv2.ellipse(boom,(150,240),(80,30),0,0,180,255,-1)
cv2.imshow("boom",boom)
boom=cv2.ellipse(boom,(300,500),(80,30),0,0,360,255,0)
cv2.imshow("boom",boom)
import numpy as np
pts=np.array([[10,5],[20,30],[20,20],[50,10]])
boom=cv2.polylines(boom,[pts],True,(0,0,0))
cv2.imshow("boom",boom)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(boom,"opencv",(10,100),font,2,(250,0,250),2)
cv2.imshow("boom",boom)




cv2.waitKey(0)
cv2.destroyAllWindows()


