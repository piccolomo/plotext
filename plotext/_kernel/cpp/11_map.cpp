// PointsMap: 2D index grid mapping (col, row) -> point index in an underlying Vector<size_t>

class PointsMap : public Vector<size_t> {
private:
    size_t cols = 0;
    size_t rows = 0;
    size_t length = 0; // number of assigned indices

public:
    // ------------ lifecycle ------------

    // Construct a map of cols x rows cells
    PointsMap(const size_t & cols, const size_t & rows) {resize(cols, rows);}

    // Copy constructor
    PointsMap(const PointsMap &) = default;

    // Move constructor
    PointsMap(PointsMap &&) noexcept = default;

    // Destructor
    ~PointsMap() noexcept {}

    // Copy assignment
    PointsMap & operator=(const PointsMap &) = default;

    // Move assignment
    PointsMap & operator=(PointsMap &&) noexcept = default;

    // Reset all cells to empty
    void clear() noexcept {fill(0); length = 0;}

    // Resize the map to cols x rows (zeroed)
    void resize(const size_t & cols, const size_t & rows) noexcept {
        this->cols = cols;
        this->rows = rows;
        Vector<size_t>::reserve(rows * cols);
        Vector<size_t>::set_length(rows * cols);
        fill(0);
        length = 0; }

    // ------------ indexing helpers ------------

    // Linear location index from (col, row)
    constexpr size_t get_location(const size_t & col, const size_t & row) const noexcept {return row * cols + col;}

    // Column from a linear location
    constexpr size_t get_col(const size_t & location) const noexcept {return location % cols;}

    // Row from a linear location
    constexpr size_t get_row(const size_t & location) const noexcept {return location / cols;}

    // Stored index at a location (returns stored-1 because 0 encodes empty)
    size_t get_index(const size_t & location) const noexcept {return at(location) - 1;}

    // Stored index at (col, row)
    size_t get_index(const size_t & col, const size_t & row) const noexcept {return get_index(get_location(col, row));}

    // Store an index at a location (encodes as index+1; increments count)
    void set_index(const size_t & location, const size_t & index) noexcept {
        at(location) = index + 1;
        length += 1;}

    // Store an index at (col, row)
    void set_index(const size_t & col, const size_t & row, const size_t & index) noexcept {
        set_index(get_location(col, row), index);}

    // ------------ presence check ------------

    // True if no index is stored at the given location
    bool is_empty(const size_t & index) const noexcept {return at(index) == 0;}

    // True if an index is stored at the given location
    bool is_present(const size_t & index) const noexcept {return !is_empty(index);}

    // True if no index is stored at (col, row)
    bool is_empty(const size_t & col, const size_t & row) const noexcept {return is_empty(get_location(col, row));}

    // True if an index is stored at (col, row)
    bool is_present(const size_t & col, const size_t & row) const noexcept {return !is_empty(col, row);}

    // ------------ getters ------------

    // Number of columns
    constexpr size_t get_cols() const noexcept {return cols;}

    // Number of rows
    constexpr size_t get_rows() const noexcept {return rows;}

    // Total number of cells
    constexpr size_t get_size() const noexcept {return cols * rows;}

    // Number of cells currently populated
    constexpr size_t get_length() const noexcept {return length;}

    // ------------ output / logging ------------

    // Get wide string summary "PointsMap CxR length N [ ... ]"
    wstring get_wstring() const noexcept {
        wostringstream log;
        log << L"PointsMap " << cols << L"x" << rows << L" length " << length << L" [";
        for (size_t l = 0; l < Vector<size_t>::get_length(); ++l) {
            if (is_present(l)) log << L"(" << get_col(l) << L"," << get_row(l) << L": " << get_index(l) << L") ";}
        log << L"]";
        return log.str();}

    // Get narrow string summary
    inline string get_string() const noexcept {return wstring_to_string(get_wstring());}

    // Log to wcout
    inline void log() const noexcept {wcout << get_wstring() << endl << flush;}

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const PointsMap & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const PointsMap & c) noexcept {os << c.get_string(); return os;}

};



extern "C" {

  // Create a new PointsMap of cols x rows
  PointsMap * points_map_new(size_t cols, size_t rows) {return new PointsMap(cols, rows);}

  // Delete the PointsMap
  void points_map_delete(PointsMap * handle) {delete handle;}

  // Clear every cell
  void points_map_clear(PointsMap * handle) {handle->clear();}

  // Resize the map to cols x rows
  void points_map_resize(PointsMap * handle, size_t cols, size_t rows) {handle->resize(cols, rows);}

  // Log the map to wcout
  void points_map_log(PointsMap * handle) {handle->log();}

  // Number of populated cells
  size_t points_map_get_length(PointsMap * handle) {return handle->get_length();}

}
