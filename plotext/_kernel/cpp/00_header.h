// Aggregator header: pulls in standard library headers and then concatenates every kernel source file in dependency order

// --- Standard Includes ---
#include <cstring>
#include <iostream>
#include <cmath>
#include <functional>
#include <codecvt>
#include <iomanip>
#include <sstream>          // the string streams the logs use, pulled in by chance elsewhere and not at all on macos
#include <cstdint>
#include <limits>
#include <cassert>
#include <algorithm>

// The windows console reads bytes, and must be told they are utf-8 before anything is written; the defines keep windows.h from bringing in the names clashing with the standard ones
#ifdef _WIN32
    #define WIN32_LEAN_AND_MEAN
    #define NOMINMAX
    #define byte windows_byte
    #include <windows.h>
    #undef byte
#endif

// --- Utility Modules ---
// Core utilities: Array, Array2D, Vector, constants, maps, strings, C-style strings, data, alignment
#include "utility/0_array.cpp"
#include "utility/1_array2d.cpp"
#include "utility/2_vector.cpp"
#include "utility/4_constants.cpp"
#include "utility/5_maps.cpp"
#include "utility/6_strings.cpp"
#include "utility/7_cstrings.cpp"
#include "utility/8_data.cpp"
#include "utility/9_alignment.cpp"
#include "utility/10_orientation.cpp"

// --- Kernel Modules ---
#include "01_color.cpp"
#include "02_style.cpp"
#include "03_pixel.cpp"
#include "04_colorize.cpp"
#include "05_mosaic.cpp"
#include "06_character.cpp"
#include "07_matrix.cpp"
#include "08_marker.cpp"
#include "09_position.cpp"
#include "10_point.cpp"
#include "11_grid.cpp"
#include "12_points.cpp"
#include "13_point_filled.cpp"
#include "14_points_filled.cpp"
#include "15_signal.cpp"
