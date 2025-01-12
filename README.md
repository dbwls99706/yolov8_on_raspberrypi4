# YOLOv8 on Raspberry Pi 4B

이 리포지토리는 Raspberry Pi 4B 내부에서 YOLOv8 객체 탐지를 실행할 수 있는 ROS2 패키지를 포함하고 있습니다. 실시간 객체 탐지를 위한 YOLOv8의 모든 구성, 의존성 및 코드가 포함되어 있습니다.

## Requirements:
- **Raspberry Pi 4B**
- **ROS2 (Humble or later)**
- **YOLOv8 model file** (e.g., yolov8n.pt)
- **Python 3.12**
- ROS2 dependencies for YOLOv8

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/dbwls99706/yolov8_on_raspberrypi4.git
   
2. Install ROS2 dependencies:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
   
3. Build the package:
   ```bash
   colcon build
   
4. Launch the YOLOv8 node:
   ```bash
   ros2 launch yolov8_on_raspberrypi4 <launch_file>
