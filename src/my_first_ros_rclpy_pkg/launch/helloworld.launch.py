import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # param_dir = LaunchConfiguration(
    #     'param_dir',
    #     default=os.path.join(
    #         get_package_share_directory('topic_service_action_rclpy_example'),
    #         'param',
    #         'arithmetic_config.yaml'))

    return LaunchDescription([
        # DeclareLaunchArgument(
        #     'param_dir',
        #     default_value=param_dir,
        #     description='Full path of parameter file'),

        Node(
            package='my_first_ros_rclpy_pkg',
            executable='helloworld_subscriber',
            name='helloworld_subscriber',
            # parameters=[param_dir],
            output='screen'),

        Node(
            package='my_first_ros_rclpy_pkg',
            executable='helloworld_publisher',
            name='helloworld_publisher',
            # parameters=[param_dir],
            output='screen'),
    ])