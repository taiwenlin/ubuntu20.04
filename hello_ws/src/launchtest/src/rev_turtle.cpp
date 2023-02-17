#include <ros/ros.h>
#include <geometry_msgs/Twist.h> // For geometry_msgs::Twist



ros::Publisher* pub_ptr;
void rev_cmd(const geometry_msgs::Twist& msg)
{
    geometry_msgs::Twist new_cmd;

	// msg to define opposite position (xyz)
    ??
	??
	??

    pub_ptr->publish(new_cmd);
}

int main ( int argc, char** argv ) 
{
	// Initialize the ROS system and become a node .
	???
	???
	
    // Create a subscriber 
    ros::Subscriber sub = nh.subscribe("/turtle1/cmd_vel", 1000, &rev_cmd);

    pub_ptr = new ros::Publisher( nh.advertise <geometry_msgs::Twist>("/turtle1/rev_cmd", 1000) );
    

    // Let ROS spin in this node
    ???
}

