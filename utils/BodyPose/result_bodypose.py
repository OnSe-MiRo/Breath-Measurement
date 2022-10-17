import cv2
import numpy as np

def result_bodypose(pose,mp_pose,mp_drawing,mp_drawing_styles,color_image,depth_image):
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    depth_colormap_dim = depth_colormap.shape
    color_colormap_dim = color_image.shape
    cv2.imshow('aa',color_image)
    pose_results=pose.process(color_image)
    
    if depth_colormap_dim != color_colormap_dim:
        resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        images = np.hstack((resized_color_image, depth_colormap))
    else:
        images = np.hstack((color_image, depth_colormap))
    color_image.flags.writeable=True
    mp_drawing.draw_landmarks(
                color_image,
                pose_results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    Crop_Depth_Image=np.zeros([480,640])
    Normalization_image=np.zeros([480,640])
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', images)
    cv2.imshow('color',color_image)
    cv2.imshow('crop',Normalization_image)
    
    return pose_results.pose_landmarks