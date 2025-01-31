#!/usr/bin/env python3

import rospy
import sys

from pid_tuning.evolutive_algorithms.evolutive_algorithms import HarmonySearch
from pid_tuning.settings.control_gazebo import ControlGazebo

reset_control = ControlGazebo()

A = 2
m = 6
N = 30
Gm = 50

r_accept = 0.7
r_pa = 0.45
hz = 25

hs = HarmonySearch(N, m, Gm, A, r_accept, r_pa, '/home/wsl/catkin_ws/src/turtlebot3/config/paths.json', epsilon_1=1, tm = 28800)

X = hs.gen_population()

def evol_loop():
    rospy.init_node("tuning_node")
    file = open("best_pid_values_HS.txt", 'w')

    reset_control.init_values()
    rate = rospy.Rate(hz)
    while not rospy.is_shutdown():
        hs.evaluate(X, reset_control, rate)
        X_best = hs.harmony_search(X, reset_control, rate)  
        file.write(str(X_best))
        file.close()
        break


if __name__ == '__main__':
    try:
        evol_loop()
    except rospy.ROSInterruptException:
        pass