// PointFilled: a Point with an optional companion "fill" point used for stem plots and filled regions

class PointFilled : public Point {
private:
    Point fill; // the fill point

public:
    // --- Constructors ---

    // Default constructor
    PointFilled() = default;

    // Construct from coordinates and an optional marker; fill defaults to none at the same coords
    PointFilled(const float & xi, const float & yi, const Marker & m = Marker()) : Point(xi, yi, m), fill(xi, yi, Marker(none)) {}

    // Construct from coordinates, a character and an optional pixel
    PointFilled(const float & xi, const float & yi, const wchar_t & c, const Pixel & p = Pixel()) : PointFilled(xi, yi, Marker(c, p)) {}

    // Construct from coordinates and a marker type
    PointFilled(const float & xi, const float & yi, const marker_type & t) : Point(xi, yi, t), fill(xi, yi, Marker(none)) {}

    // Copy constructor
    PointFilled(const PointFilled & other) : Point(other), fill(other.fill) {}

    // Construct from an explicit main point and fill point
    PointFilled(const Point & main, const Point & fill) : Point(main), fill(fill) {}

    // Move-construct from explicit main and fill points
    PointFilled(Point && main, Point && fill) : Point(move(main)), fill(move(fill)) {}

    // Move constructor
    PointFilled(PointFilled && other) noexcept : Point(std::move(other)), fill(std::move(other.fill)) {}

    // Construct from a single point (fill defaults to none at the same coords)
    PointFilled(const Point & point) : Point(point), fill(point.get_x(), point.get_y(), Marker(none)) {}

    // Destructor
    ~PointFilled() noexcept {}

    // --- Assignment ---

    // Copy assignment
    inline PointFilled & operator=(const PointFilled & other) {
        Point::operator=(other);
        fill = other.fill;
        return *this;}

    // Move assignment
    inline PointFilled & operator=(PointFilled && other) noexcept {
        Point::operator=(std::move(other));
        fill = std::move(other.fill);
        return *this;}

    // --- Setters ---

    // Set the main point from another point
    inline void set_main(const Point & p) { Point::set(p); }

    // Set the main point from coordinates and a marker
    inline void set_main(const float & xi, const float & yi, const Marker & m) { Point::set(xi, yi, m); }

    // Set the fill point from another point
    inline void set_fill(const Point & p) { fill.set(p); }

    // Set the fill point from coordinates and a marker (inherits main's background)
    inline void set_fill(const float & xi, const float & yi, const Marker & m) {
        fill.set(xi, yi, m);
        fill.fix(*this);}

    // --- Drawing logic ---

    // Fix the background of main and fill against the given pixel
    inline void fix_background(const Pixel & pixel) {
        Point::fix_background(pixel);
        if (!fill.is_none()) fill.fix_background(pixel);}

    // --- Getters ---

    // Access the main point
    inline const Point & get_main() const { return *this; }

    // Access the fill point (const)
    inline const Point & get_fill() const { return fill; }

    // Access the fill point (mutable)
    inline Point & get_fill() { return fill; }

    // True if there is no fill point
    inline bool no_fill() const { return fill.is_none(); }

    // --- Bounds ---

    // Minimum x across main and fill
    inline float get_xmin() const { return no_fill() ? get_x() : std::min(get_x(), fill.get_x()); }

    // Maximum x across main and fill
    inline float get_xmax() const { return no_fill() ? get_x() : std::max(get_x(), fill.get_x()); }

    // Minimum y across main and fill
    inline float get_ymin() const { return no_fill() ? get_y() : std::min(get_y(), fill.get_y()); }

    // Maximum y across main and fill
    inline float get_ymax() const { return no_fill() ? get_y() : std::max(get_y(), fill.get_y()); }

    // True if both main and fill are inside a matrix of the given size
    constexpr bool in_matrix(const size_t & width, const size_t & height) const noexcept {
        return Point::in_matrix(width, height) and fill.in_matrix(width, height);}

    // --- Connections ---

