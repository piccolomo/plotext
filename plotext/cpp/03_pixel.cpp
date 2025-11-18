// Pixel class manages a combination of Fullground, Background, and Style, representing a pixel with color and style properties.

class Pixel : public Fullground, public Background, public Style {

public:
  // Default constructor
  constexpr Pixel() = default;

  // Constructor with Fullground, Background, and Style
  Pixel(const Fullground & fg, const Background & bg = Background(), const Style & st = Style()) : Fullground(fg), Background(bg), Style(st) {}

  // Constructor with string-based Fullground, Background, and Style
  Pixel(const string & fg, const string & bg = "", const string & st = "") : Fullground(fg), Background(bg), Style(st) {}

  // Copy constructor
  Pixel(const Pixel & p) : Fullground(p), Background(p), Style(p) {}

  // Move constructor
  Pixel(Pixel && p) : Fullground(move(p)), Background(move(p)), Style(move(p)) {}

  // Assignment operator
  Pixel & operator=(const Pixel & p) {
    Fullground::operator=(p);
    Background::operator=(p);
    Style::operator=(p);
    return *this;}

  // Equality operator
  bool operator==(const Pixel & p) const {
    return Fullground::operator==(p) && Background::operator==(p) && Style::operator==(p);}

  // Inequality operator
  bool operator!=(const Pixel & p) const {return !(*this == p);}

  // Clears all color and style properties
  void clear() {Fullground::clear(); Background::clear(); Style::clear();}

  // Set Fullground color (RGB)
  void set_fullground(const unsigned char & r, const unsigned char & g, const unsigned char  & b) {Fullground::set(r, g, b);}

  // Set Fullground color (single value)
  void set_fullground(const unsigned char & r) {Fullground::set(r);}

  // Set Fullground color (string)
  void set_fullground(const string & color) {Fullground::set(color);}

  // Set Background color (RGB)
  void set_background(const unsigned char & r, const unsigned char & g, const unsigned char & b) {Background::set(r, g, b);}

  // Set Background color (single value)
  void set_background(const unsigned char & r) {Background::set(r);}

  // Set Background color (string)
  void set_background(string color) {Background::set(color);}

  // Set Style
  void set_style(const string style) {Style::set(style);}

  // Set Fullground, Background, and Style using strings
  void set(const string & fs, const string & bs = "", const string & ss = "") {
    Fullground::set(fs); Background::set(bs); Style::set(ss);}

  // Copy the entire pixel (Fullground, Background, and Style)
  void copy_pixel(const Pixel & p) noexcept {*this = p;}

  // Copy only the Fullground of a pixel
  void copy_fullground(const Pixel & p) noexcept {Fullground::operator=(p);}

  // Copy only the Background of a pixel
  void copy_background(const Pixel & p) noexcept {Background::operator=(p);}

  // Fix background for all dots using the given Pixel.
  void fix_background(const Pixel & pixel) noexcept {if (no_background()) {copy_background(pixel);}}
  void fix_fullground(const Pixel & pixel) noexcept {if (no_fullground()) {copy_fullground(pixel);}}

  void fix(const Pixel & pixel) noexcept {fix_background(pixel); fix_fullground(pixel);}

  // Check if Fullground color is not set
  bool no_fullground() const noexcept {return Fullground::no_color();}

  // Check if Background color is not set
  bool no_background() const noexcept {return Background::no_color();}

  // Check if Style is not set
  bool no_style() const noexcept {return Style::no_style();}

  // Check if no color or style is set (Fullground, Background, Style)
  bool no_color() const noexcept {return no_fullground() && no_background() && no_style();}
  bool has_color() const noexcept {return ! no_color();}

  // Get the total length of the pixel (Fullground, Background, and Style)
  size_t get_length() const noexcept {return Fullground::get_length() + Background::get_length() + Style::get_length();}

  inline const unsigned char get_fullground_integer_code() const noexcept {return Fullground::get_integer_code();}


  // Copy the pixel data to a buffer
  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    Fullground::to_buffer(buffer, length_buffer);
    Background::to_buffer(buffer, length_buffer);
    Style::to_buffer(buffer, length_buffer);}

  // inline void stream_fullground_code() const noexcept {return wcout<<Fullground::get_code();}
  // inline const wchar_t * get_background_code() const noexcept {return Background::get_code();}
  // inline const wchar_t * get_style_code() const noexcept {return Style::get_code();}

  const wchar_t * get_code() const noexcept {
    wchar_t * buffer = new wchar_t[pixel_size_max + 1];
    buffer[0] = '\0'; 
    size_t length = 0; 
    to_buffer(buffer, length); return buffer;}

  void show_code() const {show_ansi_wstring(get_code());}

  // Get the marker as a wide string
  wstring get_wstring() const {
      wchar_t buffer[character_size_max + 5] = {L'\0'}; // Buffer for rendering 
      size_t length = 0;
      to_buffer(buffer, length);
      cstring_to_buffer(L"Pixel", buffer, length);
      if (has_color()){cstring_to_buffer(ansi_end, buffer, length);}
      return wstring(buffer);}

  // Log the pixel information
  void print() const {wcout << get_wstring();}

  inline void stream() const {Fullground::stream(); Background::stream(); Style::stream();} 


};

// A white pixel with no Fullground and a white Background
//Pixel white_pixel = Pixel("", "white");

extern "C" {
  Pixel * pixel_new() noexcept {return new Pixel();}
  void pixel_delete(Pixel * p) noexcept {delete p;}
  void pixel_set_fullground_integer(Pixel * p, size_t r) noexcept {p->set_fullground(r);}
  void pixel_set_fullground_rgb(Pixel * p, size_t r, size_t g, size_t b) noexcept {p->set_fullground(r, g, b);}
  void pixel_set_fullground_code(Pixel * p, char * code) noexcept {p->set_fullground(code);}
  void pixel_set_background_integer(Pixel * p, size_t r) noexcept {p->set_background(r);}
  void pixel_set_background_rgb(Pixel * p, size_t r, size_t g, size_t  b) noexcept {p->set_background(r, g, b);}
  void pixel_set_background_code(Pixel * p, char * code) noexcept {p->set_background(code);}
  bool pixel_no_background(const Pixel * p) noexcept {return p->no_background();}
  void pixel_copy_background(Pixel * p, Pixel * p2) noexcept {p->copy_background(*p2);}
  void pixel_copy_pixel(Pixel * p, Pixel * p2) noexcept {p->copy_pixel(*p2);}
  void pixel_fix_background(Pixel * p, Pixel * pixel) noexcept {p->fix_background(*pixel);}
  void pixel_fix(Pixel * p, Pixel * pixel) noexcept {p->fix(*pixel);}
  void pixel_set_style_code(Pixel * p, char * code) noexcept {p->set_style(code);}
  void pixel_print(const Pixel * p) noexcept {p->print();}
  const wchar_t * pixel_get_wstring(const Pixel * c) noexcept {return wstring_to_cstring(c->get_wstring());}
  Pixel * pixel_copy(const Pixel * c) noexcept {return new Pixel(*c);}
  unsigned char pixel_get_code(const Pixel * c) noexcept {return c->get_fullground_integer_code();}
}