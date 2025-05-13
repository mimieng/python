import cv2
cap = cv2.VideoCapture(r'D:\python-learning\1.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# 前后景的分离
bgSegMog = cv2.bgsegm.createBackgroundSubtractorMOG()
line_y=600
offset = 20
car_cnt = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("no frame")
        break
    # 灰度图
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mask = bgSegMog.apply(frame_gray)
    # 腐蚀后的图
    erode_frame = cv2.erode(mask, kernel)
    # # 膨胀
    dilate_frame = cv2.dilate(erode_frame, kernel)
    # dilate_frame = cv2.dilate(dilate_frame, kernel)
    # 查找轮廓
    contours, hierarchy = cv2.findContours(dilate_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame, (0, line_y), (2400, line_y), (0, 0, 255), 2)
    for coutour  in contours:
        # 获取轮廓外接矩形
        x,y,w,h = cv2.boundingRect(coutour)
        if w < 90 and h < 90:
            continue

        if y > (line_y - offset) and y< (line_y + offset):
            car_cnt+=1
            pass
        cv2.putText(frame,str(car_cnt),(100,100), cv2.FONT_ITALIC, 2, (0,0,255), 2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow('frame', frame)
    cv2.imshow('frame_gray', frame_gray)
    cv2.imshow('mask',dilate_frame )
    cv2.waitKey(25)