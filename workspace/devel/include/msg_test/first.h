// Generated by gencpp from file msg_test/first.msg
// DO NOT EDIT!


#ifndef MSG_TEST_MESSAGE_FIRST_H
#define MSG_TEST_MESSAGE_FIRST_H

#include <ros/service_traits.h>


#include <msg_test/firstRequest.h>
#include <msg_test/firstResponse.h>


namespace msg_test
{

struct first
{

typedef firstRequest Request;
typedef firstResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct first
} // namespace msg_test


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::msg_test::first > {
  static const char* value()
  {
    return "3cbc01bc527ce12c720fe426994d5cdc";
  }

  static const char* value(const ::msg_test::first&) { return value(); }
};

template<>
struct DataType< ::msg_test::first > {
  static const char* value()
  {
    return "msg_test/first";
  }

  static const char* value(const ::msg_test::first&) { return value(); }
};


// service_traits::MD5Sum< ::msg_test::firstRequest> should match
// service_traits::MD5Sum< ::msg_test::first >
template<>
struct MD5Sum< ::msg_test::firstRequest>
{
  static const char* value()
  {
    return MD5Sum< ::msg_test::first >::value();
  }
  static const char* value(const ::msg_test::firstRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::msg_test::firstRequest> should match
// service_traits::DataType< ::msg_test::first >
template<>
struct DataType< ::msg_test::firstRequest>
{
  static const char* value()
  {
    return DataType< ::msg_test::first >::value();
  }
  static const char* value(const ::msg_test::firstRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::msg_test::firstResponse> should match
// service_traits::MD5Sum< ::msg_test::first >
template<>
struct MD5Sum< ::msg_test::firstResponse>
{
  static const char* value()
  {
    return MD5Sum< ::msg_test::first >::value();
  }
  static const char* value(const ::msg_test::firstResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::msg_test::firstResponse> should match
// service_traits::DataType< ::msg_test::first >
template<>
struct DataType< ::msg_test::firstResponse>
{
  static const char* value()
  {
    return DataType< ::msg_test::first >::value();
  }
  static const char* value(const ::msg_test::firstResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MSG_TEST_MESSAGE_FIRST_H
