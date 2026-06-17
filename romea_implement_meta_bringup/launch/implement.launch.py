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

# from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch_ros.actions import Node

import romea_common_meta_bringup.ros_launch as common
from romea_implement_meta_bringup.meta_description import generate_yaml_launch_file_str
import romea_implement_meta_bringup.ros_launch as implement


def launch_setup(context, *args, **kwargs):
    mode = common.get_mode(context)
    meta_description = implement.get_meta_description(context)
    launch_filename = f"/tmp/{meta_description.get_filename_prefix()}drivers.launch.yaml"
    with open(launch_filename, "w") as f:
        f.write(generate_yaml_launch_file_str(meta_description))

    actions = [
        IncludeLaunchDescription(
            AnyLaunchDescriptionSource(launch_filename),
            launch_arguments={
                "mode": mode,
            }.items(),
        )
    ]

    # TODO remove this test code and replace it by a better interface for the implement
    if mode.startswith("simu"):
        robot_name = meta_description.get_robot_name()
        actions += [
            Node(
                package="romea_implement_meta_bringup",
                executable="simple_command",
                exec_name="simple_command",
                namespace=meta_description.get_full_namespace(),
                parameters=[{"anchor_high": 0.0, "anchor_low": 0.36}],
                remappings=[
                    (
                        "position_controller/commands",
                        f"/{robot_name}/base/lift_arm_controller/commands",
                    ),
                    ("command", f"/{robot_name}/base/implement/rear/command"),
                ],
            )
        ]

    return actions


def generate_launch_description():

    return LaunchDescription(
        [
            common.declare_mode("live"),
            common.declare_robot_namespace(""),
            common.declare_meta_description_file_path("implement"),
            OpaqueFunction(function=launch_setup),
        ]
    )
