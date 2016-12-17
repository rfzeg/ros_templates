#!/usr/bin/env python

""" Provides a template for creating a ROS subscriber.
 Subscribes to the turtlesim color and then prints the
 data. """

from __future__ import division

__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy

from std_msgs.msg import String, Float32, UInt8
from turtlesim.msg import Color

rospy.init_node("test_sub", anonymous=True)


def callback(data):
    print("in callback")
    print(data)

# if __name__ == '__main__':
while not rospy.is_shutdown():
    print("before sub")
    rospy.Subscriber("/turtle1/color_sensor", Color, callback)
    print("after sub")
    # rospy.spin()
    print("after spin")
