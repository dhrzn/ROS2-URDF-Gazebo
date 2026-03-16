# URDF & Gazebo Fundamentals

- A differential drive robot built from scratch using URDF and simulated in Gazebo Harmonic with ROS2 Jazzy.
- This project was built as part of my robotics software engineering curriculum to develop foundational skills in robot modeling, physics simulation, and ROS2 integration.

## What This Project Demonstrates

- URDF robot modeling from scratch (links, joints, visual, collision, inertial properties)
- Gazebo Harmonic simulation with a custom launch file
- Differential drive plugin for wheel actuation
- ros_gz_bridge connecting Gazebo internal topics to ROS2
- Velocity control via /cmd_vel topic

## Tech Stack

- ROS2 Jazzy
- Gazebo Harmonic
- Ubuntu 24.04
- Python (launch files)

## Robot Specs

- Chassis: 0.3 x 0.2 x 0.1m box
- Wheel radius: 0.05m
- Wheel separation: 0.3m
- Sensor link: fixed to front of chassis

## How to Run

Clone the repo and build:
```bash
cd ~/ros2_ws/src
git clone git@github.com:dhrzn/ROS2-URDF-Gazebo.git
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Launch the simulation:
```bash
ros2 launch my_robot_pkg my_urdf_robot.launch.py
```

Drive the robot forward:
```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

Stop the robot:
```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

## DEMO

<img width="437" height="295" alt="Screenshot from 2026-03-16 13-38-41" src="https://github.com/user-attachments/assets/0ee533d4-f2b0-4d5e-968e-55c4f2efeac9" />



## About

Built by Danny Hernandez — Mechanical Engineering student at CSULB 
working toward robotics software engineering. 

- Note: This project is part of a self-structured robotics curriculum leading toward motion planning 
with MoveIt2 and dual UR5 arm simulation.
