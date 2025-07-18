cmake_minimum_required(VERSION 3.16)
project(calc C)

# C-Standard setzen
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Ninja als Generator (wird in VS Code Settings festgelegt)
# add_subdirectory(include)  # falls du weitere CMakeLists in Unterordnern hast

# Quell­dateien
set(SOURCES
    calc.c
)

# Executable erzeugen
add_executable(calc ${SOURCES})
