import cv2
img= cv2.imread("./OIP-C.jpg")
h,w,c=img.shape
# for w in range(w):
#     for h in range(h):
#
padding=20
img[:padding,:]=[255,255,255]
img[h-padding:,:]=[255,0,0]
img[:,:padding]=[0,255,255]
img[:,w-padding:]=[0,0,255]


logo=cv2.imread("./OIP-C.jpg")
w,h,c=logo.shape
w=50
h=50
s_logo=cv2.resize(logo,(w,h))
img[:w,:h]=s_logo


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()