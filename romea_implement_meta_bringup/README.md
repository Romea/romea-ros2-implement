# 1 Overview

The romea_implement_bringup package

# 2 Control the implement

```
ros2 topic pub /robot/implement/position_controller/commands std_msgs/msg/Float64MultiArray "data:
- 0.5"
```