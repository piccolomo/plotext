// FilledPoint: a Point with a companion "fill" Point. Used for stem plots, bar plots, area-under-curve. Drawing it produces the line of Points from main to fill (inclusive of both endpoints).

class FilledPoint : public Point {
private:
    Point fill;            // companion endpoint, when has_marker() is true, defines the fill segment
    bool  connected = false;  // true = a line is drawn from the previous FilledPoint to this one (set via signal.lines() / signal.line())

public:
    FilledPoint() noexcept = default; 
    FilledPoint(float x, float y, Marker * m = nullptr) noexcept : Point(x, y, m), fill(x, y) {}
    FilledPoint(float x, float y, Marker * m, const Point & f) noexcept : Point(x, y, m), fill(f) {} 
    FilledPoint(const Point & main, const Point & f) noexcept : Point(main), fill(f) {}

    // Explicit rule-of-five, the compiler-generated defaults rely on every base/member's copy/move ctor being trivial-or-correct. With polymorphic Marker* ownership in Point, that's fragile (subtle UB if any path picks the wrong default). Defining all five explicitly eliminates that class of bugs.
    FilledPoint(const FilledPoint & o) noexcept : Point(o), fill(o.fill), connected(o.connected) {}
    FilledPoint(FilledPoint && o) noexcept : Point(std::move(o)), fill(std::move(o.fill)), connected(o.connected) {}
    FilledPoint & operator=(const FilledPoint & o) noexcept {
        if (this != &o) { Point::operator=(o); fill = o.fill; connected = o.connected; }
        return *this; }
    FilledPoint & operator=(FilledPoint && o) noexcept {
        if (this != &o) { Point::operator=(std::move(o)); fill = std::move(o.fill); connected = o.connected; }
        return *this; }
    ~FilledPoint() noexcept = default;

    inline       Point & get_fill()       noexcept { return fill; }
    inline const Point & get_fill() const noexcept { return fill; }
    inline void          set_fill(const Point & f) noexcept { fill = f; }
    inline void          set_fill(float x, float y, Marker * m) noexcept { fill = Point(x, y, m); }
    inline void          set_main(float x, float y, Marker * m) noexcept { *static_cast<Point*>(this) = Point(x, y, m); }
    inline bool          has_fill() const noexcept { return fill.has_marker(); }

    inline float         get_xmin() const noexcept { return std::min(get_x(), fill.get_x()); }
    inline float         get_xmax() const noexcept { return std::max(get_x(), fill.get_x()); }
    inline float         get_ymin() const noexcept { return std::min(get_y(), fill.get_y()); }
    inline float         get_ymax() const noexcept { return std::max(get_y(), fill.get_y()); }

    inline bool          is_connected()             const noexcept { return connected; }
    inline void          set_connected(bool value)        noexcept { connected = value; }

    // Generate the line of Points from main down to fill (uses Point::get_line). When has_fill() is false, returns just the main point. method=false is the simple linspace line; method=true is the full grid-cell-crossing line (denser, fills wedges between adjacent fan rays).
    inline Vector<Point> get_filled_line(bool method = false) const noexcept {
        if (!has_fill()) { Vector<Point> single(1); single.append(*this); return single; }
        return get_line(fill, true, method); }

    inline wstring get_wstring() const {
        wstring s = Point::get_wstring();
        if (has_fill()) { s += L", fill point "; s += fill.get_wstring(); }
        return s; }

    inline void log() const { wcout << L"FilledPoint(" << get_wstring() << L")" << endl; }
};


extern "C" {
    FilledPoint * point_filled_new   (float x, float y, Marker * m) noexcept { return new FilledPoint(x, y, m); }
    void          point_filled_delete(FilledPoint * fp) noexcept { delete fp; }

    // Returns a COPY of the marker (Python wraps it in its own marker primitive whose __del__ will free it; sharing the pointer would double-free).
    Marker *      point_filled_get_marker(FilledPoint * fp) noexcept { Marker * m = fp->get_marker(); return m ? m->copy() : nullptr; }

    size_t        point_filled_get_col (FilledPoint * fp) noexcept { return fp->get_col(); }
    size_t        point_filled_get_row (FilledPoint * fp) noexcept { return fp->get_row(); }
    float         point_filled_get_x   (FilledPoint * fp) noexcept { return fp->get_x(); }
    float         point_filled_get_y   (FilledPoint * fp) noexcept { return fp->get_y(); }
    // Returns a heap-allocated copy of the main/fill marker's pixel (Python wraps it; nullptr if no marker).
    Pixel *       point_filled_get_main_pixel(FilledPoint * fp) noexcept { Marker * m = fp->get_marker();             return m ? new Pixel(m->get_pixel()) : nullptr; }
    Pixel *       point_filled_get_fill_pixel(FilledPoint * fp) noexcept { Marker * m = fp->get_fill().get_marker();  return m ? new Pixel(m->get_pixel()) : nullptr; }
    bool          point_filled_has_fill(FilledPoint * fp) noexcept { return fp->has_fill(); }

    // bool param ignored, our get_wstring always includes the fill segment.
    const wchar_t * point_filled_get_wstring(FilledPoint * fp, bool) noexcept { return wstring_to_cstring(fp->get_wstring()); }
}


// Stamp a FilledPoint: walks the main→fill line via get_filled_line() and stamps each Point. Declared inside Matrix's class body in 07_matrix.cpp; defined here because FilledPoint must be fully declared first.
inline void Matrix::insert(const FilledPoint & fp) noexcept {
    Vector<Point> line = fp.get_filled_line();
    for (size_t i = 0; i < line.get_length(); ++i) insert(line.at(i)); }
