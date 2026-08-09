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
const size_t color_size_max     = 24;                                         // Max size of a color code (RGB: `\x1b[38;2;255;255;255m\0` = 20 wchars; padded for margin so swprintf into Color::code never overshoots, only hit by per-cell RGB cells, e.g. plt.effect)
const size_t style_size_max     = 19;                                         // Max size of a style code
const size_t pixel_size_max     = 2 * color_size_max + style_size_max;        // Pixel size (fg + bg + style)
const size_t character_size_max = pixel_size_max + 1 + wcslen(ansi_end);      // Character size (pixel + 1 char + reset)

// --- Numeric limits ---
const float inf = numeric_limits<float>::infinity();

// --- Sentinel codes ---
const size_t no_color = static_cast<size_t>(-1);   // "no color" sentinel for foreground integer codes, outside the unsigned char range, can never collide with any palette index
