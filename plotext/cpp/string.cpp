class String {
private:
    Character * chars;
    size_t width;

public:
  inline String() noexcept : chars(nullptr), width(0) {}
  inline String(const size_t & w) noexcept {create(w);}
  inline String(const size_t & w, const Character & c) noexcept : String(w) {fill_character(c);}
  inline String(const size_t & w, const Pixel & p) noexcept : String(w, Character(space, p)) {}
  inline String(const wstring & str, const Pixel & p = Pixel()) noexcept : String(str.size()) {for (size_t i = 0; i < width; i++) {chars[i] = Character(str[i], p);}}
  inline ~String() noexcept {destroy();}
  
  inline String(const String & other) {create(other.width); copy_from(other);}
  inline String & operator=(const String & other) {destroy(); create(other.width); copy_from(other); return *this;}
  inline bool operator==(const String & s) const noexcept {return memcmp(chars, &(s.get_character(0)), width * sizeof(Character)) == 0;}

  inline void create(const size_t & w) noexcept {width = w; chars = new Character[width];}
  inline void destroy() noexcept {delete [] chars; chars = nullptr;}
  inline void copy_from(const String & other) noexcept {for (size_t i = 0; i < min(width, other.width); ++i) {chars[i] = other.chars[i];}}
  inline constexpr void clear() noexcept {for (size_t i = 0; i < width; i++) {chars[i].clear();}}

  inline size_t get_length() const noexcept {return get_string().size();}
  inline constexpr Character & get_character(const size_t & col) const noexcept {return chars[col]; }
  inline constexpr size_t get_width() const noexcept {return width;}

  inline bool different_pixel(const size_t & col) const noexcept {return chars[col].different_pixel(chars[col - 1]);}
  inline bool is_empty(const size_t & start, const size_t & end) const noexcept {bool res = true; for (size_t col = start; col < end; col++){res = res and get_character(col).is_empty();} return res;}
 
  inline constexpr void fill_character(const Character & c = Character()) noexcept {for (size_t i = 0; i < width; i++) {chars[i] = c;}}
  inline constexpr void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t i = 0; i < width; i++) {chars[i].set_pixel(p);}}

  inline void resize(size_t width) noexcept {
    String temp(*this);
    destroy(); create(width); copy_from(temp);
  }  
  
  inline void insert(const size_t & col, const Character & c) noexcept {chars[col] = c;}
  inline void insert(const size_t & col, const String & s) noexcept {for (size_t i = 0; i < s.get_width(); i++) {chars[col + i] = s.get_character(i);}}

  inline String part(const size_t & start, const size_t & stop) const noexcept {size_t new_width = min(stop - start, width); String s(new_width); for (size_t i = 0; i < new_width; i++) {s.get_character(i) = get_character(start + i);} return s;}
  inline String part(const size_t & stop) const noexcept {return part(0, stop);}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    bool color_seen = false;
    for(size_t col = 0; col < width; col++){
      bool is_colored;
      if (col == 0){is_colored = not chars[0].no_color();} else {is_colored = different_pixel(col);}
      color_seen = is_colored or color_seen;
      if (is_colored and col != 0) {cstring_to_buffer(ansi_end, buffer, length_buffer);}
      if (is_colored) {chars[col].pixel_to_buffer(buffer, length_buffer);}
      chars[col].character_to_buffer(buffer, length_buffer);}
    if(color_seen){cstring_to_buffer(ansi_end, buffer, length_buffer);}}  
  inline void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {for(size_t col = 0; col < width; col++){chars[col].character_to_buffer(buffer, length_buffer);}}   
  
  inline wstring get_string() const noexcept {
    size_t buffer_size = character_size_max * width;
    wchar_t buffer[buffer_size + 1]; buffer[0] = '\0'; size_t length = 0;
    to_buffer(buffer, length);
    wstring out(buffer);
    return out;}

  inline void show() const noexcept {wcout << get_string() << endl;}
};

  
  // inline void insert(const size_t & col, const StringTemplate & s, const HA & ha) noexcept {insert(col + ha.get_displacement(s.get_width()), s);}
  // inline void insert_dynamic(const size_t & col, const StringTemplate & s) noexcept {
  //   size_t w = s.get_width(); int c; HA la(-1); vector<int> displacements = get_dynamic_displacements(w);
  // for(const int & displacement: displacements){c = col + displacement; if (c >= 0 and c + w - 1 < width and is_empty(c, c + w)){insert(c, s, la); break;}}}
