# romea_ros2_implement

## Overview

`romea_ros2_implement` groups the ROS2 packages used to describe, launch and teleoperate robotic implements in the ROMEA ecosystem.

This repository-level README gives a map of the stack. Detailed behavior, configuration formats, generated files and launch examples are documented in the README of each package listed below.

## Packages

| Package | Role |
| --- | --- |
| `romea_implement` | Metapackage for the implement stack. |
| `romea_implement_description` | Implement URDF templates, meshes and Python helpers used to generate implement descriptions. |
| `romea_implement_meta_bringup` | Main user entry point: implement meta-description parser, configuration generation, URDF generation and reusable launch profiles. |
| `romea_implement_msgs` | ROS2 messages used to command implements and report implement state. |
| `romea_implement_teleop` | Teleoperation nodes and remapping configuration for joystick-controlled implements. |

## Usage

This stack is usually consumed from a larger ROMEA workspace or from a demo configuration that already selects the implement devices to launch.

In most cases, start with `romea_implement_meta_bringup`. It is the user-facing entry point of the stack: from an implement meta-description, it can generate the detailed implement configuration, generate the URDF fragment, and launch the selected implement profile. `romea_implement_description` provides the implement description data and URDF helpers used behind this entry point.

For active implements, `romea_implement_msgs` and `romea_implement_teleop` provide the command, state and joystick-control building blocks used by the runtime.

Use the specialized package README files when you need to inspect or extend a specific part of the stack:

* `romea_implement_description` to add or inspect implement meshes and URDF descriptions;
* `romea_implement_meta_bringup` to write implement meta-descriptions and launch profiles;
* `romea_implement_msgs` to inspect implement command and state messages;
* `romea_implement_teleop` to configure joystick-based implement teleoperation.

## License

This project is released under the Apache License 2.0. See the `LICENSE` file for details.

## Authors

The `romea_ros2_implement` stack was developed by Jean Laneurit in the context of research projects carried out at INRAE.

## Contact

For questions or comments about this stack, contact [Jean Laneurit](mailto:jean.laneurit@inrae.fr).
