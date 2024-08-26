class DotMatrix : public FillInfo {
private:
  DotInfo ** matrix;
  size_t cols, rows;

public:
  inline DotMatrix(const size_t cols, const size_t rows) noexcept : FillInfo() {set_size(cols, rows); create_matrix();}
  inline DotMatrix(const Point & p) noexcept : DotMatrix(p.get_cols(), p.get_rows()) {if (p.is_not_normal()) {add_dot(p.get_x(), p.get_y(), p);} FillInfo::operator=(p);}
  inline ~DotMatrix() noexcept {clear_matrix(); matrix = nullptr;}

  inline DotMatrix(const DotMatrix & c) noexcept : FillInfo(c) {copy_size(c); create_matrix(); copy_matrix(c);}
  inline DotMatrix & operator=(const DotMatrix & c) noexcept {clear_matrix(); copy_size(c); create_matrix(); copy_matrix(c); return *this;}

  inline void set_size(const size_t & cols, const size_t & rows) noexcept {this->cols = cols; this->rows = rows;}
  inline void create_matrix() noexcept {matrix = new DotInfo * [rows]; for (size_t r = 0; r < rows; r++) {matrix[r] = new DotInfo[cols];}}
  inline void clear_matrix() noexcept {for (size_t r = 0; r < rows; r++) {delete [] matrix[r];} delete [] matrix;}
  void copy_size(const DotMatrix & ch) {set_size(ch.get_cols(), ch.get_rows());}
  void copy_matrix(const DotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.matrix[r][c];}}}
  void sum(const DotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = (matrix[r][c] | ch.matrix[r][c]);}}}

  //nline void set_matrix(const size_t & col, const size_t & row, const DotInfo & di) noexcept {matrix[row][col] = di;}

  inline void add_dot(const float & col, const float & row, const FillInfo & fi) noexcept {
    size_t c = get_cols() * (col - floor(col));
    size_t r = get_rows() * (row - floor(row));
    matrix[r][c] = matrix[r][c] | fi;
    matrix[r][c].enable_dot();}

  //inline void update_fill(const FillInfo & fi) noexcept {FillInfo::operator|(fi);}

  inline constexpr size_t get_cols() const noexcept {return cols;}
  inline constexpr size_t get_rows() const noexcept {return rows;}

  inline constexpr bool get_matrix_dot(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_dot();}

  //inline MiniDotMatrix get_mini_dot_matrix() const noexcept {MiniDotMatrix out(cols, rows); out.copy_matrix(*this); return out;}

  inline unsigned char get_code() const noexcept {size_t result = 0; for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {result <<= 1; result |= (matrix[r][c].get_dot() ? 1 : 0);}} return result;}

  inline void reverse_row(const size_t & row) noexcept {for (size_t c = 0; c < cols / 2; c++) {swap(matrix[row][c], matrix[row][cols - 1 - c]);}}
  inline void reverse_col(const size_t & col) noexcept {for (size_t r = 0; r < rows / 2; r++) {swap(matrix[r][col], matrix[rows - 1 - r][col]);}}
  inline void reverse_rows() noexcept {for (size_t r = 0; r < get_rows(); r++) {reverse_row(r);}}
  inline void reverse_cols() noexcept {for (size_t c = 0; c < get_cols(); c++) {reverse_col(c);}}

  inline void fill_row(const size_t & row) noexcept {bool seen = false; for (size_t c = 0; c < cols; c++) {if (seen) {matrix[row][c].enable_dot();} else {seen |= (matrix[row][c].get_dot() and matrix[row][c].get_filly());}}}
  inline void fill_rows(const bool & forward = true) noexcept {if (not forward) {reverse_rows();} for (size_t r = 0; r < rows; r++) {fill_row(r);} if (not forward) {reverse_rows();}}

  inline void fill_col(const size_t & col) noexcept {bool seen = false; for (size_t r = 0; r < rows; r++) {if (seen) {matrix[r][col].enable_dot();} else {seen |= (matrix[r][col].get_dot() and matrix[r][col].get_fillx());}}}
  inline void fill_cols(const bool forward = true) noexcept {if (not forward) {reverse_cols();} for (size_t r = 0; r < rows; r++) {fill_col(r);} if (not forward) {reverse_cols();}}
	};
  // inline void log() const noexcept {
  //     wchar_t buffer[character_size_max + 1]; buffer[0] = '\0';  size_t length = 0;
  //     to_buffer(buffer, length);
  //     wcout << buffer;}

  // inline void set_type(const MarkerType & t) noexcept {
  //   auto type_old = get_type();
  //   if (type_old != t) {clear_matrix();} 
  //   Marker::set_type(t); 
  //   if (type_old != t) {create_matrix();} 
  // }

    // inline constexpr bool get_matrix(const size_t & col, const size_t & row) const noexcept {return matrix[row][col];}
  // inline constexpr bool get_matrix_fillx(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_fillx();}
  // inline constexpr bool get_matrix_filly(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_filly();}

  //  inline bool get_fillx() const noexcept {bool seen = false; for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {seen = seen or matrix[r][c].get_fillx();}} return seen;}
  // inline bool get_filly() const noexcept {bool seen = false; for (size_t r = 0; r < get_rows(); r++) {for (size_t c = 0; c < get_cols(); c++) {seen = seen or matrix[r][c].get_filly();}} return seen;}