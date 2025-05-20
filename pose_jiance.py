import cv2
import mediapipe as mp
import util
from grade import Grade ,ArmCountedStatus
class PoseDetect:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        # 肢体检测关键点
        self.landmark = []
        self.frame = None
        # 用于记录手臂弯曲次数
        self.grade = Grade()
        # # 统计手臂弯曲次数
        # self.cnt=0
        # # 1 表示当前动作未计数  2  当前动作已经计数
        # self.status = 1
        pass
    def process(self,frame):
        self.frame = frame
        # 获取关键点
        pose_landmark = self.get_pose_landmark(frame)
        if pose_landmark is None:
            return
        self.landmark = pose_landmark.landmark
        # 绘制样式
        self.draw_style(frame,pose_landmark)
        # 手臂弯曲
        self.arm_bend_detect(frame)
    def arm_bend_detect(self,frame):
        p12 = self.indexCvPoint(frame,  12)
        p14 = self.indexCvPoint(frame, 14)
        p16 = self.indexCvPoint(frame, 16)
        angle= util.get_angle(p12,p14,p16)
        grade = self.grade
        if angle<grade.min_angle and grade.status==ArmCountedStatus.NOT_COUNTED:
            grade.cnt+=1
            grade.status=ArmCountedStatus.COUNTED
        elif angle>grade.max_angle:
        #当前动作需要重新计数
            grade.status=ArmCountedStatus.NOT_COUNTED
        else:
            print("当前动作需要重新计数")
        self.show_info(grade.cnt)
        print(angle)


    def get_pose_landmark(self,frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(frame_rgb)
        pose_landmark = result.pose_landmarks
        return pose_landmark

    def draw_style(self,frame,pose_landmark):
        conn = mp.solutions.pose.POSE_CONNECTIONS
        mp.solutions.drawing_utils.draw_landmarks(
            frame,
            pose_landmark,
            conn,
            mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2),
            mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
        )
        landmark = pose_landmark.landmark
        h, w, _ = frame.shape
        for id, lm in enumerate(landmark):
            x, y = int(lm.x * w), int(lm.y * h)
            cv2.putText(frame, str(id), (x - 6, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    def indexCvPoint(self,frame,index):
        h,w,_ = frame.shape
        lm = self.landmark[index]
        x,y = int(lm.x*w),int(lm.y*h)
        return x,y
    def show_info(self,info,org=(50,100)):
        cv2.putText(self.frame,str(info),org=org,fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,0,0),thickness=1)