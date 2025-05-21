import cv2
import mediapipe as mp
import numpy as np
class FrameFeat:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
        pass
    def get_pose_landmarks(self,frame):
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=self.pose.process(frame_rgb)
        pose_landmarks=result.pose_landmarks
        if pose_landmarks is None:
            return
        keypoints=[]
        for lm in pose_landmarks.landmark:
            keypoints.append((lm.x,lm.y))
        keypoints=np.array(keypoints).flatten()
        return keypoints
    def get_frame_feat(self,frame):
        # 获取特征
        feat = self.get_pose_landmarks(frame)
        if feat is None:
            return

        pass
    def load_frame_feat(self,file_path):
        """加载特征"""
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
if __name__=='__main__':
    frame_feat=FrameFeat()
    frame=cv2.imread('./OIP-C.jpg')
    keypoints=frame_feat.get_pose_landmarks(frame)
    print(keypoints)