// Matrix: a 2D grid of MatrixCharacter cells. Construct, fill/clear, stamp Point(s) via merge, stream rendered output.

class Matrix : public Array2D<MatrixCharacter> {
public:
    Matrix() noexcept = default;
    Matrix(size_t w, size_t h) noexcept : Array2D<MatrixCharacter>(w, h) {}
    Matrix(size_t w, size_t h, const MatrixCharacter & c) noexcept : Array2D<MatrixCharacter>(w, h, c) {}
    Matrix(size_t w, size_t h, const Pixel & p) noexcept : Array2D<MatrixCharacter>(w, h, MatrixCharacter(L' ', p)) {}
    Matrix(const Array2D<MatrixCharacter> & a) noexcept : Array2D<MatrixCharacter>(a) {}            // wrap an Array2D returned by vstack/hstack/part
    Matrix(Array2D<MatrixCharacter> && a) noexcept : Array2D<MatrixCharacter>(std::move(a)) {}

    inline void clear() noexcept { for (size_t i = 0; i < get_size(); ++i) at(i).clear(); }
    inline void fill(const MatrixCharacter & c) noexcept { for (size_t i = 0; i < get_size(); ++i) at(i) = c; }

    // True if every cell in the (col_start..col_stop, row_start..row_stop) sub-range holds an empty glyph (L' ').
    inline bool is_empty(size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) const noexcept {
        for (size_t r = row_start; r < row_stop; ++r)
            for (size_t c = col_start; c < col_stop; ++c)
                if (!at(c, r).is_empty()) return false;
        return true; }

    // Stamp a Point: bounds-check, then merge the Point's contribution into the cell at (col, row). Same-kind Points accumulate (HD/FHD/Braille dots, Line arms+style); different-kind Points reset.
    inline void insert(const Point & p) noexcept {
        size_t col = p.get_col(), row = p.get_row();
        if (col < get_width() && row < get_height()) at(col, row).merge(p.get_matrix_character()); }

    inline void insert(const Points & ps) noexcept { for (size_t i = 0; i < ps.get_length(); ++i) insert(ps.at(i)); }

    // Stamp a FilledPoint: insert every Point on the line from main to fill.
    inline void insert(const FilledPoint & fp) noexcept {
        Vector<Point> line = fp.get_filled_line();
        for (size_t i = 0; i < line.get_length(); ++i) insert(line.at(i)); }

    // Stamp every FilledPoint in the collection.
    inline void insert(const FilledPoints & fps) noexcept { for (size_t i = 0; i < fps.get_length(); ++i) insert(fps.at(i)); }

    // Stamp a single BoxMarker into the cell at (col, row). Accepts any Marker reference for C-API ergonomics — caller is expected to pass a BoxMarker; line cells then accumulate arms via merge. Bounds responsibility is on the caller.
    inline void add_box_marker(size_t col, size_t row, const Marker & m) noexcept { at(col, row).merge(m.get_matrix_character()); }

    // Stamp a line of BoxMarkers along a fixed axis: vertical=true → column=coord, rows in [start,end); vertical=false → row=coord, cols in [start,end). Loops in C++ to keep the Python-side FFI cost down to one call per line. Bounds responsibility is on the caller.
    inline void add_line(size_t coord, const Marker & m, size_t start, size_t end, bool vertical) noexcept {
        const MatrixCharacter mc = m.get_matrix_character();
        if (vertical) {
            for (size_t r = start; r < end; ++r) at(coord, r).merge(mc);
        } else {
            for (size_t c = start; c < end; ++c) at(c, coord).merge(mc);
        }
    }

