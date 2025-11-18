// Classes to manage mappings of dots to grid positions (rows and columns).

class PointsMap : public Vector<size_t> {
  size_t cols;
  size_t rows;
  size_t length = 0;

public:
  PointsMap(const size_t & cols, const size_t & rows) {this->resize(cols, rows);}

  void clear() {fill(0); length = 0;}

  size_t get_location(const size_t & col, const size_t & row) const {return row * cols + col;}

  size_t get_col(const size_t & location) const {return location % cols;}
  size_t get_row(const size_t & location) const {return location / cols;}

  size_t get_cols() const {return cols;}
  size_t get_rows() const {return rows;}
  size_t get_size() const {return cols * rows;}
  
  size_t get_length() const {return length;}

  void resize(const size_t & cols, const size_t & rows) {this->cols = cols; this->rows = rows; Vector<size_t>::reserve(rows * cols); Vector<size_t>::set_length(rows * cols); fill(0);}  
  void set_index(const size_t & location, const size_t & index) {at(location) = index + 1; length += 1;}
  void set_index(const size_t & col, const size_t & row, const size_t & index) {set_index(get_location(col, row), index);}

  //size_t at2(const size_t & col, const size_t & row) const {return at(get_location(col, row));} //temp

  size_t get_index(const size_t & location) const {return at(location) - 1;}
  size_t get_index(const size_t & col, const size_t & row) const {return get_index(get_location(col, row));}

  bool is_empty(const size_t & index) const {return at(index) == 0;}
  bool is_present(const size_t & index) const {return not is_empty(index);}

  bool is_empty(const size_t & col, const size_t & row) const {return is_empty(get_location(col, row));}
  bool is_present(const size_t & col, const size_t & row) const {return not is_empty(col, row);}

  // // Count how many indices have been encoded (non-empty slots)
  // size_t count() const {
  //   size_t count = 0;
  //   for (size_t i = 0; i < get_length(); ++i) {if (is_present(i)) ++count;}
  //   return count;}

  void log() const {
    wcout << "PointsMap " << cols << " x " << rows << " length " << length << " [";
    for (size_t l = 0; l < Vector<size_t>::get_length(); l++) {
      if(is_present(l)) {wcout << L"(" << get_col(l) << L", " << get_row(l) << L": " << get_index(l) << L") ";}}
    wcout<< "]" << endl << flush;}

};


extern "C" {

  typedef PointsMap * PointsMapHandle;

  PointsMapHandle points_map_new(size_t cols, size_t rows) {return new PointsMap(cols, rows);}

  void points_map_delete(PointsMapHandle handle) {delete handle;}

  void points_map_clear(PointsMapHandle handle) {handle->clear();}

  void points_map_resize(PointsMapHandle handle, size_t cols, size_t rows) {handle->resize(cols, rows);}

  void points_map_log(PointsMapHandle handle) {handle->log();}

  size_t points_map_get_length(PointsMapHandle handle) {return handle->get_length();}


} 



// class DotMap {
// private:
//   size_t index; // Index in the dot map.
//   size_t row;   // Row associated with this dot.

// public:
//   DotMap() = default;

//   // Constructor to initialize a DotMap with row and index.
//   DotMap(const size_t & r, const size_t & i) : row(r), index(i) {}

//   // Equality operator to compare DotMap objects by index.
//   bool operator==(const DotMap & ei) {return ei.index == index;}

//   // Set the index of the dot.
//   void set_index(const size_t & i) {index = i;}

//   // Get the current index of the dot.
//   size_t get_index() const {return index;}

//   // Get the row of the dot.
//   size_t get_row() const {return row;}

//   // Log the dot map details.
//   void log() const {wcout << "(row " << row << ", index " << get_index() << ")";}

// };


// class ColMap : public Vector<DotMap> {
// private:
//   size_t col;            // Column associated with the dot map.

// public:

//   // Constructor to initialize ColMap with a column.
//   ColMap(const size_t & rows = 0) : col(size_max), Vector<DotMap>(rows) {}

//   // Constructor to initialize ColMap with column, row, and index.
//   ColMap(const size_t & col, const size_t & row, const size_t & index) : ColMap(col) {emplace_back(move(DotMap(row, index)));}

//   // Equality operator to compare ColMap objects by column.
//   bool operator==(const ColMap & cm) {return col == cm.col;} 

//   // Get the number of rows in this column map.
//   //size_t get_length() const {return map.get_length();}

//   // Get the column associated with this ColMap.
//   size_t get_col() const {return col;}

//   // Get the map index of a specific row.
//   size_t get_map_index(const size_t & row) {
//     size_t length = get_length();
//     for (size_t j = 0; j < length; j++) {
//       if (at(j).get_row() == row) {return j;}}
//     return size_max;}

//   // Get the dot index for a specific row.
//   size_t get_index(const size_t & row) {
//     size_t map_index = get_map_index(row);
//     if (map_index != size_max) {return at(map_index).get_index();}
//     return size_max;}

//   // Add or update the index for a specific row.
//   void add_index(const size_t & row, const size_t & index) {
//     size_t map_index = get_map_index(row);
//     if (map_index != size_max) {at(map_index).set_index(index);}
//     else {emplace_back(move(DotMap(row, index)));}}

//   // Log the column map details.
//   void log() const {
//     wcout << "[col " << col << " ";
//     for (const auto & d : *this) {d.log();}
//     wcout << "]";}
// };


// class PointsMap : Vector<ColMap> {

// public:
//   DotsMap(const size_t & cols, const size_t & rows) : Vector<ColMap>(cols) {
//         for (size_t c = 0; c < cols; ++c)
//             at(c).reserve(rows);}

//   // Get the map index for a specific column.
//   size_t get_map_index(const size_t & col) {
//     size_t length = get_length();
//     for (size_t j = 0; j < length; j++) {
//       if (at(j).get_col() == col) {return j;}}
//     return size_max;}

//   // Get the dot index for a specific column and row.
//   size_t get_index(const size_t & col, const size_t & row) {
//     size_t map_index = get_map_index(col);
//     if (map_index != size_max) {return at(map_index).get_index(row);}
//     return size_max;}

//   // Add or update the dot index for a specific column and row.
//   void add_index(const size_t & col, const size_t & row, const size_t & index) {
//     size_t map_index = get_map_index(col);
//     if (map_index != size_max) {at(map_index).add_index(row, index);}
//     else {emplace_back(move(ColMap(col, row, index)));}}

//   // Log the entire dot map.
//   void log() const {for (const auto &r : *this) {r.log();}}
// };

