import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import Float32

class FakeSensor(Node):
    def __init__(self):
        super().__init__('fake_sensor')
        self.publisher = self.create_publisher(Float32, 'data', 10)
        timer_period = 0.2
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        num = random.uniform(20.0, 24.0) # get a random value to be used
        rounded = round(num,3)
        msg.data = rounded
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = FakeSensor()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
