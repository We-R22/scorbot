#!/usr/bin/env python3

import rospy
import sys

from pid_tuning.evolutive_algorithms.dif_evolution import DifferentialEvolution
from pid_tuning.settings.control_gazebo import ControlGazebo

reset_control = ControlGazebo()

A = 5
m = 15
N = 30
Gm = 50
F = 0.90
C = 0.90
hz = 25

de = DifferentialEvolution(N, m, Gm, F, C, A, '/home/jacob/ws/src/scorbot/config/paths.json', epsilon_1=1, tm=28800)

X = de.gen_population()

def evol_loop():
    rospy.init_node("tuning_node")
    file = open("best_pid_values_DE.txt", 'w')
    
    reset_control.init_values()
    rate = rospy.Rate(hz)
    while not rospy.is_shutdown():
        de.evaluate(X, reset_control, rate)
        X_best = de.dif_evolution(X, reset_control, rate)
        file.write(str(X_best))
        file.close()
        break

if __name__ == '__main__':
    try:
        evol_loop()
    except rospy.ROSInterruptException:
        pass