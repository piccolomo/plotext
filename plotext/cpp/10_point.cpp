// A class to represent a 2D point with position, marker, and fill attributes.
// Inherits from PointPosition, Marker, and PointFill.

class Point : public PointPosition, public Marker {
public:
    // Constructors
    constexpr Point() noexcept = default;

    Point(float xi, float yi, const Marker & m = Marker()) noexcept {set(xi, yi, m);}

    Point(float xi, float yi, const Point & p) noexcept: PointPosition(xi, yi), Marker(p) {}

    Point(const PointPosition & pp, const Marker & p) noexcept : PointPosition(pp), Marker(p) {};

    Point(const Point & p) noexcept = default;
    Point(Point && p) noexcept = default;

    bool operator==(const Point & other) const noexcept {
        return Marker::operator==(other) && PointPosition::operator==(other);}

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

    Point get_rounded_point() const noexcept {
        float col = get_col() + (2.0 * get_inner_col() + 1) / (2 * get_cols());
        float row = get_row() + (2.0 * get_inner_row() + 1) / (2 * get_rows());
        return Point(col, row, *this);}

    // Check approximate proximity
    bool is_close(const Point & p) const noexcept {
        return Marker::operator==(p)
            && get_col() == p.get_col()
            && get_row() == p.get_row()
            && get_inner_col() == p.get_inner_col()
            && get_inner_row() == p.get_inner_row();}

    inline Point get_line_point(const Point & p, const float & t) const noexcept {
        float x = get_x(); float y = get_y();
        x += (p.get_x() - x) * t;
        y += (p.get_y() - y) * t;
        //wcout << "get line point "; this->log(); Point(x, y, *this).log(); nl();
        return Point(x, y, *this);}

    // Compute line length in grid units
    inline size_t get_xsteps(const Point & p) const noexcept {
        const size_t cols = get_cols();
        return static_cast<size_t>(std::abs(static_cast<int>(get_x() * cols) - static_cast<int>(p.get_x() * cols)));}

    // Compute line length in grid units
    inline size_t get_ysteps(const Point & p) const noexcept {
        const size_t rows = get_rows();
        return static_cast<size_t>(std::abs(static_cast<int>(get_y() * rows) - static_cast<int>(p.get_y() * rows)));}

    inline size_t get_simple_line_length(const Point & p) const noexcept {return max({get_xsteps(p), get_ysteps(p), (size_t)1}) + 1;}

    inline size_t get_full_line_length(const Point & p) const noexcept {return get_xsteps(p) + get_ysteps(p) + 3;}

    inline size_t get_line_length(const Point & p, bool method) const noexcept {if (method) {return get_full_line_length(p);} else {return get_simple_line_length(p);};}

    inline Point get_middle_point(const Point & p) const noexcept {return Point(get_middle(p), *this);}

    inline Vector<Point> get_simple_line(const Point & p, bool last = true) const noexcept {
        //this->log(); p.log(); nl();
        //Point start = get_rounded_point(); Point end = p.get_rounded_point();
        Point start = *this; Point end = p;
        //start.log(); end.log(); nl();
        Numerical<float> parameters = linspace<float>(0, 1, start.get_simple_line_length(end));
        Vector<Point> out(parameters.get_length()); 
        out.append(*this);
        for (size_t i = 1; i < parameters.get_length() - 1; i++) {out.append(start.get_line_point(end, parameters.at(i)));}
        if (last and not is_close(p)) {out.append(p);}
        //out.log(); nl(2);
        //wcout << parameters.get_length() << endl; nl();
        return out;}

