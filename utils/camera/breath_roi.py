def breath_roi(BodyPoints,depth_image):
    Top_Y=min([BodyPoints[0][1],BodyPoints[1][1]])+40
    Bottom_Y=max([BodyPoints[2][1],BodyPoints[3][1]])-40
    Left_X=min([BodyPoints[1][0],BodyPoints[3][0]])-30
    Right_X=max([BodyPoints[0][0],BodyPoints[2][0]])-10
    ROI_depth_image=depth_image[Top_Y:Bottom_Y,Right_X:Left_X]
    
    return ROI_depth_image