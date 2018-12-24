#!/usr/bin/env python

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

#vhc_geo.msg
#Header header
#uint32 vhcid
#geographic_msgs/GeoPoint geo

#vhc_path.msg
#uint32 vhcid
#geographic_msgs/GeoPoint start
#geographic_msgs/GeoPoint end



import rospy
import numpy
from std_msgs.msg import String
from geographic_msgs.msg import RoutePath, RouteSegment, WayPoint, GeoPoint
from edge_info.msg import map_info
from edge_info.msg import vhc_geo,vhc_cmd

def dist(A,B):
    return numpy.sqrt((A.geo.longitude-B.geo.longitude)*(A.geo.longitude-B.geo.longitude) + (A.geo.latitude-B.geo.latitude)*(A.geo.latitude-B.geo.latitude))

class vehicle:
    vhc_status = 0
    obs_status = 0
    vhcid = 1
    GeoP_msg = vhc_geo()

    def __init__(self,id):
        self.vhcid = id
        self.Obs_pub = rospy.Publisher('obspoint', vhc_geo, queue_size=10)

    def vhc_status_callback(self,data):
        if data.vhcid == self.vhcid:
            if data.cmd == 1:
                self.vhc_status = 1
            if data.cmd == 0:
                self.vhc_status = 0


    def obs_callback(self,data):
        if data.vhcid != self.GeoP_msg.vhcid and dist(self.GeoP_msg,data) < 0.0001:
            self.obs_status = 1
            Obs_msg = vhc_geo()
            Obs_msg.vhcid = self.vhcid
            Obs_msg.geo.latitude = data.geo.latitude
            Obs_msg.geo.longitude = data.geo.longitude
            Obs_msg.geo.altitude = data.geo.altitude
            print("Vehicle " + str(self.vhcid) + " finds obstacle in ["+ str(data.geo.latitude) + " , " + str(data.geo.longitude)+ " , "+str(data.geo.altitude)+"]")
            self.Obs_pub.publish(Obs_msg)

            
    def vhc_path_callback(self,data):
        self.end = data

    def fake_geo_01(self,end):
        #fake_start = [59.3365935,18.0674845,0.0]
        #fake_end = [59.3367506,18.0707389,0.0]

        r = 0.000001
        vhc_p = self.GeoP_msg
        distAB = dist(end, vhc_p)
        n = distAB/r
        #angleAB = (end.geo.longitude-vhc_p.geo.longitude)/(end.geo.latitude-vhc_p.geo.latitude)
        if n<1:
            vhc_p = end
        else:
            vhc_p.geo.latitude = vhc_p.geo.latitude + (end.geo.latitude-vhc_p.geo.latitude)/n
            vhc_p.geo.longitude = vhc_p.geo.longitude + (end.geo.longitude - vhc_p.geo.longitude)/n
            vhc_p.geo.altitude = 0.0 
        return vhc_p

    def GeoP_setstart(self,lat,lon,alt):
        vhc_p = vhc_geo()
        vhc_p.vhcid = self.vhcid
        vhc_p.geo.latitude = lat
        vhc_p.geo.longitude = lon
        vhc_p.geo.altitude = alt
        self.GeoP_msg = vhc_p

    def edge_talker(self):
        GeoP_pub = rospy.Publisher('geopoint', vhc_geo, queue_size=10)
        Obs_pub = rospy.Publisher('obspoint', vhc_geo, queue_size=10)
        rospy.Subscriber("vhc_status_m", vhc_cmd, self.vhc_status_callback)
        rospy.Subscriber("geopoint", vhc_geo, self.obs_callback)
        rospy.Subscriber("vhc_path_msg", vhc_geo, self.vhc_path_callback)
        rospy.init_node('edge_talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        self.end =  self.GeoP_msg
        i=0
        while not rospy.is_shutdown():
            if self.vhc_status == 1:
                self.GeoP_msg = self.fake_geo_01(self.end)
                i = i + 1
            elif self.vhc_status == 0:
                self.GeoP_msg = self.GeoP_msg
            self.GeoP_msg.header.stamp = rospy.Time.now()    
            GeoP_pub.publish(self.GeoP_msg)
            print("Vehicle" + str(self.GeoP_msg.vhcid) + ": [" + str(self.GeoP_msg.geo.latitude) + "," + str(self.GeoP_msg.geo.longitude) + "," + str(self.GeoP_msg.geo.altitude) + "]")
            print(self.GeoP_msg.header.stamp.secs)
            rate.sleep()
            #rospy.loginfo("Data published: [" + str(self.GeoP_msg.geo.latitude) + "," + str(self.GeoP_msg.geo.longitude) + "," + str(self.GeoP_msg.geo.altitude) + "]")
            
#if __name__ == '__main__':
#    try:
#        vhc1 = vehicle(1)
#        vhc1.GeoP_setstart(59.3365935,18.0674845,0.0)
#        vhc1.edge_talker()
#    except rospy.ROSInterruptException:
#        pass
