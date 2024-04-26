import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

class Kalman1d(Node):
    def __init__(self):
        super().__init__('kalman_filter_1d')
        self.sub = self.create_subscription(Float32,'/data',self.callback,10)
        self.sub
        self.pub = self.create_publisher(Float32, '/kalman_1d_estimate', 10)

        # variables for the kalman filter
        self.error_estimate_d1 = 2
        self.estimate_d1 = 18
        self.error_meas = 4


    def callback(self, msg):
        data = msg.data

        kalman_gain = self.kg()
        estimate = self.new_estimate(kalman_gain,data)
        error_estimate = self.new_error_estimate(kalman_gain)

        self.error_estimate_d1 = error_estimate
        self.estimate_d1 = estimate

        outgoing = Float32()
        outgoing.data = estimate
        self.pub.publish(outgoing)


    def kg(self):
        return self.error_estimate_d1/(self.error_estimate_d1 + self.error_meas)
    
    def new_estimate(self, kg, data):
        return self.estimate_d1 + kg * (data - self.estimate_d1)
    
    def new_error_estimate(self, kg):
        return (1.0 - kg) * self.error_estimate_d1
    
def main():
    rclpy.init()
    kalman = Kalman1d()
    rclpy.spin(kalman)
    kalman.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()