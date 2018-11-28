#!/bin/sh

cd ./Dependable-Edge-computing/rosws

roscore &
source devel/setup.sh
rosrun edge_info vhc1.py&
rosrun edge_info vhc2.py&
rosrun edge_info ghost_vhc.py&
roslaunch bridge rosbridge_websocket.launch&