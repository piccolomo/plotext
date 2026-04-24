// Signal: a PointsFilled with plotting metadata (xside/yside, label, marker, fill and line methods)

class Signal : public PointsFilled {
private:
    bool xside = false;
    bool yside = false;
    std::wstring label;
    Marker marker;
    bool fill_method = false;
    bool line_method = false;

public:
    using PointsFilled::set_point;
    using PointsFilled::append;

    // Default constructor
    Signal() { marker.set_type(none);}

    // Construct with the given capacity
    Signal(const size_t& size) : PointsFilled(size) { marker.set_type(none);}

    // Copy constructor
    Signal(const Signal& s) : PointsFilled(s),
          xside(s.xside), yside(s.yside),
          label(s.label),
          marker(s.marker),
          fill_method(s.fill_method),
          line_method(s.line_method) {}

    // Move constructor
    Signal(Signal&& s) noexcept : PointsFilled(std::move(s)),
          xside(s.xside), yside(s.yside),
          label(std::move(s.label)),
          marker(std::move(s.marker)),
          fill_method(s.fill_method),
          line_method(s.line_method) {}

    // Destructor
    ~Signal() noexcept {}

    // Copy assignment (self-assignment safe)
    Signal& operator=(const Signal& other){
        if (this == &other) return *this;
        PointsFilled::operator=(other);
        xside = other.xside;
        yside = other.yside;
        label = other.label;
        marker = other.marker;
        fill_method = other.fill_method;
        line_method = other.line_method;
        return *this;}

    // Move assignment (self-assignment safe)
    Signal& operator=(Signal&& other) noexcept {
        if (this == &other) return *this;
        PointsFilled::operator=(std::move(other));
        xside = other.xside;
        yside = other.yside;
        label = std::move(other.label);
        marker = std::move(other.marker);
        fill_method = other.fill_method;
        line_method = other.line_method;
        return *this;}

    // Reset every field to its default
    void clear(){
        PointsFilled::clear();
        xside = false;
        yside = false;
        label = L"";
        marker.set_type(none);}

    // --- Setters ---

    // Choose the x side (lower/upper) as a boolean
    void set_xside(bool value){ xside = value;}

    // Choose the y side (left/right) as a boolean
    void set_yside(bool value){ yside = value;}

    // Set the legend label
    void set_label(const std::wstring& value){ label = value;}

    // Set the default marker
    void set_marker(const Marker& value){ marker = value;}

    // Set the fill method (simple / full)
    void set_fill_method(bool value){ fill_method = value;}

    // Set the line method (simple / full)
    void set_line_method(bool value){ line_method = value;}

    // --- Getters ---

    // x side
    bool get_xside() const { return xside;}

    // y side
    bool get_yside() const { return yside;}

    // Legend label
    const std::wstring& get_label() const { return label;}

    // Default marker
    const Marker& get_marker() const { return marker;}

    // Fill method flag
    bool get_fill_method() const { return fill_method;}

    // Line method flag
    bool get_line_method() const { return line_method;}

    // Append a PointFilled (remembering the first one as the default marker)
    void append(const PointFilled& pf) noexcept {
        PointsFilled::append(pf);
        if (get_length() == 1) marker = pf;}

    // Append another Signal's points
    void append(const Signal& s) noexcept { PointsFilled::append(s);}

    // Append a main and a fill point
    void append(const Point& main, const Point& fill) noexcept {
        PointFilled pf(main, fill);
        append(pf);}

    // Get the main point at index i
    Point get_point(const size_t& i) const noexcept { return at(i).get_main();}

    // Get the fill point at index i
    Point get_fill_point(const size_t& i) const noexcept { return at(i).get_fill();}

    // Number of points
    size_t get_length() const noexcept { return PointsFilled::get_length();}

    // Expand the signal's points into the line sequence, replacing in place
    void plot(){
        if (get_length() > 1){
            Vector<PointFilled> out = get_lines(line_method);
            Vector<PointFilled>::operator=(out);
        }}

    // Expand the signal into a flat Points collection, honoring the fill method
    Points get_points() const noexcept {
        return PointsFilled::get_points(fill_method);}

    // Get wide string summary of the signal
    std::wstring get_wstring(const bool fill = 1) const noexcept {
        std::wostringstream woss;
        woss << L"Signal: "
             << L"xside " << bool_to_wchar(xside)
             << L", yside " << bool_to_wchar(yside)
             << L", marker " << marker.get_wstring()
             << L", label " << label
             << L", line method " << bool_to_wchar(line_method)
             << L", fill method " << bool_to_wchar(fill_method)
             << L", " << PointsFilled::get_wstring(fill);
        return woss.str();}

    // Get narrow string summary
    inline std::string get_string() const noexcept { return wstring_to_string(get_wstring()); }

    // Log to wcout
    inline void log() const noexcept { std::wcout << get_wstring() << std::endl; }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Signal & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Signal & c) noexcept {os << c.get_string(); return os;}

};


