# Assessment Report

[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsn7Josk2eGRXeETO37meCd03oritTv-gMBrg9GYSO7BSKO1JYyZLJYbgPaP6YZQ4J9Q&usqp=CAU)](https://www.ros.org/)

## Dependencies
The code functions on both ROS Melodic (Ubuntu 18.04) and Noetic (Ubuntu 20.04). It is thus necessary to install the ROS version that has been designed for your Linux distro.
To Install ROS on your linux distro please refer to https://www.ros.org/install/

## Installation

```sh
$ cd #path_to_your_desired_folder
$ git clone https://github.com/Abinav2695/crover_assessment.git
$ cd crover_assessment
$ catkin_make
$ source devel/setup.bash
```
## How to use

To launch the main localization node run the following command.
```sh
$ roslaunch gnss_navigation ekf_state_estimate.launch
```
This will launch a rviz window with simulation of data obatined from topic: /sensor/odom/ground_truth and /odometry/filered data. The output of estimated position and orientation is saved as 'output.bag' under 'bag_files' folder of the gnss_navigation package. 

To convert the bag file into CSV file run the following command.
```sh
$ rosrun gnss_navigation rosbag2csv.py
```

This code will convert bag file to CSV file and save it as 'output.csv' under 'csv_files' folder of the gnss_navigation package.


## Technical Description

The localization of the car/object provided in the task is done using extended kalman fiter. For this the robot_localization package developed by Charles River Analytics is used. Robot Localization is a package of nonlinear state estimation nodes,each of which is an implementation of a nonlinear state estimator for robots moving in 3D space. It contains two state estimation nodes, ekf_localization_node and ukf_localization_node.

The input to the ekf_localization_node is provided from playing the already provided bag files with sensore data.
The sensor inputs obtained from the topics /sensor/gnss/odom and /sensor/odom is fused to obtain the estimated state of the robot. To implement the extended kalman filter node and obtain filtered odometry data,a separate yaml file containing all the basic parameter of the model was created.This file is saved in the 'param' folder of the 'gnss_navigation' package

The parameters have been set as per the guidelines provided by the package.
![Screenshot from 2021-08-22 04-52-25.png](https://www.dropbox.com/s/srrj978fsgd0cwm/Screenshot%20from%202021-08-22%2004-52-25.png?dl=0&raw=1)

![Screenshot from 2021-08-22 05-11-53.png](https://www.dropbox.com/s/c7cfd7gjex0gsw6/Screenshot%20from%202021-08-22%2005-11-53.png?dl=0&raw=1)![Screenshot from 2021-08-22 05-12-00.png](https://www.dropbox.com/s/lflsx38a6q3xfqg/Screenshot%20from%202021-08-22%2005-12-00.png?dl=0&raw=1)

After the parameter were set , a separate launch file was created with the parameter file as argument to the launch file. This will run the ekf_localization_node and publish the estimate pose data under /odometry/filtered topic.

To convert the Output bag file to CSV file a separte code is implement under the gnss_navigation package. The code basically opens the bag file and stores the values of desired parameters of the output message as panda database and exports the data into a CSV file.

## Performance
The performance obtained from the current settings for the extended kalman filter gave good results. These results could be improved further with the help of tuning the process_noise_covariance matrix.

![Screenshot from 2021-08-22 05-17-04.png](https://www.dropbox.com/s/v5cvtwqc212del4/Screenshot%20from%202021-08-22%2005-17-04.png?dl=0&raw=1)

![Screenshot from 2021-08-22 05-20-21.png](https://www.dropbox.com/s/dh6wgmqtbv61pcc/Screenshot%20from%202021-08-22%2005-20-21.png?dl=0&raw=1)

## Work Description

1. The task given was a completely new learning for me. The concept of Kalman Filter is known to me but the use of the Extended Kalman Filter to estimate pose using non linear function is something I had to understand.
2. The major time period was spent in understanding the concept of odometry data for localisation and the fusion of many such sensor data to obtain estimated pose. This took around 7-8 hours of my time.
3. After understanding the above concepts , I had to make a decision to go ahead with developing the Extended Kalman Filter Algorithm. Since this would have taken an entire day to complete I had to switch to an open source ros library which does the job for me.
4. There are very few blogs/posts regarding robot localization ros package. This took me aroud 4-5 hours to understand how to configure the parameters for the efk model using this library. I had to go through all the example parameter files and dataset given by the robot localization package to get a fair understanding of the working.
5. Once I was all set with the knowledge base , I started developing the necessary codes and launch file to obtain the output. Once a fair output was obtained I went ahead with integrating rviz to the codebase to have a visiual representation of the robot localization. I havent created a map for the same since it would have taken more time.
6. Also I have added ros_plot charts which shows the filtered output along with the /sensor/odom/ground_truth output to represent the deviation obtained from the idle output.
7. I really wish to develop codes for the extended kalman filter model from scratch and then implement the same once again.I had to go through the concepts of frames and maps and tf transforms in ROS from scratch to develop the codes.It was a really great assessment with a lot of learning in a short period of time.

