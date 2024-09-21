class String {
private:
    Character * chars;
    size_t width;

public:
  inline String() noexcept : chars(nullptr), width(0) {}
  inline String(const size_t & w) noexcept {create(w);}
  inline String(const size_t & w, const Character & c) noexcept : String(w) {fill_character(c);}
  inline String(const size_t & w, const Pixel & p) noexcept : String(w, Character(space, p)) {}
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
  inline bool is_empty(const size_t & start, const size_t & end) const noexcept {for (size_t col = start; col < end; col++){if (not get_character(col).is_empty()) {return false;}} return true;}
 
  inline constexpr void fill_character(const Character & c = Character()) noexcept {for (size_t i = 0; i < width; i++) {chars[i] = c;}}
  inline constexpr void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t i = 0; i < width; i++) {chars[i].set_pixel(p);}}

  inline void resize(size_t width) noexcept {String temp(*this); destroy(); create(width); copy_from(temp);}

  inline bool insert(size_t col, const String & s, const Alignment & ha = -1, bool adapt = false) noexcept {
    col += ha.get_displacement(s.get_width());
    if (adapt and (col < 0 or col > get_width())) {return false;}
    size_t length = min(s.get_width(), get_length() - col);
    for (size_t i = 0; i < length; i++) {get_character(col + i) = s.get_character(i);} return true;}

  inline int insert_dynamically(const size_t & col, const wstring & s) noexcept {
    size_t w = s.size(); vector<int> displacements = get_dynamic_displacements(w);
    for (auto delta: displacements) {if (insert_aligned(col + delta, Colorize(s), 0, 1, 0)) {return col + delta;}} return -1;}

  inline bool insert_aligned(size_t col, const Colorize & s, const Alignment & ha = -1, bool check_space = false, bool change_color = true) noexcept {
    size_t length = get_length(); size_t slength = s.get_length(); col += ha.get_displacement(slength);
    if (check_space and (col < 0 or col + slength > length)) {return false;}
    if (check_space and not is_empty(max(0, (int)(col - 1)), min(length, col + slength + 1))) {return false;}
    for (size_t i = 0; i < slength; i++) {get_character(col + i).set_char(s.get_char(i)); if (change_color) {get_character(col + i).set_pixel(s);}} return true;}

  inline void insert_wstring(const size_t & col, const wstring & s) noexcept {
    size_t length = s.size(); for (size_t i = 0; i < length; i++) {get_character(col + i).set_char(s[i]);}}

  inline void set_char(const size_t & col, const Character & c) noexcept {get_character(col) = c;}

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

    //inline String(const wstring & str, const Pixel & p = Pixel()) noexcept : String(str.size()) {for (size_t i = 0; i < width; i++) {chars[i] = Character(str[i], p);}}
  // inline bool insert_colorize(size_t col, const Colorize & c, const Alignment & ha, bool check_space = false) noexcept {
  //   col += ha.get_displacement(c.get_length());
  //   if (check_space and not is_empty(col, col + c.get_length())) {return false;}
  //   for (size_t i = 0; i < c.get_length(); i++) {chars[col + i].set_pixel(c); chars[col + i].set_char(c.get_char(i));} return true;}

  // inline bool insert_colorize_dynamically(const size_t & col, const Colorize & s) noexcept {
  //   size_t w = s.get_length(); vector<int> displacements = get_dynamic_displacements(w);
  //   for(auto delta: displacements){if (insert_colorize(col + delta, s, -1, 1)) {return true;}} return false;}

  // inline void insert(const size_t & col, const StringTemplate & s, const HA & ha) noexcept {insert(col + ha.get_displacement(s.get_width()), s);}

