// Class to represent the position of a dot in a grid with row and column.

class DotPosition {
private:
  size_t col, row; // The column and row of the dot.

public:
  // Default constructor initializes col and row to 0.
  DotPosition() noexcept {col = 0; row = 0;}

  // Constructor initializing with specific column and row values.
  DotPosition(const size_t & col, const size_t & row) noexcept : col(col), row(row) {}

  // Constructor that initializes DotPosition from a Point object.
  DotPosition(const Point & p) noexcept : DotPosition(p.get_col(), p.get_row()) {}

  // Assignment operator to copy the values from another DotPosition.
  DotPosition & operator=(const DotPosition& d) noexcept {
    col = d.col; 
    row = d.row; 
    return *this;}

  // Sets the row value.
  void set_row(const float& el) {row = el;}

  // Sets the column value.
  void set_col(const float& el) {col = el;}

  // Returns the column value.
  size_t get_col() const noexcept {return col;}

  // Returns the row value.
  size_t get_row() const noexcept {return row;}


  wstring get_wstring() const { 
    // Returns a wide string representation of the point
    wostringstream woss; 
    woss << fixed << setprecision(3) << get_col() << L", " << get_row(); 
    return woss.str();}
  // Logs the position (col, row) to standard output.

  void log() const {wcout << get_wstring() << flush;} // Logs the point to standard output

};