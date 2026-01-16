import rclpy as rp
from my_first_package_msgs.action import DistTurtle
from rclpy.action.server import ActionServer
from rclpy.node import Node


class DistTurtleServer(Node):
    def __init__(self):
        super().__init__("dist_turtle_action_server")
        self.action_server = ActionServer(
            self, DistTurtle, "/dist_turtle", self.execute_callback
        )

    def execute_callback(self, goal_handle):
        goal_handle.succeed()
        result = DistTurtle.Result()
        return result


def main(args=None) -> None:
    rp.init(args=args)

    dist_turtle_action_server = DistTurtleServer()
    try:
        rp.spin(dist_turtle_action_server)
    finally:
        pass


if __name__ == "__main__":
    main()
