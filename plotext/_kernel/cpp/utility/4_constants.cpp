// Kernel-wide constants: ANSI escape sequences and pre-computed upper-bound buffer sizes

// --- ANSI escape sequences ---
const wchar_t ansi_start[]      = L"\x1b[";     // Start of an ANSI escape sequence
const wchar_t ansi_end[]        = L"\x1b[0m";   // Reset ANSI sequence
const wchar_t ansi_fullground[] = L"\x1b[38;";  // Foreground color prefix
const wchar_t ansi_background[] = L"\x1b[48;";  // Background color prefix

// --- Text constants ---
const wchar_t new_line[] = L"\n";   // Newline character
const wchar_t space      = L' ';    // Space character (used in formatting)

// --- Element size constants (in wchar_t units) ---
const size_t color_size_max     = 20;                                         // Max size of a color code
const size_t style_size_max     = 19;                                         // Max size of a style code
const size_t pixel_size_max     = 2 * color_size_max + style_size_max;        // Pixel size (fg + bg + style)
const size_t character_size_max = pixel_size_max + 1 + wcslen(ansi_end);      // Character size (pixel + 1 char + reset)
const size_t marker_size_max    = pixel_size_max + 6 + wcslen(ansi_end);      // Marker size (pixel + marker chars + reset)

// --- Numeric limits ---
const float inf = numeric_limits<float>::infinity();
