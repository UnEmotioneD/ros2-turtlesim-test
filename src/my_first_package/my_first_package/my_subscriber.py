import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtlesimSubscriber(Node):
    def __init__(self):
        # initialize with node name
        super().__init__("turtlesim_subscriber")
        self.subscription = self.create_subscription(
            Pose,  # node type
            "/turtle1/pose",  #  topic name
            self.callback,
            10,  # QoS profile depth (queue size)
        )

    def callback(self, msg):
        """prints incoming grid"""
        print(f"X: {msg.x}, Y: {msg.y}")


def main(args=None) -> None:
    # initialize ROS2 communications
    rp.init(args=args)

    # instantiate subscriber node
    turtlesim_subscriber = TurtlesimSubscriber()

    try:
        # keep node alive to process callback
        rp.spin(turtlesim_subscriber)
    finally:
        pass  # handle Ctrl+C gracefully

    # cleanup resource and shutdown
    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == "__main__":
    main()
