#include <cstring>
#include <iostream>
#include <vector>
#include <cmath>
#include <functional>
#include <codecvt>
#include <iomanip>

#ifdef _WIN32
    #include <Windows.h>
#endif


// Utility modules
#include "utility/constants.cpp"
#include "utility/maps.cpp"
#include "utility/strings.cpp"
#include "utility/cstrings.cpp"
#include "utility/data.cpp"
#include "utility/bit.cpp"


// Pixel modules
#include "pixel/color.cpp"
#include "pixel/style.cpp"
#include "pixel/pixel.cpp"
#include "pixel/colorize.cpp"


// Character modules
#include "character/character.cpp"
#include "character/marker_type.cpp"
#include "character/marker.cpp"
#include "character/matrix_bool.cpp"
#include "character/character_hd.cpp"


// Point modules
#include "point/point_position.cpp"
#include "point/point.cpp"
#include "point/points.cpp"


// Dot modules
#include "dot/dot_position.cpp"
#include "dot/dot.cpp"
#include "dot/dots_map.cpp"
#include "dot/dots.cpp"


// Matrix modules
#include "matrix/alignment.cpp"
#include "matrix/line.cpp"
#include "matrix/matrix.cpp"

// Optional/Commented out for now
// #include "matrix/matrix_hd.cpp"
