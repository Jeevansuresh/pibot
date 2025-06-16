import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class UltrasonicSensorNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_sensor_node')
        self.publisher_ = self.create_publisher(Float32, 'distance', 10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.timer = self.create_timer(0.5, self.read_and_publish)

    def read_and_publish(self):
        if self.serial_port.in_waiting:
            try:
                line = self.serial_port.readline().decode('utf-8').strip()
                if line.startswith("DIST:"):
                    distance = float(line.split(":")[1])
                    msg = Float32()
                    msg.data = distance
                    self.publisher_.publish(msg)
                    self.get_logger().info(f"Published distance: {distance:.2f} cm")
            except Exception as e:
                self.get_logger().warn(f'Failed to read/parse: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
