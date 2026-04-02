import cv2

def show_alert(frame, status):
    if status == "DANGER":
        cv2.putText(frame, "DROWSINESS ALERT!", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    elif status == "WARNING":
        cv2.putText(frame, "Stay Alert", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
