import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_ros_rclcpp_pkg',
            executable='helloworld_subscriber',
            name='helloworld_subscriber',
            output='screen'),

        Node(
            package='my_first_ros_rclcpp_pkg',
            executable='helloworld_publisher',
            name='helloworld_publisher',
            output='screen'),
    ])