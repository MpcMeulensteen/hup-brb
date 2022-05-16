#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

import rclpy
import numpy as np 
import cv2
from nav_msgs.msg import OccupancyGrid  




def main(args=None):

    rclpy.init(args=args)
    node = rclpy.create_node('readMapData')
    node.create_subscription(OccupancyGrid, "/map", sub_callback, 0)
    # while(test == False):
    #     print("wtf")
    #     rclpy.spin_once(node)
    rclpy.spin(node)
    #     
    node.destroy_node()
    rclpy.shutdown()


def sub_callback(data:OccupancyGrid):
    print("Map received")
    array = np.array(data.data, np.uint8)
    array = array.reshape(362, 490)
    array = array.resize(500, 500)
    bgr = cv2.cvtColor(array, cv2.COLOR_GRAY2BGR)
    cv2.imshow('map', bgr)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
