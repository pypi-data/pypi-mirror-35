To build the project, first assure that you have the CMake installed. To verify that your
system contains CMake, use the respected command in your Operating System.

#Any flavor of Linux
* Verify installation
    $ cmake -version
* If the above command fails, run the following command to install CMake
    $ sudo apt-get install cmake
(Assuming that you have root access)

#Windows
// TODO

Now you are ready to build the CGYM project using CMake.
We are going to place all of the build related files in the build directory. Execute the following commands from the projects main directory.

$ cd build
$ cmake ..
$ make

execute cmake . in the directory where CMakeLists.txt exists.
$ cmake .

To clean/delete this build, you can recursively delete all files/directories within build directory
PROJECT_HOME$ rm -r build/*
PROJECT_HOME$ tree      <- Tree is an external application ->

# C++17
Requires one of the following compilers

* GCC/libstdc++ 7.0+ -std=c++17
* Clang/libc++ 4.0+ -std=c++1z
* MSVC 15 (2017) \std:c+=17 or \std:latest