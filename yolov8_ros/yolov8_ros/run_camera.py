import rclpy
from rclpy.node import Node
from utils.detect import detect_camera
import pathlib


class DetectCameraNode(Node):
    def __init__(self):
        super().__init__('detect_camera_node')

        # Declare and get parameters
        self.declare_parameter('model', str(pathlib.Path(__file__).parent.parent / 'model/yolov8n.pt'))
        self.declare_parameter('q', '')

        model_path = self.get_parameter('model').get_parameter_value().string_value
        quantization = self.get_parameter('q').get_parameter_value().string_value

        # Validate model file existence and extension
        model_file = pathlib.Path(model_path)
        if not model_file.exists():
            self.get_logger().error(f"Model file not found: {model_path}")
            return
        if model_file.suffix not in ['.onnx', '.engine', '.pt']:
            self.get_logger().error(f"Invalid model file extension: {model_file.suffix}")
            return

        # Run detection
        self.get_logger().info(f"Starting detection with model: {model_path} and quantization: {quantization}")
        detect_camera(model_path, quantization)


def main(args=None):
    rclpy.init(args=args)
    node = DetectCameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

