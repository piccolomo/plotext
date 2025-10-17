// Class to represent a matrix of DotBit objects, inheriting from FillInfo.

class MatrixBool {
private:
  uint8_t bits = 0; // Stores all bits (max 3x3 = 9 bits)
  size_t rows = 1;
  size_t cols = 1;

public:
  // Constructor with variable size (max 3x3)
  MatrixBool(size_t c = 1, size_t r = 1) noexcept : cols(c), rows(r), bits(0) {}

  MatrixBool(const MatrixBool & other) noexcept = default;
  MatrixBool & operator=(const MatrixBool & other) noexcept = default;

  // Set the size (resets the matrix)
  void set_size(const size_t & new_cols, const size_t & new_rows) noexcept {
    cols = new_cols;
    rows = new_rows;}

  void zero() noexcept { bits = 0; }

  // void set(const size_t & col, const size_t & row, const bool & value) noexcept {
  //   size_t bitIndex = get_index(col, row);       // Flatten 2D position to a single bit index
  //   uint8_t mask = 1 << bitIndex;           // Create a mask for that bit = 2 ** bitIndex

  //   if (value) {bits |= mask;}   // Set the bit to 1 (enable the dot)
  //   else {bits &= ~mask;}}


    void set(size_t col, size_t row, bool value) noexcept {
        uint8_t mask = 1 << get_index(col, row);
        bits = value ? (bits | mask) : (bits & ~mask);}

  void enable(const size_t & col, const size_t & row) noexcept { set(col, row, true); }
  void disable(const size_t & col, const size_t & row) noexcept { set(col, row, false); }

  // Getters
  constexpr size_t get_cols() const noexcept { return cols; }
  constexpr size_t get_rows() const noexcept { return rows; }
  //constexpr size_t get_last_index() const noexcept { return rows * cols ; }

  constexpr size_t get_index(const size_t & col, const size_t & row) const noexcept {return (rows * cols - 1) - (row * cols + col);} 

  constexpr size_t get_col(const size_t & index) const noexcept {return cols - 1 - index % cols;} 
  constexpr size_t get_row(const size_t & index) const noexcept {return (cols * rows - 1 - index) % cols;} 
  
  // Get bit state
  //bool get(const size_t & col, const size_t & row) const noexcept {return (bits >> get_index(col, row)) & 1;}
  bool get(size_t col, size_t row) const noexcept {return bits & (1 << get_index(col, row));}
  
  // Add a dot using float coordinates (fractional)
  void add_dot(const float & col, const float & row) noexcept {
      //size_t c = size_t(cols * (col - floor(col)));
      //size_t r = size_t(rows * (row - floor(row)));
      enable(col, row);}

  // Sum another matrix (OR operation)
  void sum(const MatrixBool & other) noexcept {bits |= other.bits;}

  // Get a code representing the matrix
  uint8_t get_code() const noexcept {return bits; }

  wstring get_wstring() const {
    wostringstream log;
    for (size_t r = 0; r < rows; ++r) {
      for (size_t c = 0; c < cols; ++c) {log << (get(c, r) ? L"1" : L"0");}
        if (r < rows - 1) {log << " ";}}
        return log.str();}

  void log() const {
    // Logs the point to standard output
    wcout << get_wstring() << flush;}

      // Copy the size (rows and cols) from another matrix
  void copy_size(const MatrixBool & ch) noexcept {
      rows = ch.rows;
      cols = ch.cols;}

  // Copy the bit content (code) from another matrix
  void copy_code(const MatrixBool & ch) noexcept {
      bits = ch.bits;}

        // Copy the bit content (code) from another matrix
  void copy(const MatrixBool & ch) noexcept {copy_size(ch); copy_code(ch);}

};



// class MatrixBool {
// public:
//   bool ** matrix = nullptr;  // 2D array of DotBit objects representing the dot matrix.
//   size_t cols, rows; // Dimensions of the matrix (columns and rows).

// public:

//   // Constructor to initialize the matrix with specified columns and rows.
//   MatrixBool(const size_t & cols = 1, const size_t & rows = 1) noexcept {
//     set_size(cols, rows); 
//     create_matrix();}  // Create the matrix with the given size.
  
