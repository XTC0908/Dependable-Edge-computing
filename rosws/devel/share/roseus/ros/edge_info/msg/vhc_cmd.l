;; Auto-generated. Do not edit!


(when (boundp 'edge_info::vhc_cmd)
  (if (not (find-package "EDGE_INFO"))
    (make-package "EDGE_INFO"))
  (shadow 'vhc_cmd (find-package "EDGE_INFO")))
(unless (find-package "EDGE_INFO::VHC_CMD")
  (make-package "EDGE_INFO::VHC_CMD"))

(in-package "ROS")
;;//! \htmlinclude vhc_cmd.msg.html


(defclass edge_info::vhc_cmd
  :super ros::object
  :slots (_vhcid _cmd ))

(defmethod edge_info::vhc_cmd
  (:init
   (&key
    ((:vhcid __vhcid) 0)
    ((:cmd __cmd) 0)
    )
   (send-super :init)
   (setq _vhcid (round __vhcid))
   (setq _cmd (round __cmd))
   self)
  (:vhcid
   (&optional __vhcid)
   (if __vhcid (setq _vhcid __vhcid)) _vhcid)
  (:cmd
   (&optional __cmd)
   (if __cmd (setq _cmd __cmd)) _cmd)
  (:serialization-length
   ()
   (+
    ;; uint32 _vhcid
    4
    ;; uint32 _cmd
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _vhcid
       (write-long _vhcid s)
     ;; uint32 _cmd
       (write-long _cmd s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _vhcid
     (setq _vhcid (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _cmd
     (setq _cmd (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get edge_info::vhc_cmd :md5sum-) "431b3cb4cfa302ca931f4d197d26c3a0")
(setf (get edge_info::vhc_cmd :datatype-) "edge_info/vhc_cmd")
(setf (get edge_info::vhc_cmd :definition-)
      "uint32 vhcid
uint32 cmd

")



(provide :edge_info/vhc_cmd "431b3cb4cfa302ca931f4d197d26c3a0")


