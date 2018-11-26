// Auto-generated. Do not edit!

// (in-package edge_info.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class vhc_cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.vhcid = null;
      this.cmd = null;
    }
    else {
      if (initObj.hasOwnProperty('vhcid')) {
        this.vhcid = initObj.vhcid
      }
      else {
        this.vhcid = 0;
      }
      if (initObj.hasOwnProperty('cmd')) {
        this.cmd = initObj.cmd
      }
      else {
        this.cmd = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vhc_cmd
    // Serialize message field [vhcid]
    bufferOffset = _serializer.uint32(obj.vhcid, buffer, bufferOffset);
    // Serialize message field [cmd]
    bufferOffset = _serializer.uint32(obj.cmd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vhc_cmd
    let len;
    let data = new vhc_cmd(null);
    // Deserialize message field [vhcid]
    data.vhcid = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [cmd]
    data.cmd = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'edge_info/vhc_cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '431b3cb4cfa302ca931f4d197d26c3a0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 vhcid
    uint32 cmd
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vhc_cmd(null);
    if (msg.vhcid !== undefined) {
      resolved.vhcid = msg.vhcid;
    }
    else {
      resolved.vhcid = 0
    }

    if (msg.cmd !== undefined) {
      resolved.cmd = msg.cmd;
    }
    else {
      resolved.cmd = 0
    }

    return resolved;
    }
};

module.exports = vhc_cmd;
