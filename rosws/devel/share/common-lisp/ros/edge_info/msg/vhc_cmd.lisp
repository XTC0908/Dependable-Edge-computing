; Auto-generated. Do not edit!


(cl:in-package edge_info-msg)


;//! \htmlinclude vhc_cmd.msg.html

(cl:defclass <vhc_cmd> (roslisp-msg-protocol:ros-message)
  ((vhcid
    :reader vhcid
    :initarg :vhcid
    :type cl:integer
    :initform 0)
   (cmd
    :reader cmd
    :initarg :cmd
    :type cl:integer
    :initform 0))
)

(cl:defclass vhc_cmd (<vhc_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vhc_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vhc_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name edge_info-msg:<vhc_cmd> is deprecated: use edge_info-msg:vhc_cmd instead.")))

(cl:ensure-generic-function 'vhcid-val :lambda-list '(m))
(cl:defmethod vhcid-val ((m <vhc_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:vhcid-val is deprecated.  Use edge_info-msg:vhcid instead.")
  (vhcid m))

(cl:ensure-generic-function 'cmd-val :lambda-list '(m))
(cl:defmethod cmd-val ((m <vhc_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader edge_info-msg:cmd-val is deprecated.  Use edge_info-msg:cmd instead.")
  (cmd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vhc_cmd>) ostream)
  "Serializes a message object of type '<vhc_cmd>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'vhcid)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'cmd)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'cmd)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'cmd)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'cmd)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vhc_cmd>) istream)
  "Deserializes a message object of type '<vhc_cmd>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'vhcid)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'cmd)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'cmd)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'cmd)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'cmd)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vhc_cmd>)))
  "Returns string type for a message object of type '<vhc_cmd>"
  "edge_info/vhc_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vhc_cmd)))
  "Returns string type for a message object of type 'vhc_cmd"
  "edge_info/vhc_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vhc_cmd>)))
  "Returns md5sum for a message object of type '<vhc_cmd>"
  "431b3cb4cfa302ca931f4d197d26c3a0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vhc_cmd)))
  "Returns md5sum for a message object of type 'vhc_cmd"
  "431b3cb4cfa302ca931f4d197d26c3a0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vhc_cmd>)))
  "Returns full string definition for message of type '<vhc_cmd>"
  (cl:format cl:nil "uint32 vhcid~%uint32 cmd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vhc_cmd)))
  "Returns full string definition for message of type 'vhc_cmd"
  (cl:format cl:nil "uint32 vhcid~%uint32 cmd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vhc_cmd>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vhc_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'vhc_cmd
    (cl:cons ':vhcid (vhcid msg))
    (cl:cons ':cmd (cmd msg))
))
