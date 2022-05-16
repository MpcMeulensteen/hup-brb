# CMake generated Testfile for 
# Source directory: /home/student/sjowmm_ws/src/navigation2/nav2_system_tests/src/localization
# Build directory: /home/student/sjowmm_ws/build/nav2_system_tests/src/localization
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_localization "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/student/sjowmm_ws/build/nav2_system_tests/test_results/nav2_system_tests/test_localization.xml" "--package-name" "nav2_system_tests" "--generate-result-on-success" "--env" "TEST_MAP=/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/maps/map_circular.yaml" "TEST_EXECUTABLE=/home/student/sjowmm_ws/build/nav2_system_tests/src/localization/test_localization_node" "TEST_WORLD=/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/worlds/turtlebot3_ros2_demo.world" "GAZEBO_MODEL_PATH=/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/models" "--command" "/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/src/localization/test_localization_launch.py")
set_tests_properties(test_localization PROPERTIES  TIMEOUT "180" WORKING_DIRECTORY "/home/student/sjowmm_ws/build/nav2_system_tests/src/localization" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/src/localization/CMakeLists.txt;9;ament_add_test;/home/student/sjowmm_ws/src/navigation2/nav2_system_tests/src/localization/CMakeLists.txt;0;")
