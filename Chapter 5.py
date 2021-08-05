import cv2
import numpy as np

# to get the top view
img=cv2.imread("cards.jpg")

#coordinates of the card
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])

width,height=[250,350]

pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)

imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("perspectic",imgOutput)
cv2.waitKey(0)