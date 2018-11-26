#!/usr/bin/env python
from vehicle import vehicle
try:
    vhc = vehicle(2)
    vhc.GeoP_setstart(59.3365935,18.0674845,0.0)
    vhc.edge_talker()
except rospy.ROSInterruptException:
    pass
