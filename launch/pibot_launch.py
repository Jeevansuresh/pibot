from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pibot',
            executable='motor_control_node',
            name='motor_control'
        ),
        Node(
            package='pibot',
            executable='ultrasonic_sensor_node',
            name='ultrasonic_sensor'
        ),
        Node(
            package='pibot',
            executable='status_node',
            name='status_node'
        ),
        Node(
            package='pibot',
            executable='safety_node',
            name='safety_node'
        ),
    ])
