import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Int32

PUBLISH_PERIOD = 0.1 # секунды, 10 Гц
OVERFLOW_LIMIT = 100
QUEUE_DEPTH = 10

class EvenNumberPublisher(Node):
  def __init__(self):
    super().__init__('even_pub')
    self.number = 0
    self.even_publisher = self.create_publisher(
      Int32, 'even_numbers', QUEUE_DEPTH
    )
    self.overflow_publisher = self.create_publisher(
      Int32, 'overflow', QUEUE_DEPTH
    )
    self.timer = self.create_timer(PUBLISH_PERIOD, self.publish_number)



  def publish_number(self):
    self.even_publisher.publish(Int32(data=self.number))
    self.number += 2
    if self.number >= OVERFLOW_LIMIT:
      self.overflow_publisher.publish(Int32(data=self.number))
      self.number = 0

def main(args=None):
  rclpy.init(args=args)
  node = EvenNumberPublisher()
  try:
    rclpy.spin(node)
  except (KeyboardInterrupt, ExternalShutdownException):
    pass
  finally:
    node.destroy_node()
    rclpy.try_shutdown()

if __name__ == '__main__':
  main()