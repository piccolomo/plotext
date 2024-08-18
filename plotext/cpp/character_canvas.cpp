class CharacterCanvas: public Marker {
private:
  DotInfo ** matrix;

public:
  inline CharacterCanvas(const Marker & m = Marker()) noexcept : Marker(m) {create_matrix();}
  inline ~CharacterCanvas() noexcept {clear_matrix(); matrix = nullptr;}
  inline CharacterCanvas(const CharacterCanvas & c) : Marker(c) {create_matrix(); copy_matrix(c);}

  inline CharacterCanvas & operator=(const CharacterCanvas & c) noexcept {clear_matrix(); Marker::operator=(c); create_matrix(); copy_matrix(c); return *this;}

  inline void create_matrix() noexcept {size_t rows = get_rows(); size_t cols = get_cols(); matrix = new DotInfo * [rows]; for (size_t r = 0; r < rows; r++) {matrix[r] = new DotInfo[cols];} set_matrix_from_code(0);}
  inline void clear_matrix() noexcept {size_t rows = get_rows(); for (size_t r = 0; r < rows; r++) {delete [] matrix[r];} delete [] matrix;}
  void copy_matrix(const CharacterCanvas & ch) {size_t rows = get_rows(); size_t cols = get_cols(); for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.matrix[r][c];}}}
  void sum_matrix(const CharacterCanvas & ch) {size_t rows = get_rows(); size_t cols = get_cols(); for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = matrix[r][c] | ch.matrix[r][c];}}}

  inline constexpr void set_matrix(const size_t & col, const size_t & row, const DotInfo & di) noexcept {matrix[row][col] = di;}
  inline constexpr void set_matrix_dot(const size_t & col, const size_t & row, const bool & d) noexcept {matrix[row][col].set_dot(d);}
  inline void set_matrix_from_code(const size_t & number) noexcept {size_t rows = get_rows(); size_t cols = get_cols();for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {set_matrix_dot(r, c, get_bit(number, get_bit_position(c, r, cols, rows)));}}}

  inline constexpr bool get_matrix_dot(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_dot();}
  inline constexpr bool get_matrix_fillx(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_fillx();}
  inline constexpr bool get_matrix_filly(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_filly();}
  inline unsigned char get_code_from_matrix() const noexcept {size_t rows = get_rows(); size_t cols = get_cols(); size_t result = 0; for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {result <<= 1; result |= (get_matrix_dot(c, r) ? 1 : 0);}} return result;}
  inline wchar_t get_char() const noexcept override {if (is_normal()) {return Marker::get_char();} else {return get_marker_converter(get_type())(get_code_from_matrix());}}
  inline Character get_character() const noexcept {return Character(get_char(), *this);}
  inline bool get_fillx() const noexcept {bool seen = false; for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {seen = seen or get_matrix_fillx(c, r);}} return seen;}
  inline bool get_filly() const noexcept {bool seen = false; for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {seen = seen or get_matrix_filly(c, r);}} return seen;}
  inline bool get_fill(const bool & xaxis = 1) const noexcept {if (xaxis) {return get_fillx();} else {return get_filly();}}

  inline void add_dot(const float & col, const float & row, const FillInfo & fi = {0, 0}) noexcept {
    size_t c = get_cols() * (col - floor(col));
    size_t r = get_rows() * (row - floor(row));
    DotInfo di = matrix[r][c] | fi; di.set_dot(1);
    set_matrix(c, r, di);}

  inline void reverse_row(const size_t & row) noexcept {size_t cols = get_cols(); for (size_t c = 0; c < cols / 2; c++) {swap(matrix[row][c], matrix[row][cols - 1 - c]);}}
  inline void reverse_col(const size_t & col) noexcept {size_t rows = get_rows(); for (size_t r = 0; r < rows / 2; r++) {swap(matrix[r][col], matrix[rows - 1 - r][col]);}}

  inline void fill_row(const size_t & row) noexcept {bool seen_one = false; for (size_t c = 0; c < get_cols(); c++) {if (seen_one) {set_matrix_dot(c, row, true);} else {seen_one |= get_matrix_dot(c, row) and get_matrix_filly(c, row);}}}
  inline void reverse_rows() noexcept {for (size_t r = 0; r < get_rows(); r++) {reverse_row(r);}}
  inline void fill_rows(const bool & forward = true) noexcept {if(not forward) {reverse_rows();} for (size_t r = 0; r < get_rows(); r++) {fill_row(r);} if(not forward) {reverse_rows();}}

  inline void fill_col(const size_t & col) noexcept {bool seen_one = false; for (size_t r = 0; r < get_rows(); r++) {if (seen_one) {set_matrix_dot(col, r, true);} else {seen_one |= (get_matrix_dot(col, r) and get_matrix_fillx(col, r));}}}
  inline void reverse_cols() noexcept {for (size_t c = 0; c < get_cols(); c++) {reverse_col(c);}}
  inline void fill_cols(const bool forward = true) noexcept {if(not forward) {reverse_cols();} for (size_t r = 0; r < get_rows(); r++) {fill_col(r);} if(not forward) {reverse_cols();}}

  inline void character_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {wchar_to_buffer(get_char(), buffer, length_buffer);}
  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override {
      pixel_to_buffer(buffer, length_buffer);
      character_to_buffer(buffer, length_buffer);
      cstring_to_buffer(ansi_end, buffer, length_buffer);}
  inline void log_fillx() const noexcept {for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {wcout << get_matrix_fillx(c, r) << " ";} wcout << endl;}}
  inline void log_filly() const noexcept {for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {wcout << get_matrix_filly(c, r) << " ";} wcout << endl;}}
  inline void log() const noexcept {
      wchar_t buffer[character_size_max + 1]; buffer[0] = '\0';  size_t length = 0;
      to_buffer(buffer, length);
      wcout << buffer;}
	};

  // inline void set_type(const MarkerType & t) noexcept {
  //   auto type_old = get_type();
  //   if (type_old != t) {clear_matrix();} 
  //   Marker::set_type(t); 
  //   if (type_old != t) {create_matrix();} 
  // }