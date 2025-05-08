import cv2
# 创建视频采集对象
cap=cv2.VideoCapture(0)
while  True:
    retval,image = cap.read()
    cv2.imshow("image",image)
    cv2.waitKey(25)