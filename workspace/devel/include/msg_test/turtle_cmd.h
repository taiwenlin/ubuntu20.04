// Generated by gencpp from file msg_test/turtle_cmd.msg
// DO NOT EDIT!


#ifndef MSG_TEST_MESSAGE_TURTLE_CMD_H
#define MSG_TEST_MESSAGE_TURTLE_CMD_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace msg_test
{
template <class ContainerAllocator>
struct turtle_cmd_
{
  typedef turtle_cmd_<ContainerAllocator> Type;

  turtle_cmd_()
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
    }
  turtle_cmd_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , theta(0.0)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _theta_type;
  _theta_type theta;





  typedef boost::shared_ptr< ::msg_test::turtle_cmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::msg_test::turtle_cmd_<ContainerAllocator> const> ConstPtr;

}; // struct turtle_cmd_

typedef ::msg_test::turtle_cmd_<std::allocator<void> > turtle_cmd;

typedef boost::shared_ptr< ::msg_test::turtle_cmd > turtle_cmdPtr;
typedef boost::shared_ptr< ::msg_test::turtle_cmd const> turtle_cmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::msg_test::turtle_cmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::msg_test::turtle_cmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::msg_test::turtle_cmd_<ContainerAllocator1> & lhs, const ::msg_test::turtle_cmd_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.theta == rhs.theta;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::msg_test::turtle_cmd_<ContainerAllocator1> & lhs, const ::msg_test::turtle_cmd_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace msg_test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::msg_test::turtle_cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::msg_test::turtle_cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_test::turtle_cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_test::turtle_cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_test::turtle_cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_test::turtle_cmd_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::msg_test::turtle_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a130bc60ee6513855dc62ea83fcc5b20";
  }

  static const char* value(const ::msg_test::turtle_cmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa130bc60ee651385ULL;
  static const uint64_t static_value2 = 0x5dc62ea83fcc5b20ULL;
};

template<class ContainerAllocator>
struct DataType< ::msg_test::turtle_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msg_test/turtle_cmd";
  }

  static const char* value(const ::msg_test::turtle_cmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::msg_test::turtle_cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 theta\n"
"\n"
;
  }

  static const char* value(const ::msg_test::turtle_cmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::msg_test::turtle_cmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.theta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct turtle_cmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::msg_test::turtle_cmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::msg_test::turtle_cmd_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "theta: ";
    Printer<float>::stream(s, indent + "  ", v.theta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MSG_TEST_MESSAGE_TURTLE_CMD_H