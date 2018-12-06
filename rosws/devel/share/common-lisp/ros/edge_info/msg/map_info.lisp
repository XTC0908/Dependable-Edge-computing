; Auto-generated. Do not edit!


(cl:in-package edge_info-msg)


;//! \htmlinclude map_info.msg.html

(cl:defclass <map_info> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (WayPoints
    :reader WayPoints
    :initarg :WayPoints
    :type (cl:vector geographic_msgs-msg:WayPoint)
   :initform (cl:make-array 0 :element-type 'geographic_msgs-msg:WayPoint :initial-element (cl:make-instance 'geographic_msgs-msg:WayPoint)))
   (RouteSegments
    :reader RouteSegments
    :initarg :RouteSegments
    :type (cl:vector geographic_msgs-msg:RouteSegment)
   :initform (cl:make-array 0 :element-type 'geographic_msgs-msg:RouteSegment :initial-element (cl:make-instance 'geographic_msgs-msg:RouteSegment)))
   (RoutePaths
    :reader RoutePaths
    :initarg :RoutePaths
    :type (cl:vector geographic_msgs-msg:RoutePath)
   :initform (cl:make-array 0 :element-type 'geographic_msgs-msg:RoutePath :initial-element (cl:make-instance 'geographic_msgs-msg:RoutePath))))
)

