#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

def callback(data):
    rospy.loginfo("Position: %s", data.position)
    #print(data.position[0])
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/scorbot/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()