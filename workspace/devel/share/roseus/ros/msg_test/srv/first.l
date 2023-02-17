;; Auto-generated. Do not edit!


(when (boundp 'msg_test::first)
  (if (not (find-package "MSG_TEST"))
    (make-package "MSG_TEST"))
  (shadow 'first (find-package "MSG_TEST")))
(unless (find-package "MSG_TEST::FIRST")
  (make-package "MSG_TEST::FIRST"))
(unless (find-package "MSG_TEST::FIRSTREQUEST")
  (make-package "MSG_TEST::FIRSTREQUEST"))
(unless (find-package "MSG_TEST::FIRSTRESPONSE")
  (make-package "MSG_TEST::FIRSTRESPONSE"))

(in-package "ROS")





(defclass msg_test::firstRequest
  :super ros::object
  :slots (_val ))

(defmethod msg_test::firstRequest
  (:init
   (&key
    ((:val __val) 0)
    )
   (send-super :init)
   (setq _val (round __val))
   self)
  (:val
   (&optional __val)
   (if __val (setq _val __val)) _val)
  (:serialization-length
   ()
   (+
    ;; int32 _val
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _val
       (write-long _val s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _val
     (setq _val (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass msg_test::firstResponse
  :super ros::object
  :slots (_ans ))

(defmethod msg_test::firstResponse
  (:init
   (&key
    ((:ans __ans) 0)
    )
   (send-super :init)
   (setq _ans (round __ans))
   self)
  (:ans
   (&optional __ans)
   (if __ans (setq _ans __ans)) _ans)
  (:serialization-length
   ()
   (+
    ;; int32 _ans
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _ans
       (write-long _ans s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _ans
     (setq _ans (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass msg_test::first
  :super ros::object
  :slots ())

(setf (get msg_test::first :md5sum-) "3cbc01bc527ce12c720fe426994d5cdc")
(setf (get msg_test::first :datatype-) "msg_test/first")
(setf (get msg_test::first :request) msg_test::firstRequest)
(setf (get msg_test::first :response) msg_test::firstResponse)

(defmethod msg_test::firstRequest
  (:response () (instance msg_test::firstResponse :init)))

(setf (get msg_test::firstRequest :md5sum-) "3cbc01bc527ce12c720fe426994d5cdc")
(setf (get msg_test::firstRequest :datatype-) "msg_test/firstRequest")
(setf (get msg_test::firstRequest :definition-)
      "int32 val
---
int32 ans

")

(setf (get msg_test::firstResponse :md5sum-) "3cbc01bc527ce12c720fe426994d5cdc")
(setf (get msg_test::firstResponse :datatype-) "msg_test/firstResponse")
(setf (get msg_test::firstResponse :definition-)
      "int32 val
---
int32 ans

")



(provide :msg_test/first "3cbc01bc527ce12c720fe426994d5cdc")


