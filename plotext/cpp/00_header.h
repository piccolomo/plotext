// --- Standard Includes ---
#include <cstring>
#include <iostream>
#include <cmath>
#include <functional>
#include <codecvt>
#include <iomanip>
#include <cstdint>
#include <limits>
// #include <utility> // optional: for std::swap if needed

#ifdef _WIN32
    #include <Windows.h>
#endif

// --- Utility Modules ---
// Core utilities: Vector, constants, maps, strings, C-style strings, data creation, text alignment
#include "utility/1_vector.cpp"
#include "utility/2_constants.cpp"
#include "utility/3_maps.cpp"
#include "utility/4_strings.cpp"
#include "utility/5_cstrings.cpp"
#include "utility/6_data.cpp"
#include "utility/7_alignment.cpp"

// --- Pixel Modules ---
// Color, style, pixel representation, colorization, character handling
#include "01_color.cpp"
#include "02_style.cpp"
#include "03_pixel.cpp"
#include "04_colorize.cpp"
#include "05_character.cpp"

// --- Marker / Point Modules ---
// Marker types, marker class, boolean matrix for points
#include "06_marker_type.cpp"
#include "07_marker.cpp"
#include "08_matrix_bool.cpp"

// --- Point Modules ---
// Point position, point class, point maps, collections, filled points, signal handling
#include "09_point_position.cpp"
#include "10_point.cpp" 
#include "11_map.cpp"
#include "12_points.cpp" 
#include "13_point_filled.cpp" 
#include "14_points_filled.cpp" 
#include "15_signal.cpp"

// --- Matrix Modules ---
// Character handling in HD matrix, general matrix operations
#include "16_character_hd.cpp"
#include "17_matrix.cpp"
