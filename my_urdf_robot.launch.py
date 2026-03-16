import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('my_robot_pkg'),
        'urdf_practice',
        'my_robot.urdf'
    )

    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([
        # Step 1 - publish robot description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen',
        ),

        # Step 2 - launch Gazebo Harmonic
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(
                    get_package_share_directory('ros_gz_sim'),
                    'launch',
                    'gz_sim.launch.py'
                )
            ]),
            launch_arguments={'gz_args': '-r empty.sdf'}.items(),
        ),

        # Step 3 - spawn robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description', '-name', 'my_robot', '-z', '0.1'],
            output='screen'
        ),

        # step 4 the bridge
        Node(
    package='ros_gz_bridge',
    executable='parameter_bridge',
    arguments=[
        '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
    ],
    output='screen'
),
    ])