#!/usr/bin/env python

import rospy
import numpy as np
import random
from sensor_msgs.msg import LaserScan

pub = rospy.Publisher('fake_scan', LaserScan)
rospy.init_node('fake_scan_publisher')
rate = rospy.Rate(20)
while not rospy.is_shutdown():
    lsr_msg = LaserScan()
    # Set up values
    lsr_msg.header.stamp.secs = rospy.rostime.Time().now()
    print(type(lsr_msg))
    lsr_msg.header.frame_id = 'base_link'
    lsr_msg.angle_min = -np.pi*2./3.
    lsr_msg.angle_max = np.pi*2./3.
    lsr_msg.angle_increment = np.pi/300.
    lsr_msg.scan_time = rospy.rostime.Time().now()
    lsr_msg.range_min = 1.
    lsr_msg.range_max = 10.
    lsr_msg.ranges = list(np.random.rand(int((lsr_msg.angle_max-lsr_msg.angle_min)\
            /lsr_msg.angle_increment+1))*10.)
    #rospy.loginfo(lsr_msg)
    pub.publish(lsr_msg)
    rate.sleep()


