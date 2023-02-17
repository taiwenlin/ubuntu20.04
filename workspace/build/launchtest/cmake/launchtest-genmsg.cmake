# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "launchtest: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ilaunchtest:/home/lintaiwen/workspace/src/launchtest/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(launchtest_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_custom_target(_launchtest_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "launchtest" "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" ""
)

get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_custom_target(_launchtest_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "launchtest" "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(launchtest
  "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/launchtest
)

### Generating Services
_generate_srv_cpp(launchtest
  "/home/lintaiwen/workspace/src/launchtest/srv/First.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/launchtest
)

### Generating Module File
_generate_module_cpp(launchtest
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/launchtest
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(launchtest_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(launchtest_generate_messages launchtest_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_dependencies(launchtest_generate_messages_cpp _launchtest_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_dependencies(launchtest_generate_messages_cpp _launchtest_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(launchtest_gencpp)
add_dependencies(launchtest_gencpp launchtest_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS launchtest_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(launchtest
  "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/launchtest
)

### Generating Services
_generate_srv_eus(launchtest
  "/home/lintaiwen/workspace/src/launchtest/srv/First.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/launchtest
)

### Generating Module File
_generate_module_eus(launchtest
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/launchtest
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(launchtest_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(launchtest_generate_messages launchtest_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_dependencies(launchtest_generate_messages_eus _launchtest_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_dependencies(launchtest_generate_messages_eus _launchtest_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(launchtest_geneus)
add_dependencies(launchtest_geneus launchtest_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS launchtest_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(launchtest
  "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/launchtest
)

### Generating Services
_generate_srv_lisp(launchtest
  "/home/lintaiwen/workspace/src/launchtest/srv/First.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/launchtest
)

### Generating Module File
_generate_module_lisp(launchtest
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/launchtest
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(launchtest_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(launchtest_generate_messages launchtest_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_dependencies(launchtest_generate_messages_lisp _launchtest_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_dependencies(launchtest_generate_messages_lisp _launchtest_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(launchtest_genlisp)
add_dependencies(launchtest_genlisp launchtest_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS launchtest_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(launchtest
  "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/launchtest
)

### Generating Services
_generate_srv_nodejs(launchtest
  "/home/lintaiwen/workspace/src/launchtest/srv/First.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/launchtest
)

### Generating Module File
_generate_module_nodejs(launchtest
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/launchtest
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(launchtest_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(launchtest_generate_messages launchtest_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_dependencies(launchtest_generate_messages_nodejs _launchtest_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_dependencies(launchtest_generate_messages_nodejs _launchtest_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(launchtest_gennodejs)
add_dependencies(launchtest_gennodejs launchtest_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS launchtest_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(launchtest
  "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest
)

### Generating Services
_generate_srv_py(launchtest
  "/home/lintaiwen/workspace/src/launchtest/srv/First.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest
)

### Generating Module File
_generate_module_py(launchtest
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(launchtest_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(launchtest_generate_messages launchtest_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/msg/turtle_cmd.msg" NAME_WE)
add_dependencies(launchtest_generate_messages_py _launchtest_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/lintaiwen/workspace/src/launchtest/srv/First.srv" NAME_WE)
add_dependencies(launchtest_generate_messages_py _launchtest_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(launchtest_genpy)
add_dependencies(launchtest_genpy launchtest_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS launchtest_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/launchtest)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/launchtest
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(launchtest_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/launchtest)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/launchtest
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(launchtest_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/launchtest)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/launchtest
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(launchtest_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/launchtest)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/launchtest
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(launchtest_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/launchtest
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(launchtest_generate_messages_py std_msgs_generate_messages_py)
endif()
