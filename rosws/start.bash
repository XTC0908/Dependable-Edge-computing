#!/bin/bash

#cd /Dependable-Edge-computing/rosws
source devel/setup.sh
#roscore > /tmp/core_log.txt 2>/tmp/err_log.txt &
rosrun edge_info vhc1.py > /tmp/vhc1_log.txt 2>/tmp/err_log.txt &
roslaunch bridge rosbridge_websocket.launch > /tmp/bridge_log.txt 2>/tmp/err_log.txt &
