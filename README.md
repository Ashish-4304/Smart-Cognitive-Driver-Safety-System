# Smart-Cognitive-Driver-Safety-System

## Overview

This project presents an AI-powered real-time driver monitoring system designed to enhance road safety by detecting drowsiness, distraction, and fatigue using computer vision techniques.

Unlike traditional systems that rely on a single factor, this system integrates multiple behavioral indicators such as Eye Aspect Ratio (EAR), head pose estimation, and blink patterns to assess driver alertness.

## Features

* Drowsiness Detection using Eye Aspect Ratio (EAR)
* Real-time Eye Tracking
* Head Pose Estimation (attention tracking)
* Dynamic Driver Risk Score
* Intelligent Alert System (Safe / Warning / Danger)
* Data Logging for analysis

## Tech Stack

* Python
* OpenCV
* Dlib
* NumPy
* SciPy

## Project Structure

Smart-Cognitive-Driver-Safety-System/
│── src/
│   ├── main.py
│   ├── eye_detection.py
│   ├── head_pose.py
│   ├── risk_engine.py
│   ├── alert.py
│   ├── logger.py
│── data/
│   ├── driver_log.csv
│── models/
│── requirements.txt
│── README.md


## How to Run

### 1. Clone Repository
git clone https://github.com/your-username/Smart-Cognitive-Driver-Safety-System.git
cd Smart-Cognitive-Driver-Safety-System

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Download Required Model
Download the file:
shape_predictor_68_face_landmarks.dat

(Available from dlib official resources)
Place it in the root directory.

### 4. Run the Project
python src/main.py


## Output
(Add screenshots after running the project)

Example

images/output_safe.png
images/output_warning.png
images/output_alert.png


## How It Works

1. Webcam captures live video
2. Face is detected using Dlib
3. Facial landmarks are extracted
4. Eye Aspect Ratio (EAR) is calculated
5. Head pose is analyzed
6. Risk score is computed
7. Alerts are triggered based on risk level


## Key Innovation

This project goes beyond basic drowsiness detection by introducing a **multi-factor cognitive monitoring system** that evaluates driver behavior in real time and computes a dynamic risk score.


## Limitations

* Performance depends on lighting conditions
* Requires clear visibility of face
* Accuracy may vary with camera quality


## Future Improvements

* Deep learning-based fatigue detection
* Mobile application integration
* IoT integration with vehicles
* Voice-based alert system


## Requirements
opencv-python
dlib
numpy
scipy
imutils


## Contribution
This is an academic project. Contributions and suggestions are welcome.


## License
This project is for educational purposes only.
