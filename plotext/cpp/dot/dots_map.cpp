// Classes to manage mappings of dots to grid positions (rows and columns).

class DotMap {
private:
  size_t index; // Index in the dot map.
  size_t row;   // Row associated with this dot.

public:
  // Constructor to initialize a DotMap with row and index.
  DotMap(const size_t & r, const size_t & i) : row(r), index(i) {}

  // Equality operator to compare DotMap objects by index.
  bool operator==(const DotMap & ei) {return ei.index == index;}

  // Set the index of the dot.
  void set_index(const size_t & i) {index = i;}

  // Get the current index of the dot.
  size_t get_index() const {return index;}

  // Get the row of the dot.
  size_t get_row() const {return row;}

  // Log the dot map details.
  void log() const {wcout << "(row " << row << ", index " << get_index() << ")";}
};


class ColMap {
private:
  size_t col;            // Column associated with the dot map.
  vector<DotMap> map;    // Vector of DotMap objects for rows in this column.

public:
  // Constructor to initialize ColMap with a column.
  ColMap(const size_t & c) : col(c) {}

  // Constructor to initialize ColMap with column, row, and index.
  ColMap(const size_t & col, const size_t & row, const size_t & index) : ColMap(col) {map.emplace_back(row, index);}

  // Equality operator to compare ColMap objects by column.
  bool operator==(const ColMap & cm) {return col == cm.col;}

  // Get the number of rows in this column map.
  size_t get_length() const {return map.size();}

  // Get the column associated with this ColMap.
  size_t get_col() const {return col;}

  // Get the map index of a specific row.
  size_t get_map_index(const size_t & row) {
    size_t length = get_length();
    for (size_t j = 0; j < length; j++) {
      if (map.at(j).get_row() == row) {return j;}}
    return size_max;}

  // Get the dot index for a specific row.
  size_t get_index(const size_t & row) {
    size_t map_index = get_map_index(row);
    if (map_index != size_max) {return map.at(map_index).get_index();}
    return size_max;}

  // Add or update the index for a specific row.
  void add_index(const size_t & row, const size_t & index) {
    size_t map_index = get_map_index(row);
    if (map_index != size_max) {map.at(map_index).set_index(index);}
    else {map.emplace_back(row, index);}}

  // Log the column map details.
  void log() const {
    wcout << "[col " << col << " ";
    for (const auto & d : map) {d.log();}
    wcout << "]";}
};


class DotsMap {
private:
  vector<ColMap> map; // Vector of ColMap objects for columns in the grid.

public:
  // Get the number of columns in the dot map.
  size_t get_length() const {return map.size();}

  // Get the map index for a specific column.
  size_t get_map_index(const size_t & col) {
    size_t length = get_length();
    for (size_t j = 0; j < length; j++) {
      if (map.at(j).get_col() == col) {return j;}}
    return size_max;}

  // Get the dot index for a specific column and row.
  size_t get_index(const size_t & col, const size_t & row) {
    size_t map_index = get_map_index(col);
    if (map_index != size_max) {return map.at(map_index).get_index(row);}
    return size_max;}

  // Add or update the dot index for a specific column and row.
  void add_index(const size_t & col, const size_t & row, const size_t & index) {
    size_t map_index = get_map_index(col);
    if (map_index != size_max) {map.at(map_index).add_index(row, index);}
    else {map.emplace_back(col, row, index);}}

  // Log the entire dot map.
  void log() const {for (const auto &r : map) {r.log();}}
};

