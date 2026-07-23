import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

SAFE_DISTANCE = 0.5 

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(
            LaserScan, 'scan', self.scan_callback, 10)

    def scan_callback(self, msg):
        front_distance = min(msg.ranges[0:10] + msg.ranges[-10:]) 
        cmd = Twist()

        if front_distance < SAFE_DISTANCE:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.5  
        else:
            cmd.linear.x = 0.2
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()