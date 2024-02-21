import rospy

if __name__ == '__main__': 
    rospy.init_node('my_first_node')
    rospy.loginfo("The node has started ...")
    rospy.sleep(1)
    rospy.loginfo("Exit now")