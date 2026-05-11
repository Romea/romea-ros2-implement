# Copyright 2022 INRAE, French National Research Institute for Agriculture, Food and Environment
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from romea_joystick_utils import apply_joystick_remapping
import yaml


def get_configuration(what, context):
    argument_name = f"{what}_configuration_file_path"
    configuration_file_path = LaunchConfiguration(argument_name).perform(context)
    with open(configuration_file_path) as f:
        return yaml.safe_load(f)


def launch_setup(context, *args, **kwargs):

    joystick_configuration = get_configuration("joystick", context)
    # teleop_configuration = get_configuration("teleop", context)
    joystick_topic = LaunchConfiguration("joystick_topic").perform(context)

    teleop_configuration_file_path = (
        get_package_share_directory("romea_implement_teleop")
        + f"/config/{joystick_configuration["type"]}_remappings.yaml"
    )

    with open(teleop_configuration_file_path) as f:
        teleop_configuration = yaml.safe_load(f)

    teleop_configuration = apply_joystick_remapping(
        joystick_configuration, teleop_configuration
    )

    teleop = Node(
        package="romea_implement_teleop",
        executable="implement_teleop_node",
        name="implement_teleop",
        parameters=[teleop_configuration],
        output="screen",
        remappings=[("joystick/joy", joystick_topic)],
    )

    return [teleop]


def generate_launch_description():

    print("coucou!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    declared_arguments = []

    declared_arguments.append(DeclareLaunchArgument("joystick_configuration_file_path"))

    # declared_arguments.append(DeclareLaunchArgument("teleop_configuration_file_path"))

    declared_arguments.append(DeclareLaunchArgument("joystick_topic"))

    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])
