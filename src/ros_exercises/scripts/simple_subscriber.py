#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float32

pub = rospy.Publisher('random_float_log', Float32)

def callback(data):
    pub.publish(math.log(float(data.data)))
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

rospy.init_node('simple_subscriber', anonymous=True)
rospy.Subscriber('my_random_float', Float32, callback)
rospy.spin()
