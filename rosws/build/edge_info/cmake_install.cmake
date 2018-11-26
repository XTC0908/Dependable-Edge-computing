# Install script for directory: /home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/edge_info/msg" TYPE FILE FILES
    "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/map_info.msg"
    "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_geo.msg"
    "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg/vhc_cmd.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/edge_info/cmake" TYPE FILE FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/build/edge_info/catkin_generated/installspace/edge_info-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/include/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/share/roseus/ros/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/share/common-lisp/ros/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/share/gennodejs/ros/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/lib/python2.7/dist-packages/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/devel/lib/python2.7/dist-packages/edge_info")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/build/edge_info/catkin_generated/installspace/edge_info.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/edge_info/cmake" TYPE FILE FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/build/edge_info/catkin_generated/installspace/edge_info-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/edge_info/cmake" TYPE FILE FILES
    "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/build/edge_info/catkin_generated/installspace/edge_infoConfig.cmake"
    "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/build/edge_info/catkin_generated/installspace/edge_infoConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/edge_info" TYPE FILE FILES "/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/package.xml")
endif()

