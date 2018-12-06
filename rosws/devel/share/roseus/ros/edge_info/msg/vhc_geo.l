;; Auto-generated. Do not edit!


(when (boundp 'edge_info::vhc_geo)
  (if (not (find-package "EDGE_INFO"))
    (make-package "EDGE_INFO"))
  (shadow 'vhc_geo (find-package "EDGE_INFO")))
(unless (find-package "EDGE_INFO::VHC_GEO")
  (make-package "EDGE_INFO::VHC_GEO"))

(in-package "ROS")
;;//! \htmlinclude vhc_geo.msg.html
(if (not (find-package "GEOGRAPHIC_MSGS"))
  (ros::roseus-add-msgs "geographic_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass edge_info::vhc_geo
  :super ros::object
  :slots (_header _vhcid _geo ))

(defmethod edge_info::vhc_geo
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:vhcid __vhcid) 0)
    ((:geo __geo) (instance geographic_msgs::GeoPoint :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _vhcid (round __vhcid))
   (setq _geo __geo)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:vhcid
   (&optional __vhcid)
   (if __vhcid (setq _vhcid __vhcid)) _vhcid)
  (:geo
   (&rest __geo)
   (if (keywordp (car __geo))
       (send* _geo __geo)
     (progn
       (if __geo (setq _geo (car __geo)))
       _geo)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint32 _vhcid
    4
    ;; geographic_msgs/GeoPoint _geo
    (send _geo :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint32 _vhcid
       (write-long _vhcid s)
     ;; geographic_msgs/GeoPoint _geo
       (send _geo :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint32 _vhcid
     (setq _vhcid (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geographic_msgs/GeoPoint _geo
     (send _geo :deserialize buf ptr-) (incf ptr- (send _geo :serialization-length))
   ;;
   self)
  )

(setf (get edge_info::vhc_geo :md5sum-) "46215f2797945e983668770007bc875d")
(setf (get edge_info::vhc_geo :datatype-) "edge_info/vhc_geo")
(setf (get edge_info::vhc_geo :definition-)
      "Header header
uint32 vhcid
geographic_msgs/GeoPoint geo

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geographic_msgs/GeoPoint
# Geographic point, using the WGS 84 reference ellipsoid.

# Latitude [degrees]. Positive is north of equator; negative is south
# (-90 <= latitude <= +90).
float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is
# west (-180 <= longitude <= +180). At the poles, latitude is -90 or
# +90, and longitude is irrelevant, but must be in range.
float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).
float64 altitude

")



(provide :edge_info/vhc_geo "46215f2797945e983668770007bc875d")


