// Points: collection of Point objects built on Vector<Point>, with offsetting, matrix selection and squash-merge

class Points : public Vector<Point> {
public:
    using Vector<Point>::append;
    using Vector<Point>::begin;
    using Vector<Point>::end;


    // ------------ lifecycle ------------

    // Construct a Points container with the given capacity
    Points(const size_t & size) : Vector<Point>(size) {}

    // Copy constructor
    Points(const Points & p) : Vector<Point>(p) {}

    // Move constructor
    Points(Points && p) noexcept : Vector<Point>(std::move(p)) {}

    // Destructor
    ~Points() noexcept {}

    // ------------ assignment ------------

    // Copy assignment
    Points & operator=(const Points & other) {
        Vector<Point>::operator=(other);
        return *this;}

    // Move assignment
    Points & operator=(Points && other) noexcept {
        Vector<Point>::operator=(std::move(other));
        return *this;}

    // Assign from a plain Vector<Point>
    Points & operator=(const Vector<Point> & other) {
        Vector<Point>::operator=(other);
        return *this;}

    // ------------ basic operations ------------

    // Clear every point
    void clear() noexcept { Vector<Point>::clear(); }

    // Return a deep copy
    Points copy() const noexcept { return Points(*this); }

    // Append a single point
    inline void append(const Point & p) noexcept { Vector<Point>::append(p); }

    // Append a batch of points, reserving capacity first
    inline void append(const Vector<Point> & P) noexcept {
        Vector<Point>::reserve(get_length() + P.get_length());
        Vector<Point>::append(P);}

    // Fix the background of every point using the given pixel
    void fix_background(const Pixel & pixel) noexcept {
        for (size_t i = 0; i < get_length(); i++)
            at(i).fix_background(pixel);}

    // Number of points
    inline size_t get_length() const noexcept { return Vector<Point>::get_length(); }

    // Add (dx, dy) offset to every point
    void add_offset(const size_t & dx, const size_t & dy) noexcept {
        for (size_t i = 0; i < get_length(); i++) at(i).add_offset(dx, dy);}

    // Keep only the points that fall inside a matrix of the given size
    void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<Point> out(get_length());
        for (const Point & p : *this)
            if (p.in_matrix(width, height))
                out.append(p);
        *this = std::move(out);}

    // ------------ squash / merge points ------------

    // Merge overlapping points, using a PointsMap for O(1) look-up by (col, row)
    void squash(PointsMap & map) noexcept {
        Vector<Point> out(get_length());

        for (Point & current : *this) {
            size_t c = current.get_col(), r = current.get_row();
            bool is_present = map.is_present(c, r);

            if (is_present) {
                size_t index = map.get_index(c, r);
                Point & previous = out.at(index);
                bool close = current.is_close(previous);
                if (close) previous.set_type(none);}

            map.set_index(c, r, out.get_length());
            out.append(current);}

        Vector<Point>::clear();
        for (auto & el : out)
            if (!el.is_none()) append(el);}

    // ------------ output / logging ------------

    // Get wide string summary "Points N: [p1, p2, ...]"
    std::wstring get_wstring() const noexcept {
        std::wostringstream woss;
        size_t length = get_length();
        woss << L"Points " << length << L": [";
        for (size_t i = 0; i < length; i++) {
            woss << at(i).get_wstring();
            if (i != length - 1) woss << L", ";}
        woss << L"]";
        return woss.str();}

    // Get narrow string summary
    inline std::string get_string() const noexcept { return wstring_to_string(get_wstring()); }

    // Log to wcout
    inline void log() const noexcept { std::wcout << get_wstring() << std::endl; }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Points & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Points & c) noexcept {os << c.get_string(); return os;}
};


extern "C" {

    // Create a new Points container with the given capacity
    Points * points_new(size_t n) noexcept { return new Points(n); }

    // Delete a Points container
    void points_delete(Points * p) noexcept { delete p; }

    // Clear all points
    void points_clear(Points * p) noexcept { p->clear(); }

    // Append a single point
    void points_append_point(Points * p, const Point * point) noexcept { p->append(*point); }

    // Append a whole Points batch
    void points_append_points(Points * p, const Points * P) noexcept { p->append(*P); }

    // Get a heap-allocated copy of the point at the given index
    Point * points_get_point(const Points * p, size_t index) noexcept { return new Point(p->at(index)); }

    // Number of points
    size_t points_get_length(const Points * p) noexcept { return p->get_length(); }

    // Fix the background of every point using the given pixel
    void points_fix_background(Points* s, Pixel* p) noexcept { s->fix_background(*p); }

    // Add (dx, dy) offset to every point
    void points_add_offset(Points * p, size_t dx, size_t dy) noexcept { p->add_offset(dx, dy); }

    // Keep only points inside a matrix of the given size
    void points_select_in_matrix(Points * p, size_t width, size_t height) noexcept { p->select_in_matrix(width, height); }

    // Squash overlapping points via a PointsMap
    void points_squash(Points * s, PointsMap * map) noexcept { s->squash(*map); }

    // Log the Points to wcout
    void points_log(const Points * p) noexcept { p->log(); }

    // Caller owns the returned buffer — free it with wstring_delete
    const wchar_t * points_get_wstring(const Points * p) noexcept {
        return wstring_to_cstring(p->get_wstring()); }

    // Deep copy of the Points container
    Points * points_copy(const Points * p) noexcept { return new Points(p->copy()); }
}
