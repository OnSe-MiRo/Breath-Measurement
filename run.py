from turtle import color
import mediapipe as mp
from utils.camera import *
from utils.BodyPose import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2

PipeLine=open_camera()
pose,mp_pose,mp_drawing,mp_drawing_styles=bodypose()

def main(i):
    color_image,depth_image=frame(pipeline=PipeLine)
    pose_landmarks=result_bodypose(pose,mp_pose,mp_drawing,mp_drawing_styles,color_image,depth_image)
    try:
        x=[1,2,3,4]
        y=[6,7,8,9]
        plt.cla()
        plt.plot(x,y,label='depth')
        plt.legend()
    except:
        pass
    


ani = FuncAnimation(plt.gcf(),main, interval = 1000/60)
plt.show()