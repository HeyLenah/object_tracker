# Real-Time Object Tracker
Real-time object tracking using the CSRT algorithm. The user draws a bounding box around a specific object to track it live via webcam feed. It's built with Python and OpenCV.

## Implementation Details

This tracker uses OpenCV's CSRT algorithm, chosen for its tracking accuracy while still running fast enough to meet the real-time requirement. It learns what the selected object looks like directly from the single bounding box drawn by the user, then locates it in each subsequent frame.



