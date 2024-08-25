class MiniDotMatrix {
private:
  bool ** matrix;
  size_t cols, rows;

public:
  inline MiniDotMatrix(const size_t cols, const size_t rows) noexcept : cols(cols), rows(rows) {create_matrix();}
  inline ~MiniDotMatrix() noexcept {clear_matrix(); matrix = nullptr;}
  inline MiniDotMatrix(const MiniDotMatrix & c) {create_matrix(); copy_matrix(c);}
  inline MiniDotMatrix & operator=(const MiniDotMatrix & c) noexcept {clear_matrix(); copy_size(c); create_matrix(); copy_matrix(c); return *this;}

  inline void set_size(const size_t & cols, const size_t & rows) noexcept {this->cols = cols; this->rows = rows;}
  inline void create_matrix() noexcept {matrix = new bool * [rows]; for (size_t r = 0; r < rows; r++) {matrix[r] = new bool[cols];} set_code(0);}
  inline void clear_matrix() noexcept {for (size_t r = 0; r < rows; r++) {delete [] matrix[r];} delete [] matrix;}
  void copy_size(const MiniDotMatrix & ch) {set_size(ch.get_cols(), ch.get_rows());}
  void copy_matrix(const MiniDotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.matrix[r][c];}}}
  void copy_matrix(const DotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.get_matrix_dot(c, r);}}}
  void sum(const MiniDotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = matrix[r][c] | ch.matrix[r][c];}}}

  inline constexpr void set_matrix(const size_t & col, const size_t & row, const bool & d) noexcept {matrix[row][col] = d;}
  inline void set_code(const size_t & number) noexcept {size_t rows = get_rows(); size_t cols = get_cols();for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {set_matrix(r, c, get_bit(number, get_bit_position(c, r, cols, rows)));}}}

  inline constexpr size_t get_cols() const noexcept {return cols;}
  inline constexpr size_t get_rows() const noexcept {return rows;}

  //inline constexpr bool get_matrix(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_dot();}
  inline unsigned char get_code() const noexcept {size_t rows = get_rows(); size_t cols = get_cols(); size_t result = 0; for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {result <<= 1; result |= (matrix[r][c] ? 1 : 0);}} return result;}

  inline void add_dot(const float & col, const float & row) noexcept {
    size_t c = get_cols() * (col - floor(col));
    size_t r = get_rows() * (row - floor(row));
    set_matrix(c, r, 1);}

	};