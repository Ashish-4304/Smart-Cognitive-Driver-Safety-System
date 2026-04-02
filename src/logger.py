import csv
import time

def log_data(ear, head_pose, risk):
    with open("data/driver_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time.time(), ear, head_pose, risk])
