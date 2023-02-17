;; Auto-generated. Do not edit!


(when (boundp 'pow_service::first)
  (if (not (find-package "POW_SERVICE"))
    (make-package "POW_SERVICE"))
  (shadow 'first (find-package "POW_SERVICE")))
(unless (find-package "POW_SERVICE::FIRST")
  (make-package "POW_SERVICE::FIRST"))
(unless (find-package "POW_SERVICE::FIRSTREQUEST")
  (make-package "POW_SERVICE::FIRSTREQUEST"))
(unless (find-package "POW_SERVICE::FIRSTRESPONSE")
  (make-package "POW_SERVICE::FIRSTRESPONSE"))

(in-package "ROS")





(defclass pow_service::firstRequest
  :super ros::object
  :slots (_val _vall ))

(defmethod pow_service::firstRequest
  (:init
   (&key
    ((:val __val) 0)
    ((:vall __vall) 0)
    )
   (send-super :init)
   (setq _val (round __val))
   (setq _vall (round __vall))
   self)
  (:val
   (&optional __val)
   (if __val (setq _val __val)) _val)
  (:vall
   (&optional __vall)
   (if __vall (setq _vall __vall)) _vall)
  (:serialization-length
   ()
   (+
    ;; int32 _val
    4
    ;; int32 _vall
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _val
       (write-long _val s)
     ;; int32 _vall
       (write-long _vall s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _val
     (setq _val (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _vall
     (setq _vall (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass pow_service::firstResponse
  :super ros::object
  :slots (_ans _anss ))

(defmethod pow_service::firstResponse
  (:init
   (&key
    ((:ans __ans) 0)
    ((:anss __anss) 0)
    )
   (send-super :init)
   (setq _ans (round __ans))
   (setq _anss (round __anss))
   self)
  (:ans
   (&optional __ans)
   (if __ans (setq _ans __ans)) _ans)
  (:anss
   (&optional __anss)
   (if __anss (setq _anss __anss)) _anss)
  (:serialization-length
   ()
   (+
    ;; int32 _ans
    4
    ;; int32 _anss
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _ans
       (write-long _ans s)
     ;; int32 _anss
       (write-long _anss s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _ans
     (setq _ans (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _anss
     (setq _anss (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass pow_service::first
  :super ros::object
  :slots ())

(setf (get pow_service::first :md5sum-) "12cec05e53e1a1cd50861b841b371c18")
(setf (get pow_service::first :datatype-) "pow_service/first")
(setf (get pow_service::first :request) pow_service::firstRequest)
(setf (get pow_service::first :response) pow_service::firstResponse)

(defmethod pow_service::firstRequest
  (:response () (instance pow_service::firstResponse :init)))

(setf (get pow_service::firstRequest :md5sum-) "12cec05e53e1a1cd50861b841b371c18")
(setf (get pow_service::firstRequest :datatype-) "pow_service/firstRequest")
(setf (get pow_service::firstRequest :definition-)
      "int32 val
int32 vall
---
int32 ans
int32 anss

")

(setf (get pow_service::firstResponse :md5sum-) "12cec05e53e1a1cd50861b841b371c18")
(setf (get pow_service::firstResponse :datatype-) "pow_service/firstResponse")
(setf (get pow_service::firstResponse :definition-)
      "int32 val
int32 vall
---
int32 ans
int32 anss

")



(provide :pow_service/first "12cec05e53e1a1cd50861b841b371c18")


