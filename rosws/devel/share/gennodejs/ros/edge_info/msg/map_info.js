// Auto-generated. Do not edit!

// (in-package edge_info.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geographic_msgs = _finder('geographic_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class map_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.WayPoints = null;
      this.RouteSegments = null;
      this.RoutePaths = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('WayPoints')) {
        this.WayPoints = initObj.WayPoints
      }
      else {
        this.WayPoints = [];
      }
      if (initObj.hasOwnProperty('RouteSegments')) {
        this.RouteSegments = initObj.RouteSegments
      }
      else {
        this.RouteSegments = [];
      }
      if (initObj.hasOwnProperty('RoutePaths')) {
        this.RoutePaths = initObj.RoutePaths
      }
      else {
        this.RoutePaths = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type map_info
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [WayPoints]
    // Serialize the length for message field [WayPoints]
    bufferOffset = _serializer.uint32(obj.WayPoints.length, buffer, bufferOffset);
    obj.WayPoints.forEach((val) => {
      bufferOffset = geographic_msgs.msg.WayPoint.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [RouteSegments]
    // Serialize the length for message field [RouteSegments]
    bufferOffset = _serializer.uint32(obj.RouteSegments.length, buffer, bufferOffset);
    obj.RouteSegments.forEach((val) => {
      bufferOffset = geographic_msgs.msg.RouteSegment.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [RoutePaths]
    // Serialize the length for message field [RoutePaths]
    bufferOffset = _serializer.uint32(obj.RoutePaths.length, buffer, bufferOffset);
    obj.RoutePaths.forEach((val) => {
      bufferOffset = geographic_msgs.msg.RoutePath.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type map_info
    let len;
    let data = new map_info(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [WayPoints]
    // Deserialize array length for message field [WayPoints]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.WayPoints = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.WayPoints[i] = geographic_msgs.msg.WayPoint.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [RouteSegments]
    // Deserialize array length for message field [RouteSegments]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.RouteSegments = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.RouteSegments[i] = geographic_msgs.msg.RouteSegment.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [RoutePaths]
    // Deserialize array length for message field [RoutePaths]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.RoutePaths = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.RoutePaths[i] = geographic_msgs.msg.RoutePath.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.WayPoints.forEach((val) => {
      length += geographic_msgs.msg.WayPoint.getMessageSize(val);
    });
    object.RouteSegments.forEach((val) => {
      length += geographic_msgs.msg.RouteSegment.getMessageSize(val);
    });
    object.RoutePaths.forEach((val) => {
      length += geographic_msgs.msg.RoutePath.getMessageSize(val);
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'edge_info/map_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '07072df7d6cc23281dae048c2f9a3fa0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    # there will be another RouteSegment with "start" and "end" reversed.
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new map_info(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.WayPoints !== undefined) {
      resolved.WayPoints = new Array(msg.WayPoints.length);
      for (let i = 0; i < resolved.WayPoints.length; ++i) {
        resolved.WayPoints[i] = geographic_msgs.msg.WayPoint.Resolve(msg.WayPoints[i]);
      }
    }
    else {
      resolved.WayPoints = []
    }

    if (msg.RouteSegments !== undefined) {
      resolved.RouteSegments = new Array(msg.RouteSegments.length);
      for (let i = 0; i < resolved.RouteSegments.length; ++i) {
        resolved.RouteSegments[i] = geographic_msgs.msg.RouteSegment.Resolve(msg.RouteSegments[i]);
      }
    }
    else {
      resolved.RouteSegments = []
    }

    if (msg.RoutePaths !== undefined) {
      resolved.RoutePaths = new Array(msg.RoutePaths.length);
      for (let i = 0; i < resolved.RoutePaths.length; ++i) {
        resolved.RoutePaths[i] = geographic_msgs.msg.RoutePath.Resolve(msg.RoutePaths[i]);
      }
    }
    else {
      resolved.RoutePaths = []
    }

    return resolved;
    }
};

module.exports = map_info;
