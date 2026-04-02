def get_head_pose(landmarks):
    nose = landmarks.part(30).x

    left = landmarks.part(0).x
    right = landmarks.part(16).x

    center = (left + right) / 2

    if nose < center - 10:
        return "LEFT"
    elif nose > center + 10:
        return "RIGHT"
    else:
        return "CENTER"
