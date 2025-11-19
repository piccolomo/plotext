class Signal : public PointsFilled {
private:
    bool xside = false;
    bool yside = false;
    std::wstring label;
    Marker marker; 
    bool fill_method = false;
    bool line_method = false;

public:
    Signal(){ marker.set_type(none);}

    Signal(const size_t& size) : PointsFilled(size){ marker.set_type(none);}

    Signal(const Signal& s)
        : PointsFilled(s),
          xside(s.xside), yside(s.yside),
          label(s.label),
          marker(s.marker),
          fill_method(s.fill_method),
          line_method(s.line_method) {}

    Signal(const PointsFilled& pf) : PointsFilled(pf) {}

    Signal& operator=(const Signal& other){
        PointsFilled::operator=(other);
        xside = other.xside;
        yside = other.yside;
        label = other.label;
        marker = other.marker;
        fill_method = other.fill_method;
        line_method = other.line_method;
        return *this;}

    void clear(){
        PointsFilled::clear();
        xside = false;
        yside = false;
        label = L"";
        marker.set_type(none);}

    // --- Setters ---
    void set_xside(bool value){ xside = value;}
    void set_yside(bool value){ yside = value;}
    void set_label(const std::wstring& value){ label = value;}
    void set_marker(const Marker& value){ marker = value;}
    void set_fill_method(bool value){ fill_method = value;}
    void set_line_method(bool value){ line_method = value;}

    // --- Getters ---
    bool get_xside() const { return xside;}
    bool get_yside() const { return yside;}
    const std::wstring& get_label() const { return label;}
    const Marker& get_marker() const { return marker;}
    bool get_fill_method() const { return fill_method;}
    bool get_line_method() const { return line_method;}

    void append(const PointFilled& pf) noexcept {
        PointsFilled::append(pf);
        if (get_length() == 1) marker = pf;}

    void append(const Signal& s) noexcept { PointsFilled::append(s);}

    void append(const Point& main, const Point& fill) noexcept {
        PointFilled pf(main, fill);
        append(pf);}

    Point get_point(const size_t& i) const noexcept { return at(i).get_main();}
    Point get_fill_point(const size_t& i) const noexcept { return at(i).get_fill();}
    size_t get_length() const noexcept { return PointsFilled::get_length();}

    void plot(){
        if (get_length() > 1){
            Vector<PointFilled> out = get_lines(line_method);
            Vector<PointFilled>::operator=(out);}}

    Points get_filled_points() const noexcept {
        return PointsFilled::get_filled_points(fill_method);}

    std::wstring get_wstring(const bool fill = 1) const noexcept {
        std::wostringstream woss;
        woss << L"Signal "
             << L"xside " << bool_to_wchar(xside)
             << L", yside " << bool_to_wchar(yside)
             << L", marker " << marker.get_wstring()
             << L", label " << label << L", "
             << L", line method " << bool_to_wchar(line_method) << L", "
             << L", fill method " << bool_to_wchar(fill_method) << L", "
             << PointsFilled::get_wstring(fill);
        return woss.str();} 

    inline std::string get_string() const noexcept { return wstring_to_string(get_wstring()); }

    inline void log() const noexcept { std::wcout << get_wstring() << std::endl; }

    friend wostream & operator<<(wostream & os, const Signal & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Signal & c) noexcept {os << c.get_string(); return os;}

};


extern "C" {

    // --- Creation / Destruction ---
    Signal* signal_new(size_t n) noexcept { return new Signal(n);}
    void signal_delete(Signal* p) noexcept { delete p;}
    void signal_clear(Signal* p) noexcept { p->clear();}

    // --- Getters ---
    bool signal_get_xside(const Signal* p) noexcept { return p->get_xside();}
    bool signal_get_yside(const Signal* p) noexcept { return p->get_yside();}
    const wchar_t* signal_get_label(const Signal* s) noexcept { return wstring_to_cstring(s->get_label());}
    Marker* signal_get_marker(const Signal* s) noexcept { return new Marker(s->get_marker());}
    bool signal_get_fill_method(const Signal* p) noexcept { return p->get_fill_method();}
    bool signal_get_line_method(const Signal* p) noexcept { return p->get_line_method();}

    // --- Setters ---
    void signal_set_xside(Signal* p, bool value) noexcept { p->set_xside(value);}
    void signal_set_yside(Signal* p, bool value) noexcept { p->set_yside(value);}
    void signal_set_label(Signal* p, const wchar_t* value) noexcept { p->set_label(std::wstring(value));}
    void signal_set_marker(Signal* s, const Marker* m) noexcept { s->set_marker(*m);}
    void signal_set_fill_method(Signal* p, bool value) noexcept { p->set_fill_method(value);}
    void signal_set_line_method(Signal* p, bool value) noexcept { p->set_line_method(value);}

    // --- Points ---
    void signal_add_point(Signal* s, const PointFilled* pf) noexcept { s->append(*pf);}
    void signal_append(Signal* s, const Signal* s2) noexcept { s->append(*s2);}
    void signal_set_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept { s->set_point(i, xs, ys, *m);}
    void signal_set_fill_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept { s->set_fill(i, xs, ys, *m);}
    PointFilled* signal_get_point(const Signal* s, size_t i) noexcept { return new PointFilled(s->at(i));}
    Point* signal_get_fill_point(const Signal* s, size_t i) noexcept { return new Point(s->get_fill_point(i));}

    // --- Background ---
    void signal_fix_background(Signal* s, Pixel* p) noexcept { s->fix_background(*p);}

    // --- Info ---
    const wchar_t* signal_get_wstring(const Signal* s, bool fill) noexcept { return wstring_to_cstring(s->get_wstring(fill));}
    size_t signal_get_length(const Signal* s) noexcept { return s->get_length();}
    void signal_assign(Signal* s1, const Signal* s2) noexcept { *s1 = *s2;}

    // --- Range ---
    float signal_get_xmin(const Signal* s, float ymin = -inf, float ymax = inf) noexcept { return s->get_xmin(ymin, ymax);}
    float signal_get_xmax(const Signal* s, float ymin = -inf, float ymax = inf) noexcept { return s->get_xmax(ymin, ymax);}
    float signal_get_ymin(const Signal* s, float xmin = -inf, float xmax = inf) noexcept { return s->get_ymin(xmin, xmax);}
    float signal_get_ymax(const Signal* s, float xmin = -inf, float xmax = inf) noexcept { return s->get_ymax(xmin, xmax);}

    void signal_select_in_matrix(Signal* s, size_t width, size_t height) noexcept { s->select_in_matrix(width, height);}

    // --- Transformations ---
    void signal_log_x(Signal* s) noexcept { s->log_x();}
    void signal_log_y(Signal* s) noexcept { s->log_y();}
    void signal_rescale_x(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_x({l,h}, b, d);}
    void signal_rescale_y(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_y({l,h}, b, d);}
    void signal_add_offset(Signal* s, size_t dx, size_t dy) noexcept { s->add_offset(dx, dy);}

    // --- Copy / plotting ---
    Signal* signal_copy(const Signal* s) noexcept { return new Signal(*s);}
    void signal_plot(Signal* s) noexcept { s->plot();}
    Points* signal_get_filled_points(Signal* s) noexcept { return new Points(s->get_filled_points());}
}
