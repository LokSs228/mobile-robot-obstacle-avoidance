import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LaserReader(Node):
    def __init__(self):
        super().__init__('laser_reader')
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.listener_callback, 10)

    def listener_callback(self, msg):
        front_distance = msg.ranges[0]  # индекс 0 обычно "прямо вперёд"
        self.get_logger().info(f'Front distance: {front_distance:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = LaserReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()