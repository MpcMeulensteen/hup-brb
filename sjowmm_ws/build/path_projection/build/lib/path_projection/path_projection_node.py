import rclpy
from rclpy.node import Node
import numpy as np
import cv2

from nav_msgs.msg import Path
from nav_msgs.msg import OccupancyGrid


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.path_subscription = self.create_subscription(Path, '/plan', self.listener_callback, 10)
        self.path_subscription  # prevent unused variable warning
        self.map_subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 10)
        self.map_subscription


    def listener_callback(self, msg: Path):
        i = 0
        map = cv2.imread('~/turtlebot3_ws/src/path_projection/path_projection/map.png', cv2.IMREAD_UNCHANGED)
        frame = np.full((500,500, 3),255).astype(np.uint8)
        subframe1 = np.full((500,500, 3),255).astype(np.uint8)
        subframe2 = np.full((500,500, 3),255).astype(np.uint8)
        finalframe = np.full((500,500, 3),255).astype(np.uint8)

        for poseStamped in msg.poses:
            x = poseStamped.pose.position.x
            y = poseStamped.pose.position.y

            #self.get_logger().info(f"{i+1}: x={x:.3f} y={y:.3f}")
            i = i + 1
            cv2.circle(frame, (int((x+5)*25),int((y+5)*25)), 2, (0,0,0))
        self.get_logger().info("")
        cv2.flip(frame, -1, subframe1)
        subframe2 = cv2.rotate(subframe1, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.flip(subframe2, 0, finalframe)
        # cv2.imwrite('path.png', finalframe)
        cv2.imshow("map", finalframe)

        # path = cv2.imread('/home/student/turtlebot3_ws/path.png', cv2.IMREAD_UNCHANGED)
        # self.get_logger().info(map.shape)
        # addedimage = cv2.addWeighted(map, 0.5, path, 0.5, 0)
        # cv2.imshow("map", addedimage)
        cv2.waitKey(1)

    def map_callback(self, msg: OccupancyGrid):
        print('Frame:')
        print('Height:', msg.info.height)
        print('Width:', msg.info.width)
        print('')
        print('Orientation:')
        print('X:', msg.info.origin._position._x)
        print('Y:', msg.info.origin._position._y)
        print('X:', msg.info.origin._position._z)
        
        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()