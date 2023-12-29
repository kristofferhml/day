import rclpy
from rclpy.node import Node
from std_msgs.msg import String

SUN_RISE = 'sun-rise'
SUN_SET = 'sun-set'

class Day(Node):

    def __init__(self):
        super().__init__('day')
        self.current = SUN_RISE
        self.publisher_ = self.create_publisher(String, 'day', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        if self.current == SUN_RISE:
            msg.data = SUN_SET
        else:
            msg.data = SUN_RISE

        self.current = msg.data
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    day = Day()
    rclpy.spin(day)

    day.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()