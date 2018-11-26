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


(defclass edge_info::vhc_geo
  :super ros::object
  :slots (_vhcid _geo ))

(defmethod edge_info::vhc_geo
  (:init
   (&key
    ((:vhcid __vhcid) 0)
    ((:geo __geo) (instance geographic_msgs::GeoPoint :init))
    )
   (send-super :init)
   (setq _vhcid (round __vhcid))
   (setq _geo __geo)
   self)
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
    ;; uint32 _vhcid
    4
    ;; geographic_msgs/GeoPoint _geo
    (send _geo :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _vhcid
       (write-long _vhcid s)
     ;; geographic_msgs/GeoPoint _geo
       (send _geo :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _vhcid
     (setq _vhcid (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geographic_msgs/GeoPoint _geo
     (send _geo :deserialize buf ptr-) (incf ptr- (send _geo :serialization-length))
   ;;
   self)
  )

(setf (get edge_info::vhc_geo :md5sum-) "cfafd41cb4021d78978805fcb28453a7")
(setf (get edge_info::vhc_geo :datatype-) "edge_info/vhc_geo")
(setf (get edge_info::vhc_geo :definition-)
      "uint32 vhcid
geographic_msgs/GeoPoint geo

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



(provide :edge_info/vhc_geo "cfafd41cb4021d78978805fcb28453a7")


