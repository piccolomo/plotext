// Point: 2D point with position and marker information (position + marker behavior)

class Point : public PointPosition, public Marker {
public:
    // --- Constructors ---
    constexpr Point() noexcept = default;                                    // default
    Point(float xi, float yi, const Marker & m = Marker()) noexcept { set(xi, yi, m); } // set from coords + marker
    Point(float xi, float yi, const Point & p) noexcept : PointPosition(xi, yi), Marker(p) {} // construct from point
    Point(const PointPosition & pp, const Marker & m) noexcept : PointPosition(pp), Marker(m) {} // from parts
    Point(const Point & p) noexcept = default;                              // copy
    Point(Point && p) noexcept = default;                                   // move

    // --- Comparison / assignment ---
    inline bool operator==(const Point & other) const noexcept { return Marker::operator==(other) && PointPosition::operator==(other); } // equal if marker+pos equal
    inline bool operator!=(const Point & other) const noexcept { return !(*this == other); } // inequality

    inline Point & operator=(const Point & p) noexcept { set(p.get_x(), p.get_y(), p.get_marker()); return *this; } // assign from point

    // --- Set / get ---
    inline void set(float xi, float yi, const Marker & m) noexcept { PointPosition::set(xi, yi); Marker::operator=(m); } // set pos+marker
    inline void set(const Point & p) noexcept { set(p.get_x(), p.get_y(), p.get_marker()); } // set from point

    constexpr marker_type get_type() const noexcept { return MarkerType::get(); } // marker type
    inline const Marker & get_marker() const noexcept { return *this; } // access marker

    // Inner cell coordinates helpers
    inline unsigned char get_inner_col() const noexcept { return PointPosition::get_inner_col(get_cols()); } // sub-column
    inline unsigned char get_inner_row() const noexcept { return PointPosition::get_inner_row(get_rows()); } // sub-row

    // --- Rounded / interpolation helpers ---
    Point get_rounded_point() const noexcept { // returns a point centered for sub-marker placement
        float col = get_col() + (2.0f * get_inner_col() + 1) / (2 * get_cols());
        float row = get_row() + (2.0f * get_inner_row() + 1) / (2 * get_rows());
        return Point(col, row, *this);}

    inline bool is_close(const Point & p) const noexcept { // approximate equality including inner coords
        return Marker::operator==(p)
            && get_col() == p.get_col()
            && get_row() == p.get_row()
            && get_inner_col() == p.get_inner_col()
            && get_inner_row() == p.get_inner_row();}

    inline Point get_line_point(const Point & p, const float & t) const noexcept { // linear interpolate along line
        float x = get_x(); float y = get_y();
        x += (p.get_x() - x) * t;
        y += (p.get_y() - y) * t;
        return Point(x, y, *this);}

    // --- Grid distance / line length helpers ---
    inline size_t get_xsteps(const Point & p) const noexcept {
        const size_t cols = get_cols();
        return static_cast<size_t>(std::abs(static_cast<int>(get_x() * cols) - static_cast<int>(p.get_x() * cols)));}

    inline size_t get_ysteps(const Point & p) const noexcept {
        const size_t rows = get_rows();
        return static_cast<size_t>(std::abs(static_cast<int>(get_y() * rows) - static_cast<int>(p.get_y() * rows)));}

    inline size_t get_simple_line_length(const Point & p) const noexcept { return std::max({get_xsteps(p), get_ysteps(p), (size_t)1}) + 1; } // estimate simple length
    inline size_t get_full_line_length(const Point & p) const noexcept { return get_xsteps(p) + get_ysteps(p) + 3; } // upper bound length
    inline size_t get_line_length(const Point & p, bool method) const noexcept { if (method) { return get_full_line_length(p); } else { return get_simple_line_length(p); } } // choose method

    inline Point get_middle_point(const Point & p) const noexcept { return Point(get_middle(p), *this); } // middle between cells

