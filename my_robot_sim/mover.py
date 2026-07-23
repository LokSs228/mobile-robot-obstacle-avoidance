import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Mover(Node):
    def __init__(self):
        super().__init__('mover')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)  
        self.state = 'forward'
        self.counter = 0

    def timer_callback(self):
        msg = Twist()
        if self.state == 'forward':
            msg.linear.x = 0.2
            msg.angular.z = 0.0
        else:  # turning
            msg.linear.x = 0.0
            msg.angular.z = 0.5

        self.publisher_.publish(msg)
        self.counter += 1
        if self.counter >= 8:
            self.state = 'turning' if self.state == 'forward' else 'forward'
            self.counter = 0

def main(args=None):
    rclpy.init(args=args)
    node = Mover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()