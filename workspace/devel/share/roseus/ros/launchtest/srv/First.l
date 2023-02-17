;; Auto-generated. Do not edit!


(when (boundp 'launchtest::First)
  (if (not (find-package "LAUNCHTEST"))
    (make-package "LAUNCHTEST"))
  (shadow 'First (find-package "LAUNCHTEST")))
(unless (find-package "LAUNCHTEST::FIRST")
  (make-package "LAUNCHTEST::FIRST"))
(unless (find-package "LAUNCHTEST::FIRSTREQUEST")
  (make-package "LAUNCHTEST::FIRSTREQUEST"))
(unless (find-package "LAUNCHTEST::FIRSTRESPONSE")
  (make-package "LAUNCHTEST::FIRSTRESPONSE"))

(in-package "ROS")





(defclass launchtest::FirstRequest
  :super ros::object
  :slots (_val ))

(defmethod launchtest::FirstRequest
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

(defclass launchtest::FirstResponse
  :super ros::object
  :slots (_ans ))

(defmethod launchtest::FirstResponse
  (:init
   (&key
    ((:ans __ans) 0.0)
    )
   (send-super :init)
   (setq _ans (float __ans))
   self)
  (:ans
   (&optional __ans)
   (if __ans (setq _ans __ans)) _ans)
  (:serialization-length
   ()
   (+
    ;; float32 _ans
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _ans
       (sys::poke _ans (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _ans
     (setq _ans (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass launchtest::First
  :super ros::object
  :slots ())

(setf (get launchtest::First :md5sum-) "248a70f7fd02964b38f41b93425df109")
(setf (get launchtest::First :datatype-) "launchtest/First")
(setf (get launchtest::First :request) launchtest::FirstRequest)
(setf (get launchtest::First :response) launchtest::FirstResponse)

(defmethod launchtest::FirstRequest
  (:response () (instance launchtest::FirstResponse :init)))

(setf (get launchtest::FirstRequest :md5sum-) "248a70f7fd02964b38f41b93425df109")
(setf (get launchtest::FirstRequest :datatype-) "launchtest/FirstRequest")
(setf (get launchtest::FirstRequest :definition-)
      "int32 val
---
float32 ans

")

(setf (get launchtest::FirstResponse :md5sum-) "248a70f7fd02964b38f41b93425df109")
(setf (get launchtest::FirstResponse :datatype-) "launchtest/FirstResponse")
(setf (get launchtest::FirstResponse :definition-)
      "int32 val
---
float32 ans

")



(provide :launchtest/First "248a70f7fd02964b38f41b93425df109")


