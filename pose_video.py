import cv2
from pose_jiance import PoseDetect
class VideoProcess:
    def __init__(self):
        self.pose_detect=PoseDetect()
        pass

    def video_pocess(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            retval,frame=cap.read()
            if not  retval:
                print("no frame")
                break
            frame = cv2.flip(frame,1)
            # 肢体关键点检测
            self.pose_detect.process(frame)
            cv2.imshow("frame",frame)
            key=cv2.waitKey(25)
            if key==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    video_process=VideoProcess()
    video_process.video_pocess()