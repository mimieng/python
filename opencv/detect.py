import cv2

class Detect:
    def __init__(self):
        classifier = cv2.CascadeClassifier()
        self.classifier = classifier
        # 加载特征文件
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
        classifier.load(cascade_path)
        self.logo= cv2.imread('./2.jpg')

    def face_detect(self, face_img):

        # 检测人脸，返回包含人脸矩形列表
        face_rect = self.classifier.detectMultiScale(face_img)
        for rect in face_rect:
            x, y, w, h = rect
            cv2.rectangle(face_img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
            self.draw_logo(face_img,rect,self.logo)




    def  draw_logo(self,face_img, face_rect, logo):
        face_x,  face_y, face_w, face_h = face_rect
        ratio = min(self.logo.shape[:2])/max(self.logo.shape[:2])
        logo_w = face_w
        logo_h = int(face_w * ratio)
        scale_logo=cv2.resize(logo, dsize=(logo_w, logo_h))

        for row in range(logo_h):
            for col in range(logo_w):
                face_img[face_y+row-logo_h, face_x+col]=scale_logo[row, col]

if __name__ == '__main__':
    detect = Detect()
    face = cv2.imread('./OIP-C.jpg')
    detect.face_detect(face)
    cv2.imshow('face', face)
    cv2.waitKey(0)