// Point: a 2D position (from PointPosition) carrying a Marker, with geometric helpers and line generation

class Point : public PointPosition, public Marker {
public:
    // --- Constructors ---

    // Default constructor
    constexpr Point() noexcept = default;

    // Construct from coordinates plus an optional marker
    Point(float xi, float yi, const Marker & m = Marker()) noexcept { set(xi, yi, m); }

    // Construct from coordinates plus a template point (marker copied)
    Point(float xi, float yi, const Point & p) noexcept : PointPosition(xi, yi), Marker(p) {}

    // Construct from a PointPosition and a Marker
    Point(const PointPosition & pp, const Marker & m) noexcept : PointPosition(pp), Marker(m) {}

    // Copy constructor
    Point(const Point & p) noexcept = default;

    // Move constructor
    Point(Point && p) noexcept = default;

    // Destructor
    ~Point() noexcept {}

    // --- Comparison / assignment ---

    // Equality comparison (marker + position both match)
    inline bool operator==(const Point & other) const noexcept { return Marker::operator==(other) && PointPosition::operator==(other); }

    // Inequality comparison
    inline bool operator!=(const Point & other) const noexcept { return !(*this == other); }

    // Copy assignment
    inline Point & operator=(const Point & p) noexcept { set(p.get_x(), p.get_y(), p.get_marker()); return *this; }

    // Move assignment
    inline Point & operator=(Point && p) noexcept { PointPosition::operator=(std::move(p)); Marker::operator=(std::move(p)); return *this; }

    // --- Set / get ---

    // Set position and marker in one call
    inline void set(float xi, float yi, const Marker & m) noexcept { PointPosition::set(xi, yi); Marker::operator=(m); }

    // Copy position and marker from another point
    inline void set(const Point & p) noexcept { set(p.get_x(), p.get_y(), p.get_marker()); }

    // Get the marker type (none / normal / hd / fhd / braille)
    constexpr marker_type get_type() const noexcept { return MarkerType::get(); }

    // Access the marker
    inline const Marker & get_marker() const noexcept { return *this; }

    // Inner sub-column of the marker cell
    inline unsigned char get_inner_col() const noexcept { return PointPosition::get_inner_col(get_cols()); }

    // Inner sub-row of the marker cell
    inline unsigned char get_inner_row() const noexcept { return PointPosition::get_inner_row(get_rows()); }

    // --- Rounded / interpolation helpers ---

    // Return a point centered within its marker cell (for sub-marker placement)
    Point get_rounded_point() const noexcept {
        float col = get_col() + (2.0f * get_inner_col() + 1) / (2 * get_cols());
        float row = get_row() + (2.0f * get_inner_row() + 1) / (2 * get_rows());
        return Point(col, row, *this);}

    // Approximate equality including inner cell coordinates
    inline bool is_close(const Point & p) const noexcept {
        return Marker::operator==(p)
            && get_col() == p.get_col()
            && get_row() == p.get_row()
            && get_inner_col() == p.get_inner_col()
            && get_inner_row() == p.get_inner_row();}

    // Linear interpolation along the line from this to p at parameter t in [0, 1]
    inline Point get_line_point(const Point & p, const float & t) const noexcept {
        float x = get_x(); float y = get_y();
        x += (p.get_x() - x) * t;
        y += (p.get_y() - y) * t;
        return Point(x, y, *this);}

    // --- Grid distance / line length helpers ---

    // Absolute difference in x expressed in sub-columns
    inline size_t get_xsteps(const Point & p) const noexcept {
        const size_t cols = get_cols();
        return static_cast<size_t>(std::abs(static_cast<int>(get_x() * cols) - static_cast<int>(p.get_x() * cols)));}

    // Absolute difference in y expressed in sub-rows
    inline size_t get_ysteps(const Point & p) const noexcept {
        const size_t rows = get_rows();
        return static_cast<size_t>(std::abs(static_cast<int>(get_y() * rows) - static_cast<int>(p.get_y() * rows)));}

    // Estimated length of a simple (diagonal) line to p
    inline size_t get_simple_line_length(const Point & p) const noexcept {if (p.is_none()) {return 2;} else {return std::max({get_xsteps(p), get_ysteps(p), (size_t)1}) + 1;}}

    // Upper bound length for a full-grid-walking line to p
    inline size_t get_full_line_length(const Point & p) const noexcept {if( p.is_none()) {return 2;} else {return get_xsteps(p) + get_ysteps(p) + 3; }}

    // Choose between simple and full line length
    inline size_t get_line_length(const Point & p, bool method) const noexcept { if (method) { return get_full_line_length(p); } else { return get_simple_line_length(p); } }

    // Midpoint between this point and p (marker copied from this)
    inline Point get_middle_point(const Point & p) const noexcept { return Point(get_middle(p), *this); }

    // --- Line generation (simple) ---

    // Generate evenly-spaced points between this and p (simple method)
    inline Vector<Point> get_simple_line(const Point & p, bool last = true) const noexcept {
        Point start = *this; Point end = p; // copy endpoints
        Numerical<float> parameters = linspace<float>(0, 1, start.get_simple_line_length(end));
        Vector<Point> out(parameters.get_length());
        out.append(*this);
        for (size_t i = 1; i < parameters.get_length() - 1; i++) { out.append(start.get_line_point(end, parameters.at(i))); } // internal points
        if (last and not is_close(p)) { out.append(p); } // optionally append endpoint
        return out;}

    // Generate points crossing every grid cell boundary between this and p (full method)
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

    // Dispatcher for line generation (full when method=true, simple when method=false)
    inline Vector<Point> get_line(const Point & p, bool last = true, bool method = 0) const noexcept { if (method) { return get_full_line(p, last); } else { return get_simple_line(p, last); }}

    // Get wide string representation "(x, y, marker)" or "none"
    std::wstring get_wstring() const {
        if (is_none()) {
            return L"none";}

        wchar_t buffer[50];

        swprintf(buffer, sizeof(buffer) / sizeof(wchar_t),
                 L"(%.2f, %.2f, %ls)",
                 get_x(), get_y(),
                 get_marker().get_wstring().c_str());

        return buffer; }

    // Get narrow string representation
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout (no newline)
    inline void log() const noexcept { wcout << get_wstring() << flush; }

    // Log only the position
    inline void log_position() const noexcept { PointPosition::log(); }

    // Wide-stream output
    friend inline wostream & operator<<(wostream & os, const Point & v) { os << v.get_wstring(); return os; }

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Point & c) noexcept {os << c.get_string(); return os;}
};


// --- C API for Point ---
extern "C" {
    // Create a new point at (x, y) with the given marker
    Point* point_new_marker(float x, float y, const Marker * m) noexcept { return new Point(x, y, *m); }

    // Delete a point
    void point_delete(Point* p) noexcept { delete p; }

    // Get the x coordinate
    float point_get_x(const Point* p) noexcept { return p->get_x(); }

    // Get the y coordinate
    float point_get_y(const Point* p) noexcept { return p->get_y(); }

    // Return the rendered wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t * point_get_wstring(Point * c) noexcept { return wstring_to_cstring(c->get_wstring()); }

    // Log the point to wcout
    void point_log(const Point* p) noexcept { p->log(); }
}
