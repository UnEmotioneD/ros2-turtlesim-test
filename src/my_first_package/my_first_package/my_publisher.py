import rclpy as rp
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TurtlesimPublisher(Node):
    def __init__(self):
        super().__init__("turtlesim_publisher")
        # topic name must be same as subscriber
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # trigger callback every .5 sec
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        """makes the turtle to move"""
        msg = Twist()  # create Twist msg instance
        msg.linear.x = 2.0  # linear speed 2.0 m/s
        msg.angular.z = 2.0  # rotation speed
        self.publisher.publish(msg)  # send msg to topic


def main(args=None) -> None:
    rp.init(args=args)

    turtlesim_publisher = TurtlesimPublisher()

    try:
        rp.spin(turtlesim_publisher)
    finally:
        pass  # this is a placeholder

    turtlesim_publisher.destroy_node()
    rp.shutdown()


if __name__ == "__main__":
    main()
