## topic_service_action_rclpy_example

----
### Diagram

<img src = "./data/topic_service_action.svg">

----
### 1. Executable files

**[Terminal 1]**
```
# pwd
> ~/ROS_Robotics_Playgrounds

# build
colcon build --symlink-install --packages-select msg_srv_action_interface_example topic_service_action_rclcpp_example

# update environment
source ./install/local_setup.bash

# run 
ros2 run topic_service_action_rclcpp_example argument
```

**[Terminal 2]**
```
# update environment
source ./install/local_setup.bash 

# run 
ros2 run topic_service_action_rclcpp_example operator
```

**[Terminal 3]**
```
# update environment
source ./install/local_setup.bash 

# run 
ros2 run topic_service_action_rclcpp_example calculator
```

**[Terminal 4]**
```
# update environment
source ./install/local_setup.bash 

# run 
ros2 run topic_service_action_rclcpp_example checker
```

---- 

### 2. Launch file

**[Terminal 1]**
```
# pwd
> ~/ROS_Robotics_Playgrounds

# build
colcon build --symlink-install --packages-select msg_srv_action_interface_example topic_service_action_rclcpp_example

# update environment
source ./install/local_setup.bash 

# run 
ros2 launch topic_service_action_rclcpp_example arithmetic.launch.py
```

