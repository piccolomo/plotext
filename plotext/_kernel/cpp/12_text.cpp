// Text: a Matrix (1×N horizontal or N×1 vertical) anchored at a (PointPosition) coordinate, with alignment and orientation. Inserted into a target Matrix at its (col, row) — each cell carries its own pixel, so per-char styling survives.

class Text : public PointPosition, public Matrix {
private:
    Orientation orientation = Orientation(0);   // 0 horizontal, 1 vertical
    Alignment   alignment   = Alignment(-1);    // -1 left, 0 center, 1 right

public:
    Text() noexcept = default;
    Text(float xi, float yi, const Matrix   & m, const Orientation & o = Orientation(0), const Alignment & a = Alignment(-1)) : PointPosition(xi, yi), Matrix(m),                     orientation(o), alignment(a) {}
    Text(float xi, float yi, const Colorize & c, const Orientation & o = Orientation(0), const Alignment & a = Alignment(-1)) : PointPosition(xi, yi), Matrix(colorize_to_matrix(c)), orientation(o), alignment(a) {}
    Text(const Text & t) = default;
    Text(Text && t) noexcept = default;
    ~Text() {}

    Text & operator=(const Text & t) = default;
    Text & operator=(Text && t) noexcept = default;

    void set_position   (float xi, float yi)         noexcept { PointPosition::operator=(PointPosition(xi, yi)); }
    void set_alignment  (const Alignment   & a)      noexcept { alignment   = a; }
    void set_orientation(const Orientation & o)      noexcept { orientation = o; }

    const Alignment   & get_alignment()   const noexcept { return alignment; }
    const Orientation & get_orientation() const noexcept { return orientation; }

    using Matrix::get_wstring;                                                  // keep Matrix::get_wstring(bool) accessible alongside the no-arg debug version below

    wstring get_wstring() noexcept {
        wostringstream woss;
        woss << L"Text(" << Matrix::get_wstring(true) << L", x=" << get_x() << L", y=" << get_y()
             << L", alignment=" << alignment.get_integer() << L", orientation=" << orientation.get_integer() << L")";
        return woss.str(); }

    inline void log() { wcout << get_wstring() << endl; }
};


extern "C" {
    Text * text_new_from_colorize(float x, float y, Colorize * c, int orientation, int alignment) noexcept { return new Text(x, y, *c, Orientation(orientation), Alignment(alignment)); }
    Text * text_new_from_matrix  (float x, float y, Matrix   * m, int orientation, int alignment) noexcept { return new Text(x, y, *m, Orientation(orientation), Alignment(alignment)); }
    Text * text_copy  (Text * t) noexcept { return new Text(*t); }
    void   text_delete(Text * t) noexcept { delete t; }

    void   text_set_position   (Text * t, float x, float y) noexcept { t->set_position(x, y); }
    void   text_set_alignment  (Text * t, int a) noexcept { t->set_alignment(Alignment(a)); }
    void   text_set_orientation(Text * t, int o) noexcept { t->set_orientation(Orientation(o)); }

    float  text_get_x          (Text * t) noexcept { return t->get_x(); }
    float  text_get_y          (Text * t) noexcept { return t->get_y(); }
    int    text_get_alignment  (Text * t) noexcept { return t->get_alignment().get_integer(); }
    int    text_get_orientation(Text * t) noexcept { return t->get_orientation().get_integer(); }

    void   text_rescale_x(Text * t, float lo, float hi, size_t width,  float delta) noexcept { t->rescale_x({lo, hi}, width,  delta); }
    void   text_rescale_y(Text * t, float lo, float hi, size_t height, float delta) noexcept { t->rescale_y({lo, hi}, height, delta); }

    void   text_fix_background(Text * /*t*/, Pixel * /*p*/) noexcept { /* no-op: Text now inherits Matrix (per-cell pixels); a Matrix-wide fix_background lives on the migration TODO. */ }

    const wchar_t * text_get_wstring(Text * t) noexcept { return wstring_to_cstring(t->get_wstring()); }
}


// Split a multi-line Colorize into a Matrix — one row per line, width = longest line. Stamps cells directly (not via Text) to avoid an infinite recursion with Text(Colorize), which itself calls this function.
inline Matrix colorize_to_matrix(const Colorize & c) noexcept {
    vector<wstring> lines = split_wstring(c.get_colorless_wstring());
    size_t height = lines.size();
    size_t width  = 0;
    for (const auto & line : lines) width = std::max(width, line.size());
    Matrix out(width, height);
    const Pixel & p = c;                                                        // Colorize is-a Pixel — every stamped cell uses this pixel
    for (size_t row = 0; row < height; ++row) {
        const wstring & line = lines[row];
        for (size_t col = 0; col < line.size(); ++col)
            out.at(col, row) = MatrixCharacter(line[col], p);
    }
    return out;
}


// Out-of-class definition of Matrix::insert(const Text&). Lives here because Text inherits Matrix; the body needs Text fully declared, which only happens above. See the forward declaration in 11_matrix.cpp.
inline bool Matrix::insert(const Text & t, bool check_space) noexcept {
    const bool horizontal = t.get_orientation().is_horizontal();
    const size_t length = horizontal ? t.get_width() : t.get_height();
    if (length == 0) return true;

    if (t.get_alignment().is_dynamic()) {
        if (t.get_row() >= get_height()) return false;
        Text candidate = t;
        candidate.set_alignment(Alignment(0));
        for (int delta : get_dynamic_displacements(length)) {
            candidate.set_position(t.get_col() + delta, t.get_row());
            if (insert(candidate, true)) return true; }
        return false; }

    const int  disp = t.get_alignment().get_displacement(length);
    const int  col0 = (int)t.get_col() + (horizontal ? disp : 0);
    const int  row0 = (int)t.get_row() + (horizontal ? 0    : disp);
    const int  col1 = col0 + (horizontal ? (int)length : 1);
    const int  row1 = row0 + (horizontal ? 1           : (int)length);
    if (col0 < 0 || row0 < 0) return false;
    if ((size_t)col1 > get_width() || (size_t)row1 > get_height()) return false;

    if (check_space && !is_empty(col0, col1, row0, row1)) return false;

    for (size_t i = 0; i < length; ++i) {
        const size_t c = col0 + (horizontal ? i : 0);
        const size_t r = row0 + (horizontal ? 0 : i);
        at(c, r).merge(horizontal ? t.Matrix::at(i, 0) : t.Matrix::at(0, i));   // copy the cell from Text's own matrix, preserving its per-cell pixel
    }
    return true;
}
