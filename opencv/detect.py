import cv2
import numpy as np


class Detect:
    def __init__(self):
        classifier = cv2.CascadeClassifier()
        self.classifier = classifier
        # 加载特征文件
        # cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
        classifier.load(r'D:\python-learning\model\haarcascade_frontalface_alt.xml')
        # 不能有中文

        moth_classifier = cv2.CascadeClassifier()
        self.moth_classifier = moth_classifier
        # 加载特征文件
        # 获取Haar分类器文件夹路径


        moth_classifier.load(r'D:\python-learning\model\haarcascade_mcs_mouth.xml')
        self.logo= cv2.imread('./OIP-C.jpg')

    def face_detect(self, face_img):

        # 检测人脸，返回包含人脸矩形列表
        face_rect = self.classifier.detectMultiScale(face_img)
        for rect in face_rect:
            x, y, w, h = rect
            cv2.rectangle(face_img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
            self.draw_logo2(face_img,rect,self.logo)
            # self.mouth_detect(rect,face_img)

    def mouth_detect(self,face_rect, face_img):
        # 检测嘴部区域
        mouth_rect = self.moth_classifier.detectMultiScale(face_img)
        face_min_x, face_min_y, face_w, face_h = face_rect
        face_max_x=face_min_x+face_w
        face_max_y=face_min_y+face_h
        for rect in mouth_rect:
            x, y, w, h = rect
            # 排除脸部两边的区域
            if x<face_min_x or x>face_max_x:
                continue
            # 排除脸部上下区域
            if y<face_min_y or y>face_max_y:
                continue
            mouth_min_y=face_min_y+0.6*face_h
            if y<mouth_min_y:
                continue
            cv2.rectangle(face_img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)




    def  draw_logo(self,face_img, face_rect, logo):
        face_x,  face_y, face_w, face_h = face_rect
        ratio = min(self.logo.shape[:2])/max(self.logo.shape[:2])
        logo_w = face_w
        logo_h = int(face_w * ratio)
        scale_logo=cv2.resize(logo, dsize=(logo_w, logo_h))
    # 循环
    #     for row in range(logo_h):
    #         for col in range(logo_w):
    #             face_img[face_y+row-logo_h, face_x+col]=scale_logo[row, col]
    # 切片

    def draw_logo2(self, face_img, face_rect, logo):
        # 将原图转为灰度图
        logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        # 将灰度图转为二值图
        retval, logo_binary = cv2.threshold(logo_gray, 177, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 查找外轮廓
        contours, hierarchy = cv2.findContours(logo_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 产生黑色背景
        mask = np.zeros_like(logo_binary)
        # 绘制所有外轮廓
        cv2.drawContours(mask, contours, 1, (0, 0, 0), -1)

        face_x, face_y, face_w, face_h = face_rect
        ratio = min(self.logo.shape[:2]) / max(self.logo.shape[:2])
        logo_w = face_w
        logo_h = int(face_w * ratio)
        scale_logo = cv2.resize(logo, dsize=(logo_w, logo_h))
        scale_mask = cv2.resize(mask, dsize=(logo_w, logo_h))
        # cv2.imshow('scale_logo', scale_logo)
        print('阈值:', retval)
        idx= scale_mask ==255
        part_img=face_img[:logo_h, :logo_w]
        part_img[idx]=scale_logo[idx]
        cv2.imshow('part_img', scale_logo)
        cv2.imshow('scal',scale_mask)
        # 显示二值图和掩膜
        # cv2.imshow("logo_binary", logo_binary)
        # cv2.imshow('mask', mask)
        cv2.waitKey(0)


if __name__ == '__main__':
    detect = Detect()
    face = cv2.imread('./1.jpg')

    detect.face_detect(face)

    cv2.imshow('face', face)
    cv2.waitKey(0)