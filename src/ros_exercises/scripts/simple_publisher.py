#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32

pub = rospy.Publisher('my_random_float', Float32,queue_size =10)
rospy.init_node('simple_publisher')
rate = rospy.Rate(20)
while not rospy.is_shutdown():
    rnd_num = random.random()*10
    if rnd_num == 0:
        rnd_num = 10
    rospy.loginfo(rnd_num)
    pub.publish(rnd_num)
    rate.sleep()


