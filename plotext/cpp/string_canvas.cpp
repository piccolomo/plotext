class StringCanvas {
private:
    CharacterCanvas * chars;
    size_t width;

public:
  inline StringCanvas() noexcept : chars(nullptr), width(0) {}
  inline StringCanvas(const size_t & w) noexcept: chars(new CharacterCanvas[w]), width(w) {}
  inline StringCanvas(const size_t & w, const CharacterCanvas & c) noexcept: StringCanvas(w) {fill_character(c);}
  inline StringCanvas(const size_t & w, const Pixel & p) noexcept: StringCanvas(w) {fill_pixel(p);}
  inline ~StringCanvas() noexcept {delete [] chars; chars = nullptr;}

  inline constexpr size_t get_width() const noexcept {return width;}
  inline CharacterCanvas & get_character(const size_t & col) const noexcept {return chars[col];}
  inline String get_string() noexcept {String s(width); for (size_t i = 0; i < width; i++) {s.set_char(i, chars[i].get_character());} return s;}

  inline constexpr void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t i = 0; i < width; i++) {chars[i].set_pixel(p);}}
  inline constexpr void fill_character(const CharacterCanvas & c) noexcept {for (size_t i = 0; i < width; i++) {chars[i] = c;}}

  inline void insert(const size_t & col, const CharacterCanvas & c) noexcept {get_character(col) = c;}
  //inline void insert(const size_t & col, const StringCanvas & s) noexcept {for (size_t i = 0; i < s.get_width(); i++) {chars[col + i] = s.get_character(i);}}
};

  //inline bool operator==(const StringCanvas & s) const noexcept {return memcmp(chars, &(s.get_character(0)), width * sizeof(Character)) == 0;}
  //inline constexpr void clear() noexcept {for (size_t i = 0; i < width; i++) {chars[i].clear();}}