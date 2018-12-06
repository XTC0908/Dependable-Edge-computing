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

class vhc_geo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.vhcid = null;
      this.geo = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('vhcid')) {
        this.vhcid = initObj.vhcid
      }
      else {
        this.vhcid = 0;
      }
      if (initObj.hasOwnProperty('geo')) {
        this.geo = initObj.geo
      }
      else {
        this.geo = new geographic_msgs.msg.GeoPoint();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vhc_geo
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [vhcid]
    bufferOffset = _serializer.uint32(obj.vhcid, buffer, bufferOffset);
    // Serialize message field [geo]
    bufferOffset = geographic_msgs.msg.GeoPoint.serialize(obj.geo, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vhc_geo
    let len;
    let data = new vhc_geo(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [vhcid]
    data.vhcid = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [geo]
    data.geo = geographic_msgs.msg.GeoPoint.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'edge_info/vhc_geo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '46215f2797945e983668770007bc875d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    uint32 vhcid
    geographic_msgs/GeoPoint geo
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vhc_geo(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.vhcid !== undefined) {
      resolved.vhcid = msg.vhcid;
    }
    else {
      resolved.vhcid = 0
    }

    if (msg.geo !== undefined) {
      resolved.geo = geographic_msgs.msg.GeoPoint.Resolve(msg.geo)
    }
    else {
      resolved.geo = new geographic_msgs.msg.GeoPoint()
    }

    return resolved;
    }
};

module.exports = vhc_geo;
