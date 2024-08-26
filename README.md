
# Tello Drone Projects

This repository contains multiple drone projects developed using the DJI Tello drone and the `djitellopy` Python library. Each project focuses on different aspects of drone control, computer vision, and automation.

## Projects

### 1. Mapping
- **Description**: A mapping project that visualizes the drone's flight path and positions on a 2D plane.
- **Folder**: `Mapping/`
- **Main Script**: `mapping.py`
- **Dependencies**: `djitellopy`, `cv2`, `numpy`, `KeyPressModule`

### 2. Face Tracking
- **Description**: A face tracking system where the drone autonomously follows detected faces.
- **Folder**: `FaceTracking/`
- **Main Script**: `face_tracking.py`
- **Dependencies**: `djitellopy`, `cv2`
- **Resources**: Includes a pre-trained Haar Cascade classifier for face detection.

### 3. Line Follower
- **Description**: A line-following project where the drone detects and follows a line based on color segmentation.
- **Folder**: `LineFollower/`
- **Main Script**: `line_follower.py`
- **Dependencies**: `djitellopy`, `cv2`, `numpy`

### 4. Color Picker
- **Description**: A color picker project that uses HSV values to detect and track specific colors in the drone's camera feed.
- **Folder**: `ColorPicker/`
- **Main Script**: `color_picker.py`
- **Dependencies**: `djitellopy`, `cv2`, `numpy`

## Additional Files

- **KeyPressModule.py**: A module for capturing keyboard input using `pygame`, used for controlling the drone with keyboard commands. This file is required for the `Mapping` project and other projects that involve manual control.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Tello-Drone-Projects.git
   cd Tello-Drone-Projects
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the desired project:
   ```bash
   python <project_folder>/<script_name>.py
   ```

## Requirements
- Python 3.x
- djitellopy
- OpenCV (`cv2`)
- Numpy
- Pygame (for `KeyPressModule.py`)

## License
This project is licensed under the MIT License.
