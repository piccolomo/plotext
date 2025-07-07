// This section defines ANSI escape sequences for color and style formatting
// as well as size constants for different elements (colors, styles, pixels, characters, and markers).

// ANSI Escape Sequences for Color
const wchar_t ansi_start[] = L"\x1b[";     // Start of ANSI escape sequence
const wchar_t ansi_end[] = L"\x1b[0m";     // End ANSI sequence
const wchar_t new_line[] = L"\n";          // New line character
const wchar_t ansi_fullground[] = L"\x1b[38;"; // Foreground color ANSI sequence
const wchar_t ansi_background[] = L"\x1b[48;"; // Background color ANSI sequence
wchar_t space = L' '; // Space character (used in formatting)

// Element Size Constants (in number of wchar_t)
const size_t color_size_max = 20;          // Max size for color data
const size_t style_size_max = 19;          // Max size for style data
const size_t pixel_size_max = 2 * color_size_max + style_size_max; // Pixel data size (color + style)
const size_t character_size_max = pixel_size_max + 1 + wcslen(ansi_end); // Max size for a character (includes reset)
const size_t marker_size_max = pixel_size_max + 6 + wcslen(ansi_end); // Max size for a marker (includes extra space for marker)

// Utility Variables
size_t size_max = numeric_limits<size_t>::max(); // Max size possible for size_t
