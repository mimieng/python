import cv2
from FrameFeat import FrameFeat
class VideoProcess:
    def __init__(self):
        self.hand=Hand()
        pass

    def video_pocess(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            retval,frame=cap.read()
            if not  retval:
                print("no frame")
                break
            frame = cv2.flip(frame,1)
            # 手部关键点检测
            self.hand.process(frame)
            cv2.imshow("frame",frame)
            key=cv2.waitKey(25)
            if key==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    video_process=VideoProcess()
    video_process.video_pocess()