//   // Destructor to clean up the dynamically allocated matrix.
//   ~MatrixBool() noexcept {
//     clear_matrix(); 
//     matrix = nullptr;}  // Set the matrix pointer to nullptr.
  
//   // Copy constructor to initialize a new MatrixBool from another.
//   MatrixBool(const MatrixBool & c) noexcept {
//     copy_size(c); 
//     create_matrix(); 
//     copy_matrix(c);}  // Copy matrix content.
  
//   // Assignment operator to copy content from another MatrixBool.
//   MatrixBool & operator=(const MatrixBool & c) noexcept {
//     clear_matrix(); 
//     copy_size(c); 
//     create_matrix(); 
//     copy_matrix(c); 
//     return *this;}

//   // Dynamically allocate memory for the matrix.
//   void create_matrix() noexcept {
//     if (rows == 0) {matrix = nullptr;}
//     matrix = new bool*[rows];
//     for (size_t r = 0; r < rows; r++) {matrix[r] = new bool[cols]{false};}}

//   // Deallocate memory for the matrix.
//   void clear_matrix() noexcept { 
//     for (size_t r = 0; r < rows; r++) {delete[] matrix[r];} 
//     delete[] matrix;}

//   // Set the size of the matrix (columns and rows).
//   void set_size(const size_t & cols, const size_t & rows) noexcept { 
//     this->cols = cols; 
//     this->rows = rows;}

//   void zero() noexcept {
//     clear_matrix();
//     set_size(0, 0);
//     create_matrix();}

//   // Set the dot state for the matrix element at (col, row).
//   constexpr void set(const size_t & col, const size_t & row, const bool & d) noexcept {matrix[row][col] = d;}
//   constexpr void enable(const size_t & col, const size_t & row) noexcept {set(col, row, true);}
//   constexpr void disable(const size_t & col, const size_t & row) noexcept {set(col, row, false);}

//   // Set matrix state using a code.
//   void set_code(const size_t & number) noexcept {
//     for (size_t r = 0; r < rows; r++) {
//       for (size_t c = 0; c < cols; c++) {
//         set(r, c, get_bit(number, get_bit_position(c, r, cols, rows)));}}}


//   // Get the number of columns in the matrix.
//   size_t get_cols() const noexcept {return cols;}

//   // Get the number of rows in the matrix.
//   size_t get_rows() const noexcept {return rows;}

//   // Get the dot state for the matrix element at (col, row).
//   bool get(const size_t & col, const size_t & row) const noexcept {return matrix[row][col];}

//   // Get a code representing the matrix (as a single byte).
//   unsigned char get_code() const noexcept { 
//     size_t result = 0; 
//     for (size_t r = 0; r < rows; r++) {
//       for (size_t c = 0; c < cols; c++) {
//         result <<= 1; 
//         result |= (matrix[r][c] ? 1 : 0);}} // Set result bit based on dot state.
//     return result;}

//   // Copy the size (columns and rows) from another MatrixBool.
//   void copy_size(const MatrixBool & ch) { 
//     set_size(ch.get_cols(), ch.get_rows());}

//   // Copy the matrix content from another MatrixBool.
//   void copy_matrix(const MatrixBool & ch) { 
//     for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.matrix[r][c];}}}

//   // Sum two matrices by performing the logical OR operation on each element.
//   void sum(const MatrixBool & ch) { 
//     for (size_t r = 0; r < rows; r++) {
//       for (size_t c = 0; c < cols; c++) {
//         matrix[r][c] = (matrix[r][c] | ch.matrix[r][c]);}}}

//   // Add a dot to the matrix at the specified (col, row) position.
//   void add_dot(const float & col, const float & row) noexcept {
//     size_t c = get_cols() * (col - floor(col));  // Calculate column based on fractional part.
//     size_t r = get_rows() * (row - floor(row));  // Calculate row based on fractional part.
//     //wcout<< col << " " << c << endl;
//     enable(c, r);}  // Enable the dot.
  
