#!/bin/bash

cd /Dependable-Edge-computing/rosws
source devel/setup.sh
roscore > /tmp/core_log.txt 2>&1 &
rosrun edge_info vhc1.py > /tmp/vhc1_log.txt 2>&1 &
roslaunch bridge rosbridge_websocket.launch > /tmp/bridge_log.txt 2>&1 &