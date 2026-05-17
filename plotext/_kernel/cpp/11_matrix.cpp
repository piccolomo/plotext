// Matrix: a 2D grid of MatrixCharacter cells. Construct, fill/clear, stamp Point(s) via merge, stream rendered output.

class Text;                                                                          // forward declaration: Matrix::insert(const Text&) is defined out-of-class at the bottom of 12_text.cpp (after Text is fully declared)

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
    // Body is defined at the bottom of 12_text.cpp — Text inherits Matrix, so the body needs Text fully declared (only the declaration is legal here).
    inline bool insert(const Text & t, bool check_space = false) noexcept;

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

    // Render the matrix as HTML into a wchar buffer. Same per-cell logic as to_buffer: emit a new <span style="..."> only when the pixel differs from the previous cell or at row start. Wraps the whole output in <pre> so whitespace is preserved without &nbsp;. HTML-escapes < > & inside cell glyphs.
    inline void html_to_buffer(wchar_t * buffer, size_t & length) noexcept {
        cstring_to_buffer(L"<pre>", 5, buffer, length);
        const size_t total = get_size();
        const size_t w     = get_width();
        bool open = false;
        for (size_t i = 0; i < total; ++i) {
            at(i).update_wcharacter();
            const bool end_line        = (i + 1) % w == 0;
            const bool start_of_row    = (i % w) == 0;
            const bool different_pixel = i == 0 or start_of_row or at(i).different_pixel(at(i - 1));
            if (different_pixel) {
                if (open) { cstring_to_buffer(L"</span>", 7, buffer, length); open = false; }
                if (at(i).Pixel::has_color()) {
                    cstring_to_buffer(L"<span style=\"", 13, buffer, length);
                    at(i).Pixel::html_to_buffer(buffer, length);
                    cstring_to_buffer(L"\">", 2, buffer, length);
                    open = true; } }
            const wchar_t c = at(i).get_wcharacter();
            // HTML-escape special characters so Text-stamped labels containing "<", ">" or "&" don't corrupt the page
            if      (c == L'<') cstring_to_buffer(L"&lt;",  4, buffer, length);
            else if (c == L'>') cstring_to_buffer(L"&gt;",  4, buffer, length);
            else if (c == L'&') cstring_to_buffer(L"&amp;", 5, buffer, length);
            else                wchar_to_buffer(c, buffer, length);
            if (end_line) {
                if (open) { cstring_to_buffer(L"</span>", 7, buffer, length); open = false; }
                wchar_to_buffer(L'\n', buffer, length); } }
        cstring_to_buffer(L"</pre>", 6, buffer, length);
        buffer[length] = L'\0'; }

    // Render the matrix as HTML into a wstring. Heap-allocated buffer to survive large matrices.
    inline wstring get_html() noexcept {
        const size_t cap = 400 * get_size() + 10 * get_height() + 16;
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        html_to_buffer(buffer.begin(), length);
        return wstring(buffer.begin(), length); }

    // Render to wstring; uses Array<wchar_t> on the heap because a stack VLA overflows the default 8 MB stack for matrices with thousands of cells. Fast path: build once, copy out.
    inline wstring get_wstring(bool colorless = false) noexcept {
        const size_t cap = character_size_max * get_size() + (1 + wcslen(ansi_end)) * get_height() + 1;   // per row: newline + trailing ansi_end
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, !colorless);
        return wstring(buffer.begin(), length); }

    // Stream to stdout: build the whole matrix into a single buffer, then one wcout.write — much faster than per-cell wcout calls (saves the per-call streambuf overhead). Heap-allocated buffer (Array<wchar_t>) to survive matrices large enough to overflow the stack.
    inline void stream(bool colorfull = true, bool flushing = true) noexcept {
        const size_t cap = character_size_max * get_size() + (1 + wcslen(ansi_end)) * get_height() + 1;   // per row: newline + trailing ansi_end
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, colorfull);
        wcout.write(buffer.begin(), length);
        if (flushing) flush(); }

    // Apply `p`'s background to every cell that doesn't already have one. Each MatrixCharacter is-a Pixel, so this is a per-cell forward to Pixel::fix_background.
    inline void fix_background(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_size(); ++i) at(i).fix_background(p); }

    // Apply `p` as the pixel of every cell, preserving the cached glyph. Per-cell forward to NormalCharacter::set_pixel.
    inline void set_pixel(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_size(); ++i) at(i).set_pixel(p); }

    inline void log() noexcept { wcout << L"Matrix(" << get_width() << L"x" << get_height() << L")" << endl; stream(); }
};


// `colorize_to_matrix` body lives at the bottom of 12_text.cpp (uses Text, which inherits Matrix — same cycle as Matrix::insert(const Text&)).
inline Matrix colorize_to_matrix(const Colorize & c) noexcept;                       // forward declaration: defined at the bottom of 12_text.cpp


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
    void     matrix_fix_background(Matrix * m, Pixel * p) noexcept { m->fix_background(*p); }
    void     matrix_apply_pixel  (Matrix * m, Pixel * p) noexcept { m->set_pixel(*p); }
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
    const wchar_t * matrix_get_html   (Matrix * m) noexcept { return wstring_to_cstring(m->get_html()); }
}
