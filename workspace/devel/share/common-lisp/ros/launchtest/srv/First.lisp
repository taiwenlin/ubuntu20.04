; Auto-generated. Do not edit!


(cl:in-package launchtest-srv)


;//! \htmlinclude First-request.msg.html

(cl:defclass <First-request> (roslisp-msg-protocol:ros-message)
  ((val
    :reader val
    :initarg :val
    :type cl:integer
    :initform 0))
)

(cl:defclass First-request (<First-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <First-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'First-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name launchtest-srv:<First-request> is deprecated: use launchtest-srv:First-request instead.")))

(cl:ensure-generic-function 'val-val :lambda-list '(m))
(cl:defmethod val-val ((m <First-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader launchtest-srv:val-val is deprecated.  Use launchtest-srv:val instead.")
  (val m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <First-request>) ostream)
  "Serializes a message object of type '<First-request>"
  (cl:let* ((signed (cl:slot-value msg 'val)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <First-request>) istream)
  "Deserializes a message object of type '<First-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'val) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<First-request>)))
  "Returns string type for a service object of type '<First-request>"
  "launchtest/FirstRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'First-request)))
  "Returns string type for a service object of type 'First-request"
  "launchtest/FirstRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<First-request>)))
  "Returns md5sum for a message object of type '<First-request>"
  "248a70f7fd02964b38f41b93425df109")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'First-request)))
  "Returns md5sum for a message object of type 'First-request"
  "248a70f7fd02964b38f41b93425df109")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<First-request>)))
  "Returns full string definition for message of type '<First-request>"
  (cl:format cl:nil "int32 val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'First-request)))
  "Returns full string definition for message of type 'First-request"
  (cl:format cl:nil "int32 val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <First-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <First-request>))
  "Converts a ROS message object to a list"
  (cl:list 'First-request
    (cl:cons ':val (val msg))
))
;//! \htmlinclude First-response.msg.html

(cl:defclass <First-response> (roslisp-msg-protocol:ros-message)
  ((ans
    :reader ans
    :initarg :ans
    :type cl:float
    :initform 0.0))
)

(cl:defclass First-response (<First-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <First-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'First-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name launchtest-srv:<First-response> is deprecated: use launchtest-srv:First-response instead.")))

(cl:ensure-generic-function 'ans-val :lambda-list '(m))
(cl:defmethod ans-val ((m <First-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader launchtest-srv:ans-val is deprecated.  Use launchtest-srv:ans instead.")
  (ans m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <First-response>) ostream)
  "Serializes a message object of type '<First-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ans))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <First-response>) istream)
  "Deserializes a message object of type '<First-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ans) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<First-response>)))
  "Returns string type for a service object of type '<First-response>"
  "launchtest/FirstResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'First-response)))
  "Returns string type for a service object of type 'First-response"
  "launchtest/FirstResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<First-response>)))
  "Returns md5sum for a message object of type '<First-response>"
  "248a70f7fd02964b38f41b93425df109")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'First-response)))
  "Returns md5sum for a message object of type 'First-response"
  "248a70f7fd02964b38f41b93425df109")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<First-response>)))
  "Returns full string definition for message of type '<First-response>"
  (cl:format cl:nil "float32 ans~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'First-response)))
  "Returns full string definition for message of type 'First-response"
  (cl:format cl:nil "float32 ans~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <First-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <First-response>))
  "Converts a ROS message object to a list"
  (cl:list 'First-response
    (cl:cons ':ans (ans msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'First)))
  'First-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'First)))
  'First-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'First)))
  "Returns string type for a service object of type '<First>"
  "launchtest/First")