// Points: a collection of Point built on top of plotext's Vector. Minimal version, append, size, iteration via at(), and log.

class Points : public Vector<Point> {
public:
    using Vector<Point>::append;                                                            // bring inherited append(Point) overload back into scope (the Points overload below would otherwise hide it)

    Points() noexcept : Vector<Point>() {}
    explicit Points(size_t capacity) : Vector<Point>(capacity) {}

    inline void log() const {
        wcout << L"Points (" << get_length() << L"):" << endl;
        for (size_t i = 0; i < get_length(); ++i) { wcout << L"  "; at(i).log(); } }

    // Add (dx, dy) offset to every contained Point.
    inline void add_offset(size_t dx, size_t dy) noexcept { for (size_t i = 0; i < get_length(); ++i) at(i).add_offset(dx, dy); }

    // Apply background to every Point's marker (Marker::fix_background → Pixel::fix_background; only sets bg if not already set).
    inline void fix_background(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_length(); ++i) { Marker * m = at(i).get_marker(); if (m) m->fix_background(p); } }

    // Deduplicate overlapping points. Walks each Point: if the (col, row) cell already holds an index, mark the previous Point as null when the new one is_close (same sub-cell). After the pass, drop nulled entries. Uses Grid for O(1) (col, row) → previous-index lookup. Before dropping the previous, call Marker::merge so box-marker crossings (│ over ─) carry both arm sets into the survivor (┼/┤/├ etc.); for every other marker kind, merge is a no-op and the new one wins as before.
    inline void squash(Grid & grid) noexcept {
        Vector<Point> out(get_length());
        for (Point & current : *this) {
            size_t c = current.get_col(), r = current.get_row();
            if (grid.is_present(c, r)) {
                Point & previous = out.at(grid.at_index(c, r));
                if (current.is_close(previous)) {
                    current.get_marker()->merge(*previous.get_marker());
                    previous.set_marker(nullptr); } }
            grid.set_at(c, r, out.get_length());
            out.append(current); }
        Vector<Point>::clear();
        for (auto & el : out) if (el.has_marker()) append(el); }

    // Drop every Point whose (x, y) falls outside a (width, height) matrix.
    inline void select_in_matrix(size_t width, size_t height) noexcept {
        Points kept(get_length());
        for (size_t i = 0; i < get_length(); ++i) if (at(i).in_matrix(width, height)) kept.append(at(i));
        *this = std::move(kept); }

    // Append every Point from another Points collection (Vector::append for-each loop).
    inline void append(const Points & other) noexcept { Vector<Point>::append(other); }

    // Connect consecutive Points with lines via Point::get_line. Returns a flattened Vector<Point> sampling every pair (last=false on all but the final pair to avoid duplicating shared endpoints). Two-pass: first count total samples, then allocate exactly + fill.
    inline Vector<Point> get_lines() const noexcept {
        const size_t n = get_length();
        if (n == 0) return Vector<Point>(0);
        if (n == 1) { Vector<Point> single(1); single.append(at(0)); return single; }

        size_t total = 0;
        for (size_t i = 0; i + 1 < n; ++i) {
            const bool   last     = (i + 2 == n);
            const size_t seg_size = at(i).get_line_size(at(i + 1));    // includes both endpoints
            total += last ? seg_size : seg_size - 1;                    // drop trailing endpoint except on final segment
        }

        Vector<Point> out(total);
        for (size_t i = 0; i + 1 < n; ++i) {
            const bool last = (i + 2 == n);
            Vector<Point> seg = at(i).get_line(at(i + 1), last);
            for (size_t j = 0; j < seg.get_length(); ++j) out.append(seg.at(j)); }
        return out; }
};


extern "C" {
    Points * points_new          (size_t capacity) noexcept { return new Points(capacity); }
    void     points_delete       (Points * ps) noexcept { delete ps; }
    void     points_clear        (Points * ps) noexcept { ps->clear(); }
    void     points_append_point (Points * ps, Point * p) noexcept { ps->append(*p); }
    void     points_append_points(Points * ps, Points * other) noexcept { ps->append(*other); }
    Point  * points_get_point    (Points * ps, size_t i) noexcept { return new Point(ps->at(i)); }   // returns a copy, Python owns and frees it
    size_t   points_get_length   (Points * ps) noexcept { return ps->get_length(); }
    void     points_log          (Points * ps) noexcept { ps->log(); }
    Points * points_copy         (Points * ps) noexcept { return new Points(*ps); }

    void     points_add_offset       (Points * ps, size_t dx, size_t dy) noexcept { ps->add_offset(dx, dy); }
    void     points_select_in_matrix (Points * ps, size_t w, size_t h) noexcept { ps->select_in_matrix(w, h); }
    void     points_fix_background   (Points * ps, Pixel * p) noexcept { ps->fix_background(*p); }
    void     points_squash           (Points * ps, Grid * g) noexcept { ps->squash(*g); }
    void     matrix_insert_points    (Matrix * m, Points * pts) noexcept { m->insert(*pts); }
}


// Stamp every Point in the collection. Declared inside Matrix's class body in 07_matrix.cpp; defined here because Points must be fully declared first.
inline void Matrix::insert(const Points & ps) noexcept {
    for (size_t i = 0; i < ps.get_length(); ++i) insert(ps.at(i)); }
