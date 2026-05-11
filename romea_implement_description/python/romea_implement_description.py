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


from ament_index_python.packages import get_package_share_directory

import romea_common_description
from romea_common_utils import save_temporary_file

import yaml


# def get_specifications_file_path(implement_description):
#     return romea_common_description.get_specifications_file_path(
#         "romea_implement_description", implement_description
#     )


# def get_specifications(implement_description):
#     with open(get_specifications_file_path(implement_description)) as f:
#         return yaml.safe_load(f)


# def get_geometry_file_path(implement_description):
#     return romea_common_description.get_geometry_file_path(
#         "romea_implement_description", implement_description
#     )


# def get_geometry(implement_description):
#     with open(get_geometry_file_path(implement_description)) as f:
#         return yaml.safe_load(f)


# def get_specification_units_file_path():
#     pkg_path = get_package_share_directory("romea_implement_description")
#     return f"{pkg_path}/config/specifications_units.yaml"


# def get_specification_units():
#     with open(get_specification_units_file_path()) as f:
#         return yaml.safe_load(f)


def get_xacro_file_path(implement_description):
    pkg = get_package_share_directory("romea_implement_description")
    return (
        f"{pkg}/urdf/{implement_description["model"]}_"
        f"{implement_description["version"]}.xacro.urdf"
    )


def get_complete_configuration(implement_name, implement_description, implement_location):
    # model = implement_description["model"]
    # version = implement_description["version"]
    # manufacturer = implement_description["manufacturer"]
    # implement_name = f"{manufacturer} {model} {version} implement called {implement_name}"
    # specifications = get_specifications(implement_description)
    # specifications_units = get_specification_units()

    # implement = romea_common_description.DeviceConfiguration(
    #     implement_name, specifications, implement_description, specifications_units
    # )

    # configuration = {}
    # configuration["model"] = implement_description["model"]
    # configuration["version"] = implement_description["version"]
    # configuration["manufacturer"] = implement_description["manufacturer"]
    # configuration["control_rate"] = implement.get("control_rate")
    # configuration["home_joint_positions"] = implement.get("home_joint_positions")
    # return {**configuration, **implement_location}

    configuration = {}
    configuration["model"] = implement_description["model"]
    configuration["version"] = implement_description["version"]
    configuration["manufacturer"] = ""
    return {**configuration, **implement_location}


def generate_configuration_file_str(configuration, extended=False):
    yaml.dump(configuration)
    # units = get_specification_units()
    # return romea_common_description.generate_configuration_file(configuration, units, extended)


def generate_urdf_description_str(
    prefix,
    mode,
    implement_name,
    implement_description,
    implement_location,
    ros_namespace,
):
    if mode == "simulation":
        mode += "_gazebo"

    configuration = get_complete_configuration(
        implement_name, implement_description, implement_location
    )

    # configuration_yaml_file =
    # save_temporary_file(
    #     f"{prefix}{implement_name}_configuration.yaml",
    #     generate_configuration_file_str(configuration),
    # )

    return romea_common_description.generate_urdf_description_str(
        get_xacro_file_path(implement_description),
        mappings={
            "prefix": prefix,
            "mode": mode,
            "name": implement_name,
            "parent_link": implement_location["parent_link"],
            "xyz": " ".join(map(str, implement_location["xyz"])),
            "rpy": " ".join(map(str, implement_location["xyz"])),
        },
    )
