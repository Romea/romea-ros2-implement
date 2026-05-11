cmake_minimum_required(VERSION 3.5)
project(romea_implement_teleop)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(romea_core_common REQUIRED)
find_package(romea_common_utils REQUIRED)
find_package(romea_joystick_utils REQUIRED)
find_package(romea_implement_msgs REQUIRED)
find_package(romea_cmd_mux_msgs REQUIRED)
find_package(romea_cmd_mux_utils REQUIRED)


add_library(${PROJECT_NAME} SHARED
  src/implement_teleop.cpp
  src/joystick_parameters.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)

target_compile_definitions(${PROJECT_NAME}
  PRIVATE "ROMEA_IMPLEMENT_TELEOP_BUILDING_DLL")

ament_target_dependencies(${PROJECT_NAME}
  rclcpp
  rclcpp_components
  romea_core_common
  romea_common_utils
  romea_cmd_mux_msgs
  romea_joystick_utils
  romea_implement_msgs
  romea_cmd_mux_msgs
  romea_cmd_mux_utils)

rclcpp_components_register_node(${PROJECT_NAME}
  PLUGIN romea::ros2::ImplementTeleop
  EXECUTABLE implement_teleop_node
)

ament_export_dependencies(rclcpp)
ament_export_dependencies(romea_core_common)
ament_export_dependencies(romea_common_utils)
ament_export_dependencies(romea_joystick_utils)
ament_export_dependencies(romea_implement_msgs)
ament_export_dependencies(romea_cmd_mux_msgs)
ament_export_dependencies(romea_cmd_mux_utils)

ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})

install(TARGETS
  ${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin)

install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME})

install(
  DIRECTORY include/
  DESTINATION include)


ament_package()