    // --- Line generation (simple) ---
    inline Vector<Point> get_simple_line(const Point & p, bool last = true) const noexcept {
        Point start = *this; Point end = p; // copy endpoints
        Numerical<float> parameters = linspace<float>(0, 1, start.get_simple_line_length(end));
        Vector<Point> out(parameters.get_length());
        out.append(*this);
        for (size_t i = 1; i < parameters.get_length() - 1; i++) { out.append(start.get_line_point(end, parameters.at(i))); } // internal points
        if (last and not is_close(p)) { out.append(p); } // optionally append endpoint
        return out;}

    inline Vector<Point> get_full_line(const Point & p, bool last = true) const noexcept {
        const size_t cols = get_cols();
        const size_t rows = get_rows();

        float x0 = get_x() * cols;
        float x1 = p.get_x() * cols;
        float y0 = get_y() * rows;
        float y1 = p.get_y() * rows;

        float dx = x1 - x0;
        float dy = y1 - y0;
        float m  = dy / dx;
        float mi = 1 / m;

        float x_int, y_int;
        float delta_x = 1, delta_y = 1;

        if (dx >= 0) { x_int = floor(x0) + 1; }
        else         { x_int = ceil(x0) - 1; delta_x = -1; }

        if (dy >= 0) { y_int = floor(y0) + 1; }
        else         { y_int = ceil(y0) - 1; delta_y = -1; }

        float x_line, y_line;

        size_t size = get_full_line_length(p);
        Vector<Point> crossings(size + 4);

        crossings.append(*this);

        Point previous, next, middle;
        previous = *this;

        while (true) {

            bool test_x = (delta_x * (x_int - x0)) < (delta_x * dx);
            bool test_y = (delta_y * (y_int - y0)) < (delta_y * dy);

            if (not (test_x or test_y))
                break;

            x_line = x0 + mi * (y_int - y0);
            y_line = y0 + m  * (x_int - x0);

            if (abs(abs(m) - 1) < 1e-4) {
                write("m=1");
                next   = Point(x_int / cols, y_int / rows, *this);
                middle = previous.get_middle_point(next);
                x_int += delta_x;
                y_int += delta_y;}

            else if (delta_x * (x_line - x_int) >= 0) {
                y_line = y0 + m * (x_int - x0);
                next   = Point(x_int / cols, y_line / rows, *this);
                middle = previous.get_middle_point(next);
                x_int += delta_x;}

            else if (delta_y * (y_line - y_int) >= 0) {
                next   = Point(x_line / cols, y_int / rows, *this);
                middle = previous.get_middle_point(next);
                y_int += delta_y;}

            crossings.append(middle);
            previous = next;}

        crossings.append(previous.get_middle_point(p));

        if (last and not is_close(p))
            crossings.append(p);

        return crossings;}

    // Dispatcher for line generation
    inline Vector<Point> get_line(const Point & p, bool last = true, bool method = 0) const noexcept { if (method) { return get_full_line(p, last); } else { return get_simple_line(p, last); }}

    // --- String / output helpers ---
    wstring get_wstring() const {
        wchar_t buffer[128]; // NB: adjust if needed for bigger representations
        swprintf(buffer, sizeof(buffer) / sizeof(wchar_t), L"(%ls, %ls)",
                 PointPosition::get_wstring().c_str(),
                 Marker::get_wstring().c_str());
        return wstring(buffer);}

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    inline void log() const noexcept { wcout << get_wstring() << flush; } // quick print
    inline void log_position() const noexcept { PointPosition::log(); } // print position only

    // Stream operator
    friend inline wostream & operator<<(wostream & os, const Point & v) { os << v.get_wstring(); return os; }

    friend ostream & operator<<(ostream & os, const Point & c) noexcept {os << c.get_string(); return os;}
}; // class Point


// --- C API for Point ---
extern "C" {
    // Creation / destruction
    Point* point_new_marker(float x, float y, const Marker * m) noexcept { return new Point(x, y, *m); }
    void point_delete(Point* p) noexcept { delete p; }

    // Getters
    float point_get_x(const Point* p) noexcept { return p->get_x(); }
    float point_get_y(const Point* p) noexcept { return p->get_y(); }

    // Logging / wstring
    const wchar_t * point_get_wstring(Point * c) noexcept { return wstring_to_cstring(c->get_wstring()); }
    void point_log(const Point* p) noexcept { p->log(); }
}
