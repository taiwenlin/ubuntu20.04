#include "ros/ros.h"
#include <msg_test/first.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv,"srv_client");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<msg_test::first>("msg_test");
    msg_test::first srv;
    srv.request.val = atoll(argv[1]);
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