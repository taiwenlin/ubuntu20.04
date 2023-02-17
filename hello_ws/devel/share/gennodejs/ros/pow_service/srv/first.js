// Auto-generated. Do not edit!

// (in-package pow_service.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class firstRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.val = null;
      this.vall = null;
    }
    else {
      if (initObj.hasOwnProperty('val')) {
        this.val = initObj.val
      }
      else {
        this.val = 0;
      }
      if (initObj.hasOwnProperty('vall')) {
        this.vall = initObj.vall
      }
      else {
        this.vall = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type firstRequest
    // Serialize message field [val]
    bufferOffset = _serializer.int32(obj.val, buffer, bufferOffset);
    // Serialize message field [vall]
    bufferOffset = _serializer.int32(obj.vall, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type firstRequest
    let len;
    let data = new firstRequest(null);
    // Deserialize message field [val]
    data.val = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [vall]
    data.vall = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pow_service/firstRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ca4d9d1a54980c2b651a9cf4ec37f691';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 val
    int32 vall
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new firstRequest(null);
    if (msg.val !== undefined) {
      resolved.val = msg.val;
    }
    else {
      resolved.val = 0
    }

    if (msg.vall !== undefined) {
      resolved.vall = msg.vall;
    }
    else {
      resolved.vall = 0
    }

    return resolved;
    }
};

class firstResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ans = null;
      this.anss = null;
    }
    else {
      if (initObj.hasOwnProperty('ans')) {
        this.ans = initObj.ans
      }
      else {
        this.ans = 0;
      }
      if (initObj.hasOwnProperty('anss')) {
        this.anss = initObj.anss
      }
      else {
        this.anss = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type firstResponse
    // Serialize message field [ans]
    bufferOffset = _serializer.int32(obj.ans, buffer, bufferOffset);
    // Serialize message field [anss]
    bufferOffset = _serializer.int32(obj.anss, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type firstResponse
    let len;
    let data = new firstResponse(null);
    // Deserialize message field [ans]
    data.ans = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [anss]
    data.anss = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pow_service/firstResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f779ceb789f558662afb61bf76076cd0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 ans
    int32 anss
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new firstResponse(null);
    if (msg.ans !== undefined) {
      resolved.ans = msg.ans;
    }
    else {
      resolved.ans = 0
    }

    if (msg.anss !== undefined) {
      resolved.anss = msg.anss;
    }
    else {
      resolved.anss = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: firstRequest,
  Response: firstResponse,
  md5sum() { return '12cec05e53e1a1cd50861b841b371c18'; },
  datatype() { return 'pow_service/first'; }
};
