# 先膨胀,再腐蚀
# 去除图像内的小点
import cv2
import numpy as np

img = cv2.imread('./1.jpg')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

img_dilation = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=1)
# img_dilation = cv2.dilate(img, kernel, iterations=1)
# img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)