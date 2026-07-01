Virtual Mouse

Control your computer's mouse cursor using hand gestures and your webcam. This project uses computer vision and machine learning to track your hand movements in real-time, allowing you to move the cursor and click without touching a physical mouse.

## Features
* Real-time Hand Tracking: Uses Google's MediaPipe for fast and accurate hand landmark detection.
* Smooth Cursor Movement: Implements a low-pass mathematical filter to eliminate cursor jitter and provide smooth gliding.
* Pinch to Click: Simply bring your index finger and thumb together to simulate a left mouse click.
* Active Mapping Region: You don't need to stretch your hand to the edges of the camera. A constrained active region allows you to reach all corners of your screen with minimal physical effort.
* Click Debouncing: Prevents accidental spam-clicking by enforcing a brief cooldown between clicks.

## Tech Stack
* Python 3.x
* OpenCV (cv2): For accessing the webcam and image processing.
* MediaPipe: For the AI hand-tracking model.
* PyAutoGUI: For controlling the operating system's mouse cursor.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harshk007-p/Virtual-Mouse.git
   cd Virtual-Mouse
   ```
2. Install The required libraries
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

Note: Enusre you're using python version 3.10 or 3.9, mediapipe might not work on newer versions

3. Run the file
   ```bash
   python virtual_mouse_py
   ```
   