//   wstring get_wstring() const {
//     wostringstream log;
//     for (size_t i = 0; i < rows; ++i) {
//       for (size_t j = 0; j < cols; ++j) {log << (matrix[i][j] ? "1" : "0");}
//         if (i < rows - 1) {log << " ";}
//             //log << "\n";
//             } // Newline after each row
//         return log.str();}

//   void log() const {
//     // Logs the point to standard output
//     wcout << get_wstring() << flush;}

// };



// class DotMatrix : public FillInfo {
// private:
//   DotBit ** matrix;
//   size_t cols, rows;

// public:
//   inline DotMatrix(const size_t cols, const size_t rows) noexcept : FillInfo() {set_size(cols, rows); create_matrix();}
//   inline DotMatrix(const Point & p) noexcept : DotMatrix(p.get_cols(), p.get_rows()) {if (p.is_not_normal()) {add_dot(p.get_x(), p.get_y(), p);} FillInfo::operator=(p);}
//   inline ~DotMatrix() noexcept {clear_matrix(); matrix = nullptr;}

//   inline DotMatrix(const DotMatrix & c) noexcept : FillInfo(c) {copy_size(c); create_matrix(); copy_matrix(c);}
//   inline DotMatrix & operator=(const DotMatrix & c) noexcept {clear_matrix(); copy_size(c); create_matrix(); copy_matrix(c); return *this;}

//   inline void set_size(const size_t & cols, const size_t & rows) noexcept {this->cols = cols; this->rows = rows;}
//   inline void create_matrix() noexcept {matrix = new DotBit * [rows]; for (size_t r = 0; r < rows; r++) {matrix[r] = new DotBit[cols];}}
//   inline void clear_matrix() noexcept {for (size_t r = 0; r < rows; r++) {delete [] matrix[r];} delete [] matrix;}
//   void copy_size(const DotMatrix & ch) {set_size(ch.get_cols(), ch.get_rows());}
//   void copy_matrix(const DotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = ch.matrix[r][c];}}}
//   void sum(const DotMatrix & ch) {for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {matrix[r][c] = (matrix[r][c] | ch.matrix[r][c]);}}}

//   //nline void set_matrix(const size_t & col, const size_t & row, const DotBit & di) noexcept {matrix[row][col] = di;}

//   inline void add_dot(const float & col, const float & row, const FillInfo & fi) noexcept {
//     size_t c = get_cols() * (col - floor(col));
//     size_t r = get_rows() * (row - floor(row));
//     matrix[r][c] = matrix[r][c] | fi;
//     matrix[r][c].enable_dot();}

//   //inline void update_fill(const FillInfo & fi) noexcept {FillInfo::operator|(fi);}

//   inline constexpr size_t get_cols() const noexcept {return cols;}
//   inline constexpr size_t get_rows() const noexcept {return rows;}

//   inline constexpr bool get_matrix_dot(const size_t & col, const size_t & row) const noexcept {return matrix[row][col].get_dot();}

//   //inline MiniDotMatrix get_mini_dot_matrix() const noexcept {MiniDotMatrix out(cols, rows); out.copy_matrix(*this); return out;}

//   inline unsigned char get_code() const noexcept {size_t result = 0; for (size_t r = 0; r < rows; r++) {for (size_t c = 0; c < cols; c++) {result <<= 1; result |= (matrix[r][c].get_dot() ? 1 : 0);}} return result;}

//   inline void reverse_row(const size_t & row) noexcept {for (size_t c = 0; c < cols / 2; c++) {swap(matrix[row][c], matrix[row][cols - 1 - c]);}}
//   inline void reverse_col(const size_t & col) noexcept {for (size_t r = 0; r < rows / 2; r++) {swap(matrix[r][col], matrix[rows - 1 - r][col]);}}
//   inline void reverse_rows() noexcept {for (size_t r = 0; r < get_rows(); r++) {reverse_row(r);}}
//   inline void reverse_cols() noexcept {for (size_t c = 0; c < get_cols(); c++) {reverse_col(c);}}

