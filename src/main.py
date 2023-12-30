import rclpy
from . import utils
from rclpy.node import Node
from std_msgs.msg import String

SUN_RISE = 'sun-rise'
SUN_SET = 'sun-set'
DAY = 'day'
NIGHT = 'night'
NOON = 'noon'

DAY_START = 8
NOON = 12
DAY_END = 22

class Day(Node):

    def __init__(self):
        super().__init__('day')
        self.publisher_ = self.create_publisher(String, 'day', 10)
        timer_period = 5  # seconds
        hour_of_day = utils.nanoseconds_to_hours(self.get_clock().now().nanoseconds)        
        is_day = hour_of_day in range(DAY_START, DAY_END)
        if is_day:
            self.current = DAY
        else:
            self.current = NIGHT

        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):

        hour_of_day = utils.nanoseconds_to_hours(self.get_clock().now().nanoseconds)  
        is_day = hour_of_day in range(DAY_START, DAY_END)
        
        status_msg = String()
        if is_day:
            status_msg.data = DAY
        else:
            status_msg.data = NIGHT
        
        self.publisher_.publish(status_msg)
        self.get_logger().info('Publishing: "%s"' % status_msg.data)

        change_msg = String()
        if self.current != status_msg.data:
            if is_day:
                change_msg.data = SUN_RISE
            else:
                change_msg.data = SUN_SET
        
        self.publisher_.publish(change_msg)
        self.get_logger().info('Publishing: "%s"' % change_msg.data)
        
        self.current = status_msg.data
        
def main(args=None):
    rclpy.init(args=args)
    day = Day()
    rclpy.spin(day)

    day.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()