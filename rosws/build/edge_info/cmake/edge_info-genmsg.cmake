# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "edge_info: 3 messages, 0 services")

set(MSG_I_FLAGS "-Iedge_info:/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg;-Igeographic_msgs:/opt/ros/kinetic/share/geographic_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Iuuid_msgs:/opt/ros/kinetic/share/uuid_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(edge_info_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_custom_target(_edge_info_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "edge_info" "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" "geographic_msgs/RouteSegment:geographic_msgs/GeoPoint:std_msgs/Header:geographic_msgs/WayPoint:geographic_msgs/RoutePath:geographic_msgs/KeyValue:uuid_msgs/UniqueID"
)

get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_custom_target(_edge_info_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "edge_info" "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" "geographic_msgs/GeoPoint:std_msgs/Header"
)

get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_custom_target(_edge_info_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "edge_info" "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RouteSegment.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/WayPoint.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RoutePath.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/KeyValue.msg;/opt/ros/kinetic/share/uuid_msgs/cmake/../msg/UniqueID.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info
)
_generate_msg_cpp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info
)
_generate_msg_cpp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info
)

### Generating Services

### Generating Module File
_generate_module_cpp(edge_info
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(edge_info_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(edge_info_generate_messages edge_info_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_cpp _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_cpp _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_cpp _edge_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(edge_info_gencpp)
add_dependencies(edge_info_gencpp edge_info_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS edge_info_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RouteSegment.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/WayPoint.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RoutePath.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/KeyValue.msg;/opt/ros/kinetic/share/uuid_msgs/cmake/../msg/UniqueID.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info
)
_generate_msg_eus(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info
)
_generate_msg_eus(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info
)

### Generating Services

### Generating Module File
_generate_module_eus(edge_info
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(edge_info_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(edge_info_generate_messages edge_info_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_eus _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_eus _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_eus _edge_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(edge_info_geneus)
add_dependencies(edge_info_geneus edge_info_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS edge_info_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RouteSegment.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/WayPoint.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RoutePath.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/KeyValue.msg;/opt/ros/kinetic/share/uuid_msgs/cmake/../msg/UniqueID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info
)
_generate_msg_lisp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info
)
_generate_msg_lisp(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info
)

### Generating Services

### Generating Module File
_generate_module_lisp(edge_info
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(edge_info_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(edge_info_generate_messages edge_info_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_lisp _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_lisp _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_lisp _edge_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(edge_info_genlisp)
add_dependencies(edge_info_genlisp edge_info_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS edge_info_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RouteSegment.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/WayPoint.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RoutePath.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/KeyValue.msg;/opt/ros/kinetic/share/uuid_msgs/cmake/../msg/UniqueID.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info
)
_generate_msg_nodejs(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info
)
_generate_msg_nodejs(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info
)

### Generating Services

### Generating Module File
_generate_module_nodejs(edge_info
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(edge_info_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(edge_info_generate_messages edge_info_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_nodejs _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_nodejs _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_nodejs _edge_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(edge_info_gennodejs)
add_dependencies(edge_info_gennodejs edge_info_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS edge_info_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RouteSegment.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/WayPoint.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/RoutePath.msg;/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/KeyValue.msg;/opt/ros/kinetic/share/uuid_msgs/cmake/../msg/UniqueID.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info
)
_generate_msg_py(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geographic_msgs/cmake/../msg/GeoPoint.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info
)
_generate_msg_py(edge_info
  "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info
)

### Generating Services

### Generating Module File
_generate_module_py(edge_info
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(edge_info_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(edge_info_generate_messages edge_info_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_py _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_py _edge_info_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg" NAME_WE)
add_dependencies(edge_info_generate_messages_py _edge_info_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(edge_info_genpy)
add_dependencies(edge_info_genpy edge_info_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS edge_info_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/edge_info
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geographic_msgs_generate_messages_cpp)
  add_dependencies(edge_info_generate_messages_cpp geographic_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(edge_info_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/edge_info
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geographic_msgs_generate_messages_eus)
  add_dependencies(edge_info_generate_messages_eus geographic_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(edge_info_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/edge_info
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geographic_msgs_generate_messages_lisp)
  add_dependencies(edge_info_generate_messages_lisp geographic_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(edge_info_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/edge_info
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geographic_msgs_generate_messages_nodejs)
  add_dependencies(edge_info_generate_messages_nodejs geographic_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(edge_info_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/edge_info
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geographic_msgs_generate_messages_py)
  add_dependencies(edge_info_generate_messages_py geographic_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(edge_info_generate_messages_py std_msgs_generate_messages_py)
endif()
