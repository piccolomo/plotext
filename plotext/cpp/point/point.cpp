// A class to represent a 2D point with position, marker, and fill attributes.
// Inherits from PointPosition, Marker, and PointFill.

class Point : public PointPosition, public Marker {
public:
    // Constructors
    constexpr Point() noexcept = default;

    Point(float xi, float yi, const Marker & m = Marker()) noexcept {
        set(xi, yi, m);}

    Point(float xi, float yi, const Point & p) noexcept
        : PointPosition(xi, yi), Marker(p) {}

    Point(const Point & p) noexcept = default;
    Point(Point && p) noexcept = default;

    // Assignment operator
    Point & operator=(const Point & p) noexcept {
        set(p.get_x(), p.get_y(), p.get_marker());
        return *this;}

    // Set position + marker
    void set(float xi, float yi, const Marker & m) noexcept {
        PointPosition::set(xi, yi);
        Marker::operator=(m);}

    void set(const Point & p) noexcept { set(p.get_x(), p.get_y(), p.get_marker()); }

    // Marker type & marker access
    constexpr marker_type get_type() const noexcept { return MarkerType::get(); }
    inline const Marker & get_marker() const noexcept { return *this; }

    // Inner coordinates for sub-marker positioning
    unsigned char get_inner_col() const noexcept { return PointPosition::get_inner_col(get_cols()); }
    unsigned char get_inner_row() const noexcept { return PointPosition::get_inner_row(get_rows()); }

    // Check approximate proximity
    bool is_close(const Point & p) const noexcept {
        return Marker::operator==(p)
            && get_inner_col() == p.get_inner_col()
            && get_inner_row() == p.get_inner_row();}

    // Compute line length in grid units
    size_t get_line_length(const Point & p) const noexcept {
        const size_t cols = get_cols();
        const size_t rows = get_rows();
        size_t Dx = static_cast<size_t>(std::abs(static_cast<int>(get_x() * cols) - static_cast<int>(p.get_x() * cols)));
        size_t Dy = static_cast<size_t>(std::abs(static_cast<int>(get_y() * rows) - static_cast<int>(p.get_y() * rows)));
        return std::max(Dx, Dy) + 1; }

    // Generate points along a line
    Vector<Point> get_line(const Point & p, size_t count, bool last = false) const {
        Vector<Point> out(count);
        if (count == 0) return out;

        out.append(*this); // first point

        const float Dx = p.get_x() - get_x();
        const float Dy = p.get_y() - get_y();
        const float inv_len = 1.0f / static_cast<float>(count - 1);

        for (size_t i = 1; i < count - 1; i++) {
            float t = inv_len * i;
            out.move_back(Point(get_x() + t * Dx, get_y() + t * Dy, *this));}

        if (last && count > 1) out.append(p);
        return out;}

    // Fast wide string representation
    wstring get_wstring() const {
        wchar_t buffer[128]; // Adjust size if needed
        swprintf(buffer, sizeof(buffer)/sizeof(wchar_t), L"(%ls, %ls)",
                 PointPosition::get_wstring().c_str(),
                 Marker::get_wstring().c_str());
        return wstring(buffer);}

    // Output operator
    friend inline std::wostream& operator<<(std::wostream& os, const Point& v) {
        os << v.get_wstring();
        return os;}

    // Fast log directly
    inline void log() const { wcout << get_wstring() << flush; }

};





// class PointPair : public Point {
// private:
//     Point fill; // the secondary point

// public:
//     PointPair() = default;

//     PointPair(const float & xi, const float & yi, const Marker & m = Marker()) 
//         : Point(xi, yi, m), fill(xi, yi, Marker(none)) {}

//     PointPair(const PointPair & other) : Point(other), fill(other.fill) {}

//     PointPair(PointPair && other) noexcept : Point(std::move(other)), fill(std::move(other.fill)) {}

//     PointPair(const Point & point) : Point(point), fill(point.get_x(), point.get_y(), Marker(none)) {} // Copy constructor

//     PointPair & operator=(const PointPair & other) {
//         Point::operator=(other);   // assign base part 
//         fill = other.fill; 
//         return *this;} 

//     PointPair & operator=(PointPair && other) noexcept {
//         Point::operator=(std::move(other)); 
//         fill = std::move(other.fill); 
//         return *this;} 

//     void set_point(const Point & p) {Point::set(p);} 

//     void set_point(const float & xi, const float & yi, const Marker & m) {Point::set(xi, yi, m);}
//     void set_fill_point(const Point & p) {fill.set(p);}
//     void set_fill_point(const float & xi, const float & yi, const Marker & m) {fill.set(xi, yi, m);}

//     void fix_background(Pixel & pixel) { 
//         Point::fix_background(pixel); // call base version 
//         if (!fill.is_none()) {fill.fix_background(pixel);}}

//     inline const Point & get_main() const { return *this;}
//     inline const Point & get_fill() const { return fill;}
//     inline Point & get_fill() { return fill; }

//     float get_xmin() const {
//     return std::min(get_x(), fill.get_x());}

//     float get_xmax() const {
//       return std::max(get_x(), fill.get_x());}

//     float get_ymin() const {
//       return std::min(get_y(), fill.get_y());}

//     float get_ymax() const {
//       return std::max(get_y(), fill.get_y());}

//     void add_offset(const float & dx, const float & dy) noexcept {
//         Point::add_offset(dx, dy);
//         fill.add_offset(dx, dy);}

//     void rescale_x(const std::pair<float, float> & xlim, const size_t & width, const float & delta) noexcept {
//         Point::rescale_x(xlim, width, delta);
//         fill.rescale_x(xlim, width, delta);}

//     void rescale_y(const std::pair<float, float> & ylim, const size_t & height, const float & delta) noexcept {
//         Point::rescale_y(ylim, height, delta);
//         fill.rescale_y(ylim, height, delta);}

//     void log_x() noexcept {
//         Point::log_x();
//         fill.log_x();}

//     void log_y() noexcept {
//         Point::log_y();
//         fill.log_y();}

//     std::wstring get_wstring() const {
//         std::wostringstream woss;
//         woss << Point::get_wstring();
//         if (!fill.is_none()) {woss << L" → " << fill.get_wstring();}
//         //else {woss << L" → " << fill.get_wstring();}
//         return woss.str();}
// };