// Points - manages a collection of Point objects with utility methods and logging

class Points : public Vector<Point> {
public:
    using Vector<Point>::append;
    using Vector<Point>::begin;
    using Vector<Point>::end;


    // ------------ lifecycle ------------
    Points(const size_t & size) : Vector<Point>(size) {}
    Points(const Points & p) : Vector<Point>(p) {}
    Points(Points && p) noexcept : Vector<Point>(std::move(p)) {}
    ~Points() = default;

    // ------------ assignment ------------
    Points & operator=(const Points & other) {
        Vector<Point>::operator=(other);
        return *this;}

    Points & operator=(const Vector<Point> & other) {
        Vector<Point>::operator=(other);
        return *this;}

    // ------------ basic operations ------------
    void clear() noexcept { Vector<Point>::clear(); }

    Points copy() const noexcept { return Points(*this); }

    inline void append(const Point & p) noexcept { Vector<Point>::append(p); }

    inline void append(const Vector<Point> & P) noexcept {
        Vector<Point>::reserve(get_length() + P.get_length());
        Vector<Point>::append(P);}

    void fix_background(Pixel & pixel) noexcept {
        for (size_t i = 0; i < get_length(); i++)
            at(i).fix_background(pixel);}

    inline size_t get_length() const noexcept { return Vector<Point>::get_length(); }

    void add_offset(const size_t & dx, const size_t & dy) noexcept {
        for (size_t i = 0; i < get_length(); i++) at(i).add_offset(dx, dy);}

    void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<Point> out(get_length());
        for (const Point & p : *this)
            if (p.in_matrix(width, height))
                out.append(p);
        *this = out;}

    // ------------ squash / merge points ------------
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
    std::wstring get_wstring() const noexcept {
        std::wostringstream woss;
        size_t length = get_length();
        woss << L"Points " << length << L" [";
        for (size_t i = 0; i < length; i++) {
            woss << at(i).get_wstring();
            if (i != length - 1) woss << L", ";}
        woss << L"]";
        return woss.str();}

    inline std::string get_string() const noexcept { return wstring_to_string(get_wstring()); }

    inline void log() const noexcept { std::wcout << get_wstring() << std::endl; }

    friend wostream & operator<<(wostream & os, const Points & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Points & c) noexcept {os << c.get_string(); return os;}
};




extern "C" {

    // --- Creation / Destruction ---
    Points * points_new(size_t n) noexcept { return new Points(n); }
    void points_delete(Points * p) noexcept { delete p; }
    void points_clear(Points * p) noexcept { p->clear(); }

    // --- Append operations ---
    void points_append_point(Points * p, const Point * point) noexcept { p->append(*point); }
    void points_append_points(Points * p, const Points * P) noexcept { p->append(*P); }

    // --- Getters ---
    Point * points_get_point(const Points * p, size_t index) noexcept { return new Point(p->at(index)); }
    size_t points_get_length(const Points * p) noexcept { return p->get_length(); }

    void points_fix_background(Points* s, Pixel* p) noexcept { s->fix_background(*p); }
    void points_add_offset(Points * p, size_t dx, size_t dy) noexcept { p->add_offset(dx, dy); }
    void points_select_in_matrix(Points * p, size_t width, size_t height) noexcept { p->select_in_matrix(width, height); }

    // --- Derived Data ---
    void points_squash(Points * s, PointsMap * map) noexcept { s->squash(*map); }

    // --- Logging / Output ---
    void points_log(const Points * p) noexcept { p->log(); }

    const wchar_t * points_get_wstring(const Points * p) noexcept {
        static std::wstring wstr; 
        wstr = p->get_wstring(); 
        return wstr.c_str();}

    const char * points_get_string(const Points * p) noexcept {
        static std::string str;
        str = p->get_string();
        return str.c_str();}

    // --- Copying ---
    Points * points_copy(const Points * p) noexcept { return new Points(p->copy()); }
}


