##Environment
###add path to bashrc
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/Dependable-Edge-computing/rosws

###install rosbridge
http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge

##gathermsg

Treminal 1
roscore

Terminal 2
source devel/setup.sh
rosrun gathermsg talker.py

Terminal 3
rosrun gathermsg listener.py

Terminal 4
roslaunch bridge rosbridge_websocket.launch

open msgweb.html in brouser
To watch concole, press F12


##edge_info

Treminal 1
roscore

Terminal 2
source devel/setup.sh
rosrun edge_info edge_talker.py

#listener not completed
#Terminal 3
#source devel/setup.sh
#rosrun gathermsg listener.py

Terminal 4
roslaunch bridge rosbridge_websocket.launch

open edgeweb.html in brouser
To watch concole, press F12



Terminator Ctrl-Shift E split vertically
	   Ctrl-Shift O split horizontally
