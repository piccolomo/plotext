// Color Management Class: Handles color representation for foreground and background using ANSI escape codes.


class Color {
private:
  wchar_t code[color_size_max]; // Stores the ANSI color code

public:
  // Default constructor: Initializes the color to no color (empty string).
  Color() {clear();}

  // Constructor to set color with a given string color code.
  Color(bool is_fullground, const string & color) {
    clear(); 
    set(is_fullground, color);}

  // Constructor to set color using RGB or single integer code.
  Color(bool is_fullground, bool is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
    clear(); 
    set(is_fullground, is_integer, r, g, b);}

  // Copy constructor (default).
  Color(const Color & c) = default;

  // Move constructor (default).
  Color(Color && c) = default;

  // Checks if two colors have the same code.
  bool same(const Color & c) const {return same_cstrings(code, c.get_code());}

  // Copies the color code from another Color object.
  void copy(const Color & c) {copy_cstring(c.get_code(), code);}

  // Clears the color code (sets it to an empty string).
  void clear() {code[0] = L'\0';}

  // Sets the color using fullground flag, integer flag, and RGB values.
  void set(bool is_fullground, bool is_integer, const unsigned char r = 0, const unsigned char g = 0, const unsigned char b = 0) {
    if (is_fullground) {wcscpy(code, ansi_fullground);} 
    else {wcscpy(code, ansi_background);}
    if (is_integer) {swprintf(code + 5, 7, L"5;%dm", r);} 
    else {swprintf(code + 5, 16, L"2;%d;%d;%dm", r, g, b);}}

  // Sets the color using a string color code (e.g., "red").
  void set(bool is_fullground, const string & color) {
    unsigned char color_code = get_color_code(color);
    if (color_code == 100) {code[0] = L'\0';} 
    else {set(is_fullground, true, color_code);}}

  // Returns the length of the color code.
  size_t get_length() const {return wcslen(code);}

  // Returns the color code (wchar_t array).
  const wchar_t * get_code() const {return code;}

  // Returns true if there is no color set.
  bool no_color() const {return code[0] == L'\0';}

  // Returns true if there is color
  bool has_color() const {return not no_color();}

  // Copies the color code to a buffer, appending it to the current buffer.
  void to_buffer(wchar_t * buffer, size_t & length_buffer) const {
    if (has_color()) {cstring_to_buffer(code, buffer, length_buffer);}}

  // Logs the color to the console.
  void log() const {wcout << code << "color" << ansi_end << endl;}};



// Fullground class: Represents foreground colors.
class Fullground : public Color {
public:
  // Default constructor
  Fullground() = default;

  // Constructor to set color using a string code.
  Fullground(const string & color) : Color(true, color) {}

  // Constructor to set color using a single RGB value.
  Fullground(const unsigned char & r) : Color(true, true, r) {}

  // Constructor to set color using RGB values.
  Fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(true, false, r, g, b) {}

  // Copy constructor (default).
  Fullground(const Fullground & c) = default;

  // Move constructor (default).
  Fullground(Fullground && c) = default;

  // Equality operator to compare two Fullground colors.
  bool operator==(const Fullground & fg) const {return Color::same(fg);}

  // Assignment operator to copy code from another Fullground color.
  Fullground & operator=(const Fullground & fg) {
    Color::copy(fg); 
    return *this;}

  // Set color using RGB values.
  void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) {Color::set(true, false, r, g, b);}

  // Set color using a single integer value.
  void set(const unsigned char & r) {Color::set(true, true, r);}

  // Set color using a string color code.
  void set(const std::string & color) {Color::set(true, color);}
};



// Background class: Represents background colors.
class Background : public Color {
public:
  // Default constructor
  Background() = default;

  // Constructor to set color using a string code.
  Background(const string & color) : Color(false, color) {}

  // Constructor to set color using a single RGB value.
  Background(const unsigned char & r) : Color(false, true, r) {}

  // Constructor to set color using RGB values.
  Background(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(false, false, r, g, b) {}

  // Copy constructor (default).
  Background(const Background & c) = default;

  // Move constructor (default).
  Background(Background && c) = default;

  // Equality operator to compare two Background colors.
  bool operator==(const Background & bg) const {return Color::same(bg);}

  // Assignment operator to copy code from another Background color.
  Background& operator=(const Background & bg) {
    Color::copy(bg); 
    return *this;}

  // Set color using RGB values.
  void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) {Color::set(false, false, r, g, b);}

  // Set color using a single integer value.
  void set(const unsigned char & r) {Color::set(false, true, r);}

  // Set color using a string color code.
  void set(const string & color) {Color::set(false, color);}
};
