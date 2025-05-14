# 手部关键点检测
import cv2
import mediapipe as mp
class Hand:
    def __init__(self):
        pass
    def process(self,frame):

        # 创建对象（加载模型--创建对象）
        hands = mp.solutions.hands.Hands()
        # opencv里的是RGB格式
        frame_bgr=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=hands.process(frame_bgr)
        multi_hand_landmarks = result.multi_hand_landmarks
        if multi_hand_landmarks is None:
            return
        hand_landmarks = multi_hand_landmarks[0]
        left_landmark = hand_landmarks.landmark
#        参数1：绘制在什么地方
#        参数2：绘制的点
#        参数3：点的序号链接
#        参数4：点的样式
        landmark_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2)
        line_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
        conn = mp.solutions.hands_connections.HAND_CONNECTIONS
        mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, conn, landmark_style, line_style)
        pass









