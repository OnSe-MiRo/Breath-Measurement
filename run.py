from utils.camera import *
from utils.BodyPose import *
from utils.filter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
def main(i):
    t=time.time()
    global raw_data
    global time_data
    
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
    time_data.append(t)
    time_data=time_data[-300:]
    
    if len(raw_data) < XAxisRange:  
        pass
    else:
        raw_data=raw_data[-500:]
        smooth_data=smooth_filter.smooth(raw_data,10)
        smooth_data_fft_y,freq=fft(smooth_data[-140:-40],time_data[-140:-40])
        
        smooth_data_fft_y[0]=0
        ax1.cla()
        ax2.cla()
        ax1.plot(raw_data[-100:],label='depth')
        ax1.plot(smooth_data[-100:-40],label='filter')
        ax2.plot(freq,abs(smooth_data_fft_y),label='FFT')
        
fig=plt.figure(1)
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
error_code=0
pose,mp_pose,mp_drawing,mp_drawing_styles=bodypose()
raw_data=[]
time_data=[]
try:
    PipeLine=open_camera()
    print('INFO: Device Connected')
except:
    print('INFO: No device Connected')
    error_code=1

if error_code==0:
    ani = FuncAnimation(plt.gcf(),main, interval = 1000/60)
    plt.show()