extern "C" {
    // Create a new Signal with the given capacity
    Signal * signal_new(size_t length) {return new Signal(length);}

    // Delete a Signal
    void signal_delete(Signal* s) {delete s;}

    // Deep copy of a Signal
    Signal* signal_copy(Signal* s) {if (!s) return nullptr; return new Signal(*s);}

    // Clear every field of the signal
    void signal_clear(Signal* p) noexcept { p->clear();}

    // Get the x side
    bool signal_get_xside(const Signal* p) noexcept { return p->get_xside();}

    // Get the y side
    bool signal_get_yside(const Signal* p) noexcept { return p->get_yside();}

    // Return the label wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t* signal_get_label(const Signal* s) noexcept { return wstring_to_cstring(s->get_label());}

    // Get a heap-allocated copy of the marker
    Marker* signal_get_marker(const Signal* s) noexcept { return new Marker(s->get_marker());}

    // Get the fill method flag
    bool signal_get_fill_method(const Signal* p) noexcept { return p->get_fill_method();}

    // Get the line method flag
    bool signal_get_line_method(const Signal* p) noexcept { return p->get_line_method();}

    // Set the x side
    void signal_set_xside(Signal* p, bool value) noexcept { p->set_xside(value);}

    // Set the y side
    void signal_set_yside(Signal* p, bool value) noexcept { p->set_yside(value);}

    // Set the legend label
    void signal_set_label(Signal* p, const wchar_t* value) noexcept { p->set_label(std::wstring(value));}

    // Set the default marker
    void signal_set_marker(Signal* s, const Marker* m) noexcept { s->set_marker(*m);}

    // Set the fill method
    void signal_set_fill_method(Signal* p, bool value) noexcept { p->set_fill_method(value);}

    // Set the line method
    void signal_set_line_method(Signal* p, bool value) noexcept { p->set_line_method(value);}

    // Append a single point from coordinates and a marker
    void signal_append_point(Signal* s, float xs, float ys, Marker* m) noexcept { s->append(xs, ys, *m);}

    // Append another signal's points
    void signal_append(Signal* s, const Signal* s2) noexcept { s->append(*s2);}

    // Replace the main point at index i
    void signal_set_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept { s->set_point(i, xs, ys, *m);}

    // Replace the fill point at index i
    void signal_set_fill_point(Signal* s, size_t i, float xs, float ys, Marker* m) noexcept { s->set_fill(i, xs, ys, *m);}

    // Get a heap-allocated copy of the main point at index i
    PointFilled * signal_get_point(const Signal* s, size_t i) noexcept { return new PointFilled(s->at(i));}

    // Get a heap-allocated copy of the fill point at index i
    Point* signal_get_fill_point(const Signal* s, size_t i) noexcept { return new Point(s->get_fill_point(i));}

    // Fix the background of every point against the given pixel
    void signal_fix_background(Signal* s, Pixel* p) noexcept { s->fix_background(*p);}

    // Return the rendered wide string summary (caller owns the buffer, free with wstring_delete)
    const wchar_t * signal_get_wstring(const Signal* s, bool fill) noexcept { return wstring_to_cstring(s->get_wstring(fill));}

    // Number of points
    size_t signal_get_length(const Signal* s) noexcept { return s->get_length();}

    // Copy-assign signal s2 into s1
    void signal_assign(Signal* s1, const Signal* s2) noexcept { *s1 = *s2;}

    // Minimum x within the optional y window
    float signal_get_xmin(const Signal* s, float ymin, float ymax) noexcept { return s->get_xmin(ymin, ymax);}

    // Maximum x within the optional y window
    float signal_get_xmax(const Signal* s, float ymin, float ymax) noexcept { return s->get_xmax(ymin, ymax);}

    // Minimum y within the optional x window
    float signal_get_ymin(const Signal* s, float xmin, float xmax) noexcept { return s->get_ymin(xmin, xmax);}

    // Maximum y within the optional x window
    float signal_get_ymax(const Signal* s, float xmin, float xmax) noexcept { return s->get_ymax(xmin, xmax);}

    // Keep only points inside a matrix of the given size
    void signal_select_in_matrix(Signal* s, size_t width, size_t height) noexcept { s->select_in_matrix(width, height);}

    // Apply log10 to x of every point
    void signal_log_x(Signal* s) noexcept {s->log_x();}

    // Apply log10 to y of every point
    void signal_log_y(Signal* s) noexcept {s->log_y();}

    // Rescale x of every point
    void signal_rescale_x(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_x({l,h}, b, d);}

    // Rescale y of every point
    void signal_rescale_y(Signal* s, float l, float h, size_t b, float d) noexcept { s->rescale_y({l,h}, b, d);}

    // Add (dx, dy) offset to every point
    void signal_add_offset(Signal* s, size_t dx, size_t dy) noexcept { s->add_offset(dx, dy);}

    // Expand the signal's points into the line sequence (in place)
    void signal_plot(Signal * s) noexcept { s->plot();}

    // Get a heap-allocated Points expansion of the signal
    Points* signal_get_points(Signal * s) noexcept { return new Points(s->get_points());}
}
