import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class MotorControlNode(Node):
    def __init__(self):
        super().__init__("motor_control_node")
        self.subscription = self.create_subscription(String, 'robot_cmd', self.cmd_callback, 10)
        self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    def cmd_callback(self, msg):
        command = msg.data.lower()
        if command in ["forward", "backward", "left", "right", "stop"]:
            self.arduino.write((command + '\n').encode())
            self.get_logger().info(f"Sent command to Arduino: {command}")
        else:
            self.get_logger().warn(f"Unknown command: {command}")

def main(args=None):
    rclpy.init(args=args)
    node = MotorControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
