; Auto-generated. Do not edit!


(cl:in-package edge_info-msg)


;//! \htmlinclude vhc_geo.msg.html

(cl:defclass <vhc_geo> (roslisp-msg-protocol:ros-message)
  ((vhcid
    :reader vhcid
    :initarg :vhcid
    :type cl:integer
    :initform 0)
   (geo
    :reader geo
    :initarg :geo
    :type geographic_msgs-msg:GeoPoint
    :initform (cl:make-instance 'geographic_msgs-msg:GeoPoint)))
)

(cl:defclass vhc_geo (<vhc_geo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vhc_geo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vhc_geo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name edge_info-msg:<vhc_geo> is deprecated: use edge_info-msg:vhc_geo instead.")))

(cl:ensure-generic-function 'vhcid-val :lambda-list '(m))
(cl:defmethod vhcid-val ((m <vhc_geo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:vhcid-val is deprecated.  Use edge_info-msg:vhcid instead.")
  (vhcid m))

(cl:ensure-generic-function 'geo-val :lambda-list '(m))
(cl:defmethod geo-val ((m <vhc_geo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:geo-val is deprecated.  Use edge_info-msg:geo instead.")
  (geo m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vhc_geo>) ostream)
  "Serializes a message object of type '<vhc_geo>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'vhcid)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'geo) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vhc_geo>) istream)
  "Deserializes a message object of type '<vhc_geo>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'geo) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vhc_geo>)))
  "Returns string type for a message object of type '<vhc_geo>"
  "edge_info/vhc_geo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vhc_geo)))
  "Returns string type for a message object of type 'vhc_geo"
  "edge_info/vhc_geo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vhc_geo>)))
  "Returns md5sum for a message object of type '<vhc_geo>"
  "cfafd41cb4021d78978805fcb28453a7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vhc_geo)))
  "Returns md5sum for a message object of type 'vhc_geo"
  "cfafd41cb4021d78978805fcb28453a7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vhc_geo>)))
  "Returns full string definition for message of type '<vhc_geo>"
  (cl:format cl:nil "uint32 vhcid~%geographic_msgs/GeoPoint geo~%~%================================================================================~%MSG: geographic_msgs/GeoPoint~%# Geographic point, using the WGS 84 reference ellipsoid.~%~%# Latitude [degrees]. Positive is north of equator; negative is south~%# (-90 <= latitude <= +90).~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is~%# west (-180 <= longitude <= +180). At the poles, latitude is -90 or~%# +90, and longitude is irrelevant, but must be in range.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).~%float64 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vhc_geo)))
  "Returns full string definition for message of type 'vhc_geo"
  (cl:format cl:nil "uint32 vhcid~%geographic_msgs/GeoPoint geo~%~%================================================================================~%MSG: geographic_msgs/GeoPoint~%# Geographic point, using the WGS 84 reference ellipsoid.~%~%# Latitude [degrees]. Positive is north of equator; negative is south~%# (-90 <= latitude <= +90).~%float64 latitude~%~%# Longitude [degrees]. Positive is east of prime meridian; negative is~%# west (-180 <= longitude <= +180). At the poles, latitude is -90 or~%# +90, and longitude is irrelevant, but must be in range.~%float64 longitude~%~%# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).~%float64 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vhc_geo>))
  (cl:+ 0
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'geo))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vhc_geo>))
  "Converts a ROS message object to a list"
  (cl:list 'vhc_geo
    (cl:cons ':vhcid (vhcid msg))
    (cl:cons ':geo (geo msg))
))