(cl:defclass map_info (<map_info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <map_info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'map_info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name edge_info-msg:<map_info> is deprecated: use edge_info-msg:map_info instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <map_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:header-val is deprecated.  Use edge_info-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'WayPoints-val :lambda-list '(m))
(cl:defmethod WayPoints-val ((m <map_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:WayPoints-val is deprecated.  Use edge_info-msg:WayPoints instead.")
  (WayPoints m))

(cl:ensure-generic-function 'RouteSegments-val :lambda-list '(m))
(cl:defmethod RouteSegments-val ((m <map_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:RouteSegments-val is deprecated.  Use edge_info-msg:RouteSegments instead.")
  (RouteSegments m))

(cl:ensure-generic-function 'RoutePaths-val :lambda-list '(m))
(cl:defmethod RoutePaths-val ((m <map_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:RoutePaths-val is deprecated.  Use edge_info-msg:RoutePaths instead.")
  (RoutePaths m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <map_info>) ostream)
  "Serializes a message object of type '<map_info>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'WayPoints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'WayPoints))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'RouteSegments))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'RouteSegments))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'RoutePaths))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'RoutePaths))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <map_info>) istream)
  "Deserializes a message object of type '<map_info>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'WayPoints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'WayPoints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geographic_msgs-msg:WayPoint))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'RouteSegments) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'RouteSegments)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geographic_msgs-msg:RouteSegment))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'RoutePaths) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'RoutePaths)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geographic_msgs-msg:RoutePath))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<map_info>)))
  "Returns string type for a message object of type '<map_info>"
  "edge_info/map_info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'map_info)))
  "Returns string type for a message object of type 'map_info"
  "edge_info/map_info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<map_info>)))
  "Returns md5sum for a message object of type '<map_info>"
  "07072df7d6cc23281dae048c2f9a3fa0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'map_info)))
  "Returns md5sum for a message object of type 'map_info"
  "07072df7d6cc23281dae048c2f9a3fa0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<map_info>)))
  "Returns full string definition for message of type '<map_info>"
  (cl:format cl:nil "Header header~%geographic_msgs/WayPoint[] WayPoints~%geographic_msgs/RouteSegment[] RouteSegments~%geographic_msgs/RoutePath[] RoutePaths ~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geographic_msgs/WayPoint~%# Way-point element for a geographic map.~%~%uuid_msgs/UniqueID id   # Unique way-point identifier~%GeoPoint   position     # Position relative to WGS 84 ellipsoid~%KeyValue[] props        # Key/value properties for this point~%~%================================================================================~%MSG: uuid_msgs/UniqueID~%# A universally unique identifier (UUID).~%#~%#  http://en.wikipedia.org/wiki/Universally_unique_identifier~%#  http://tools.ietf.org/html/rfc4122.html~%~%uint8[16] uuid~%~%================================================================================~%MSG: geographic_msgs/GeoPoint~%# Geographic point, using the WGS 84 reference ellipsoid.~%~%# Latitude [degrees]. Positive is north of equator; negative is south~%# (-90 <= latitude <= +90).~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is~%# west (-180 <= longitude <= +180). At the poles, latitude is -90 or~%# +90, and longitude is irrelevant, but must be in range.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).~%float64 altitude~%~%================================================================================~%MSG: geographic_msgs/KeyValue~%# Geographic map tag (key, value) pair~%#~%# This is equivalent to diagnostic_msgs/KeyValue, repeated here to~%# avoid introducing a trivial stack dependency.~%~%string key                     # tag label~%string value                   # corresponding value~%~%================================================================================~%MSG: geographic_msgs/RouteSegment~%# Route network segment.~%#~%# This is one directed edge of a RouteNetwork graph. It represents a~%# known path from one way point to another.  If the path is two-way,~%# there will be another RouteSegment with \"start\" and \"end\" reversed.~%~%uuid_msgs/UniqueID id           # Unique identifier for this segment~%~%uuid_msgs/UniqueID start        # beginning way point of segment~%uuid_msgs/UniqueID end          # ending way point of segment~%~%KeyValue[] props                # segment properties~%~%================================================================================~%MSG: geographic_msgs/RoutePath~%# Path through a route network.~%#~%# A path is a sequence of RouteSegment edges.  This information is~%# extracted from a RouteNetwork graph.  A RoutePath lists the route~%# segments needed to reach some chosen goal.~%~%Header header~%~%uuid_msgs/UniqueID   network    # Route network containing this path~%uuid_msgs/UniqueID[] segments   # Sequence of RouteSegment IDs~%KeyValue[]           props      # Key/value properties~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'map_info)))
  "Returns full string definition for message of type 'map_info"
  (cl:format cl:nil "Header header~%geographic_msgs/WayPoint[] WayPoints~%geographic_msgs/RouteSegment[] RouteSegments~%geographic_msgs/RoutePath[] RoutePaths ~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geographic_msgs/WayPoint~%# Way-point element for a geographic map.~%~%uuid_msgs/UniqueID id   # Unique way-point identifier~%GeoPoint   position     # Position relative to WGS 84 ellipsoid~%KeyValue[] props        # Key/value properties for this point~%~%================================================================================~%MSG: uuid_msgs/UniqueID~%# A universally unique identifier (UUID).~%#~%#  http://en.wikipedia.org/wiki/Universally_unique_identifier~%#  http://tools.ietf.org/html/rfc4122.html~%~%uint8[16] uuid~%~%================================================================================~%MSG: geographic_msgs/GeoPoint~%# Geographic point, using the WGS 84 reference ellipsoid.~%~%# Latitude [degrees]. Positive is north of equator; negative is south~%# (-90 <= latitude <= +90).~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is~%# west (-180 <= longitude <= +180). At the poles, latitude is -90 or~%# +90, and longitude is irrelevant, but must be in range.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).~%float64 altitude~%~%================================================================================~%MSG: geographic_msgs/KeyValue~%# Geographic map tag (key, value) pair~%#~%# This is equivalent to diagnostic_msgs/KeyValue, repeated here to~%# avoid introducing a trivial stack dependency.~%~%string key                     # tag label~%string value                   # corresponding value~%~%================================================================================~%MSG: geographic_msgs/RouteSegment~%# Route network segment.~%#~%# This is one directed edge of a RouteNetwork graph. It represents a~%# known path from one way point to another.  If the path is two-way,~%# there will be another RouteSegment with \"start\" and \"end\" reversed.~%~%uuid_msgs/UniqueID id           # Unique identifier for this segment~%~%uuid_msgs/UniqueID start        # beginning way point of segment~%uuid_msgs/UniqueID end          # ending way point of segment~%~%KeyValue[] props                # segment properties~%~%================================================================================~%MSG: geographic_msgs/RoutePath~%# Path through a route network.~%#~%# A path is a sequence of RouteSegment edges.  This information is~%# extracted from a RouteNetwork graph.  A RoutePath lists the route~%# segments needed to reach some chosen goal.~%~%Header header~%~%uuid_msgs/UniqueID   network    # Route network containing this path~%uuid_msgs/UniqueID[] segments   # Sequence of RouteSegment IDs~%KeyValue[]           props      # Key/value properties~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <map_info>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'WayPoints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'RouteSegments) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'RoutePaths) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <map_info>))
  "Converts a ROS message object to a list"
  (cl:list 'map_info
    (cl:cons ':header (header msg))
    (cl:cons ':WayPoints (WayPoints msg))
    (cl:cons ':RouteSegments (RouteSegments msg))
    (cl:cons ':RoutePaths (RoutePaths msg))
))
