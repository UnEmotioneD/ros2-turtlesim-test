import rclpy as rp
from my_first_package_msgs.msg import CmdAndPoseVel
from rclpy.node import Node
from turtlesim.msg import Pose


class CmdAndPose(Node):
    def __init__(self):
        super().__init__("turtle_cmd_and_pose")
        self.sub_pose = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_pose, 10
        )
        self.cmd_pose = CmdAndPoseVel()

    def callback_pose(self, msg):
        self.cmd_pose.pose_x = msg.x
        self.cmd_pose.pose_y = msg.y
        self.cmd_pose.linear_vel = msg.linear_velocity
        self.cmd_pose.angular_vel = msg.angular_velocity
        print(self.cmd_pose)


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
