#!/usr/bin/env python  
import roslib
roslib.load_manifest('turtlebro')
import rospy

import tf
from nav_msgs.msg import Odometry

def handle_pose(msg, br):
    pose = msg.pose.pose.position
    ori = msg.pose.pose.orientation
    # rospy.Time.now()
    br.sendTransform((pose.x, pose.y, pose.z),
                     (ori.x, ori.y, ori.z, ori.w),
                     msg.header.stamp,
                     "base_link",
                     "odom")

if __name__ == '__main__':
    rospy.init_node('odom_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rospy.Subscriber('odom',
                     Odometry,
                     handle_pose, br)

    rospy.loginfo("Start odom tf broadcaster")
    rospy.spin()