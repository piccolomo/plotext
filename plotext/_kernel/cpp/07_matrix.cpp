// Matrix: a grid of MatrixCharacter cells, built, filled, cleared and rendered here; the insert paths of Point, Points, FilledPoint and FilledPoints live in their own files instead, since they need Matrix declared first.

class Point;         // body of Matrix::insert(const Point&)         lives at the bottom of 10_point.cpp
class Points;        // body of Matrix::insert(const Points&)        lives at the bottom of 12_points.cpp
class FilledPoint;   // body of Matrix::insert(const FilledPoint&)   lives at the bottom of 13_point_filled.cpp
class FilledPoints;  // body of Matrix::insert(const FilledPoints&)  lives at the bottom of 14_points_filled.cpp
class Marker;        // bodies of Matrix::add_box_marker / add_line  live at the bottom of 08_marker.cpp

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

    // Stamp a single MatrixCharacter at (col, row): bounds-check + cell-merge. Returns true on successful placement, false if (col, row) is out of bounds or, with check_space on, already taken. Used by Marker::stamp (single-cell markers) so the bounds check lives in one place.
    inline bool insert(const MatrixCharacter & c, size_t col, size_t row, bool check_space = false) noexcept {
        if (col >= get_width() || row >= get_height()) return false;
        if (check_space && !is_empty(col, col + 1, row, row + 1)) return false;
        at(col, row).merge(c); return true; }

    // Stamp a Point, body lives at the bottom of 10_point.cpp where Point is fully declared. Returns the stamp() bool from the Point's marker.
    inline bool insert(const Point &, bool check_space = false) noexcept;

    // Stamp every Point in a Points collection, body lives at the bottom of 12_points.cpp.
    inline void insert(const Points &) noexcept;

    // Stamp a FilledPoint (walks the main→fill line and stamps each Point), body lives at the bottom of 13_point_filled.cpp.
    inline void insert(const FilledPoint &) noexcept;

    // Stamp every FilledPoint in a FilledPoints collection, body lives at the bottom of 14_points_filled.cpp.
    inline void insert(const FilledPoints &) noexcept;

    // Viability check at canvas position (col, row) for a region of (width × height) cells: in-bounds + (when check_space) empty cells, the column before the region included, so that two objects placed left to right never end up touching. Pure geometric predicate, doesn't need the source matrix.
    inline bool fits(int col, int row, size_t width, size_t height, bool check_space) const noexcept {
        if (col < 0 || row < 0) return false;
        if ((size_t)col + width > get_width() || (size_t)row + height > get_height()) return false;
        const size_t start = col > 0 ? col - 1 : 0;
        if (check_space && !is_empty(start, col + width, row, row + height)) return false;
        return true; }

    // Insert another Matrix at (col, row) with horizontal/vertical alignment, clipped to bounds. Dynamic alignment on either axis triggers a 1D search across candidate displacements centred on the anchor; both axes dynamic → 2D cross-product search (vertical-outer × horizontal-inner). check_space=true requires empty target cells even for static alignments; dynamic path implicitly requires empty cells. Returns true on success, false if no viable spot found.
    inline bool insert(const Matrix & m, size_t col, size_t row, const Alignment & ha, const Alignment & va, bool check_space = false) noexcept {
        const size_t mw = m.get_width(), mh = m.get_height();
        const bool need_empty = check_space || ha.is_dynamic() || va.is_dynamic();
        const Vector<int> h_deltas = get_displacements(ha, mw);
        const Vector<int> v_deltas = get_displacements(va, mh);
        for (size_t vi = 0; vi < v_deltas.get_length(); ++vi)
            for (size_t hi = 0; hi < h_deltas.get_length(); ++hi) {
                const int ac = (int)col + h_deltas.at(hi);
                const int ar = (int)row + v_deltas.at(vi);
                if (fits(ac, ar, mw, mh, need_empty)) { Array2D<MatrixCharacter>::insert(ac, ar, m); return true; }
            }
        return false; }

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
            const wchar_t ch = at(i).get_wcharacter();
            if (ch != L'\0') wchar_to_buffer(ch, buffer, length);   // skip wide-char continuation cell
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
            // HTML-escape special characters so stamped labels containing "<", ">" or "&" don't corrupt the page; skip wide-char continuation cells (L'\0').
            if      (c == L'\0') {/* skip */}
            else if (c == L'<') cstring_to_buffer(L"&lt;",  4, buffer, length);
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
        const size_t cap = character_size_max * get_size() + (1 + wcslen(ansi_end)) * get_height() + 1;
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, !colorless);
        return wstring(buffer.begin(), length); }

    // Stream to stdout: build the whole matrix into a single buffer, then one wcout.write, much faster than per-cell wcout calls (saves the per-call streambuf overhead). Heap-allocated buffer (Array<wchar_t>) to survive matrices large enough to overflow the stack.
    inline void stream(bool colorfull = true, bool flushing = true) noexcept {
        const size_t cap = character_size_max * get_size() + (1 + wcslen(ansi_end)) * get_height() + 1;
        Array<wchar_t> buffer(cap, L'\0');
        size_t length = 0;
        to_buffer(buffer.begin(), length, colorfull);
        write_wide(buffer.begin(), length, flushing); }

    // Apply `p`'s background to every cell that doesn't already have one. Each MatrixCharacter is-a Pixel, so this is a per-cell forward to Pixel::fix_background.
    inline void fix_background(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_size(); ++i) at(i).fix_background(p); }

    // Apply `p`'s background, foreground and style to every cell that has none of its own. Per-cell forward to Pixel::fix.
    inline void fix(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_size(); ++i) at(i).fix(p); }

    // Apply `p` as the pixel of every cell, preserving the cached glyph. Per-cell forward to NormalCharacter::set_pixel.
    inline void set_pixel(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_size(); ++i) at(i).set_pixel(p); }

    // Build a transposed copy: W×H → H×W, cell (c, r) in source becomes (r, c) in result. Used by vertical-text construction (a W×1 label matrix becomes 1×W stack).
    inline Matrix get_transpose() const noexcept {
        const size_t w = get_width(), h = get_height();
        Matrix out(h, w);
        for (size_t r = 0; r < h; ++r)
            for (size_t c = 0; c < w; ++c)
                out.at(r, c) = at(c, r);
        return out; }

    // Transpose in place: replaces self with get_transpose().
    inline void transpose() noexcept { *this = get_transpose(); }

    inline void log() noexcept { wcout << L"Matrix(" << get_width() << L"x" << get_height() << L")" << endl; stream(); }
};


