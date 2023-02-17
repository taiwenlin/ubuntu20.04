; Auto-generated. Do not edit!


(cl:in-package msg_test-srv)


;//! \htmlinclude first-request.msg.html

(cl:defclass <first-request> (roslisp-msg-protocol:ros-message)
  ((val
    :reader val
    :initarg :val
    :type cl:integer
    :initform 0))
)

(cl:defclass first-request (<first-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <first-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'first-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg_test-srv:<first-request> is deprecated: use msg_test-srv:first-request instead.")))

(cl:ensure-generic-function 'val-val :lambda-list '(m))
(cl:defmethod val-val ((m <first-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg_test-srv:val-val is deprecated.  Use msg_test-srv:val instead.")
  (val m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <first-request>) ostream)
  "Serializes a message object of type '<first-request>"
  (cl:let* ((signed (cl:slot-value msg 'val)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <first-request>) istream)
  "Deserializes a message object of type '<first-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'val) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<first-request>)))
  "Returns string type for a service object of type '<first-request>"
  "msg_test/firstRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'first-request)))
  "Returns string type for a service object of type 'first-request"
  "msg_test/firstRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<first-request>)))
  "Returns md5sum for a message object of type '<first-request>"
  "3cbc01bc527ce12c720fe426994d5cdc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'first-request)))
  "Returns md5sum for a message object of type 'first-request"
  "3cbc01bc527ce12c720fe426994d5cdc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<first-request>)))
  "Returns full string definition for message of type '<first-request>"
  (cl:format cl:nil "int32 val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'first-request)))
  "Returns full string definition for message of type 'first-request"
  (cl:format cl:nil "int32 val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <first-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <first-request>))
  "Converts a ROS message object to a list"
  (cl:list 'first-request
    (cl:cons ':val (val msg))
))
;//! \htmlinclude first-response.msg.html

(cl:defclass <first-response> (roslisp-msg-protocol:ros-message)
  ((ans
    :reader ans
    :initarg :ans
    :type cl:integer
    :initform 0))
)

(cl:defclass first-response (<first-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <first-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'first-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msg_test-srv:<first-response> is deprecated: use msg_test-srv:first-response instead.")))

(cl:ensure-generic-function 'ans-val :lambda-list '(m))
(cl:defmethod ans-val ((m <first-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msg_test-srv:ans-val is deprecated.  Use msg_test-srv:ans instead.")
  (ans m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <first-response>) ostream)
  "Serializes a message object of type '<first-response>"
  (cl:let* ((signed (cl:slot-value msg 'ans)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <first-response>) istream)
  "Deserializes a message object of type '<first-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ans) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<first-response>)))
  "Returns string type for a service object of type '<first-response>"
  "msg_test/firstResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'first-response)))
  "Returns string type for a service object of type 'first-response"
  "msg_test/firstResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<first-response>)))
  "Returns md5sum for a message object of type '<first-response>"
  "3cbc01bc527ce12c720fe426994d5cdc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'first-response)))
  "Returns md5sum for a message object of type 'first-response"
  "3cbc01bc527ce12c720fe426994d5cdc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<first-response>)))
  "Returns full string definition for message of type '<first-response>"
  (cl:format cl:nil "int32 ans~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'first-response)))
  "Returns full string definition for message of type 'first-response"
  (cl:format cl:nil "int32 ans~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <first-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <first-response>))
  "Converts a ROS message object to a list"
  (cl:list 'first-response
    (cl:cons ':ans (ans msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'first)))
  'first-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'first)))
  'first-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'first)))
  "Returns string type for a service object of type '<first>"
  "msg_test/first")