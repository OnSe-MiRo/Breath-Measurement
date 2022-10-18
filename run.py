from utils.camera import *
from utils.BodyPose import *
from utils.filter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
def main(i):
    time1=time.time()
    global raw_data
    color_image,depth_image=frame(pipeline=PipeLine)
    pose_landmarks=result_bodypose(pose,mp_pose,mp_drawing,mp_drawing_styles,color_image,depth_image)
    XAxisRange=50
    if pose_landmarks!=None:
        BodyPoints=body_points(pose_landmarks,color_image.shape)
        if BodyPoints!=None:
            Breath_roi_image=breath_roi(BodyPoints,depth_image)
            raw_data.append(np.mean(Breath_roi_image))
        else: 
            if raw_data!=[]:
                raw_data.append(raw_data[-1])
    
    if len(raw_data) < XAxisRange:  
        try:
            plt.cla()
            plt.plot(raw_data,label='depth')
            plt.legend()
        except:
            pass
    else:
        raw_data=raw_data[-500:]
        smooth_data=smooth_filter.smooth(raw_data,40)
        plt.cla()
        plt.plot(raw_data[-200:],label='depth')
        plt.plot(smooth_data[-240:-40],label='filter')
        plt.legend()
    time2=time.time()
    print(time2-time1)
error_code=0
pose,mp_pose,mp_drawing,mp_drawing_styles=bodypose()
raw_data=[]

try:
    PipeLine=open_camera()
    print('INFO: Device Connected')
except:
    print('INFO: No device Connected')
    error_code=1

if error_code==0:
    ani = FuncAnimation(plt.gcf(),main, interval = 1000/60)
    plt.show()




