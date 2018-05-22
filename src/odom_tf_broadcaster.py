#!/usr/bin/env python  
import roslib
roslib.load_manifest('turtlebro')
import rospy

import tf
from nav_msgs.msg import Odometry

def handle_pose(msg):
    br = tf.TransformBroadcaster()
    pose = msg.pose.pose.position
    ori = msg.pose.pose.orientation
    br.sendTransform((pose.x, pose.y, pose.z),
                     (ori.x, ori.y, ori.z, ori.w),
                     rospy.Time.now(),
                     "base_link",
                     "odom")

if __name__ == '__main__':
    rospy.init_node('odom_tf_broadcaster')
    rospy.Subscriber('odom',
                     Odometry,
                     handle_pose)
    rospy.loginfo("Start odom tf broadcaster")
    rospy.spin()