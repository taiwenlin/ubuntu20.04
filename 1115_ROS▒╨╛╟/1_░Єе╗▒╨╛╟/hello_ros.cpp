
#include <ros/ros.h>

int main ( int argc, char** argv ) 
{
	// Initialize the ROS system and become a node .
	ros::init ( argc, argv, "hello" ) ;
	ros::NodeHandle nh ;
    ROS_INFO_STREAM("hello ROS");
	return 0;
}