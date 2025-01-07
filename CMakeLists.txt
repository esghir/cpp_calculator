# Minimum required CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(CppProject VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Define the directories for source and tests
set(SRC_DIR ${PROJECT_SOURCE_DIR}/src)
set(TEST_DIR ${PROJECT_SOURCE_DIR}/tests)

# Add the main executable
add_executable(CppProject
    ${SRC_DIR}/main.cpp
    ${SRC_DIR}/calculator.cpp
)

# Include directories
target_include_directories(CppProject PRIVATE ${SRC_DIR})

# Add the test executable
add_executable(TestCalculator
    ${TEST_DIR}/test_calculator.cpp
    ${SRC_DIR}/calculator.cpp
)

# Include directories for tests
target_include_directories(TestCalculator PRIVATE ${SRC_DIR})

# Link libraries for unit testing (if needed, e.g., Google Test)
# find_package(GTest REQUIRED)
# target_link_libraries(TestCalculator PRIVATE GTest::GTest GTest::Main)

# Install target (optional, for installation paths)
install(TARGETS CppProject DESTINATION bin)
