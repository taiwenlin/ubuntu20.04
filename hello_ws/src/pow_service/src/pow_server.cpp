#include "ros/ros.h"
#include <pow_service/first.h>

int muti(int a,int b)
{
    return a * b;
}
int add(int a,int b)
{
    return a + b;
}
bool service_request(pow_service::first::Request &req,pow_service::first::Response &res)
{
    ROS_INFO("Request Num1 = %d",req.val);
    ROS_INFO("Request Num2 = %d",req.vall);
    res.ans = muti( req.val ,req.vall);
    res.anss = add( req.val ,req.vall);
    ROS_INFO("Response: muti is %d ", (res.ans));
    ROS_INFO("Response: add is %d ", (res.anss));
    return true;
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "srv_server");
    ros::NodeHandle nh;
    ros::ServiceServer srv = nh.advertiseService("pow_service",service_request);
    ros::spin();

    return 0;

}
