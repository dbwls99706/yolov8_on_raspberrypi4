# YOLOv8 on Raspberry Pi 4B

This repository contains a ROS2 package that enables running YOLOv8 object detection on a Raspberry Pi 4B. It includes all necessary configurations, dependencies, and code to perform real-time object detection using YOLOv8.

## Requirements:
- **Raspberry Pi 4B**
- **ROS2 (Humble or later)**
- **YOLOv8 model file** (e.g., yolov8n.pt)
- **Python 3.x**
- ROS2 dependencies for YOLOv8

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/dbwls99706/yolov8_on_raspberrypi4.git
Install ROS2 dependencies:
bash
코드 복사
rosdep install --from-paths src --ignore-src -r -y
Build the package:
bash
코드 복사
colcon build
Usage:
Launch the YOLOv8 node:
bash
코드 복사
ros2 launch yolov8_on_raspberrypi4 <launch_file>
