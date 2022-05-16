import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge, CvBridgeError
from action_msgs.msg import GoalStatusArray, GoalStatus
 
class robot_controller(Node):
    def __init__(self):
        self.subscription_pose = self.create_subscription(
            GoalStatusArray,
            'navigate_to_pose/_action/status',
            self.goal_callback,
            1
        )

    def callback(self, data):
        bridge = CvBridge()
        try:
            self.cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().log(e)

    def goal_callback(self, data):
        self.goal_status = data[0].status
        print(self.goal_status)

def main():
    rclpy.init(args=None)
    rc = robot_controller()
    rclpy.spin(rc)

if __name__ == '__main__':
    main()