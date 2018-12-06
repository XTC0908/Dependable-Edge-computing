;; Auto-generated. Do not edit!


(when (boundp 'edge_info::map_info)
  (if (not (find-package "EDGE_INFO"))
    (make-package "EDGE_INFO"))
  (shadow 'map_info (find-package "EDGE_INFO")))
(unless (find-package "EDGE_INFO::MAP_INFO")
  (make-package "EDGE_INFO::MAP_INFO"))

(in-package "ROS")
;;//! \htmlinclude map_info.msg.html
(if (not (find-package "GEOGRAPHIC_MSGS"))
  (ros::roseus-add-msgs "geographic_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass edge_info::map_info
  :super ros::object
  :slots (_header _WayPoints _RouteSegments _RoutePaths ))

(defmethod edge_info::map_info
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:WayPoints __WayPoints) (let (r) (dotimes (i 0) (push (instance geographic_msgs::WayPoint :init) r)) r))
    ((:RouteSegments __RouteSegments) (let (r) (dotimes (i 0) (push (instance geographic_msgs::RouteSegment :init) r)) r))
    ((:RoutePaths __RoutePaths) (let (r) (dotimes (i 0) (push (instance geographic_msgs::RoutePath :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _WayPoints __WayPoints)
   (setq _RouteSegments __RouteSegments)
   (setq _RoutePaths __RoutePaths)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:WayPoints
   (&rest __WayPoints)
   (if (keywordp (car __WayPoints))
       (send* _WayPoints __WayPoints)
     (progn
       (if __WayPoints (setq _WayPoints (car __WayPoints)))
       _WayPoints)))
  (:RouteSegments
   (&rest __RouteSegments)
   (if (keywordp (car __RouteSegments))
       (send* _RouteSegments __RouteSegments)
     (progn
       (if __RouteSegments (setq _RouteSegments (car __RouteSegments)))
       _RouteSegments)))
  (:RoutePaths
   (&rest __RoutePaths)
   (if (keywordp (car __RoutePaths))
       (send* _RoutePaths __RoutePaths)
     (progn
       (if __RoutePaths (setq _RoutePaths (car __RoutePaths)))
       _RoutePaths)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geographic_msgs/WayPoint[] _WayPoints
    (apply #'+ (send-all _WayPoints :serialization-length)) 4
    ;; geographic_msgs/RouteSegment[] _RouteSegments
    (apply #'+ (send-all _RouteSegments :serialization-length)) 4
    ;; geographic_msgs/RoutePath[] _RoutePaths
    (apply #'+ (send-all _RoutePaths :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geographic_msgs/WayPoint[] _WayPoints
     (write-long (length _WayPoints) s)
     (dolist (elem _WayPoints)
       (send elem :serialize s)
       )
     ;; geographic_msgs/RouteSegment[] _RouteSegments
     (write-long (length _RouteSegments) s)
     (dolist (elem _RouteSegments)
       (send elem :serialize s)
       )
     ;; geographic_msgs/RoutePath[] _RoutePaths
     (write-long (length _RoutePaths) s)
     (dolist (elem _RoutePaths)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geographic_msgs/WayPoint[] _WayPoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _WayPoints (let (r) (dotimes (i n) (push (instance geographic_msgs::WayPoint :init) r)) r))
     (dolist (elem- _WayPoints)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geographic_msgs/RouteSegment[] _RouteSegments
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _RouteSegments (let (r) (dotimes (i n) (push (instance geographic_msgs::RouteSegment :init) r)) r))
     (dolist (elem- _RouteSegments)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geographic_msgs/RoutePath[] _RoutePaths
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _RoutePaths (let (r) (dotimes (i n) (push (instance geographic_msgs::RoutePath :init) r)) r))
     (dolist (elem- _RoutePaths)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get edge_info::map_info :md5sum-) "07072df7d6cc23281dae048c2f9a3fa0")
(setf (get edge_info::map_info :datatype-) "edge_info/map_info")
(setf (get edge_info::map_info :definition-)
      "Header header
geographic_msgs/WayPoint[] WayPoints
geographic_msgs/RouteSegment[] RouteSegments
geographic_msgs/RoutePath[] RoutePaths 

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
MSG: geographic_msgs/WayPoint
# Way-point element for a geographic map.

uuid_msgs/UniqueID id   # Unique way-point identifier
GeoPoint   position     # Position relative to WGS 84 ellipsoid
KeyValue[] props        # Key/value properties for this point

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

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

================================================================================
MSG: geographic_msgs/KeyValue
# Geographic map tag (key, value) pair
#
# This is equivalent to diagnostic_msgs/KeyValue, repeated here to
# avoid introducing a trivial stack dependency.

string key                     # tag label
string value                   # corresponding value

================================================================================
MSG: geographic_msgs/RouteSegment
# Route network segment.
#
# This is one directed edge of a RouteNetwork graph. It represents a
# known path from one way point to another.  If the path is two-way,
# there will be another RouteSegment with \"start\" and \"end\" reversed.

uuid_msgs/UniqueID id           # Unique identifier for this segment

uuid_msgs/UniqueID start        # beginning way point of segment
uuid_msgs/UniqueID end          # ending way point of segment

KeyValue[] props                # segment properties

================================================================================
MSG: geographic_msgs/RoutePath
# Path through a route network.
#
# A path is a sequence of RouteSegment edges.  This information is
# extracted from a RouteNetwork graph.  A RoutePath lists the route
# segments needed to reach some chosen goal.

Header header

uuid_msgs/UniqueID   network    # Route network containing this path
uuid_msgs/UniqueID[] segments   # Sequence of RouteSegment IDs
KeyValue[]           props      # Key/value properties

")



(provide :edge_info/map_info "07072df7d6cc23281dae048c2f9a3fa0")


