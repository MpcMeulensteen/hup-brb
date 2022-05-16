# CMake generated Testfile for 
# Source directory: /home/student/sjowmm_ws/src/navigation2/nav2_costmap_2d/test/unit
# Build directory: /home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(array_parser_test "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/student/sjowmm_ws/build/nav2_costmap_2d/test_results/nav2_costmap_2d/array_parser_test.gtest.xml" "--package-name" "nav2_costmap_2d" "--output-file" "/home/student/sjowmm_ws/build/nav2_costmap_2d/ament_cmake_gtest/array_parser_test.txt" "--command" "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit/array_parser_test" "--gtest_output=xml:/home/student/sjowmm_ws/build/nav2_costmap_2d/test_results/nav2_costmap_2d/array_parser_test.gtest.xml")
set_tests_properties(array_parser_test PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit/array_parser_test" TIMEOUT "60" WORKING_DIRECTORY "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;86;ament_add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/student/sjowmm_ws/src/navigation2/nav2_costmap_2d/test/unit/CMakeLists.txt;1;ament_add_gtest;/home/student/sjowmm_ws/src/navigation2/nav2_costmap_2d/test/unit/CMakeLists.txt;0;")
add_test(collision_footprint_test "/usr/bin/python3" "-u" "/opt/ros/foxy/share/ament_cmake_test/cmake/run_test.py" "/home/student/sjowmm_ws/build/nav2_costmap_2d/test_results/nav2_costmap_2d/collision_footprint_test.gtest.xml" "--package-name" "nav2_costmap_2d" "--output-file" "/home/student/sjowmm_ws/build/nav2_costmap_2d/ament_cmake_gtest/collision_footprint_test.txt" "--command" "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit/collision_footprint_test" "--gtest_output=xml:/home/student/sjowmm_ws/build/nav2_costmap_2d/test_results/nav2_costmap_2d/collision_footprint_test.gtest.xml")
set_tests_properties(collision_footprint_test PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit/collision_footprint_test" TIMEOUT "60" WORKING_DIRECTORY "/home/student/sjowmm_ws/build/nav2_costmap_2d/test/unit" _BACKTRACE_TRIPLES "/opt/ros/foxy/share/ament_cmake_test/cmake/ament_add_test.cmake;118;add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;86;ament_add_test;/opt/ros/foxy/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/student/sjowmm_ws/src/navigation2/nav2_costmap_2d/test/unit/CMakeLists.txt;6;ament_add_gtest;/home/student/sjowmm_ws/src/navigation2/nav2_costmap_2d/test/unit/CMakeLists.txt;0;")
subdirs("../../gtest")
