## my_first_ros_rclpy_pkg

Simple ROS2 Publisher–Subscriber application in ROS client library for Python (rclpy).

----

### 1. Executable files

**[Terminal 1]**
```
# pwd
> ~/ROS_Robotics_Playgrounds

# build
colcon build --symlink-install --packages-select my_first_ros_rclpy_pkg

# update environment
source ./install/local_setup.bash

# run
ros2 run my_first_ros_rclpy_pkg helloworld_subscriber
```

**[Terminal 2]**
```
# update environment
source ./install/local_setup.bash

# run
ros2 run my_first_ros_rclpy_pkg helloworld_publisher
```

----
### 2. Launch file

**[Terminal 1]**
```
# pwd
> ~/ROS_Robotics_Playgrounds

# build
colcon build --symlink-install --packages-select my_first_ros_rclpy_pkg

# update environment
source ./install/local_setup.bash

# run
ros2 launch my_first_ros_rclpy_pkg helloworld.launch.py
```