    // Generate a line of PointFilled between this and p by pairing main and fill line points
    Vector<PointFilled> get_line(const PointFilled & p, bool last = false, bool method = 0) const {
        const Point & m0 = get_main(); const Point & m1 = p.get_main();
        const Point & f0 = get_fill(); const Point & f1 = p.get_fill();

        Vector<Point> main_points = m0.get_line(m1, last, method);
        Vector<Point> fill_points = f0.get_line(f1, last, method);

        size_t n_main = main_points.get_length();
        size_t n_fill = fill_points.get_length();

        // Equalize lengths
        if (n_main > n_fill) { fill_points.reserve(n_main); fill_points.stretch(n_main); }
        else if (n_main < n_fill) { main_points.reserve(n_fill); main_points.stretch(n_fill); }

        // Merge into PointFilled objects
        size_t n = max(n_main, n_fill);
        Vector<PointFilled> out(n);

        for (size_t i = 0; i < n; ++i)
            out.append(PointFilled(main_points.at(i), fill_points.at(i)));

        return out;}

    // Generate the line of Point from main down to fill
    inline Vector<Point> get_filled_line(bool method = 0) const noexcept {
        Point p1 = get_main(); Point p2 = get_fill();
        return p1.get_line(p2, true, method);}

    // Approximate equality on both main and fill
    inline bool is_close(const PointFilled & p) {
        return Point::is_close(p.get_main()) and fill.is_close(p.get_fill());}

    // --- Transformations ---

    // Rescale x of both main and fill
    inline void rescale_x(const std::pair<float,float> & xlim, const size_t & width, const float & delta) noexcept {
        Point::rescale_x(xlim, width, delta);
        fill.rescale_x(xlim, width, delta);}

    // Rescale y of both main and fill
    inline void rescale_y(const std::pair<float,float> & ylim, const size_t & height, const float & delta) noexcept {
        Point::rescale_y(ylim, height, delta);
        fill.rescale_y(ylim, height, delta);}

    // Apply log10 to x of both main and fill
    inline void log_x() noexcept { Point::log_x(); fill.log_x(); }

    // Apply log10 to y of both main and fill
    inline void log_y() noexcept { Point::log_y(); fill.log_y(); }

    // Add (dx, dy) offset to both main and fill
    inline void add_offset(const size_t & dx, const size_t & dy) noexcept {
        Point::add_offset(dx, dy);
        fill.add_offset(dx, dy);}

    // --- Display ---

    // Get wide string "main [→ fill]"
    inline wstring get_wstring(const bool & include_fill = true) const {
        std::wostringstream woss;
        woss << Point::get_wstring();
        if (include_fill) woss << L" → " << fill.get_wstring();
        return woss.str();}

    // Get narrow string
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Wide-stream output
    friend inline std::wostream & operator<<(std::wostream & os, const PointFilled & v) {return os << v.get_wstring(true);}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const PointFilled & c) noexcept {os << c.get_string(); return os;}

    // Log to wcout
    inline void log(const bool & include_fill = true) const { wcout << get_wstring(include_fill); }
};


// --- C API ---
extern "C" {
    // Create a new PointFilled at (x, y) with the given marker
    PointFilled * point_filled_new(float x, float y, Marker * c) { return new PointFilled(x, y, *c); }

    // Delete a PointFilled
    void point_filled_delete(PointFilled * p) { delete p; }

    // Get a heap-allocated copy of the marker
    Marker * point_filled_get_marker(PointFilled * p) { return new Marker(p->get_marker()); }

    // Integer column (truncated x)
    size_t point_filled_get_col(PointFilled * c) noexcept { return c->get_col(); }

    // Integer row (truncated y)
    size_t point_filled_get_row(PointFilled * c) noexcept { return c->get_row(); }

    // Get the x coordinate
    float point_filled_get_x(PointFilled * c) noexcept { return c->get_x(); }

    // Get the y coordinate
    float point_filled_get_y(PointFilled * c) noexcept { return c->get_y(); }

    // Return the rendered wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t * point_filled_get_wstring(PointFilled * c, bool fill) { return wstring_to_cstring(c->get_wstring(fill)); }

    // Get the foreground palette index from the marker's pixel
    unsigned char point_filled_get_code(const PointFilled * c) noexcept { return c->get_fullground_integer_code(); }
}
