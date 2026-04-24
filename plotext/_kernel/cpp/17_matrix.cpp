// Matrix: 2D grid of CharacterHD cells; supports insert (char/pixel/wstring/Colorize/Matrix/Point/Points), stacking and buffered rendering

using ArrayCh = Array2D<CharacterHD>;


class Matrix : public ArrayCh {
public:
    using ArrayCh::insert;

    // -------------------- lifecycle --------------------

    // Default constructor
    Matrix() noexcept = default;

    // Construct an empty matrix of the given size
    Matrix(size_t w, size_t h) noexcept : ArrayCh(w, h) {}

    // Construct a matrix of the given size filled with the given character
    Matrix(size_t w, size_t h, const CharacterHD & c) noexcept : ArrayCh(w, h, c) {}

    // Construct a matrix of the given size filled with a marker built from the given pixel and character
    Matrix(size_t w, size_t h, const Pixel & p, wchar_t ch = L' ') noexcept : ArrayCh(w, h, Marker(ch, p)) {}

    // Copy constructor (base handles the storage copy)
    Matrix(const Matrix & other) noexcept : ArrayCh(other) {}

    // Construct from a raw ArrayCh (upcast helper)
    Matrix(const ArrayCh & other) noexcept : ArrayCh(other) {}

    // Move constructor
    Matrix(Matrix && other) noexcept : ArrayCh(std::move(other)) {}

    // Destructor
    ~Matrix() noexcept = default;

    // Copy assignment (self-assignment safe)
    Matrix & operator=(const Matrix & other) noexcept {
        if (this != &other) ArrayCh::operator=(other);
        return *this;}

    // Move assignment
    Matrix & operator=(Matrix && other) noexcept {
        if (this != &other) ArrayCh::operator=(std::move(other));
        return *this;}

    // Equality / inequality (delegate to the base array)
    bool operator==(const Matrix & other) const {return ArrayCh::operator==(other); }
    bool operator!=(const Matrix & other) const {return ArrayCh::operator!=(other); }

    // -------------------- modifiers --------------------

    // Reset every cell to empty
    void clear() noexcept { for (size_t i = 0; i < get_size(); i++) at(i).clear(); }

    // Apply a pixel (foreground/background/style) to every cell
    inline void fill(const Pixel & p) noexcept {for (auto &ch : *this) ch.set_pixel(p);}

    // Overwrite every cell with a copy of the given character
    inline void fill(const CharacterHD & c) noexcept {for (auto &ch : *this) ch = c;}

    // Check if every cell in the (col0..col1, row0..row1) sub-range is empty
    inline bool is_empty(size_t col0, size_t col1, size_t row0, size_t row1) const noexcept {
        for (size_t r = row0; r < row1; r++)
            for (size_t c = col0; c < col1; c++)
                if (not at(c, r).is_empty()) return false;
        return true;}

    // Write a single character at (c, r)
    inline void insert(size_t c, size_t r, wchar_t wch) noexcept {at(c, r).set_wcharacter(wch);}

    // Apply a pixel to the cell at (c, r)
    inline void insert(size_t c, size_t r, const Pixel & p) noexcept {at(c, r).set_pixel(p);}

    // Write a wide string starting at (col, row)
    void insert(const size_t col, const size_t row, const wstring & s) noexcept {
        for (size_t i = 0; i < s.size(); i++) at(col + i, row).set_wcharacter(s[i]);}

    // Insert another matrix at (col, row), cell by cell
    inline void insert(const size_t & col, const size_t & row, const Matrix & m) noexcept {
        size_t m_width = m.get_width();
        size_t m_height = m.get_height();
        for (size_t r = 0; r < m_height; r++) {for (size_t c = 0; c < m_width; ++c) {insert(col + c, row + r, m.at(c, r));}}}

