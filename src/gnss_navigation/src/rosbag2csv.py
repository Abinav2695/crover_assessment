#!/usr/bin/python3
import rospy
import rosbag
import rospkg
import pandas as pd


rp = rospkg.RosPack()

#Get the rospackage path
package_path = rp.get_path('gnss_navigation')
bagfile_path_suffix = '/bag_files/output.bag'
csvfile_path_suffix = '/csv_files/output.csv'

bagFilePath = package_path + bagfile_path_suffix
csvFilePath = package_path + csvfile_path_suffix

def main():

    #open ros bag file
    bag = rosbag.Bag(bagFilePath)


    topic = '/odometry/filtered'
    column_names = ['seq', 'x','y','orient_x','orient_y','orient_z','orient_w','linear_x','linear_y','angular_z']
    df = pd.DataFrame(columns=column_names)

    for topic, msg, t in bag.read_messages(topics=topic):
    

        seq = msg.header.seq
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        orient_x = msg.pose.pose.orientation.x
        orient_y = msg.pose.pose.orientation.y
        orient_z = msg.pose.pose.orientation.z
        orient_w = msg.pose.pose.orientation.w
        linearx = msg.twist.twist.linear.x
        lineary = msg.twist.twist.linear.y
        angularz = msg.twist.twist.angular.z

        df = df.append({'seq': seq,
            'x': x,
            'y':y,
            'orient_x':orient_x,
            'orient_x':orient_x,
            'orient_x':orient_x,
            'orient_x':orient_x,
            'linear_x':linearx,
            'linear_y':lineary,
            'angular_z':angularz},ignore_index=True)

    df.to_csv(csvFilePath)
    bag.close()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

