def calculate_risk(ear, head_pose, prev_risk):
    risk = prev_risk

    # Drowsiness factor
    if ear < 0.25:
        risk += 2
    else:
        risk -= 1

    # Distraction factor
    if head_pose != "CENTER":
        risk += 1

    # Clamp values
    risk = max(0, min(100, risk))

    # Status
    if risk > 50:
        status = "DANGER"
    elif risk > 20:
        status = "WARNING"
    else:
        status = "SAFE"

    return risk, status
