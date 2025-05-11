import cv2

import  numpy as np
img=cv2.imread('1.jpg')
kernel=np.ones((5,5),np.uint8)
erode=cv2.erode(img,kernel,iterations=2)
cv2.imshow('img',img)
cv2.imshow('erode',erode)
cv2.waitKey(0)