    // Insert another Matrix at (col, row) with horizontal/vertical alignment, clipped to bounds. No-op if the placement would land out of the canvas.
    inline void insert(size_t col, size_t row, const Matrix & m, const Alignment & ha, const Alignment & va) noexcept {
        const size_t mw = m.get_width(), mh = m.get_height();
        const int aligned_col = static_cast<int>(col) + ha.get_displacement(mw);
        const int aligned_row = static_cast<int>(row) + va.get_displacement(mh);
        if (aligned_col >= 0 && aligned_row >= 0 &&
            static_cast<size_t>(aligned_col) + mw <= get_width() &&
            static_cast<size_t>(aligned_row) + mh <= get_height())
            Array2D<MatrixCharacter>::insert(aligned_col, aligned_row, m); }

    // Insert a Text. Static alignment → place at computed start. Dynamic alignment → search center-relative displacements until one fits with check_space=true. check_space requires the target span to be empty.
    inline bool insert(const Text & t, bool check_space = false) noexcept {
        const size_t length = t.get_length();
        if (length == 0) return true;

        if (t.get_alignment().is_dynamic()) {
            if (t.get_row() >= get_height()) return false;
            Text candidate = t;
            candidate.set_alignment(Alignment(0));
            for (int delta : get_dynamic_displacements(length)) {
                candidate.set_position(t.get_col() + delta, t.get_row());
                if (insert(candidate, true)) return true; }
            return false; }

        const bool horizontal = t.get_orientation().is_horizontal();
        const int  disp       = t.get_alignment().get_displacement(length);
        const int  col0       = (int)t.get_col() + (horizontal ? disp : 0);
        const int  row0       = (int)t.get_row() + (horizontal ? 0    : disp);
        const int  col1       = col0 + (horizontal ? (int)length : 1);
        const int  row1       = row0 + (horizontal ? 1           : (int)length);
        if (col0 < 0 || row0 < 0) return false;
        if ((size_t)col1 > get_width() || (size_t)row1 > get_height()) return false;

        if (check_space && !is_empty(col0, col1, row0, row1)) return false;

        for (size_t i = 0; i < length; ++i) {
            const size_t c = col0 + (horizontal ? i : 0);
            const size_t r = row0 + (horizontal ? 0 : i);
            at(c, r).merge(MatrixCharacter(marker_normal, t, t.get_wcharacter(i))); }
        return true; }

    // Render the matrix into a wchar_t buffer. Same per-cell logic the old stream() had: refresh glyph, emit pixel transition only when it changes, ansi_end + newline at row ends. Buffer must be sized for character_size_max * size + height + 1 wchars.
    inline void to_buffer(wchar_t * buffer, size_t & length, bool colorfull = true) noexcept {
        const size_t total = get_size();
        const size_t w     = get_width();
        for (size_t i = 0; i < total; ++i) {
            at(i).update_wcharacter();
            const bool end_line       = (i + 1) % w == 0;
            const bool start_of_row   = (i % w) == 0;
            const bool different_pixel = i == 0 or start_of_row or at(i).different_pixel(at(i - 1));
            if (colorfull and different_pixel) {
                cstring_to_buffer(ansi_end, buffer, length);
                at(i).Pixel::to_buffer(buffer, length); }
            wchar_to_buffer(at(i).get_wcharacter(), buffer, length);
            if (end_line) {
                if (colorfull) cstring_to_buffer(ansi_end, buffer, length);
                wchar_to_buffer(L'\n', buffer, length); } }
        buffer[length] = L'\0'; }

    // Render to wstring; uses Array<wchar_t> on the heap because a stack VLA overflows the default 8 MB stack for matrices with thousands of cells. Fast path: build once, copy out.
    inline wstring get_wstring(bool colorless = false) noexcept {
        const size_t cap = character_size_max * get_size() + get_height() + 1;
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, !colorless);
        return wstring(buffer.begin(), length); }

    // Stream to stdout: build the whole matrix into a single buffer, then one wcout.write — much faster than per-cell wcout calls (saves the per-call streambuf overhead). Heap-allocated buffer (Array<wchar_t>) to survive matrices large enough to overflow the stack.
    inline void stream(bool colorfull = true, bool flushing = true) noexcept {
        const size_t cap = character_size_max * get_size() + get_height() + 1;
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, colorfull);
        wcout.write(buffer.begin(), length);
        if (flushing) flush(); }

    inline void log() noexcept { wcout << L"Matrix(" << get_width() << L"x" << get_height() << L")" << endl; stream(); }
};


