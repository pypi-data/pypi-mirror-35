#=======================================================================================================================
# Project Setup
# CMakeLists files in this project can refer to the root source directory of the project as ${ORENDA_SOURCE_DIR} and
# to the root binary directory of the project as ${ORENDA_BINARY_DIR}.
#=======================================================================================================================
cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

# Global project name
project(ORENDA)

# C++ Version
set(CMAKE_CXX_STANDARD 17)

# Tell CMake not to define WIN32 when building with Cygwin.
set(CMAKE_LEGACY_CYGWIN_WIN32 0)

#=======================================================================================================================
# Setup CMake Options
#=======================================================================================================================
option(ENABLE_UNIT_TESTS            "Includes and enbales Google tests as well as Python unit tests."   OFF)
option(ENABLE_COMPILE_TIME_TESTS    "Allows for the unit tests to be run at compile time."              OFF)
option(ADD_PYTHON_BINDINGS          "Adds the subdirectory of python bindings to the code base."        OFF)

#=======================================================================================================================
# Check Compiler Support
#=======================================================================================================================
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
include(CheckCxxCompilerSupport)



#=======================================================================================================================
# Setup warning flags
#=======================================================================================================================
# Turn on most warnings and have the compiler treat them as errors.
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU" OR
        "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    set(warnings "-Wall -Wextra -Werror")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    set(warnings "/W4 /WX /EHsc")
endif()


if (NOT CONFIGURED_ONCE)
    set(CMAKE_C_FLAGS   "${CMAKE_C_FLAGS}   ${warnings}"
            CACHE STRING "Flags used by the compiler during all build types." FORCE)

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${warnings}"
            CACHE STRING "Flags used by the compiler during all build types." FORCE)
endif()


#=======================================================================================================================
# Add subdirectories
#=======================================================================================================================
# Recurse into the subdirectories. This does not cause another cmake executable to run.
add_subdirectory(Orenda)

if(ADD_PYTHON_BINDINGS)
    add_subdirectory(PythonBindings)
endif()

set(CONFIGURED_ONCE TRUE CACHE INTERNAL
    "A flag showing that CMake has configured at least once.")