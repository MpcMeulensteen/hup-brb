import os
from launch import LaunchDescription
import launch
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


WORLD_CONSTANT = 'waffle_pi'
MODEL_CONSTANT = 'waffle_pi'

def gen_robot_list(number_of_robots):

    robots = []

    for i in range(number_of_robots):
        robot_name = "robot"+str(i)
        x_pos = float(i)
        robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': 0.0, 'z_pose': 0.01})

    return robots

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    package_description = get_package_share_directory('simulation')

    # We have to change this to our own package and model when we get it

    #World model 
    world = os.path.join(get_package_share_directory('simulation'), 'worlds', WORLD_CONSTANT + ".model")
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    #-------------------------------------------------------------Launch gazebo------------------------------------------------------------------------#

    gz_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')),
        launch_arguments={'world': world, "verbose": "true"}.items()
    )

    gz_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py'))
    )

    #-------------------------------------------------------------Launch RVIZ-----------------------------------------------------------------------------#
    # RVIZ Configuration
    """
    rviz_config_dir = os.path.join(get_package_share_directory(
        package_description), 'rviz', 'simulation.rviz')

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        name='rviz_node',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir])
    """

    #--------------------------------------------------------------Robot spawning------------------------------------------------------------------------#
    
    test = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(package_description, 'launch', 'spawn_launch.py'))
        )

    ld = LaunchDescription()
    ld.add_action(gz_server)
    ld.add_action(gz_client)   
    ld.add_action(test)
    return ld
