#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose2D
import math

rospy.init_node("simple_odom")
cmd_vel_pub = rospy.Publisher("/odom_pose2d", Pose2D, queue_size=1)

def quaternion_to_theta(odom):

    t1 = +2.0 * (odom.pose.pose.orientation.w * odom.pose.pose.orientation.z + odom.pose.pose.orientation.x * odom.pose.pose.orientation.y)
    t2 = +1.0 - 2.0 * (odom.pose.pose.orientation.y ** 2 + odom.pose.pose.orientation.z**2)

    return math.atan2(t1, t2)

def cb_scan(msg, pub):
    pose = Pose2D()    
    pose.x = msg.pose.pose.position.x
    pose.y = msg.pose.pose.position.y
    pose.theta = quaternion_to_theta(msg)

    pub.publish(pose)

rospy.Subscriber("odom", Odometry, cb_scan, cmd_vel_pub)

while not rospy.is_shutdown():
    rospy.spin()
