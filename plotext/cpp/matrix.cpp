class Matrix {
private:
  String * strings; 
  size_t height;

public:
  inline Matrix(const size_t & w, const size_t & h, const Character & c = Character()) noexcept {create(h); create_strings(w, c);}
  inline Matrix(const size_t & w, const size_t & h, const Pixel & p) noexcept : Matrix(w, h, Character(space, p)) {}
  inline ~Matrix() noexcept {destroy();}

  inline Matrix(const Matrix & other) {create(other.height); copy_from(other);}
  inline Matrix & operator=(const Matrix & other) {destroy(); create(other.height); copy_from(other); return *this;}

  inline void create(const size_t & h) noexcept {height = h; strings = new String[height];}
  inline void create_strings(const size_t & w, const Character & c) noexcept {for (int row = 0; row < height; row++) {String * address = &strings[row]; new(address) String(w, c);}}
  inline void destroy() noexcept {delete [] strings; strings = nullptr;}
  inline void copy_from(const Matrix & other) noexcept {for (size_t i = 0; i < min(height, other.height); ++i) {strings[i] = other.strings[i];}}
  inline constexpr void clear(){for (size_t row = 0; row < height; row ++){strings[row].clear();}}

  inline size_t get_length() const noexcept {size_t size = 0; for(size_t row = 0; row < height; row++){size += get_wstring().size();} return size;}
  inline constexpr String & get_string(const size_t & row) const noexcept {return strings[row];}
  inline constexpr Character & get_character(const size_t & col, const size_t & row) const noexcept {return get_string(row).get_character(col);}
  inline constexpr size_t get_height() const {return height;}
  inline constexpr size_t get_width() const {if (height == 0){return 0;} else {return strings[0].get_width();}}
  inline bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept {for (size_t row = row_start; row < row_stop; row++){if (not get_string(row).is_empty(col_start, col_stop)) {return false;};} return true;}

  inline constexpr void fill_character(const Character & c = Character()) noexcept {for (size_t row = 0; row < height; row++){strings[row].fill_character(c);}}
  inline constexpr void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t row = 0; row < height; row++){strings[row].fill_pixel(p);}}
  inline void resize(const size_t & width, const size_t & height) noexcept {
    for (size_t row = 0; row < min(height, get_height()); row++){strings[row].resize(width);}
    Matrix temp(*this);
    destroy(); create(height); copy_from(temp);}
   
  inline bool insert(size_t col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1, const bool adapt = false) noexcept {
    row += va.get_displacement(m.get_height());
    for (size_t r = 0; r < m.get_height(); r++) {if (not get_string(row + r).insert(col, m.get_string(r), ha, adapt)) {return false;}} return true;}

  inline void insert_string(const size_t & col, const size_t & row, const String & s) noexcept {get_string(row).insert(col, s);} 

  inline int insert_dynamically(const size_t & col, const size_t & row, const wstring & s) noexcept {return get_string(row).insert_dynamically(col, s);}

  inline bool insert_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, bool check_space = false, bool change_color = true) noexcept {return get_string(row).insert_aligned(col, s, ha, check_space, change_color);}

  inline void insert_wstring(const size_t & col, const size_t & row, const wstring & s) noexcept {get_string(row).insert_wstring(col, s);}

  inline void set_char(const size_t & col, const size_t & row, const wchar_t & cs) noexcept {get_character(col, row).set_char(cs);} 
  

  // inline void insert(const size_t & col, const size_t & row, const Matrix & m) noexcept {for (size_t r = 0; r < m.get_height(); r++){strings[row + r].insert(col, m.get_string(r));}}

  // inline void insert(size_t col, size_t row, const Matrix & m, const bool & adapt) noexcept {if (not adapt) {insert(col, row, m);} else if (col < get_width() and row < get_height()) {insert(col, row, m.part(min(m.get_width(), get_width() - col), min(m.get_height(), get_height() - row)));}}
  
  inline Matrix vstack(const Matrix & m, const bool & adapt = false) noexcept {
    size_t width; if (adapt) {width = max(get_width(), m.get_width());} else {width = get_width();}
    Matrix out(width, get_height() + m.get_height());
    out.insert(0, 0, *this);
    out.insert(0, get_height(), m); return out;}

  inline Matrix hstack(const Matrix & m, const bool & adapt = false) noexcept {
    size_t height; if (adapt) {height = max(get_height(), m.get_height());} else {height = get_height();}
    Matrix out(get_width() + m.get_width(), height);
    out.insert(0, 0, *this);
    out.insert(get_width(), 0, m); return out;}

  inline Matrix copy() const {return Matrix(*this);}
  inline Matrix part(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept {
    size_t new_height = min(row_stop - row_start, height);
    size_t new_width = min(col_stop - col_start, get_width());
    Matrix m(new_width, new_height); for (size_t row = 0; row < new_height; row++) {m.get_string(row) = get_string(row_start + row).part(col_start, col_stop);} return m;}
  inline Matrix part(const size_t col_stop, const size_t row_stop) const noexcept {return part(0, col_stop, 0, row_stop);}
  inline Matrix transpose() const noexcept {
    size_t width = get_width();
    Matrix novel(height, width);
    for (size_t col = 0; col < height; col++){for (size_t row = 0; row < width; row ++){novel.get_character(col, row).operator=(get_character(row, col));}}
    return novel;}
    
  inline void to_buffer(wchar_t * buffer, size_t & length_buffer, const bool & colorless = false) const noexcept {
    for(size_t row = 0; row < height; row++){
      if (colorless) {strings[row].to_colorless_buffer(buffer, length_buffer);} else {strings[row].to_buffer(buffer, length_buffer);}
      if(row != height - 1){cstring_to_buffer(new_line, buffer, length_buffer);}}}

  inline wstring get_wstring(const bool & colorless = false) const noexcept {
      size_t buffer_size = character_size_max * get_width() * height + height;
      wchar_t buffer[buffer_size + 1]; buffer[0] = '\0'; size_t length = 0;
      to_buffer(buffer, length, colorless);
      wstring out(buffer);
      return out;}

  inline void show(const bool & colorless = false) const noexcept {wcout << get_wstring(colorless) << flush;}
};


  inline Matrix colorize_to_matrix(const Colorize & c) noexcept {
    vector<wstring> wstrings = split_string(c.get_string(), wstring(new_line));
    size_t width = get_width_strings(wstrings);
    size_t height = wstrings.size();
    Matrix out(width, height);
    for (size_t row = 0; row < height; row++) {
      wstring s = wstrings.at(row); 
      Colorize cs(s, c); 
      //s.resize(width, L' ');
      out.insert_aligned(0, row, cs, -1, 0, 1);}
      return out;}


  //line void insert(const size_t & col, const size_t & row, const Matrix & m, const HA & ha, const VA & va = -1, const bool & flexible = false) {insert(col + ha.get_displacement(m.get_width()), row + va.get_displacement(m.get_height()), m, flexible);}
  // inline void insert(const size_t & col, const size_t & row, const MatrixTemplate & m, const HA & ha, const VA & va = -1, const bool & flexible = false) {insert(col + ha.get_displacement(m.get_width()), row + va.get_displacement(m.get_height()), m, flexible);}
  // inline void insert_dynamic(const size_t & col, const size_t & row, const  StringTemplate<T> & s) noexcept {strings[row].insert_dynamic(col, s);}
