# 手部关键点检测
import cv2
import mediapipe as mp
import numpy as np

# 双手数字检测
# 检测到左右手同时检测
# 数字识别，区分左右手
class Hand:
    def __init__(self):
        # 创建对象（加载模型--创建对象）
        self.hands = mp.solutions.hands.Hands()
        # 存储左手关键点
        self.left_hand = []
        # 存储右手关键点
        self.right_hand = []
        #因为很多地方都要使用定义成员变量
        self.frame = None
        # 存储手指的序号
        self.tip_nums=[4,8,12,16,20]
        # 存放手的类型
        self.hand_type = []
        pass
    def process(self,frame):
        self.frame = frame
        right_hand_landmarks_list,left_hand_landmarks_list = self.get_landmark(frame)
        if right_hand_landmarks_list is None and  left_hand_landmarks_list is None:
            return
        # 获取左手关键点
        if left_hand_landmarks_list:
            left_hand = left_hand_landmarks_list.landmark
            self.left_hand = left_hand
            self.draw_style(frame, left_hand_landmarks_list,isRight=False)
        if right_hand_landmarks_list:
            right_hand = right_hand_landmarks_list.landmark
            self.right_hand = right_hand
            self.draw_style(frame, right_hand_landmarks_list,isRight=True)
        # 统计双手的数字
        mul_hand_num_cnt = 0
        # 数字识别
        for hand_type in self.hand_type:
            isRight = hand_type == "Right"
            cnt = self.gesture_num_detect(isRight)
            mul_hand_num_cnt+=cnt
        self.show_info(mul_hand_num_cnt,org=(300,100))
    # 获取关键带点
    def get_landmark(self,frame):
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_bgr)
        multi_hand_landmarks = result.multi_hand_landmarks
        right_hand_landmarks_list,left_hand_landmarks_list=0,0
        if multi_hand_landmarks is None:
            return right_hand_landmarks_list,left_hand_landmarks_list
        hand_type = []
        self.hand_type=hand_type
        for handness in result.multi_handedness:
            for cls in handness.classification:
                if cls.label not in hand_type:
                    hand_type.append(cls.label)
        for idx, hand_type in enumerate(hand_type):
            isRight = hand_type == "Right"
            if isRight:
               right_hand_landmarks_list= multi_hand_landmarks[idx]
            else:
                left_hand_landmarks_list = multi_hand_landmarks[idx]
        return right_hand_landmarks_list,left_hand_landmarks_list
    def gesture_num_detect(self,isRight):
        # y8=self.indexCVPoint(8)[1]
        # y6=self.indexCVPoint(6)[1]
        # if y8>y6:
        #     print("弯曲")
        # y12=self.indexCVPoint(12)[1]
        # y10=self.indexCVPoint(10)[1]
        # if y12>y10:
        #     print("中指弯曲")
        finger_status = np.zeros((5,),dtype=np.bool_)
        for idx,num in enumerate(self.tip_nums):
            if idx==0:
                continue
            tip = self.indexCVPoint(num,isRight=isRight)[1]
            other = self.indexCVPoint(num-2,isRight=isRight)[1]
            finger_status[idx] = tip < other
        cnt=np.sum(finger_status)
        print(cnt)
        if isRight:
            self.show_info(cnt,org=(50,100))
        else:
            self.show_info(cnt,org=(100,100))
        return cnt
        # cv2.putText(self.frame,str(cnt),org=(50,50),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,0,0),thickness=1)
    # 绘制样式

    def draw_style(self,frame,hand_landmarks,isRight=True):
        landmark_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=2)
        line_style = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
        conn = mp.solutions.hands_connections.HAND_CONNECTIONS
        mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, conn, landmark_style, line_style)
        # 绘制序号
        h,w,_ = frame.shape
        # 因为返回的值x，y值是在0-1之间，所以乘以w，h得到实际坐标
        for num, lm in enumerate(hand_landmarks.landmark):
            x=int(lm.x*w)
            y=int(lm.y*h)
            cv2.putText(frame,str(num),org=(x-8,y),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,0,0),thickness=1)
            pass
    def indexCVPoint(self,index,isRight=True):
#通过索引将关键点转换到对应屏幕坐标
        h,w,_ = self.frame.shape
        if isRight:
            lm=self.right_hand[index]
        else:
            lm=self.left_hand[index]
        x=int(lm.x*w)
        y=int(lm.y*h)
        return x,y
    def show_info(self,info,org=(50,100)):
        cv2.putText(self.frame,str(info),org=org,fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,0,0),thickness=1)




