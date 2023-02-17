// Auto-generated. Do not edit!

// (in-package msg_test.srv)


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
    }
    else {
      if (initObj.hasOwnProperty('val')) {
        this.val = initObj.val
      }
      else {
        this.val = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type firstRequest
    // Serialize message field [val]
    bufferOffset = _serializer.int32(obj.val, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type firstRequest
    let len;
    let data = new firstRequest(null);
    // Deserialize message field [val]
    data.val = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'msg_test/firstRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '50ce5d329885e7178604b54270ec733c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 val
    
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

    return resolved;
    }
};

class firstResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ans = null;
    }
    else {
      if (initObj.hasOwnProperty('ans')) {
        this.ans = initObj.ans
      }
      else {
        this.ans = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type firstResponse
    // Serialize message field [ans]
    bufferOffset = _serializer.int32(obj.ans, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type firstResponse
    let len;
    let data = new firstResponse(null);
    // Deserialize message field [ans]
    data.ans = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'msg_test/firstResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fd5d0466a761324f0f90b3b2afef3d69';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 ans
    
    
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

    return resolved;
    }
};

module.exports = {
  Request: firstRequest,
  Response: firstResponse,
  md5sum() { return '3cbc01bc527ce12c720fe426994d5cdc'; },
  datatype() { return 'msg_test/first'; }
};
