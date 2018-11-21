#!/usr/bin/env python
# license removed for brevity


# Way-point element for a geographic map.

#uuid_msgs/UniqueID id   # Unique way-point identifier
#GeoPoint   position     # Position relative to WGS 84 ellipsoid
#KeyValue[] props        # Key/value properties for this point

# Route network segment.
#
# This is one directed edge of a RouteNetwork graph. It represents a
# known path from one way point to another.  If the path is two-way,
# there will be another RouteSegment with "start" and "end" reversed.
#uuid_msgs/UniqueID id           # Unique identifier for this segment
#uuid_msgs/UniqueID start        # beginning way point of segment
#uuid_msgs/UniqueID end          # ending way point of segment
#KeyValue[] props                # segment properties


# Path through a route network.
#
# A path is a sequence of RouteSegment edges.  This information is
# extracted from a RouteNetwork graph.  A RoutePath lists the route
# segments needed to reach some chosen goal.

#Header header

#uuid_msgs/UniqueID   network    # Route network containing this path
#uuid_msgs/UniqueID[] segments   # Sequence of RouteSegment IDs
#KeyValue[]           props      # Key/value properties

# Geographic point, using the WGS 84 reference ellipsoid.

# Latitude [degrees]. Positive is north of equator; negative is south
# (-90 <= latitude <= +90).
#float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is
# west (-180 <= longitude <= +180). At the poles, latitude is -90 or
# +90, and longitude is irrelevant, but must be in range.
#float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).
#float64 altitude



import rospy
from std_msgs.msg import String
from geographic_msgs.msg import RoutePath, RouteSegment, WayPoint, GeoPoint
from edge_info.msg import map_info
from edge_info.msg import vhc_geo

vhc_status = 1
obs_status = 0
def vhc_status_callback(data):
    global vhc_status
    if data.data == "Start":
    	vhc_status = 1

def obs_callback(data):
   global obs_status

        

def fake_geo_02(i):
    fake_start = [59.3365935,18.0674845,0.0]
    fake_end = [59.3367506,18.0707389,0.0]
    num = 1000
    vhc_p = vhc_geo()
    vhc_p.vhcid = 2
    i = i-200
    if i<0:
        vhc_p.geo.latitude = fake_start[0]
        vhc_p.geo.longitude = fake_start[1]
        vhc_p.geo.altitude = fake_start[2]
    elif i<num:
        vhc_p.geo.latitude = (fake_end[0]-fake_start[0])/num*i+fake_start[0]
        vhc_p.geo.longitude =  (fake_end[1]-fake_start[1])/num*i+fake_start[1]
        vhc_p.geo.altitude = 0.0
    else:
        vhc_p.geo.latitude = fake_end[0]
        vhc_p.geo.longitude = fake_end[1]
        vhc_p.geo.altitude = fake_end[2]
    return vhc_p



def edge_talker():
    global start, map_status
    GeoP_pub = rospy.Publisher('geopoint', vhc_geo, queue_size=10)
    rospy.Subscriber("vhc_status_msg", String, vhc_status_callback)
    rospy.Subscriber("geopoint", vhc_geo, obs_callback)
    rospy.init_node('edge_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0
    while not rospy.is_shutdown():
        if vhc_status == 1:
            GeoP_msg = vhc_geo()
            GeoP_msg = fake_geo_02(i)
            i = i + 1
            GeoP_pub.publish(GeoP_msg)
            print("Vehicle" + str(GeoP_msg.vhcid) + ": [" + str(GeoP_msg.geo.latitude) + "," + str(GeoP_msg.geo.longitude) + "," + str(GeoP_msg.geo.altitude) + "]")
	    #rospy.loginfo("Data published: [" + str(GeoP_msg.geo.latitude) + "," + str(GeoP_msg.geo.longitude) + "," + str(GeoP_msg.geo.altitude) + "]")
	rate.sleep()


if __name__ == '__main__':
    try:
        edge_talker()
    except rospy.ROSInterruptException:
        pass
