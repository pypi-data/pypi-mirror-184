cmake_minimum_required(VERSION 3.4...3.18)
set(CMAKE_CXX_STANDARD 20)
project(gcspy)

include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11
        GIT_TAG        v2.10.0
)

FetchContent_GetProperties(pybind11)
if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
endif()

FetchContent_Declare(
        glasgow_constraint_solver
        GIT_REPOSITORY https://github.com/ciaranm/glasgow-constraint-solver
        GIT_TAG        8638a1eb4b371b5514615b0f7fd9b98d2466c713
)

pybind11_add_module(gcspy src/api.cc)

FetchContent_GetProperties(glasgow_constraint_solver)

if(NOT glasgow_constraint_solver_POPULATED)
    FetchContent_Populate(glasgow_constraint_solver)
    set(GCS_ENABLE_DOXYGEN OFF)
    set(GCS_ENABLE_XCSP OFF)
    set(GCS_ENABLE_EXAMPLES OFF)
    message(${glasgow_constraint_solver_SOURCE_DIR} ${glasgow_constraint_solver_BINARY_DIR})
    add_subdirectory(${glasgow_constraint_solver_SOURCE_DIR} ${glasgow_constraint_solver_BINARY_DIR})
endif()



target_link_libraries(gcspy PUBLIC glasgow_constraint_solver)
target_include_directories(gcspy PUBLIC ${glasgow_constraint_solver_SOURCE_DIR})

add_test(NAME python_bindings COMMAND python3 ${CMAKE_SOURCE_DIR}/cpmpy/gcspytest.py)