// Build a Matrix from a Colorize by stamping its colourless characters cell-by-cell, all sharing the Colorize's pixel. Used by MatrixMarker construction paths (Python text builder) to turn a Colorize into a stampable Matrix. Wide characters (CJK / fullwidth / common emoji) occupy two matrix columns: the glyph in the first, L'\0' in the second as a "skip me" sentinel that the renderers (to_buffer / html_to_buffer) ignore so the terminal's own 2-cell rendering lines up with the matrix layout.
inline Matrix colorize_to_matrix(const Colorize & c) noexcept {
    vector<wstring> lines = split_wstring(c.get_colorless_wstring());
    size_t height = lines.size();
    size_t width  = 0;
    for (const auto & line : lines) width = std::max(width, get_wstring_real_width(line));
    Matrix out(width, height);
    const Pixel & p = c;
    for (size_t row = 0; row < height; ++row) {
        const wstring & line = lines[row];
        size_t col = 0;
        for (wchar_t ch : line) {
            const size_t cw = get_wchar_real_width(ch);
            out.at(col, row) = MatrixCharacter(ch, p);
            if (cw == 2 && col + 1 < width) out.at(col + 1, row) = MatrixCharacter(L'\0', p);
            col += cw;
        }
    }
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
    void     matrix_clone        (Matrix * dest, Matrix * src) noexcept { *dest = *src; }
    void     matrix_transpose    (Matrix * m) noexcept { m->transpose(); }
    void     matrix_fill_pixel   (Matrix * m, Pixel * p) noexcept { m->fill(MatrixCharacter(L' ', *p)); }
    void     matrix_fix_background(Matrix * m, Pixel * p) noexcept { m->fix_background(*p); }
    void     matrix_fix(Matrix * m, Pixel * p) noexcept { m->fix(*p); }
    void     matrix_apply_pixel  (Matrix * m, Pixel * p) noexcept { m->set_pixel(*p); }
    void     matrix_set_pixel    (Matrix * m, size_t col, size_t row, Pixel * p) noexcept { m->at(col, row).set_pixel(*p); }
    Pixel *  matrix_get_pixel    (Matrix * m, size_t col, size_t row) noexcept { return new Pixel(static_cast<const Pixel &>(m->at(col, row))); }
    // Set the cell at (col, row) to a NormalCharacter built from (wchar, pixel). Builds a transient MatrixCharacter (kind=marker_normal, bits=0) and dispatches to Array2D::insert.
    void     matrix_set_normal_character(Matrix * m, size_t col, size_t row, wchar_t c, Pixel * p) noexcept { m->Array2D<MatrixCharacter>::insert(col, row, MatrixCharacter(c, *p)); }
    void     matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va) noexcept { m->insert(*mi, col, row, Alignment(ha), Alignment(va)); }
    Matrix * matrix_vstack       (Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->vstack(*m2, adapt)); }
    Matrix * matrix_hstack       (Matrix * m1, Matrix * m2, bool adapt) noexcept { return new Matrix(m1->hstack(*m2, adapt)); }
    Matrix * matrix_part         (Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept { return new Matrix(m->part(col_start, col_stop, row_start, row_stop)); }
    const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) noexcept { return wstring_to_cstring(m->get_wstring(colorless)); }
    const wchar_t * matrix_get_html   (Matrix * m) noexcept { return wstring_to_cstring(m->get_html()); }
}
