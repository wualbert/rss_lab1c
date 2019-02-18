#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32

pub_dist = rospy.Publisher('open_space/distance', Float32)
pub_angle = rospy.Publisher('open_space/angle', Float32)
 
def callback(data):

rospy.init_node('open_space_publisher', anonymous=False)
rospy.Subscriber('my_random_float', Float32, callback)
rospy.spin()
