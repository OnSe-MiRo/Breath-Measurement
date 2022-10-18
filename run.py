from utils.camera import *
from utils.BodyPose import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

PipeLine=open_camera()
pose,mp_pose,mp_drawing,mp_drawing_styles=bodypose()
raw_data=[]
def main(i):
    color_image,depth_image=frame(pipeline=PipeLine)
    pose_landmarks=result_bodypose(pose,mp_pose,mp_drawing,mp_drawing_styles,color_image,depth_image)

    if pose_landmarks!=None:
        BodyPoints=body_points(pose_landmarks,color_image.shape)
        if BodyPoints!=None:
            Breath_roi_image=breath_roi(BodyPoints,depth_image)
            raw_data.append(np.mean(Breath_roi_image))
    try:
        plt.cla()
        plt.plot(raw_data,label='depth')
        plt.legend()
    except:
        pass
    


ani = FuncAnimation(plt.gcf(),main, interval = 1000/60)
plt.show()