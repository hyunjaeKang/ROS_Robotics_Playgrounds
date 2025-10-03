# ROS Rbotics Playground

-----

## Intall ROS-Humble


### Check Systems

```
lsb_release -a 

> No LSB modules are available.
> Distributor ID: Ubuntu
> Description:    Ubuntu 22.04.5 LTS
> Release:        22.04
> Codename:       jammy
```

### Set locale

```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

### Setup Sources
```
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```

### Install ROS 2 packages
```
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-desktop
sudo apt install ros-dev-tools
```

### Environment setup
```
conda deactivate # if conda env is activated
source /opt/ros/humble/setup.bash

```
----


----

### Reference:


- ***Papers***:
    - ....

- ***Blog***:
    - [ROS Humble Install](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)


- ***Github***:
    - ....
