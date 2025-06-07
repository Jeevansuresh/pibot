from setuptools import find_packages, setup

package_name = 'pibot'

setup(
    name=package_name,
    version='0.0.1',  # bumped version
    packages=find_packages(exclude=['test', 'tests']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}/launch', ['launch/pibot_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jeevan Suresh',
    maintainer_email='jeevansuresh258@gmail.com',
    description='ROS2 package for PiBot motor control and safety monitoring',
    license='Apache License 2.0',  # update this with your actual license
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_control_node = pibot.motor_control_node:main',
            'ultrasonic_sensor_node = pibot.ultrasonic_sensor_node:main',
            'status_node = pibot.status_node:main',
            'safety_node = pibot.safety_node:main',
        ],
    },
)
