#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geographic_msgs.msg import RoutePath, RouteSegment, WayPoint, GeoPoint

start = 0

def callback(data):
    global start
    start = 1

def edge_talker():
    global start
    Route_pub = rospy.Publisher('route', RoutePath, queue_size=10)
    RouteSeg_pub = rospy.Publisher('routeseg', RouteSegment, queue_size=10)
    WayP_pub = rospy.Publisher('waypoint', WayPoint, queue_size=10)
    GeoP_pub = rospy.Publisher('geopoint', GeoPoint, queue_size=10)
    rospy.Subscriber("start_msg", String, callback)
    rospy.init_node('edge_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if start == 1:
		Route_msg = RoutePath()
		RouteSeg_msg = RouteSegment()
		WayP_msg = WayPoint()
		GeoP_msg = GeoPoint(0.0,0.0,0.0)
		#hello_str = "hello world %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		Route_pub.publish(Route_msg)
		RouteSeg_pub.publish(RouteSeg_msg)
		WayP_pub.publish(WayP_msg)
		GeoP_pub.publish(GeoP_msg)
		rospy.loginfo("All data published.")
	rate.sleep()


if __name__ == '__main__':
    try:
        edge_talker()
    except rospy.ROSInterruptException:
        pass
