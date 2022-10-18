from lib2to3.pgen2.token import LEFTSHIFT


def return_point(pose_data,shape):
    x=int(pose_data[0]*shape[1])
    y=int(pose_data[1]*shape[0])
    return (x,y)

def body_points(pose_landmarks,color_colormap_dim):
    assert len(pose_landmarks.landmark)==3,  'Unexpected number of predicted pose landmarks: {}'.format(len(pose_landmarks.landmark))
    pose_landmarks = [[lmk.x, lmk.y, lmk.z] for lmk in pose_landmarks.landmark]
    Right_Shoulder=return_point(pose_landmarks[12],color_colormap_dim)
    LEft_Shoulder=return_point(pose_landmarks[11],color_colormap_dim)
    Right_Waist=return_point(pose_landmarks[24],color_colormap_dim)
    Left_Waist=return_point(pose_landmarks[23],color_colormap_dim)
    return Right_Shoulder,LEft_Shoulder,Right_Waist,Left_Waist