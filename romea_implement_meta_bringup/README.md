# romea_implement_meta_bringup

## Overview

romea_implement_meta_bringup provides tools to describe and launch robotic implements using a meta-description approach.

It allows defining implement systems in a high-level YAML format and automatically generating consistent ROS 2 artifacts such as:

* configuration files → used as generic ROS 2 configuration inputs
* launch files → used to start implement drivers if an active implement is used
* URDF description files → used to load the implement into simulators

This package is built on top of `romea_common_meta_bringup` and specializes it for robotic implement integration. 

It also provides launch files that allow controlling the implement both on a real robot and in simulation.

---

## implement meta-description concept

An `implement meta-description` is a YAML file that defines a robotic implement and how it should be integrated into a system. It centralizes:

* implement identification (name, namespace)
* hardware + control configuration (manufacturer, model, version)
* kinematic attachment (parent link, pose)
* ROS2 launch description

---

### Example meta-description

```yaml id="9lfc1h"
name: implement
namespace: ns

configuration:
  manufacturer: "?"
  model: "cultivator"
  version: "mounted"

location:
  parent_link: implement_link
  xyz: [1.0, 2.0, 3.0]
  rpy: [4.0, 5.0, 6.0]

launch:
  - include:
      file: $(find-pkg-share romea_implement_meta_bringup)/profile/foo.launch.py
```

### Launch files Profiles

The `profile/` directory is currently empty, but it is intended to contain ready-to-use ROS 2 launch files for controlling active implements.

These profiles will make it possible to:

* launch implement drivers
* launch simulator bridges
* reuse standardized bringup configurations

---

## Scripts

`romea_implement_meta_bringup` provides several scripts to generate ROS2 artifacts (configuration, controllers configuration, launch and URDF files) from an implement meta-description; the usage and resulting outputs are described below.

### Generate configuration file

```bash id="rq0ybi"
generate-implement-configuration-file \
  meta_description_file_path:=path/to/implement_meta_description.yaml \
  extended:=false
```

#### Example output

```yaml id="pgd8yu"
model: cultivator
version: mounted
manufacturer: "?"
parent_link: implement_link
xyz: [1.0, 2.0, 3.0]  # unit m
rpy: [4.0, 5.0, 6.0]  # unit °
```

---

### Generate launch file

Generates a YAML ROS 2 launch file from the meta-description.

```bash
generate-implement-launch-file \
  robot_namespace:=robot \
  meta_description_file_path:=path/to/implement_meta_description.yaml
```

#### Example output

```yaml
launch:
- arg:
    name: mode
    default: live
- group:
  - push-ros-namespace: {namespace: robot}
  - push-ros-namespace: {namespace: ns}
  - push-ros-namespace: {namespace: implement}
  - let: {name: model, value: cultivator}
  - let: {name: version, value: mounted}
  - let: {name: manufacturer, value: "?"}
  - let: {name: parent_link, value: implement_link}
  - let: {name: xyz, value: '[1.0, 2.0, 3.0]'}
  - let: {name: rpy, value: '[4.0, 5.0, 6.0]'}
  - let: {name: tf_prefix, value: robot_}
  - let: {name: frame_id, value: robot_implement_link}
  - include:
      file: $(find-pkg-share romea_implement_meta_bringup)/profile/foo.launch.py
```

#### Notes

* the launch file is generated from the `launch` section of the meta-description
* namespaces are automatically constructed (`robot → device → implement`)
* all configuration values are exposed as `let` variables
* the selected profile is included at the end

This file can be used directly with ROS2 or generated dynamically using `implement.launch.py`.

## Usage

The package provides **two main launch files**:

* `implement.launch.py` → for dynamic bringup (live or simulation mode)
* `simulation_test.launch.py` → for full simulation test

---

### Dynamic bringup

When using `implement.launch.py`, the following steps are performed automatically:

```bash
ros2 launch romea_implement_meta_bringup implement.launch.py \
  mode:=live \
  robot_namespace:=robot \
  meta_description_file_path:=path/to/implement_meta_description.yaml
```

* generation of the URDF description
* generation of the implement configuration file
* generation of the launch file
* execution of the generated launch file


#### Live or simulation mode

The `mode` parameter controls the behavior:

* `live` → starts the implement driver and controllers
* `simulation_<simulator>` → starts simulation bridges for active implements

---

### Simulation test

For a complete simulation setup, use:

```bash
ros2 launch romea_implement_meta_bringup simulation_test.launch.py \
  simulator_type:=gazebo \
  robot_namespace:=robot \
  meta_description_file_path:=path/to/implement_meta_description.yaml
```

This launch file:

* starts the simulator
* generates and loads the URDF
* spawns the implement in simulation
* calls `implement.launch.py` to start controllers and bridges

---
## Supported implements

Coming soon
