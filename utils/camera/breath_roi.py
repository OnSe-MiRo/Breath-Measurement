import numpy as np

def breath_roi(BodyPoints,depth_image):
    Crop_Depth_Image=np.zeros([480,640])
    Top_Y=min([BodyPoints[0][1],BodyPoints[1][1]])+40
    Bottom_Y=max([BodyPoints[2][1],BodyPoints[3][1]])-40
    Left_X=min([BodyPoints[1][0],BodyPoints[3][0]])-30
    Right_X=max([BodyPoints[0][0],BodyPoints[2][0]])-10
    ROI_depth_image=depth_image[Top_Y:Bottom_Y,Right_X:Left_X]
    Crop_Depth_Image[Top_Y:Bottom_Y,Right_X:Left_X]=ROI_depth_image
    Crop_Depth_Image[Crop_Depth_Image>2000]=0
    Crop_Depth_Image[Crop_Depth_Image<1000]=0
    return Crop_Depth_Image