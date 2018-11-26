
The ros workspace simulates the edge behaviours. 

## Environment

### add path to bashrc

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/Dependable-Edge-computing/rosws

### install rosbridge

http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge

## How to run

#### Treminal 1

roscore

#### Terminal 2

source devel/setup.sh

rosrun edge_info vhc1.py

#### Terminal 3

source devel/setup.sh

rosrun edge_info vhc2.py

#### Terminal 4

source devel/setup.sh

rosrun edge_info vhc2.py

#### Terminal 5

source devel/setup.sh

rosrun edge_info ghost_vhc.py

#### Terminal 6

roslaunch bridge rosbridge_websocket.launch

#### WEB 

open edgeweb.html in brouser

To watch concole, press F12

