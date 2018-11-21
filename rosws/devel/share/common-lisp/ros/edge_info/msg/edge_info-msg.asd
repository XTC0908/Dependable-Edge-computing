
(cl:in-package :asdf)

(defsystem "edge_info-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geographic_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "map_info" :depends-on ("_package_map_info"))
    (:file "_package_map_info" :depends-on ("_package"))
    (:file "vhc_geo" :depends-on ("_package_vhc_geo"))
    (:file "_package_vhc_geo" :depends-on ("_package"))
  ))