//   inline void fill_row(const size_t & row) noexcept {bool seen = false; for (size_t c = 0; c < cols; c++) {if (seen) {matrix[row][c].enable_dot();} else {seen |= (matrix[row][c].get_dot() and matrix[row][c].get_filly());}}}
//   inline void fill_rows(const bool & forward = true) noexcept {if (not forward) {reverse_rows();} for (size_t r = 0; r < rows; r++) {fill_row(r);} if (not forward) {reverse_rows();}}

//   inline void fill_col(const size_t & col) noexcept {bool seen = false; for (size_t r = 0; r < rows; r++) {if (seen) {matrix[r][col].enable_dot();} else {seen |= (matrix[r][col].get_dot() and matrix[r][col].get_fillx());}}}
//   inline void fill_cols(const bool forward = true) noexcept {if (not forward) {reverse_cols();} for (size_t r = 0; r < rows; r++) {fill_col(r);} if (not forward) {reverse_cols();}}
// 	};

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



  // Reverse the elements of a specific row.
  // void reverse_row(const size_t& row) noexcept { 
  //   for (size_t c = 0; c < cols / 2; c++) {
  //     swap(matrix[row][c], matrix[row][cols - 1 - c]);}}  // Swap elements.

  // // Reverse the elements of a specific column.
  // void reverse_col(const size_t& col) noexcept { 
  //   for (size_t r = 0; r < rows / 2; r++) {
  //     swap(matrix[r][col], matrix[rows - 1 - r][col]);  // Swap elements.
  //   }
  // }

  // // Reverse all rows in the matrix.
  // void reverse_rows() noexcept { 
  //   for (size_t r = 0; r < get_rows(); r++) {
  //     reverse_row(r);  // Reverse individual row.
  //   }
  // }

  // // Reverse all columns in the matrix.
  // void reverse_cols() noexcept { 
  //   for (size_t c = 0; c < get_cols(); c++) {
  //     reverse_col(c);  // Reverse individual column.
  //   }
  // }

  // // Fill a specific row based on the current dot state.
  // void fill_row(const size_t& row) noexcept { 
  //   bool seen = false; 
  //   for (size_t c = 0; c < cols; c++) {
  //     if (seen) { 
  //       matrix[row][c].enable_dot();  // Enable dot if seen before.
  //     } else { 
  //       seen |= (matrix[row][c].get_dot() and matrix[row][c].get_filly());  // Check if fillable.
  //     }
  //   } 
  // }

  // // Fill all rows in the matrix (optional reverse order).
  // void fill_rows(const bool& forward = true) noexcept { 
  //   if (not forward) {
  //     reverse_rows();  // Reverse rows if not in forward order.
  //   } 
  //   for (size_t r = 0; r < rows; r++) {
  //     fill_row(r);  // Fill each row.
  //   } 
  //   if (not forward) {
  //     reverse_rows();  // Reverse rows back to original order.
  //   }
  // }

  // // Fill a specific column based on the current dot state.
  // void fill_col(const size_t& col) noexcept { 
  //   bool seen = false; 
  //   for (size_t r = 0; r < rows; r++) {
  //     if (seen) { 
  //       matrix[r][col].enable_dot();  // Enable dot if seen before.
  //     } else { 
  //       seen |= (matrix[r][col].get_dot() and matrix[r][col].get_fillx());  // Check if fillable.
  //     }
  //   } 
  // }

  // // Fill all columns in the matrix (optional reverse order).
  // void fill_cols(const bool forward = true) noexcept { 
  //   if (not forward) {
  //     reverse_cols();  // Reverse columns if not in forward order.
  //   } 
  //   for (size_t r = 0; r < rows; r++) {
  //     fill_col(r);  // Fill each column.
  //   } 
  //   if (not forward) {
  //     reverse_cols();  // Reverse columns back to original order.
  //   }
  // }

  // // Method to log the current state of the object (in this case, matrix state or other data).
  // void log() const noexcept {
  //     wchar_t buffer[character_size_max + 1];  // Buffer to store the string representation.
  //     buffer[0] = '\0';  // Initialize buffer with null character.
  //     size_t length = 0;
  //     to_buffer(buffer, length);  // Convert data to buffer format.
  //     wcout << buffer;}  // Output the buffer to the console.