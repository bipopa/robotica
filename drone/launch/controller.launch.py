#Librerias para Ubicar Archivos
import os
from ament_index_python import get_package_share_directory
#Librerias para Procesar Archivos
import xacro
from launch.launch_description_sources import PythonLaunchDescriptionSource
#Librerias para Lanzar Nodos
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription

pkg_file_path = os.path.join(get_package_share_directory("drone"))

gazebo_launch_file_path = os.path.join(pkg_file_path, "launch", "gazebo.launch.py")

urdf_file_path = os.path.join(pkg_file_path, "urdf", "drone.urdf")
robot_description_file = xacro.process_file(urdf_file_path)
robot_description_config = {"robot_description": robot_description_file.toxml()}

controller_file_path = os.path.join(pkg_file_path, "config", "joint_names_drone.yaml")

def generate_launch_description():
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch_file_path])
    )

    controller_manager_node = Node(
        package= "controller_manager",
        executable= "ros2_control_node",
        parameters= [robot_description_config, controller_file_path]
    )

    jsb_spawner_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments= ["joint_state_broadcaster"]
    )
    
    jpc_spawner_node = Node(
        package="controller_manager",
        executable="spawner",
        arguments= ["joint_group_position_controller"]
    )

    nodes_to_run = [gazebo_launch, controller_manager_node, jsb_spawner_node, jpc_spawner_node]
    return LaunchDescription(nodes_to_run)
