import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,512),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,150),(234,123,231),2,cv2.FILLED)
cv2.circle(img,(200,200),50,(0,255,0),5)

cv2.putText(img,"OPENCV",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(150,0,100),2)
cv2.imshow("image",img)
cv2.waitKey(0)