cmake_minimum_required(VERSION 3.10)
project(CppCalculator)

# GoogleTest requires at least C++11
set(CMAKE_CXX_STANDARD 11)

# Add GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.10.0.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

# Disable -Werror for Google Test
set_target_properties(gtest PROPERTIES COMPILE_FLAGS "-Wno-error")

add_executable(
  test_calculator_gtest
  tests/test_calculator_gtest.cpp
  src/calculator.cpp
)

target_link_libraries(
  test_calculator_gtest
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(test_calculator_gtest)

# Configure CTest to output results in XML format
set(CTEST_OUTPUT_ON_FAILURE TRUE)
add_custom_target(
  generate_test_report
  COMMAND ${CMAKE_COMMAND} -E env SITE=rabat BUILDNAME=amine ${CMAKE_CTEST_COMMAND} --output-on-failure -T Test --no-compress-output -O ${CMAKE_SOURCE_DIR}/docs/TestResults.xml
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)