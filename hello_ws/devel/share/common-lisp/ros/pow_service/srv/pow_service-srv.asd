
(cl:in-package :asdf)

(defsystem "pow_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "first" :depends-on ("_package_first"))
    (:file "_package_first" :depends-on ("_package"))
  ))