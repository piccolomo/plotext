// PointsMap - manages mappings of dots to grid positions (rows and columns) with logging and string output

class PointsMap : public Vector<size_t> {
private:
    size_t cols = 0;
    size_t rows = 0;
    size_t length = 0; // number of assigned indices

public:
    // ------------ lifecycle ------------
    PointsMap(const size_t & cols, const size_t & rows) {resize(cols, rows);}

    void clear() noexcept {fill(0); length = 0;}

    void resize(const size_t & cols, const size_t & rows) noexcept {
        this->cols = cols;
        this->rows = rows;
        Vector<size_t>::reserve(rows * cols);
        Vector<size_t>::set_length(rows * cols);
        fill(0);
        length = 0; }

    // ------------ indexing helpers ------------
    constexpr size_t get_location(const size_t & col, const size_t & row) const noexcept {return row * cols + col;}
    constexpr size_t get_col(const size_t & location) const noexcept {return location % cols;}
    constexpr size_t get_row(const size_t & location) const noexcept {return location / cols;}
    
    size_t get_index(const size_t & location) const noexcept {return at(location) - 1;}
    size_t get_index(const size_t & col, const size_t & row) const noexcept {return get_index(get_location(col, row));}

    void set_index(const size_t & location, const size_t & index) noexcept {
        at(location) = index + 1;
        length += 1;}

    void set_index(const size_t & col, const size_t & row, const size_t & index) noexcept {
        set_index(get_location(col, row), index);}

    // ------------ presence check ------------
    bool is_empty(const size_t & index) const noexcept {return at(index) == 0;}
    bool is_present(const size_t & index) const noexcept {return !is_empty(index);}

    bool is_empty(const size_t & col, const size_t & row) const noexcept {return is_empty(get_location(col, row));}
    bool is_present(const size_t & col, const size_t & row) const noexcept {return !is_empty(col, row);}

    // ------------ getters ------------
    constexpr size_t get_cols() const noexcept {return cols;}
    constexpr size_t get_rows() const noexcept {return rows;}
    constexpr size_t get_size() const noexcept {return cols * rows;}
    constexpr size_t get_length() const noexcept {return length;}

    // ------------ output / logging ------------
    wstring get_wstring() const noexcept {
        wostringstream log;
        log << L"PointsMap " << cols << L"x" << rows << L" length " << length << L" [";
        for (size_t l = 0; l < Vector<size_t>::get_length(); ++l) {
            if (is_present(l)) log << L"(" << get_col(l) << L"," << get_row(l) << L": " << get_index(l) << L") ";}
        log << L"]";
        return log.str();}

    inline string get_string() const noexcept {return wstring_to_string(get_wstring());}

    inline void log() const noexcept {wcout << get_wstring() << endl << flush;}

    friend wostream & operator<<(wostream & os, const PointsMap & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const PointsMap & c) noexcept {os << c.get_string(); return os;}

};



extern "C" {

  PointsMap * points_map_new(size_t cols, size_t rows) {return new PointsMap(cols, rows);}

  void points_map_delete(PointsMap * handle) {delete handle;}

  void points_map_clear(PointsMap * handle) {handle->clear();}

  void points_map_resize(PointsMap * handle, size_t cols, size_t rows) {handle->resize(cols, rows);}

  void points_map_log(PointsMap * handle) {handle->log();}

  size_t points_map_get_length(PointsMap * handle) {return handle->get_length();}

} 
