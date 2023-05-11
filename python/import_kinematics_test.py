import kinematics_sample
import math
link = [10, 60, 50, 20]
six_dof_link = kinematics_sample.kinematics(link)
x = 60
y = 60
z = 10
end_position = [x, y, z]
###  手臂末端點姿態
pitch = math.radians(0)
roll  = math.radians(0)
yaw   = math.radians(0)
end_orientation = [pitch, roll, yaw]

six_dof_link.demo(end_position, end_orientation)