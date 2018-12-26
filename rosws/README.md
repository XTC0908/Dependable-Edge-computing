
The ros workspace simulates the edge behaviours. 

## Environment

### Install ROS kinectic

http://wiki.ros.org/kinetic/Installation/Ubuntu

### Install catkin workspace

http://wiki.ros.org/catkin

### Install rosbridge

http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge

sudo apt-get install ros-kinetic-rosbridge-suite

source /opt/ros/kinetic/setup.bash

### install geographic messages


### Add path to bashrc

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/Dependable-Edge-computing/rosws


## Make workspace

Delete 'build' and 'devel' folder. 

catkin_make clean & catkin_make

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

rosrun edge_info ghost_vhc.py


#### Terminal 5

roslaunch bridge rosbridge_websocket.launch

#### Client 

##### Web Client

open edgeweb.html in brouser

To watch concole, press F12

##### Python client

Install required python package

python pub_client.py

Send command: [vhcid cmd lat lon alt]

vhcid: vehicle ID

cmd: command, 0 - stop, 1 - start, 2 - send destination

lat lon alt: latitude, longitude, altitude. If command is 0 or 1, just input three random number in this place. If command  is 2, input the destination GPS

python sub_client.py

## How to develop

### message type

Message type suggested: geographic_msgs/GeoPoint, geographic_msgs/RoutePath, geographic_msgs/RouteSegment, geographic_msgs/WayPoint

Message type used: See notes at the beginning of src/edge_info/vehicle.py

### Pack messages

Define messages in src/<package name>/msg/ 

Modify src/<package name>/Cmakelist.txt: Add the name of newly created message in 'add_message_files()' around line 53.

catkin_make clean $ catkin_make

#### Receive messages from client


### Create connection

Local connection : in pub_client.py, sub_client.py, TCP_IP = '127.0.0.1'. In edgeweb.html,  url : 'ws://localhost:9090'.

Connect from another computer: Check local IP address using 'ifconfig' command. Change TCP_IP/url to local IP address.




