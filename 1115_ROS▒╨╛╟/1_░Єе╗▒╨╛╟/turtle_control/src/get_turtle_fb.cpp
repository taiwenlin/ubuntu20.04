#include <ros/ros.h>
#include <turtlesim/Pose.h> // For geometry_msgs::Twist

void Get_PoseMsg(const turtlesim::Pose& msg)
{
    ROS_INFO_STREAM(std::setprecision(2)<<std::fixed 
                    <<"position = (" <<msg.x <<", "<<msg.y <<")"
                    <<"direction = " <<msg.theta);
}


int main ( int argc, char** argv ) 
{
	// Initialize the ROS system and become a node .
	ros::init ( argc, argv, "get_turtle_fb" ) ;
	ros::NodeHandle nh ;
	
    // Create a subscriber 
    ros::Subscriber sub = nh.subscribe("turtle1/pose", 1000, &Get_PoseMsg);

    // Let ROS spin in this node
    ros::spin();
}


// not complete yet