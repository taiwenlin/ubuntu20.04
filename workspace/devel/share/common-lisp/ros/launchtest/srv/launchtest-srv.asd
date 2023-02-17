
(cl:in-package :asdf)

(defsystem "launchtest-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "First" :depends-on ("_package_First"))
    (:file "_package_First" :depends-on ("_package"))
  ))