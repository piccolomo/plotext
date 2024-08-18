// Color

const wchar_t ansi_start[] = L"\x1b[";
const wchar_t ansi_end[] = L"\x1b[0m";
const wchar_t new_line[] = L"\n";
const wchar_t ansi_fullground[] = L"\x1b[38;";
const wchar_t ansi_background[] = L"\x1b[48;";


// Elements Size (number of wchar_t)
const size_t color_size_max = 20;
const size_t style_size_max = 19;
const size_t pixel_size_max = 2 * color_size_max + style_size_max;
const size_t character_size_max = pixel_size_max + 1 + wcslen(ansi_end);
const size_t marker_size_max = pixel_size_max + 6 + wcslen(ansi_end);

// Other
size_t size_max = numeric_limits<size_t>::max();
wchar_t space = L' ';
