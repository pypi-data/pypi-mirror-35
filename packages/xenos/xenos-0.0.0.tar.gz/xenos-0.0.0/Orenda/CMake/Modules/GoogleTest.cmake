set(GOOGLE_TEST_DIR "ThirdParty/googletest"
        CACHE PATH "The path to the Google Test framework." FORCE)

# if(CMAKE_C_COMPILER_ID MATCHES "^(Apple)?Clang$")
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    set(THREAD_LIBRARY pthread)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
    # Force this option to ON so that Google Tests will use /MD instead of /MT
    # /MD is now the default for Visual Studio, so it should be our default, too
    option(gtest_force_shared_crt "USE shared (DLL) run-time lib even when Google Test is built as static lib." ON)
    set(THREAD_LIBRARY -pthread)
endif()

if(APPLE)
    add_definitions(-DGTEST_USE_OWN_TR1_TUPLE=1)
endif()

add_subdirectory(${GOOGLE_TEST_DIR} ${CMAKE_BINARY_DIR}/googletest)

# Turn off strict warning check for gtest as those warnings do not concern us.
set_property(TARGET gtest APPEND_STRING PROPERTY COMPILE_FLAGS " -w")

include_directories(SYSTEM
        ${GOOGLE_TEST_DIR}/googlemock/include
        ${GOOGLE_TEST_DIR}/googletest/include)


##
# add_google_test(<targer> <sources>...)
#
# Adds a Google Mock based test executable, <target>, built from <sources> and
# addds the test so that CTest will run it. Both the executable and test will be
# named <target>
##
function(add_google_test target)
    add_executable(${target} ${ARGN})
    target_link_libraries(${target} PRIVATE Orenda gtest gtest_main gmock_main ${THREAD_LIBRARY})

    add_test(${target} ${target})

    if(ENABLE_COMPILE_TIME_TESTS)
        # Runs the tests automatically at build time
        add_custom_command(TARGET ${target}
                           POST_BUILD
                           COMMAND ${target}
                           WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                           COMMENT "Running ${target}" VERBATIM)
    endif()
endfunction()