from launch import LaunchDescription
from launch_ros.actions import Node
import os

cur_dir = os.path.dirname(__file__)
print("cur_dir : ", cur_dir)
git_root_dir = os.path.abspath(os.path.join(cur_dir, "..", "..", "..", ".."))
print("git_root_dir : ", git_root_dir)
src_dir = os.path.abspath(os.path.join(git_root_dir, "src", "ros2_monocular_slam"))
print("src_dir : ", src_dir)
data_dir = os.path.abspath(os.path.join(git_root_dir, "data"))
print("data_dir : ", data_dir) 
test_video_path = os.path.join(data_dir, 'car.mp4')
print("test_video_path : ", test_video_path)
rviz2_path = os.path.join(src_dir, "rviz", "py_slam_ros2_v4.rviz")
print("rviz2_path : ", rviz2_path)


def generate_launch_description():
    ld = LaunchDescription()

    video_pub = Node(
        package="ros2_monocular_slam",
        executable="vod_img_pub",  # Ensure this matches the entry point defined in your setup.py or CMakeLists.txt
        name='vod_img_pub',  # Optional, but useful for debugging
        arguments=[test_video_path],
        output='screen',
        emulate_tty=True,  # Ensures proper handling of console output
    )

    slam_pub = Node(
            package='ros2_monocular_slam',
            executable='slam_pub',
            name='slam_pub',
            output='screen',
            emulate_tty=True,  # Optional, useful for debugging
        )
    

    rviz = Node(
        package="rviz2",
        executable="rviz2",  # Ensure this matches the entry point defined in your setup.py or CMakeLists.txt
        output='screen',
        arguments=['-d' + rviz2_path]
    )


    ld.add_action(video_pub)
    ld.add_action(slam_pub)
    ld.add_action(rviz)

    return ld