    // Insert another matrix around (col, row) with the given horizontal/vertical alignment, clipped to bounds
    inline void insert(const size_t & col, size_t row, const Matrix & m, const Alignment & ha, const Alignment & va) noexcept {
        const size_t m_width = m.get_width();
        const size_t m_height = m.get_height();
        const int v_disp = va.get_displacement(m_height);
        const int h_disp = ha.get_displacement(m_width);

        const int aligned_row = row + v_disp;
        const int aligned_col = col + h_disp;
        // Use <= so an inserted matrix that exactly fills the remaining
        // canvas width/height is accepted (insert at col 0 with m_width == width
        // was previously rejected silently).
        if (aligned_row >= 0 and aligned_col >= 0
            and static_cast<size_t>(aligned_row) + m_height <= get_height()
            and static_cast<size_t>(aligned_col) + m_width  <= get_width()) {
            insert(aligned_col, aligned_row, m);}}

    // Insert a Colorize string at (col, row) with alignment; optionally check for space and change cell colors
    inline bool insert(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha, const bool & check_space, const bool & change_color) noexcept {
        if (row >= get_height() || col >= get_width()) return false;
        const int c = static_cast<int>(col) + ha.get_displacement(s.get_length());
        const size_t start = std::max(0, c - 1);
        const size_t stop = std::min(get_width(), c + s.get_length() + 1);
        if (check_space && (c < 0 || c + s.get_length() > get_width() || !is_empty(start, stop, row, row + 1))) return false;
        for (size_t i = 0; i < s.get_length(); ++i) {
            auto & ch = at(c + i, row);
            ch.set_wcharacter(s.get_wcharacter(i));
            if (change_color) ch.set_pixel(s);}
        return true;}

    // Insert a Colorize string, trying alignment displacements dynamically; return the column it landed at, or -1
    inline int insert(const size_t & col, const size_t & row, const Colorize & s) noexcept {
        if (row >= get_height()) return -1;
        for (int delta : get_dynamic_displacements(s.get_length()))
            if (insert(col + delta, row, s, 0, true, true)) return static_cast<int>(col) + delta;
        return -1;}

    // Insert a single Point (delegates to the target cell's update)
    inline void insert(const Point & p) noexcept { at(p.get_col(), p.get_row()).update(p); }

    // Insert every Point from a Points collection
    inline void insert(const Points & points) noexcept { for (const Point & p : points) insert(p); }

    // -------------------- rendering / output --------------------

    // Write the full matrix to a wchar_t buffer, row by row, applying styles when they change.
    // The first cell of every row always re-emits its pixel: the ansi_end written at the end of
    // the previous row resets all styling, so we cannot rely on the preceding cell's state.
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer, const bool & colorfull = true) const noexcept {
        const size_t total = get_size();
        for (size_t i = 0; i < total; ++i) {
            const bool end_line = (i + 1) % get_width() == 0;
            const bool start_of_row = (i % get_width()) == 0;
            const bool different_pixel = i == 0 or start_of_row or at(i).different_pixel(at(i - 1));
            at(i).to_matrix_buffer(buffer, length_buffer, colorfull and different_pixel);
            if (end_line) {
                cstring_to_buffer(ansi_end, buffer, length_buffer);
                wchar_to_buffer(L'\n', buffer, length_buffer); } } }

    // Stream the full matrix directly to stdout, row by row, with optional flush.
    // See to_buffer above for the start_of_row rationale.
    inline void stream(const bool & colorfull = true, const bool flushing = true) const noexcept {
        const size_t total = get_size();
        for (size_t i = 0; i < total; ++i) {
            const bool end_line = (i + 1) % get_width() == 0;
            const bool start_of_row = (i % get_width()) == 0;
            const bool different_pixel = i == 0 or start_of_row or at(i).different_pixel(at(i - 1));
            at(i).stream(colorfull and different_pixel);
            if (end_line) {
                wcout.write(ansi_end, 4);
                wcout.write(new_line, 1); } }
        if (flushing) flush(); }

    // Build the wide string representation (optionally stripping color codes)
    wstring get_wstring(const bool colorless = false) const noexcept {
        wchar_t buffer[character_size_max * get_width() * get_height() + get_height() + 1] = {0};
        size_t length = 0;
        to_buffer(buffer, length, not colorless);
        return wstring(buffer);}

    // Build the narrow string representation
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Stream operators
    friend wostream & operator<<(wostream & os, const Matrix & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Matrix & c) noexcept {os << c.get_string(); return os;}

};


