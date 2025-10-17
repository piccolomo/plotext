class Signal : public PointsFilled {
private:
    bool xside = false;
    bool yside = false;
    std::wstring label;

public:
    using PointsFilled::squash;

    Signal() = default;

    Signal(const size_t& size) : PointsFilled(size) {}

    // Copy constructor
    Signal(const Signal& s)
        : PointsFilled(s), xside(s.xside), yside(s.yside), label(s.label) {}

    // Constructor from PointsFilled
    Signal(const PointsFilled& pf)
        : PointsFilled(pf) {}

    Signal& operator=(const Signal & other) {
        PointsFilled::operator=(other);
        xside = other.xside;
        yside = other.yside;
        label = other.label;
        return *this;}

    void clear() {
        PointsFilled::clear();
        xside = false;
        yside = false;
        label = L"";}

    void set_details(const bool & xs, const bool & ys, const wstring & l) {
        xside = xs;
        yside = ys;
        label = l;}


    void add_point(const PointFilled& pf) noexcept {PointsFilled::add_point(pf);}

    void add_point(const Point& main, const Point& fill) noexcept {PointFilled pf(main, fill); add_point(pf);}

    // Access main and fill points via PointFilled
    Point get_point(const size_t& i) const noexcept { return at(i).get_main(); }
    Point get_fill_point(const size_t& i) const noexcept { return at(i).get_fill(); }

    size_t get_length() const noexcept { return PointsFilled::get_length(); }

    // float get_xmin() const noexcept { return PointsFilled::get_xmin(); }
    // float get_xmax() const noexcept { return PointsFilled::get_xmax(); }
    // float get_ymin() const noexcept { return PointsFilled::get_ymin(); }
    // float get_ymax() const noexcept { return PointsFilled::get_ymax(); }

    // void log_x() { PointsFilled::log_x(); }
    // void log_y() { PointsFilled::log_y(); }
    // void rescale_x(const std::pair<float, float>& xlim, const size_t& width, const float& delta) {PointsFilled::rescale_x(xlim, width, delta);}

    // void rescale_y(const std::pair<float, float>& ylim, const size_t& height, const float& delta) {PointsFilled::rescale_y(ylim, height, delta);}
    // void add_offset(const float& dx, const float& dy) { PointsFilled::add_offset(dx, dy); }

    std::wstring get_label() const noexcept { return label; }
    bool get_xside() const noexcept { return xside; }
    bool get_yside() const noexcept { return yside; }

    // Get string representation of points
    std::wstring get_wstring(const bool fill) const {
        std::wostringstream woss;
        size_t length = this->get_length();
        woss << L"Signal " << "xside" << " " << bool_to_wchar(xside) << ", yside" << " " << bool_to_wchar(yside) << ", ";
        woss << PointsFilled::get_wstring(fill);
        return woss.str(); }

    // void log(const bool fill = false) const { std::wcout << get_wstring(fill) << std::endl << std::flush; }

};


extern "C" {

    // Creation / destruction
    Signal* signal_new(size_t n) noexcept { return new Signal(n); }
    void signal_delete(Signal* p) noexcept { delete p; }
    void signal_clear(Signal* p) noexcept { p->clear(); }

    // Metadata
    void signal_set_details(Signal* s, bool xs, bool ys, wchar_t * l) noexcept { s->set_details(xs, ys, l); }
    const wchar_t* signal_get_label(Signal* s) noexcept { return wstring_to_cstring(s->get_label()); }
    bool signal_get_side(Signal* s, bool axis) noexcept { return axis ? s->get_yside() : s->get_xside(); }

    // Points
    void signal_add_point(Signal* s, const PointFilled* pf) noexcept { s->add_point(*pf); }
    void signal_set_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept {s->set_point(i, xs, ys, *m);};
    void signal_set_fill_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept {s->set_fill(i, xs, ys, *m);};


    PointFilled * signal_get_point(const Signal* s, size_t i) noexcept { return new PointFilled(s->get(i)); }
    Point* signal_get_fill_point(const Signal* s, size_t i) noexcept { return new Point(s->get_fill_point(i)); }

    // Background
    void signal_fix_background(Signal* s, Pixel* p) noexcept { s->fix_background(*p); }

    // Info
    const wchar_t* signal_get_wstring(const Signal* s, bool fill) noexcept { return wstring_to_cstring(s->get_wstring(fill)); }
    size_t signal_get_length(const Signal* s) noexcept { return s->get_length(); }
    void signal_assign(Signal* s1, const Signal* s2) noexcept { *s1 = *s2; }

    // Range
    float signal_get_xmin(Signal* s) noexcept { return s->get_xmin(); }
    float signal_get_xmax(Signal* s) noexcept { return s->get_xmax(); }
    float signal_get_ymin(Signal* s) noexcept { return s->get_ymin(); }
    float signal_get_ymax(Signal* s) noexcept { return s->get_ymax(); }

    // Transformations
    void signal_log_x(Signal* s) noexcept { s->log_x(); }
    void signal_log_y(Signal* s) noexcept { s->log_y(); }
    void signal_rescale_x(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_x({l,h}, b, d); }
    void signal_rescale_y(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_y({l,h}, b, d); }
    void signal_add_offset(Signal* s, size_t dx, size_t dy) noexcept {s->add_offset(dx, dy); }

    // Copy / plotting
    Signal* signal_copy(const Signal* s) noexcept { return new Signal(*s); }
    void signal_plot(Signal* s) noexcept {s->plot(); }
    //void signal_fill(Signal* s, Vector<Point> * P) noexcept {s->fill(*P); }
    void signal_squash(Signal* s, PointsMap * map) noexcept {s->squash(*map); }

    //size_t signal_get_filled_lines_length(Signal* s) {return s->get_filled_lines_length();}

    Vector<Point> * points_new(size_t n) {return new Vector<Point>(n);}
    void points_delete(Vector<Point> * p) noexcept { delete p; }
    void points_log(Vector<Point> * p) noexcept {p->log(); }
    size_t points_get_length(Vector<Point> * p) noexcept {return p->get_length(); }
    size_t points_get_capacity(Vector<Point> * p) noexcept {return p->get_capacity(); }

} 