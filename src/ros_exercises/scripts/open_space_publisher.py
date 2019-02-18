#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan
# from std_msgs.msg import Float32
from ros_exercises.msg import OpenSpace

pub_dist = rospy.Publisher('open_space', OpenSpace)
#pub_angle = rospy.Publisher('open_space/angle', Float32)
 
def callback(data):
    max_dist = None
    max_angle = None
    max_index = 0
    for i, dist in enumerate(data.ranges):
        if max_dist:
            if max_dist < data:
                max_index = int(i)
                max_dist = float(dist)
    os_msg = OpenSpace()
    os_msg.distance = max_dist
    max_angle = data.angle_min + max_index*data.angle_increment
    os_msg.angle = max_angle
    pub_dist.publish(os_msg)
#    pub_angle.publish(max_angle)

rospy.init_node('open_space_publisher', anonymous=False)
rospy.Subscriber('fake_scan', LaserScan, callback)
rospy.spin()
