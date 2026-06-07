// Grid: 2D grid mapping (col, row) → point index in some Points collection. Cell stores index+1; 0 means empty (saves a sentinel value). Used by Points::squash for fast O(1) overlap lookup.

class Grid : public Vector<size_t> {
private:
    size_t cols  = 0;
    size_t rows  = 0;
    size_t count = 0;     // populated cells (distinct from Vector::get_length, which is total cells)

public:
    Grid(size_t c, size_t r) { resize(c, r); }
    ~Grid() noexcept = default;

    void clear()  noexcept { fill(0); count = 0; }
    void resize(size_t c, size_t r) noexcept { cols = c; rows = r; reserve(c * r); set_length(c * r); fill(0); count = 0; }

    // (col, row) ↔ linear location helpers
    constexpr size_t location_of(size_t col, size_t row) const noexcept { return row * cols + col; }
    constexpr size_t col_of     (size_t loc)             const noexcept { return loc % cols; }
    constexpr size_t row_of     (size_t loc)             const noexcept { return loc / cols; }

    // Stored index access (subtracts 1 because 0 encodes empty)
    size_t at_index(size_t loc)             const noexcept { return at(loc) - 1; }
    size_t at_index(size_t col, size_t row) const noexcept { return at_index(location_of(col, row)); }
    void   set_at  (size_t loc, size_t idx)       noexcept { at(loc) = idx + 1; ++count; }
    void   set_at  (size_t col, size_t row, size_t idx) noexcept { set_at(location_of(col, row), idx); }

    // Presence checks
    bool is_empty  (size_t loc)             const noexcept { return at(loc) == 0; }
    bool is_present(size_t loc)             const noexcept { return !is_empty(loc); }
    bool is_empty  (size_t col, size_t row) const noexcept { return is_empty(location_of(col, row)); }
    bool is_present(size_t col, size_t row) const noexcept { return !is_empty(col, row); }

    constexpr size_t get_cols()  const noexcept { return cols; }
    constexpr size_t get_rows()  const noexcept { return rows; }
    constexpr size_t get_size()  const noexcept { return cols * rows; }
    constexpr size_t get_count() const noexcept { return count; }

    wstring get_wstring() const noexcept {
        wostringstream os;
        os << L"Grid " << cols << L"x" << rows << L" count " << count << L" [";
        for (size_t loc = 0; loc < Vector<size_t>::get_length(); ++loc)
            if (is_present(loc)) os << L"(" << col_of(loc) << L"," << row_of(loc) << L": " << at_index(loc) << L") ";
        os << L"]";
        return os.str(); }

    void log() const noexcept { wcout << get_wstring() << endl; }
};


extern "C" {
    Grid * grid_new       (size_t cols, size_t rows) noexcept { return new Grid(cols, rows); }
    void         grid_delete    (Grid * g) noexcept { delete g; }
    void         grid_clear     (Grid * g) noexcept { g->clear(); }
    void         grid_log       (Grid * g) noexcept { g->log(); }
    size_t       grid_get_length(Grid * g) noexcept { return g->get_count(); }
}
