# Real-Time Object Tracker
Real-time object tracking using the CSRT algorithm. The user draws a bounding box around a specific object to track it live via webcam feed. It's built with Python and OpenCV.

## Implementation Details

This tracker uses OpenCV's CSRT algorithm. It is chosen for its tracking accuracy while still running fast enough to meet the real-time requirement. It learns what the selected object looks like from a single bounding box drawn by the user, then locates it in each frame.

## Setup

Clone this repository and install the required dependency: `pip install -r requirements.txt`



## Usage

Run the script: `python ObjectTracker.py`



- Press **s** to freeze the current frame and draw a bounding box around the object you want to track.
- Press **q** to exit the program.

  A webcam is required.