// Convert a multi-line Colorize into a Matrix, splitting on newlines and preserving coloring per row
Matrix colorize_to_matrix(const Colorize & c) noexcept {
    // Split the colorless string by newline
    vector<wstring> wstrings = split_wstring(c.get_colorless_wstring());

    // Determine maximum width and height
    size_t height = wstrings.size();
    size_t width = 0;
    for (const auto & line : wstrings) width = std::max(width, line.size());

    Matrix out(width, height); // Create matrix

    // Insert each line as Colorize into the matrix
    for (size_t row = 0; row < height; ++row) {
        const wstring & line = wstrings[row];
        Colorize cs(line, c); // preserve coloring
        out.insert(0, row, cs, -1, false, true);}

    return out;}


extern "C" {

    // Create a new matrix filled with the given pixel
    Matrix * matrix_new(size_t width, size_t height, Pixel * p) noexcept { return new Matrix(width, height, *p); }

    // Clear all cells of the matrix
    void matrix_clear(Matrix * m) noexcept { m->clear(); }

    // Delete the matrix
    void matrix_delete(Matrix * m) noexcept { delete m; }

    // Width in columns
    size_t matrix_get_width(Matrix * m) noexcept { return m->get_width(); }

    // Height in rows
    size_t matrix_get_height(Matrix * m) noexcept { return m->get_height(); }

    // Check if the given sub-rectangle is entirely empty
    bool matrix_is_empty(Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept {
        return m->is_empty(col_start, col_stop, row_start, row_stop);}

    // Resize the matrix (preserving cells where possible)
    void matrix_resize(Matrix * m, size_t width, size_t height) noexcept { m->resize(width, height); }

    // Fill every cell with the given pixel
    void matrix_fill_pixel(Matrix * m, Pixel * p) noexcept { m->fill(*p); }

    // Return the rendered wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) noexcept { return wstring_to_cstring(m->get_wstring(colorless)); }

    // Stack matrices vertically
    Matrix * matrix_vstack(Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->vstack(*m2, adapt)); }

    // Stack matrices horizontally
    Matrix * matrix_hstack(Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->hstack(*m2, adapt)); }

    // Extract a sub-matrix from col_start..col_stop, row_start..row_stop
    Matrix * matrix_part(const Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept { return new Matrix(m->part(col_start, col_stop, row_start, row_stop)); }

    // Create a copy of the matrix
    Matrix * matrix_copy(const Matrix * m) noexcept { return new Matrix(*m); }

    // Write a single character at (col, row)
    void matrix_set_wcharacter(Matrix * m, size_t col, size_t row, wchar_t cs) noexcept { m->insert(col, row, cs); }

    // Apply a pixel to the cell at (col, row)
    void matrix_set_pixel(Matrix * m, size_t col, size_t row, Pixel * p) noexcept { m->insert(col, row, *p); }

    // Write a wide string starting at (col, row)
    void matrix_insert_wstring(Matrix * m, size_t col, size_t row, wchar_t * s) noexcept { m->insert(col, row, s); }

    // Insert another matrix at (col, row)
    void matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * mi) noexcept { m->insert(col, row, *mi); }

    // Insert another matrix at (col, row) with horizontal/vertical alignment
    void matrix_insert_matrix_aligned(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va) noexcept { m->insert(col, row, *mi, ha, va); }

    // Insert a Colorize at (col, row) with alignment, optional space-check and color-change
    bool matrix_insert_colorized_aligned(Matrix * m, size_t col, size_t row, Colorize * c, int ha, bool check_space, bool change_color) noexcept {return m->insert(col, row, *c, ha, check_space, change_color);}

    // Insert a Colorize dynamically (tries alignment offsets); returns the placed column or -1
    int matrix_insert_colorized_dynamically(Matrix * m, size_t col, size_t row, const Colorize * c) noexcept { return m->insert(col, row, *c); }

    // Insert every point from a Points into the matrix
    void matrix_insert_points(Matrix * m, Points * points) noexcept { m->insert(*points); }

    // Print the matrix to stdout
    void matrix_print(Matrix * m, bool colorless, bool flush) noexcept { m->stream(not colorless, flush); }

    // Convert a Colorize object to a Matrix
    Matrix * colorize_get_matrix(Colorize * c) noexcept { return new Matrix(colorize_to_matrix(*c)); }

}
