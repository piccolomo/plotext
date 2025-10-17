// Color Management Class: Handles color representation for foreground and background using ANSI escape codes.

class Color {
private:
    wchar_t code[color_size_max]; // Stores the ANSI color code
    size_t length = 0;       // Cache the length of the color code

public:
    constexpr Color() noexcept : code{}, length(0) {}

    Color(bool is_fullground, const string & color) { clear(); set(is_fullground, color); }

    Color(bool is_fullground, bool is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
        clear();
        set(is_fullground, is_integer, r, g, b);}

    Color(const Color & c) = default;
    Color(Color && c) = default;

    bool same(const Color & c) const { return length == c.length and same_cstrings(code, c.get_code(), c.length); }

    void copy(const Color & c) { 
        copy_cstring(c.get_code(), code, c.length);
        length = c.length; }

    void clear() { code[0] = L'\0'; length = 0; }

    void update_length() {length = wcslen(code);}

     // Sets the color using fullground flag, integer flag, and RGB values.
    void set(bool is_fullground, bool is_integer, const unsigned char r = 0, const unsigned char g = 0, const unsigned char b = 0) {
      if (is_fullground) {wcscpy(code, ansi_fullground);} 
      else {wcscpy(code, ansi_background);}
      if (is_integer) {swprintf(code + 5, 7, L"5;%dm", r);} 
      else {swprintf(code + 5, 16, L"2;%d;%d;%dm", r, g, b);}
      update_length();
    }

    // Sets the color using a string color code (e.g., "red").
    void set(bool is_fullground, const string & color) {
      unsigned char color_code = get_color_code(color);
      if (color_code == 100) {code[0] = L'\0'; length = 0;} 
      else {set(is_fullground, true, color_code);}}


    size_t get_length() const { return length; }
    const wchar_t * get_code() const { return code; }
    bool no_color() const { return length == 0; }
    bool has_color() const { return length != 0; }

    // Optimized to_buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (has_color()) {cstring_to_buffer(code, length, buffer, length_buffer); }}

    void log() const { wcout << code << L"color" << ansi_end << endl; }

    inline void stream() const {wcout.write(code, length);} 
};


// Fullground class: Represents foreground colors.
class Fullground : public Color {
public:
  // Default constructor
  constexpr Fullground() = default;

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
  constexpr Background() = default;

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
