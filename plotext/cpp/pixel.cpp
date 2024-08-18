class Pixel : public Fullground, public Background, public Style {

public:
  inline Pixel() noexcept = default;
  inline Pixel(const Fullground & fg, const Background & bg = Background(), const Style & st = Style()) noexcept : Fullground(fg), Background(bg), Style(st) {}
  inline Pixel(const string & fg, const string & bg = "", const string & st = "") noexcept : Fullground(fg), Background(bg), Style(st) {}

 
  inline Pixel & operator=(const Pixel & p) noexcept {Fullground::operator=(p); Background::operator=(p); Style::operator=(p); return *this;}
  inline bool operator==(const Pixel & p) const noexcept {return Fullground::operator==(p) and Background::operator==(p) and Style::operator==(p);}
  inline bool operator!=(const Pixel & p) const noexcept {return not (*this == p);}

  inline constexpr void clear() noexcept {Fullground::clear(); Background::clear(); Style::clear(); };

  inline void set_fullground(const size_t & r, const size_t & g, const size_t & b) noexcept {Fullground::set(r, g, b);}
  inline void set_fullground(const size_t & r) noexcept {Fullground::set(r);}
  inline void set_fullground(string color) noexcept {Fullground::set(color);}
  
  inline void set_background(const size_t & r, const size_t & g, const size_t & bs) noexcept {Background::set(r, g, bs);}
  inline void set_background(const size_t & r) noexcept {Background::set(r);}
  inline void set_background(string color) noexcept {Background::set(color);}

  inline void set_style(const string style) noexcept {Style::set(style);}

  inline void set(const string & fs, const string & bs = "", const string & ss = "") noexcept  {Fullground::set(fs); Background::set(bs); Style::set(ss);}

  inline void copy_pixel(const Pixel & p) noexcept {operator=(p);}

  inline constexpr bool no_fullground() noexcept {return Fullground::no_color();}
  inline constexpr bool no_background() noexcept {return Background::no_color();}
  inline constexpr bool no_style() noexcept {return Style::no_style();}
  inline constexpr bool no_color() noexcept {return no_fullground() and no_background() and no_style();}

  inline const size_t get_length() const noexcept {return Fullground::get_length() + Background::get_length() + Style::get_length();}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    Fullground::to_buffer(buffer, length_buffer);
    Background::to_buffer(buffer, length_buffer);
    Style::to_buffer(buffer, length_buffer);}
  
  inline void log() const noexcept {
    wchar_t buffer[pixel_size_max + 1]; buffer[0] = '\0'; size_t length = 0;
    to_buffer(buffer, length);
    wcout << buffer << L"pixel" << ansi_end << endl;}
};
