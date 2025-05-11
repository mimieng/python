import cv2

import  numpy as np
img=cv2.imread('1.jpg')
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
erode=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('img',img)
cv2.imshow('erode',erode)
cv2.waitKey(0)