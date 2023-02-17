#include "ros/ros.h"
#include <pow_service/first.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv,"srv_client");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<pow_service::first>("pow_service");
    pow_service::first srv;
    srv.request.val = atoll(argv[1]);
    srv.request.vall = atoll(argv[2]);
    if(client.call(srv))
    {
        ROS_INFO("Finish send data");
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }
    return 0;
}
