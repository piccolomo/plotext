// Color Manipulation Functions

// These functions are used for manipulating ANSI color codes and style codes, 
// which are typically used in terminal environments to control the color and styling of text. 


// Color Manipulation 

// Add an integer-based ANSI color to the buffer.
inline void add_color_integer_ansi(wchar_t * buffer, const unsigned char & r) {
    swprintf(buffer, 7, L"5;%dm", r);}

// Add an RGB-based ANSI color to the buffer.
inline void add_color_rgb_ansi(wchar_t * buffer, const unsigned char & r, const unsigned char & g, const unsigned char & b) {
    swprintf(buffer, 16, L"2;%d;%d;%dm", r, g, b);}

// Add an ANSI color (integer or RGB) to the buffer based on the color type.
inline void add_color_ansi(wchar_t *buffer, const bool & is_fullground, const bool & is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
    if (is_fullground) {wcscpy(buffer, ansi_fullground);} 
        else {wcscpy(buffer, ansi_background);}
    if (is_integer) {add_color_integer_ansi(buffer + 5, r);} 
        else {add_color_rgb_ansi(buffer + 5, r, g, b);}}

// Add a color code to the buffer.
inline void add_color_code(wchar_t *buffer, const bool & is_fullground, const string & color) {
    unsigned char code = get_color_code(color);
    if (code == 100) {buffer[0] = L'\0';} 
    else {add_color_ansi(buffer, is_fullground, true, code);}}


// Style

inline vector<size_t> get_style_codes(const string & style){
  vector<size_t> codes;
  vector<string> styles = split_string(style, string(" "));
  for(const string & style : styles) {
    unsigned char code = get_style_code(style);
    if (code != 100){codes.push_back(code);}} return codes;}

inline void add_style_code(wchar_t * buffer, const string & style){
  vector<size_t> codes = get_style_codes(style);
  if(codes.size() != 0){wcscpy(buffer, ansi_start);}
  for(const size_t & code : codes) {swprintf(buffer + wcslen(buffer), 3, L"%d;", code);}
  if(codes.size() != 0){
    size_t len = wcslen(buffer);
    buffer[len - 1] = L'm';
    buffer[len] = L'\0';}}
