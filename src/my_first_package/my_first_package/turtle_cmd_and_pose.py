import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose


class CmdAndPose(Node):
    def __init__(self):
        super().__init__("turtle_cmd_and_pose")
        self.sub_pose = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_pose, 10
        )

    def callback_pose(self, msg):
        print(msg)


def main(args=None) -> None:
    rp.init(args=args)

    turtle_cmd_and_pose = CmdAndPose()

    try:
        rp.spin(turtle_cmd_and_pose)
    finally:
        turtle_cmd_and_pose.destroy_node()
        rp.shutdown()


if __name__ == "__main__":
    main()
