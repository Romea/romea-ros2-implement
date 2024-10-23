# Copyright 2024 INRAE, French National Research Institute for Agriculture, Food and Environment
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


from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import (
    DeclareLaunchArgument,
    OpaqueFunction,
    GroupAction,
)

from launch_ros.actions import Node, PushRosNamespace


from romea_common_bringup import device_namespace
from romea_implement_bringup import ImplementMetaDescription, implement_prefix, create_configuration_file


def get_mode(context):
    return LaunchConfiguration("mode").perform(context)


def get_robot_namespace(context):
    return LaunchConfiguration("robot_namespace").perform(context)


def get_meta_description(context):
    implement_meta_description_file_path = LaunchConfiguration(
        "meta_description_file_path"
    ).perform(context)

    return ImplementMetaDescription(implement_meta_description_file_path)


def launch_setup(context, *args, **kwargs):

    robot_namespace = get_robot_namespace(context)
    meta_description = get_meta_description(context)
    controller_manager_name = implement_prefix(robot_namespace, meta_description)+"controller_manager"
    implement_name = meta_description.get_name()

    controllers_configuration_file_path = create_configuration_file(
        robot_namespace, meta_description, "controllers"
    )

    actions = []

    actions.append(PushRosNamespace(robot_namespace))
    actions.append(PushRosNamespace(implement_name))

    actions.append(
        Node(
            package="romea_mobile_base_controllers",
            executable="spawner.py",
            exec_name="joint_state_broadcaster_spawner",
            arguments=[
                "joint_state_broadcaster",
                "--controller-manager",
                controller_manager_name,
            ],
            # output="screen",
        )
    )

    for controller_name in meta_description.get_controllers()["selected"]:

        actions.append(
            Node(
                package="romea_mobile_base_controllers",
                executable="spawner.py",
                exec_name=controller_name + "_spawner",
                arguments=[
                    controller_name,
                    "--param-file",
                    controllers_configuration_file_path,
                    "--controller-manager",
                    controller_manager_name,
                    "--namespace",
                    device_namespace(robot_namespace, None, implement_name)
                ],
            )
        )

    return [GroupAction(actions)]


def generate_launch_description():

    declared_arguments = []

    declared_arguments.append(DeclareLaunchArgument("mode"))

    declared_arguments.append(DeclareLaunchArgument("robot_namespace"))

    declared_arguments.append(DeclareLaunchArgument("meta_description_file_path"))

    return LaunchDescription(
        declared_arguments + [OpaqueFunction(function=launch_setup)]
    )
