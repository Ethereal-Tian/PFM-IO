cmake_minimum_required(VERSION 2.8.3)
project(rgbd2polari)

set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_DIRS})

add_library(pfm_io src/PFMReadWrite.cpp)
target_link_libraries(pfm_io ${OpenCV_LIBS} )

add_executable(pfm_main src/pfm_main.cpp)
target_link_libraries(pfm_main pfm_io ${OpenCV_LIBS})

add_executable(pfm_test src/pfm_test.cpp)
target_link_libraries(pfm_test pfm_io ${OpenCV_LIBS})



