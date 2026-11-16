import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Int32


class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        self.overflow_subscription = self.create_subscription(Int32, 'overflow', self.on_overflow, 10)

    def on_overflow(self, msg):
        self.get_logger().warning(f'Переполнение счётчика. Получено значение {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()