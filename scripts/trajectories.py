#!/usr/bin/env python3
#!-*- using: utf-8 -*-

import rospy
from rospy.timer import Rate
from std_msgs.msg import Float64
import numpy as np

def talker():
    rospy.init_node('posicion')
    pub_1 = rospy.Publisher('/scorbot/m1_position_controller/command', Float64, queue_size=10)
    pub_2 = rospy.Publisher('/scorbot/m2_position_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    s = Float64()

    t = np.arange(0, 60, 0.6)
    sine = np.sin(t/10)

    while not rospy.is_shutdown():
        for i in range(len(sine)):
            s = sine[i]
            pub_1.publish(s)
            pub_2.publish(s)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass