// Copyright 2022 INRAE, French National Research Institute for Agriculture,
// Food and Environment
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// std
#include <memory>

// romea
#include "romea_common_utils/params/node_parameters.hpp"

// local
#include "romea_implement_teleop/joystick_parameters.hpp"

namespace {

const char UP_DOWN_IMPLEMENT_AXE_MAPPING_PARAM_NAME[] =
    "joystick_mapping.axes.up_down_implement";
const char TURBO_MODE_BUTTON_MAPPING_PARAM_NAME[] =
    "joystick_mapping.buttons.turbo_mode";
const char DOWN_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME[] =
    "joystick_mapping.buttons.down_implement";
const char UP_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME[] =
    "joystick_mapping.buttons.up_implement";

}  // namespace

namespace romea {
namespace ros2 {

//-----------------------------------------------------------------------------
void declare_up_down_implement_axe_mapping(std::shared_ptr<rclcpp::Node> node) {
  declare_parameter_with_default<int>(
      node, UP_DOWN_IMPLEMENT_AXE_MAPPING_PARAM_NAME, -1);
}

//-----------------------------------------------------------------------------
void declare_down_implement_button_mapping(std::shared_ptr<rclcpp::Node> node) {
  declare_parameter_with_default<int>(
      node, DOWN_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME, -1);
}

//-----------------------------------------------------------------------------
void declare_up_implement_button_mapping(std::shared_ptr<rclcpp::Node> node) {
  declare_parameter_with_default<int>(
      node, UP_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME, -1);
}

//-----------------------------------------------------------------------------
int get_up_down_implement_axe_mapping(std::shared_ptr<rclcpp::Node> node) {
  return get_parameter<int>(node, UP_DOWN_IMPLEMENT_AXE_MAPPING_PARAM_NAME);
}

//-----------------------------------------------------------------------------
int get_down_implement_button_mapping(std::shared_ptr<rclcpp::Node> node) {
  return get_parameter<int>(node, DOWN_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME);
}

//-----------------------------------------------------------------------------
int get_up_implement_button_mapping(std::shared_ptr<rclcpp::Node> node) {
  return get_parameter<int>(node, UP_IMPLEMENT_BUTTON_MAPPING_PARAM_NAME);
}

}  // namespace ros2
}  // namespace romea
