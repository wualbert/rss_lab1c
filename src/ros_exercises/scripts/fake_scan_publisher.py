#!/usr/bin/env python

import rospy
import numpy as np
import random
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

pub = rospy.Publisher(rospy.get_param("/Fake_scan_publisher/topic"), LaserScan)
rospy.init_node('fake_scan_publisher')
rate = rospy.Rate(rospy.get_param("/Fake_scan_publisher/rate"))
while not rospy.is_shutdown():
    lsr_msg = LaserScan()
    # Set up values
    lsr_msg.header.stamp = rospy.rostime.Time().now()
    #print(type(lsr_msg))
    lsr_msg.header.frame_id = 'base_link'
    lsr_msg.angle_min = rospy.get_param("/Fake_scan_publisher/angle_min")#-np.pi*2./3.
    lsr_msg.angle_max = rospy.get_param("/Fake_scan_publisher/angle_max")#np.pi*2./3.
    lsr_msg.angle_increment = rospy.get_param("/Fake_scan_publisher/angle_increment")#np.pi/300.
    lsr_msg.scan_time = rospy.rostime.Time().now().to_sec()
    lsr_msg.range_min = rospy.get_param("/Fake_scan_publisher/range_min")#1.
    lsr_msg.range_max = rospy.get_param("/Fake_scan_publisher/range_max")#10.
    increment_count = int((lsr_msg.angle_max-lsr_msg.angle_min)\
            /lsr_msg.angle_increment+1)
    for i in range(increment_count):
        lsr_msg.ranges.append(random.random()*9+1)
    #rospy.loginfo(lsr_msg)
    pub.publish(lsr_msg)
    rate.sleep()