// Split a multi-line Colorize into a Matrix — one row per line, width = longest line. Each line keeps the source Colorize's pixel.
inline Matrix colorize_to_matrix(const Colorize & c) noexcept {
    vector<wstring> lines = split_wstring(c.get_colorless_wstring());
    size_t height = lines.size();
    size_t width  = 0;
    for (const auto & line : lines) width = std::max(width, line.size());
    Matrix out(width, height);
    for (size_t row = 0; row < height; ++row) {
        Colorize cs(lines[row], c);
        Text t(0.0f, static_cast<float>(row), cs, Orientation(0), Alignment(-1));
        out.insert(t); }
    return out;
}


extern "C" {
    Matrix * colorize_get_matrix(Colorize * c) noexcept { return new Matrix(colorize_to_matrix(*c)); }
    Matrix * matrix_new          (size_t width, size_t height, Pixel * p) noexcept { return new Matrix(width, height, *p); }
    void     matrix_delete       (Matrix * m) noexcept { delete m; }
    void     matrix_clear        (Matrix * m) noexcept { m->clear(); }
    size_t   matrix_get_width    (Matrix * m) noexcept { return m->get_width(); }
    size_t   matrix_get_height   (Matrix * m) noexcept { return m->get_height(); }
    void     matrix_print        (Matrix * m, bool colorless, bool flush) noexcept { m->stream(!colorless, flush); }
    Matrix * matrix_copy         (Matrix * m) noexcept { return new Matrix(*m); }
    void     matrix_fill_pixel   (Matrix * m, Pixel * p) noexcept { m->fill(MatrixCharacter(L' ', *p)); }
    void     matrix_set_pixel    (Matrix * m, size_t col, size_t row, Pixel * p) noexcept { m->at(col, row).set_pixel(*p); }
    // Set the cell at (col, row) to a NormalCharacter built from (wchar, pixel). Builds a transient MatrixCharacter (kind=marker_normal, bits=0) and dispatches to Array2D::insert.
    void     matrix_set_normal_character(Matrix * m, size_t col, size_t row, wchar_t c, Pixel * p) noexcept { m->Array2D<MatrixCharacter>::insert(col, row, MatrixCharacter(c, *p)); }
    // Stamp a BoxMarker at (col, row). Caller passes the polymorphic Marker pointer (must be a BoxMarker — Python's `line` primitive guarantees this). Bounds responsibility is on the caller.
    void     matrix_add_box_marker(Matrix * m, size_t col, size_t row, Marker * box) noexcept { m->add_box_marker(col, row, *box); }
    void     matrix_add_line      (Matrix * m, size_t coord, Marker * box, size_t start, size_t end, bool vertical) noexcept { m->add_line(coord, *box, start, end, vertical); }
    void     matrix_insert_points(Matrix * m, Points * pts) noexcept { m->insert(*pts); }
    bool     matrix_insert_text  (Matrix * m, Text * t, bool check_space, bool) noexcept { return m->insert(*t, check_space); }   // change_color ignored. Dynamic-alignment search is automatic when the Text's alignment is set to dynamic (Alignment(2)).
    void     matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va) noexcept { m->insert(col, row, *mi, Alignment(ha), Alignment(va)); }
    Matrix * matrix_vstack       (Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->vstack(*m2, adapt)); }
    Matrix * matrix_hstack       (Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->hstack(*m2, adapt)); }
    Matrix * matrix_part         (Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept { return new Matrix(m->part(col_start, col_stop, row_start, row_stop)); }
    const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) noexcept { return wstring_to_cstring(m->get_wstring(colorless)); }
}
