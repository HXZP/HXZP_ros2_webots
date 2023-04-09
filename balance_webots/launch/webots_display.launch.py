import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher, Ros2SupervisorLauncher
from webots_ros2_driver.utils import controller_url_prefix




def generate_launch_description():
    
    package_name = 'balance_webots'
    world_name = 'balance.wbt'
    robot_name = 'Balance'
    
    robot_description = pathlib.Path(os.path.join(package_name, 'resource', 'balance_webots_plugin.urdf')).read_text()
    
    webots_robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + robot_name},
        parameters=[
            {'robot_description': robot_description},
        ],
        
        # The following line is important!
        # Every time one resets the simulation the controller is automatically respawned
        respawn=True
    )

    webots = WebotsLauncher(
        world=os.path.join(package_name, 'worlds', world_name)    
    )
    
    # Starts the Ros2Supervisor node, with by default respawn=True
    #ros2_supervisor = Ros2SupervisorLauncher() # Only with the develop branch!    
    
    return LaunchDescription([
        webots,
        webots_robot_driver,
        
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
    
    
    
    
    
    
    
    
    
    
    
    
    
