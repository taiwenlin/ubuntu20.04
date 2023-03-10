// Generated by gencpp from file pow_service/firstRequest.msg
// DO NOT EDIT!


#ifndef POW_SERVICE_MESSAGE_FIRSTREQUEST_H
#define POW_SERVICE_MESSAGE_FIRSTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pow_service
{
template <class ContainerAllocator>
struct firstRequest_
{
  typedef firstRequest_<ContainerAllocator> Type;

  firstRequest_()
    : val(0)
    , vall(0)  {
    }
  firstRequest_(const ContainerAllocator& _alloc)
    : val(0)
    , vall(0)  {
  (void)_alloc;
    }



   typedef int32_t _val_type;
  _val_type val;

   typedef int32_t _vall_type;
  _vall_type vall;





  typedef boost::shared_ptr< ::pow_service::firstRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pow_service::firstRequest_<ContainerAllocator> const> ConstPtr;

}; // struct firstRequest_

typedef ::pow_service::firstRequest_<std::allocator<void> > firstRequest;

typedef boost::shared_ptr< ::pow_service::firstRequest > firstRequestPtr;
typedef boost::shared_ptr< ::pow_service::firstRequest const> firstRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pow_service::firstRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pow_service::firstRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pow_service::firstRequest_<ContainerAllocator1> & lhs, const ::pow_service::firstRequest_<ContainerAllocator2> & rhs)
{
  return lhs.val == rhs.val &&
    lhs.vall == rhs.vall;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pow_service::firstRequest_<ContainerAllocator1> & lhs, const ::pow_service::firstRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pow_service

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pow_service::firstRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pow_service::firstRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pow_service::firstRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pow_service::firstRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pow_service::firstRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pow_service::firstRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pow_service::firstRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ca4d9d1a54980c2b651a9cf4ec37f691";
  }

  static const char* value(const ::pow_service::firstRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xca4d9d1a54980c2bULL;
  static const uint64_t static_value2 = 0x651a9cf4ec37f691ULL;
};

template<class ContainerAllocator>
struct DataType< ::pow_service::firstRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pow_service/firstRequest";
  }

  static const char* value(const ::pow_service::firstRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pow_service::firstRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 val\n"
"int32 vall\n"
;
  }

  static const char* value(const ::pow_service::firstRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pow_service::firstRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.val);
      stream.next(m.vall);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct firstRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pow_service::firstRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pow_service::firstRequest_<ContainerAllocator>& v)
  {
    s << indent << "val: ";
    Printer<int32_t>::stream(s, indent + "  ", v.val);
    s << indent << "vall: ";
    Printer<int32_t>::stream(s, indent + "  ", v.vall);
  }
};

} // namespace message_operations
} // namespace ros

#endif // POW_SERVICE_MESSAGE_FIRSTREQUEST_H
