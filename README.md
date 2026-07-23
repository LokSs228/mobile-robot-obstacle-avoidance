# Mobile Robot Obstacle Avoidance (ROS2 + Gazebo)

   Simple reactive navigation stack built with ROS2 Humble and Gazebo,
   using a TurtleBot3-based diff-drive robot.

   ## Architecture
   - `mover` — publishes velocity commands on a timed cycle
   - `laser_reader` — subscribes to /scan and logs distance readings
   - `obstacle_avoider` — combines both: stops and turns when an obstacle
     is closer than 0.5 m, otherwise drives forward

   ## Topics
   | Topic     | Type                    | Direction  |
   |-----------|-------------------------|------------|
   | /cmd_vel  | geometry_msgs/Twist     | published  |
   | /scan     | sensor_msgs/LaserScan   | subscribed |

   ## Run
```bash
   export TURTLEBOT3_MODEL=burger
   ros2 launch turtlebot3_gazebo empty_world.launch.py
   ros2 run my_robot_sim obstacle_avoider
```

  ## Demo
![demo](2026-07-2321-46-34-ezgif.com-video-to-gif-converter.gif)
