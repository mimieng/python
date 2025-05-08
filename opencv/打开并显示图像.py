import cv2
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 640, 480)
img=cv2.imread("./OIP-C.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()