// Point with an optional fill point
class PointFilled : public Point {
private:
    Point fill; // the fill point

public:
    // --- Constructors ---
    PointFilled() = default;

    PointFilled(const float & xi, const float & yi, const Marker & m = Marker()) : Point(xi, yi, m), fill(xi, yi, Marker(none)) {}

    PointFilled(const float & xi, const float & yi, const wchar_t & c, const Pixel & p = Pixel()) : PointFilled(xi, yi, Marker(c, p)) {}

    PointFilled(const float & xi, const float & yi, const marker_type & t) : Point(xi, yi, t), fill(xi, yi, Marker(none)) {}

    PointFilled(const PointFilled & other) : Point(other), fill(other.fill) {}

    PointFilled(const Point & main, const Point & fill) : Point(main), fill(fill) {}

    PointFilled(Point && main, Point && fill) : Point(move(main)), fill(move(fill)) {}

    PointFilled(PointFilled && other) noexcept : Point(std::move(other)), fill(std::move(other.fill)) {}

    PointFilled(const Point & point) : Point(point), fill(point.get_x(), point.get_y(), Marker(none)) {} // fill defaults to none

    // --- Assignment ---
    inline PointFilled & operator=(const PointFilled & other) {
        Point::operator=(other);
        fill = other.fill;
        return *this;}

    inline PointFilled & operator=(PointFilled && other) noexcept {
        Point::operator=(std::move(other));
        fill = std::move(other.fill);
        return *this;}

    // --- Setters ---
    inline void set_main(const Point & p) { Point::set(p); }
    inline void set_main(const float & xi, const float & yi, const Marker & m) { Point::set(xi, yi, m); }

    inline void set_fill(const Point & p) { fill.set(p); }
    inline void set_fill(const float & xi, const float & yi, const Marker & m) {
        fill.set(xi, yi, m);
        fill.fix(*this);} // ensure fill overlays correctly

    // --- Drawing logic ---
    inline void fix_background(Pixel & pixel) {
        Point::fix_background(pixel);
        if (!fill.is_none()) fill.fix_background(pixel);}

    // --- Getters ---
    inline const Point & get_main() const { return *this; }
    inline const Point & get_fill() const { return fill; }
    inline Point & get_fill() { return fill; }
    inline bool no_fill() const { return fill.is_none(); }

    // --- Bounds ---
    inline float get_xmin() const { return std::min(get_x(), fill.get_x()); }
    inline float get_xmax() const { return std::max(get_x(), fill.get_x()); }
    inline float get_ymin() const { return std::min(get_y(), fill.get_y()); }
    inline float get_ymax() const { return std::max(get_y(), fill.get_y()); }

    // Check if both main + fill are inside matrix
    constexpr bool in_matrix(const size_t & width, const size_t & height) const noexcept {
        return Point::in_matrix(width, height) and fill.in_matrix(width, height);}

    // --- Connections ---
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

    // Line from main → fill
    inline Vector<Point> get_filled_line(bool method = 0) const noexcept {
        Point p1 = get_main(); Point p2 = get_fill();
        return p1.get_line(p2, true, method);}

    // Close check
    inline bool is_close(const PointFilled & p) {
        return Point::is_close(p.get_main()) and fill.is_close(p.get_fill());}

    // --- Transformations ---
    inline void rescale_x(const std::pair<float,float> & xlim, const size_t & width, const float & delta) noexcept {
        Point::rescale_x(xlim, width, delta);
        fill.rescale_x(xlim, width, delta);}

    inline void rescale_y(const std::pair<float,float> & ylim, const size_t & height, const float & delta) noexcept {
        Point::rescale_y(ylim, height, delta);
        fill.rescale_y(ylim, height, delta);}

    inline void log_x() noexcept { Point::log_x(); fill.log_x(); }
    inline void log_y() noexcept { Point::log_y(); fill.log_y(); }

    inline void add_offset(const size_t & dx, const size_t & dy) noexcept {
        Point::add_offset(dx, dy);
        fill.add_offset(dx, dy);}

    // --- Display ---
    inline wstring get_wstring(const bool & include_fill = true) const {
        std::wostringstream woss;
        woss << Point::get_wstring();
        if (include_fill) woss << L" → " << fill.get_wstring();
        return woss.str();}

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    friend inline std::wostream & operator<<(std::wostream & os, const PointFilled & v) {return os << v.get_wstring(true);}
    friend ostream & operator<<(ostream & os, const PointFilled & c) noexcept {os << c.get_string(); return os;}

    inline void log(const bool & include_fill = true) const { wcout << get_wstring(include_fill); }
};


// --- C API ---
extern "C" {
    Point * point_filled_new(float x, float y, Marker * c) { return new PointFilled(x, y, *c); }
    void point_filled_delete(PointFilled * p) { delete p; }
    Marker * point_filled_get_marker(PointFilled * p) { return new Marker(p->get_marker()); }
    size_t point_filled_get_col(PointFilled * c) noexcept { return c->get_col(); }
    size_t point_filled_get_row(PointFilled * c) noexcept { return c->get_row(); }
    float point_filled_get_x(PointFilled * c) noexcept { return c->get_x(); }
    float point_filled_get_y(PointFilled * c) noexcept { return c->get_y(); }
    const wchar_t * point_filled_get_wstring(PointFilled * c, bool fill) { return wstring_to_cstring(c->get_wstring(fill)); }
    unsigned char point_filled_get_code(const PointFilled * c) noexcept { return c->get_fullground_integer_code(); }
}
