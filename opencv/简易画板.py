import cv2

qi=(-1,-1)
zong=(-1,-1)

def on_mouse(event, x, y, flags, param):
    global qi,zong
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y,'anxia')
        qi=(x,y)
    if event == cv2.EVENT_LBUTTONUP:
        print(x, y,"tanqi")
        zong=(x,y)
        cv2.line(img, qi, zong, (0, 255, 255), 2)
        cv2.imshow('image', img)

if __name__ == '__main__':
    img = cv2.imread('./OIP-C.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 640, 480)
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()