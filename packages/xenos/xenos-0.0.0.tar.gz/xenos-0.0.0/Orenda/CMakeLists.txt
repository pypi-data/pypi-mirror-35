cmake_minimum_required(VERSION 3.10)

if (ENABLE_UNIT_TESTS)
    # Enable add_test() command
    enable_testing()

    # Append the Google Test Framework custom module path
    # NOTE: CMAKE_MODULE_PATH stores the absolute path of modules in your system. Therefore, it is important to include
    #       the path of module relative to ${CMAKE_SOURCE_DIR} while also including the variable itself or CMake will
    #       not include it and silently fails.
    list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/CMake/Modules)
    include(GoogleTest)

    # Add Tests
    add_subdirectory(Tests)
endif()

### Set directories
set(SOURCE_DIR     ${CMAKE_CURRENT_SOURCE_DIR}/Source)
set(THIRDPARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/ThirdParty)

### Define Source files
## Core Types
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Core/Types.h)
#list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Core/Types/Space.h)
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Core/Types/Discrete.h)
#list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Core/Types/Tuple.h)

## Environments Math Libraries
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Core/Math/Random.h)
list(APPEND CPP_FILES ${SOURCE_DIR}/Private/Core/Math/Random.cpp)

## WEnvironment Interface
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Environments/Environments.h)
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Environments/Registry/EnvironmentRegistry.h)
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Environments/Interface/DiscreteEnvironment.h)
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Environments/Interface/TransitionalEnvironment.h)

## Blackjack
list(APPEND HPP_FILES ${SOURCE_DIR}/Public/Environments/ToyText/Blackjack.h)
list(APPEND CPP_FILES ${SOURCE_DIR}/Private/Environments/ToyText/Blackjack.cpp)

### Add all sources to Environments Project
add_library(Orenda STATIC ${HPP_FILES} ${CPP_FILES})

set_target_properties(Orenda PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(Orenda PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

### Include directories
## Source home
target_include_directories(Orenda PUBLIC Source/Public)

## ThirdParty Libraries
# Boost
target_include_directories(Orenda PUBLIC ${THIRDPARTY_DIR}/boost/include/)
