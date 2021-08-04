import cv2

#to read image
img=cv2.imread('lena.png')

cv2.imshow("output",img)
#to show output for long time
cv2.waitKey(0)
#read videos
cap=cv2.VideoCapture("WIN_20210804_20_03_25_Pro.mp4")
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

#read camera
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,490)

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
