class Character : public Pixel {
private:
  wchar_t c = space;

public: 
  inline Character() noexcept = default;
  inline Character(const wchar_t & cn) noexcept : c(cn), Pixel() {}
  inline Character(const wchar_t & cn, const Pixel & p) noexcept : c(cn), Pixel(p) {}

  inline Character(const Character & p) noexcept : Pixel(p), c(p.c) {}
  inline Character(Character && p) noexcept : Pixel(move(p)), c(p.c) {}
  
  inline Character & operator=(const Character & cn) noexcept {c = cn.c; Pixel::operator=(cn); return *this;}
  
  inline void clear() noexcept  {c = L' '; Pixel::clear();};
  
  inline constexpr void set_char(const wchar_t & cs) noexcept {c = cs;}
  inline void set_pixel(const Pixel & p) noexcept {Pixel::operator=(p);}

  inline constexpr virtual wchar_t get_char() const noexcept {return c;}
  
  inline bool different_pixel(const Character & cn) const noexcept {return not Pixel::operator==(cn);}
  inline bool same_pixel(const Character & c) const noexcept {return Pixel::operator==(c);}
  inline constexpr bool is_empty() const noexcept {return c == L' ';}

  inline void pixel_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {Pixel::to_buffer(buffer, length_buffer);}
  inline void character_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {wchar_to_buffer(c, buffer, length_buffer);}
  virtual inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    pixel_to_buffer(buffer, length_buffer);
    character_to_buffer(buffer, length_buffer);
    cstring_to_buffer(ansi_end, buffer, length_buffer);}
  
  inline void log() const noexcept {
    wchar_t buffer[character_size_max + 1]; buffer[0] = '\0';  size_t length = 0;
    to_buffer(buffer, length);
    wcout << buffer;}
};