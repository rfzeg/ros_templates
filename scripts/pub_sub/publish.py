#!/usr/bin/env python

"""
Provides a basic template for creating a ROS Publisher.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import rospy

from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
