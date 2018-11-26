// Generated by gencpp from file edge_info/vhc_geo.msg
// DO NOT EDIT!


#ifndef EDGE_INFO_MESSAGE_VHC_GEO_H
#define EDGE_INFO_MESSAGE_VHC_GEO_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geographic_msgs/GeoPoint.h>

namespace edge_info
{
template <class ContainerAllocator>
struct vhc_geo_
{
  typedef vhc_geo_<ContainerAllocator> Type;

  vhc_geo_()
    : vhcid(0)
    , geo()  {
    }
  vhc_geo_(const ContainerAllocator& _alloc)
    : vhcid(0)
    , geo(_alloc)  {
  (void)_alloc;
    }



   typedef uint32_t _vhcid_type;
  _vhcid_type vhcid;

   typedef  ::geographic_msgs::GeoPoint_<ContainerAllocator>  _geo_type;
  _geo_type geo;





  typedef boost::shared_ptr< ::edge_info::vhc_geo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::edge_info::vhc_geo_<ContainerAllocator> const> ConstPtr;

}; // struct vhc_geo_

typedef ::edge_info::vhc_geo_<std::allocator<void> > vhc_geo;

typedef boost::shared_ptr< ::edge_info::vhc_geo > vhc_geoPtr;
typedef boost::shared_ptr< ::edge_info::vhc_geo const> vhc_geoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::edge_info::vhc_geo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::edge_info::vhc_geo_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace edge_info

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geographic_msgs': ['/opt/ros/kinetic/share/geographic_msgs/cmake/../msg'], 'edge_info': ['/home/yulans/Documents/edge/cnedge/Dependable-Edge-computing/rosws/src/edge_info/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'uuid_msgs': ['/opt/ros/kinetic/share/uuid_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::edge_info::vhc_geo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::edge_info::vhc_geo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::edge_info::vhc_geo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::edge_info::vhc_geo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::edge_info::vhc_geo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::edge_info::vhc_geo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::edge_info::vhc_geo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cfafd41cb4021d78978805fcb28453a7";
  }

  static const char* value(const ::edge_info::vhc_geo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcfafd41cb4021d78ULL;
  static const uint64_t static_value2 = 0x978805fcb28453a7ULL;
};

template<class ContainerAllocator>
struct DataType< ::edge_info::vhc_geo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "edge_info/vhc_geo";
  }

  static const char* value(const ::edge_info::vhc_geo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::edge_info::vhc_geo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint32 vhcid\n\
geographic_msgs/GeoPoint geo\n\
\n\
================================================================================\n\
MSG: geographic_msgs/GeoPoint\n\
# Geographic point, using the WGS 84 reference ellipsoid.\n\
\n\
# Latitude [degrees]. Positive is north of equator; negative is south\n\
# (-90 <= latitude <= +90).\n\
float64 latitude\n\
\n\
# Longitude [degrees]. Positive is east of prime meridian; negative is\n\
# west (-180 <= longitude <= +180). At the poles, latitude is -90 or\n\
# +90, and longitude is irrelevant, but must be in range.\n\
float64 longitude\n\
\n\
# Altitude [m]. Positive is above the WGS 84 ellipsoid (NaN if unspecified).\n\
float64 altitude\n\
";
  }

  static const char* value(const ::edge_info::vhc_geo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::edge_info::vhc_geo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.vhcid);
      stream.next(m.geo);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct vhc_geo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::edge_info::vhc_geo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::edge_info::vhc_geo_<ContainerAllocator>& v)
  {
    s << indent << "vhcid: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.vhcid);
    s << indent << "geo: ";
    s << std::endl;
    Printer< ::geographic_msgs::GeoPoint_<ContainerAllocator> >::stream(s, indent + "  ", v.geo);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EDGE_INFO_MESSAGE_VHC_GEO_H
