# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-src"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-build"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix/tmp"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix/src/glasgow_constraint_solver-populate-stamp"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix/src"
  "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix/src/glasgow_constraint_solver-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/matthewmcilree/PhD_Code/gcspy/cmake-build-debug/_deps/glasgow_constraint_solver-subbuild/glasgow_constraint_solver-populate-prefix/src/glasgow_constraint_solver-populate-stamp/${subDir}")
endforeach()
