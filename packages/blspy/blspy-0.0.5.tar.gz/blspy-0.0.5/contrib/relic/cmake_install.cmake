# Install script for directory: /Users/mariano/Chia/Programs/bls-signatures/contrib/relic

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/relic" TYPE FILE FILES
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_arch.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_bc.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_bench.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_bn.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_conf.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_core.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_cp.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_dv.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_eb.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_ec.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_ed.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_ep.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_epx.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_err.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_fb.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_fbx.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_fp.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_fpx.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_label.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_md.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_pc.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_pool.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_pp.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_rand.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_test.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_trace.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_types.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/relic_util.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/relic/low" TYPE FILE FILES
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/low/relic_bn_low.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/low/relic_dv_low.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/low/relic_fb_low.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/low/relic_fp_low.h"
    "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/low/relic_fpx_low.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/relic" TYPE DIRECTORY FILES "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/include/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/cmake/relic-config.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/src/cmake_install.cmake")
  include("/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/test/cmake_install.cmake")
  include("/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/bench/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/mariano/Chia/Programs/bls-signatures/contrib/relic/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
