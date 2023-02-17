// Generated by gencpp from file msg_test/firstResponse.msg
// DO NOT EDIT!


#ifndef MSG_TEST_MESSAGE_FIRSTRESPONSE_H
#define MSG_TEST_MESSAGE_FIRSTRESPONSE_H


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
struct firstResponse_
{
  typedef firstResponse_<ContainerAllocator> Type;

  firstResponse_()
    : ans(0)  {
    }
  firstResponse_(const ContainerAllocator& _alloc)
    : ans(0)  {
  (void)_alloc;
    }



   typedef int32_t _ans_type;
  _ans_type ans;





  typedef boost::shared_ptr< ::msg_test::firstResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::msg_test::firstResponse_<ContainerAllocator> const> ConstPtr;

}; // struct firstResponse_

typedef ::msg_test::firstResponse_<std::allocator<void> > firstResponse;

typedef boost::shared_ptr< ::msg_test::firstResponse > firstResponsePtr;
typedef boost::shared_ptr< ::msg_test::firstResponse const> firstResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::msg_test::firstResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::msg_test::firstResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::msg_test::firstResponse_<ContainerAllocator1> & lhs, const ::msg_test::firstResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ans == rhs.ans;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::msg_test::firstResponse_<ContainerAllocator1> & lhs, const ::msg_test::firstResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace msg_test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::msg_test::firstResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::msg_test::firstResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_test::firstResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_test::firstResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_test::firstResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_test::firstResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::msg_test::firstResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fd5d0466a761324f0f90b3b2afef3d69";
  }

  static const char* value(const ::msg_test::firstResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfd5d0466a761324fULL;
  static const uint64_t static_value2 = 0x0f90b3b2afef3d69ULL;
};

template<class ContainerAllocator>
struct DataType< ::msg_test::firstResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msg_test/firstResponse";
  }

  static const char* value(const ::msg_test::firstResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::msg_test::firstResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 ans\n"
"\n"
;
  }

  static const char* value(const ::msg_test::firstResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::msg_test::firstResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ans);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct firstResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::msg_test::firstResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::msg_test::firstResponse_<ContainerAllocator>& v)
  {
    s << indent << "ans: ";
    Printer<int32_t>::stream(s, indent + "  ", v.ans);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MSG_TEST_MESSAGE_FIRSTRESPONSE_H
