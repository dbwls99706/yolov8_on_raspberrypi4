from setuptools import setup

package_name = 'yolov8_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 모델 파일 포함
        (package_name + '/model', ['model/yolov8n.pt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='yujinhong3@gmail.com',
    description='YOLOv8 ROS package',
    license='Apache License 2.0',
    tests_require=['pytest'],  # 'tests_require'는 최근 버전의 setuptools에서 경고를 발생시킬 수 있음
    entry_points={
        'console_scripts': [
            'detect_camera_node = yolov8_ros.run_camera:main',
        ],
    },
)

