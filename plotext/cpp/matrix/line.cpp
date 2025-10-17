class Line {
private:
    CharacterHD * chars = nullptr;  // Pointer to array of CharacterHD
    size_t width = 0;               // Width of the line

public:
    // Constructors
    constexpr Line() noexcept = default;

    explicit Line(const size_t w) noexcept
        : chars(new CharacterHD[w]()), width(w) {}

    Line(const size_t w, const CharacterHD & c) noexcept
        : Line(w) { fill_character(c); }

    Line(const size_t w, const Pixel & p) noexcept
        : Line(w) { fill_pixel(p); }

    Line(const Line & other) {
        create(other.width);
        copy_from(other);}

  // Copy assignment operator.
  Line & operator=(const Line & other) {
    destroy();
    create(other.width);
    copy_from(other);
    return *this;}

  // Equality operator compares character arrays.
  constexpr bool operator==(const Line & s) const noexcept {return width == s.width && memcmp(chars, s.chars, width * sizeof(CharacterHD)) == 0;}

  // Allocate memory for the string and set its width.
  inline void create(const size_t w) noexcept {width = w; chars = new CharacterHD[width];}

  // Release allocated memory.
  inline void destroy() noexcept {delete[] chars; chars = nullptr; width = 0;}

  // Clear the content of the string.
  inline void clear() noexcept {for (size_t i = 0; i < width; i++) {chars[i].clear();}}

    // Resize the string while preserving content.
  void resize(size_t new_width) {
    Line temp(*this);
    destroy();
    create(new_width);
    copy_from(temp);}

  inline void fill_pixel(const Pixel & p = Pixel()) noexcept {
        for (size_t i = 0; i < width; i++) { chars[i].set_pixel(p); }}

  inline void fill_character(const CharacterHD & c) noexcept {
      for (size_t i = 0; i < width; i++) { chars[i] = c; }}

  inline void copy_from(const Line & other) noexcept {
      const size_t n = std::min(width, other.width);
      for (size_t i = 0; i < n; ++i) { chars[i] = other.chars[i]; }}

// Accessors
  constexpr size_t get_width() const noexcept { return width; }
  inline CharacterHD & get_character(const size_t col) const noexcept { return chars[col]; }
  inline wchar_t get_wcharacter(const size_t col) const noexcept { return chars[col].get_wcharacter(); }

    // Checks
  bool is_empty(const size_t start, const size_t end) const noexcept {
      for (size_t col = start; col < end; col++)
          if (!get_character(col).is_empty()) return false;
      return true;}

  constexpr bool different_pixel(const size_t col) const noexcept {return chars[col].different(chars[col - 1]);}

  // Modifiers
  inline void set_character(const size_t col, const CharacterHD & c) noexcept {get_character(col) = c;}



  // Get a part of the string between two positions.
  Line part(const size_t & start, const size_t & stop) const {
    size_t new_width = min(stop - start, width);
    Line s(new_width);
    for (size_t i = 0; i < new_width; i++) {s.chars[i] = chars[start + i];}
    return s;}

  // Overloaded part method for a single stop position.
  Line part(const size_t & stop) const {return part(0, stop);}

  // Returns the width of the canvas
  size_t get_width() const {return width;}

  // Returns the CharacterHD at the specified column
  CharacterHD & get_character(const size_t & col) const {return chars[col];}

  wchar_t get_wcharacter(const size_t & col) const {return chars[col].get_wcharacter();}

  // Check if a range of characters is empty.
  bool is_empty(const size_t & start, const size_t & end) const {
    for (size_t col = start; col < end; col++) {
      if (!get_character(col).is_empty()) {return false;}} return true;}

  // Check if a pixel differs from the previous one.
  bool different_pixel(const size_t & col) const {return chars[col].different(chars[col - 1]);}

  // Inserts a CharacterHD at the specified column
  void set_character(const size_t & col, const CharacterHD & c) {get_character(col) = c;}

  // Insert a wide string at a specific position.
  void insert_wstring(const size_t & col, const wstring & s) {
    size_t length = s.size(); 
    for (size_t i = 0; i < length; i++) {get_character(col + i).set_wcharacter(s[i]);}}

  // Insert a line at a specific position 
  void insert_line(size_t col, const Line & s) {for (size_t i = 0; i < s.get_width(); i++) {chars[col + i] = s.chars[i];}}

  // Insert a string at a specific position with alignment and optional adaptation.
  void insert_line_aligned(size_t col, const Line & s, const Alignment & ha = -1) {
    col += ha.get_displacement(s.get_width()); 
    for (size_t i = 0; i < s.get_width(); i++) {chars[col + i] = s.chars[i];}}

  // Insert a Colorize object with alignment and optional checks.
  bool insert_colorized_aligned(size_t col, const Colorize & s, const Alignment & ha = -1, bool check_space = false, bool change_color = true) {
    size_t length = get_width();
    size_t slength = s.get_length();
    int c = col + ha.get_displacement(slength);
    size_t start = max(0, (int)(c - 1));
    size_t stop = min(length, c + slength + 1);
    if (check_space && (c < 0 || c + slength > length || !is_empty(start, stop))) {return false;}
    for (size_t i = 0; i < slength; i++) {
      get_character(c + i).set_wcharacter(s.get_wcharacter(i));
      if (change_color) {get_character(c + i).set_pixel(s);}}
    return true;}

  // Dynamically insert a Colorize object with alignment.
  int insert_colorized_dynamically(const size_t & col, const Colorize & s) {
    size_t w = s.get_length();
    vector<int> displacements = get_dynamic_displacements(w);
    for (auto delta : displacements) {
      if (insert_colorized_aligned(col + delta, s, 0, true, true)) {return col + delta;}}
    return -1;}


  // Convert the string to a buffer with colors.
  void to_buffer(wchar_t * buffer, size_t & length_buffer) const {
    bool color_seen = false;
    for (size_t col = 0; col < width; col++) {
      bool is_colored = (col == 0) ? !chars[0].no_color() : different_pixel(col);
      color_seen = is_colored || color_seen;
      if (is_colored && col != 0) {cstring_to_buffer(ansi_end, buffer, length_buffer);}
      if (is_colored) {chars[col].pixel_to_buffer(buffer, length_buffer);}
      chars[col].character_to_buffer(buffer, length_buffer);}
    if (color_seen) {cstring_to_buffer(ansi_end, buffer, length_buffer);}}

  // Convert the string to a buffer without colors 
  void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const {
    for (size_t col = 0; col < width; col++) {chars[col].character_to_buffer(buffer, length_buffer);}}

  // Get the string as a wide string 
  wstring get_wstring(const bool colorless = false) const {
    size_t buffer_size = character_size_max * width;
    wchar_t buffer[buffer_size + 1];
    buffer[0] = '\0';
    size_t length = 0;
    if (colorless) {to_colorless_buffer(buffer, length);} else {to_buffer(buffer, length);}
    return wstring(buffer);}

  // Display the string
  void print(const bool colorless = false) const {wcout << get_wstring(colorless) << endl;}
};




  // // Insert a string at a specific position with alignment and optional adaptation.
  // void insert_string_aligned(size_t col, const String & s, const Alignment & ha = -1) {
  //   size_t s_width = s.get_width(); 
  //   col += ha.get_displacement(s_width);
  //   if (col < 0 or col + s_width > width or col >= width) {return;}
  //   for (size_t i = 0; i < s_width; i++) {get_character(col + i) = s.get_character(i);}}

  // // Insert a Colorize object with alignment and optional checks.
  // bool insert_colorized_aligned(size_t col, const Colorize & s, const Alignment & ha = -1, bool check_space = false, bool change_color = true) {
  //   size_t length = get_width();
  //   size_t slength = s.get_length();
  //   int c = col + ha.get_displacement(slength);
  //   size_t start = max(0, (int)(c - 1));
  //   size_t stop = min(length, c + slength + 1);
  //   if (check_space && (c < 0 || c + slength > length || !is_empty(start, stop))) {return false;}
  //   for (size_t i = 0; i < slength; i++) {
  //     get_character(c + i).set_char(s.get_char(i));
  //     if (change_color) {get_character(c + i).set_pixel(s);}}
  //   return true;}



  // // Converts the canvas into a String by extracting characters from each CharacterHD
  // String get_line() const {
  //   String s(width);
  //   for (size_t i = 0; i < width; i++) {
  //     s.set_char(i, chars[i].get_character());}
  //   return s;}