    inline Vector<Point> get_full_line(const Point & p, bool last = true) const noexcept {
        const size_t cols = get_cols();
        const size_t rows = get_rows();

        float x0 = get_x() * cols; float x1 = p.get_x() * cols; 
        float y0 = get_y() * rows; float y1 = p.get_y() * rows; 

        float dx = x1 - x0; 
        float dy = y1 - y0; 

        float m = dy / dx; 
        float mi = 1 / m; 

        float x_int, y_int;  
        float delta_x = 1, delta_y = 1; 

        if (dx >= 0){x_int = floor(x0) + 1;} else {x_int = ceil(x0) - 1; delta_x = -1;}
        if (dy >= 0){y_int = floor(y0) + 1;} else {y_int = ceil(y0) - 1; delta_y = -1;}

        float x_line, y_line; 

        // bool test = (p.get_col() == 59) and (p.get_row() == 2);
        // if (test) {p.log();}

        size_t size = get_full_line_length(p); 
        Vector<Point> crossings(size + 4); 
        crossings.append(*this);

        Point previous, next, middle; 
        previous = *this;

        while (true) {
            bool test_x = (delta_x * (x_int - x0)) < (delta_x * dx);
            bool test_y = (delta_y * (y_int - y0)) < (delta_y * dy);

            if (not (test_x or test_y)) break;

            x_line = x0 + mi * (y_int - y0); 
            y_line = y0 + m  * (x_int - x0);

            //if (test) wcout << " x int " <<  x_int << " y int " << y_int << " x line " << x_line << " y line " << y_line << endl;

            if (abs(abs(m) - 1) < 1e-4) {
                write("m=1");
                next = Point(x_int / cols, y_int / rows, *this);
                middle = previous.get_middle_point(next);
                x_int += delta_x; 
                y_int += delta_y;} 

            else if (delta_x * (x_line - x_int) >= 0) {
                y_line = y0 + m * (x_int - x0);
                //write("get full line x");
                next = Point(x_int / cols, y_line / rows, *this);
                middle = previous.get_middle_point(next);
                x_int += delta_x;}

            else if (delta_y * (y_line - y_int) >= 0) {
                //write("get full line y");
                next = Point(x_line / cols, y_int / rows, *this);
                middle = previous.get_middle_point(next);
                y_int += delta_y;}
            
            //write("get full line end");
            //crossings.append(next);
            crossings.append(middle);
            previous = next;}
        
        //write("next"); next.log(); flush(); nl();
        //if (last and not is_close(p)) {crossings.append(p);} 
        //wcout << "last " << last << "close " << is_close(p); nl();
        crossings.append(previous.get_middle_point(p)); 
        if (last and not is_close(p)) {
            //write("something ", 0); previous.get_middle_point(p).log(); nl();
            crossings.append(p);} 

        //this->log(); p.log(); crossings.log();

        return crossings;}


    inline Vector<Point> get_line(const Point & p, bool last = true, bool method = 0) const noexcept {
        if (method) {return get_full_line(p, last);} else {return get_simple_line(p, last);}}


    // Fast wide string representation
    wstring get_wstring() const {
        wchar_t buffer[128]; // Adjust size if needed
        swprintf(buffer, sizeof(buffer)/sizeof(wchar_t), L"(%ls, %ls)",
                 PointPosition::get_wstring().c_str(),
                 Marker::get_wstring().c_str());
        return wstring(buffer);}

    //string get_string() const {return get_wstring().c_str();}

    // Output operator
    friend inline std::wostream & operator<<(std::wostream& os, const Point& v) {
        os << v.get_wstring();
        return os;}

    // Fast log directly
    inline void log() const { wcout << get_wstring() << flush; }
    inline void log_position() const {PointPosition::log();}

};


extern "C" {

    // --- Creation / Destruction ---
    Point* point_new_marker(float x, float y, const Marker * m) noexcept { return new Point(x, y, *m); }
    void point_delete(Point* p) noexcept { delete p; }

    // --- Getters ---
    float point_get_x(const Point* p) noexcept { return p->get_x(); }
    float point_get_y(const Point* p) noexcept { return p->get_y(); }

    // --- Logging ---
    const wchar_t * point_get_wstring(Point * c) {return wstring_to_cstring(c->get_wstring());}
    void point_log(const Point* p) noexcept { p->log(); }
}
