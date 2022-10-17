import pyrealsense2 as rs
import numpy as np
import cv2
def frame(pipeline):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()
    spatial = rs.spatial_filter()   # spatial Filter
    depth_frame = spatial.process(depth_frame)
    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    return color_image,depth_image
    