import rclpy
from rclpy.node import Node
import time

class TimeNode(Node):

    def __init__(self):
        super().__init__('time_node')
        self.timer = self.create_timer(5.0, self.timer_callback)

    def timer_callback(self):
        current_time = time.strftime('%H:%M:%S')
        self.get_logger().info(f'Текущее время: {current_time}')

def main(args=None):

    rclpy.init(args=args)
    node = TimeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()