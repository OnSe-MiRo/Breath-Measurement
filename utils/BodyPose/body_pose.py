import mediapipe as mp

def bodypose():
    mp_pose=mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    pose=mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
    return pose,mp_pose,mp_drawing,mp_drawing_styles

