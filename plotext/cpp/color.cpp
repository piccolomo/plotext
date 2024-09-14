class Color {
private:
  wchar_t code [color_size_max];

public:
  inline Color() noexcept {clear();};
  inline Color(const bool & is_fullground, const string & color) noexcept {clear(); set(is_fullground, color);}
  inline Color(const bool & is_fullground, const bool & is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) noexcept {clear(); set(is_fullground, is_integer, r, g, b);}
  
  inline constexpr Color(const Color & c) noexcept = default;
  inline constexpr Color(Color && c) noexcept = default;

  inline bool same_code(const Color & c) const noexcept {return same_cstrings(code, c.get_code());}
  inline void copy_code(const Color & c) noexcept {copy_cstring(c.get_code(), code);}
  
  inline constexpr void clear() noexcept {code[0] = L'\0';}
  inline void set(const bool & is_fullground, const bool & is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0){add_color_ansi(code, is_fullground, is_integer, r, g, b);}
  inline void set(const bool & is_fullground, const string & color){add_color_code(code, is_fullground, color);}

  inline const size_t get_length() const noexcept {return wcslen(code);}
  inline constexpr const wchar_t * get_code() const noexcept {return code;}
  inline constexpr bool no_color() const noexcept {return code[0] == L'\0';}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {if(not no_color()) {cstring_to_buffer(code, buffer, length_buffer);}}
  inline void log() const noexcept {wcout << code << "color" << ansi_end << endl;}
};



class Fullground : public Color{
public:
  inline Fullground() noexcept = default;
  inline Fullground(const string & color) noexcept : Color(true, color) {}
  inline Fullground(const unsigned char & r) noexcept : Color(true, true, r) {}
  inline Fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept : Color(true, false, r, g, b) {}
    
  inline constexpr Fullground(const Fullground & c) noexcept = default;
  inline constexpr Fullground(Fullground && c) noexcept = default;
  inline bool operator==(const Fullground & fg) const noexcept {return Color::same_code(fg);}
  inline Fullground & operator=(const Fullground & fg) noexcept {Color::copy_code(fg); return *this;}

  inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b){Color::set(true, false, r, g, b);}
  inline void set(const unsigned char & r){Color::set(true, true, r);}
  inline void set(const string & color){Color::set(true, color);}
 };



class Background : public Color {
public:
  inline Background() noexcept = default;
  inline Background(const string & color) noexcept : Color(false, color) {}
  inline Background(const unsigned char & r) noexcept : Color(false, true, r) {}
  inline Background(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept : Color(false, false, r, g, b) {}
  
  inline constexpr Background(const Background & c) noexcept = default;
  inline constexpr Background(Background && c) noexcept = default;
  inline bool operator==(const Background & bg) const noexcept {return Color::same_code(bg);}
  inline Background & operator=(const Background & bg) noexcept {Color::copy_code(bg); return *this;}

  inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b){Color::set(false, false, r, g, b);}
  inline void set(const unsigned char & r){Color::set(false, true, r);}
  inline void set(const string & color){Color::set(false, color);}
};
