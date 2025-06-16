import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SafetyNode(Node):
    def __init__(self):
        super().__init__('safety_node')
        self.threshold = 70.0  # degrees Celsius
        self.timer = self.create_timer(1.0, self.monitor_temp)
        self.status_pub = self.create_publisher(String, 'robot_status', 10)
        self.cmd_pub = self.create_publisher(String, 'robot_cmd', 10)

    def read_cpu_temp(self):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp_str = f.readline().strip()
                temp_c = float(temp_str) / 1000.0
                return temp_c
        except Exception as e:
            self.get_logger().error(f"Failed to read CPU temp: {e}")
            return None

    def monitor_temp(self):
        temp = self.read_cpu_temp()
        msg = String()
        if temp is None:
            msg.data = "Error reading CPU temperature"
            self.status_pub.publish(msg)
            return

        if temp > self.threshold:
            msg.data = f"WARNING: CPU Temperature high! {temp:.1f}°C. Stopping robot."
            self.status_pub.publish(msg)
            stop_msg = String()
            stop_msg.data = 'stop'
            self.cmd_pub.publish(stop_msg)
        else:
            msg.data = f"CPU Temperature Normal: {temp:.1f}°C"
            self.status_pub.publish(msg)
            self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = SafetyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
