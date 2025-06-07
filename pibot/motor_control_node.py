import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorControlNode(Node):
    def __init__(self):
        super().__init__("motor_control_node")
        self.subscription = self.create_subscription(String,'robot_cmd',self.cmd_callback,10)


    def cmd_callback(self, msg):
        command = msg.data.lower()
        if command == "forward":
            self.get_logger().info("Moving forward")
        elif command == "backward":
            self.get_logger().info("Moving backward")
        elif command == "left":
            self.get_logger().info("Turning left")
        elif command == "right":
            self.get_logger().info("Turning right")
        elif command == "stop":
            self.get_logger().info("Stopping")
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
