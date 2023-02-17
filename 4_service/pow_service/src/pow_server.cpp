#include "ros/ros.h"
#include <pow_service/first.h>

int muti(int a)
{
    return a * a;
}
bool service_request(pow_service::first::Request &req,pow_service::first::Response &res)
{
    ROS_INFO("Request Num = %d",req.val);
    res.ans = muti( req.val );
    ROS_INFO("Response: ans is %d ", (res.ans));
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
