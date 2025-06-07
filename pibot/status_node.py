import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

class StatusNode(Node):
    def __init__(self):
        super().__init__("status_node")
        self.cmd = 'stopped'
        self.distance = 100.0
        self.threshold = 15.0

        self.cmd_sub = self.create_subscription(String, 'robot_cmd', self.cmd_callback, 10)
        self.dist_sub = self.create_subscription(Float32, 'distance', self.dist_callback, 10)
        self.publisher_ = self.create_publisher(String, 'robot_status', 10)

        self.timer = self.create_timer(0.5, self.publish_status)

    def cmd_callback(self, msg):
        self.cmd = msg.data.lower()

    def dist_callback(self, msg):
        self.distance = msg.data

    def publish_status(self):
        msg = String()
        if self.distance < self.threshold and self.cmd != 'stop':
            msg.data = "Obstacle ahead! Stopping!"
        else:
            msg.data = f"Current action: {self.cmd}"

        self.publisher_.publish(msg)
        self.get_logger().info(f"Status: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = StatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
