import cv2
import numpy as np

img=cv2.imread("lena.png")


imgResize=cv2.resize(img,(1000,1000))
imgCropped=img[0:200,0:400,1:2]
cv2.imshow("output",img)
cv2.imshow("resized",imgResize)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)