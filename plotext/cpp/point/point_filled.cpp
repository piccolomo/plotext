class PointFilled : public Point {
private:
    Point fill; // the fill point

public:
    // Constructors
    PointFilled() = default;

    PointFilled(const float & xi, const float & yi, const Marker & m) : Point(xi, yi, m), fill(xi, yi, Marker(none)) {}

    PointFilled(const float & xi, const float & yi, const wchar_t & c, const Pixel & p = Pixel()) : PointFilled(xi, yi, Marker(c, p)) {}

    PointFilled(const float & xi, const float & yi, const marker_type & t) : Point(xi, yi, t), fill(xi, yi, Marker(none)) {}

    PointFilled(const PointFilled & other) : Point(other), fill(other.fill) {}

    PointFilled(const Point & main, const Point & fill) : Point(main), fill(fill) {}

    PointFilled(const Point && main, const Point && fill) : Point(move(main)), fill(move(fill)) {}

    PointFilled(PointFilled && other) noexcept : Point(std::move(other)), fill(std::move(other.fill)) {}

    PointFilled(const Point & point) : Point(point), fill(point.get_x(), point.get_y(), Marker(none)) {} // main from point, fill is none

    // Assignment
    PointFilled & operator=(const PointFilled & other) {
        Point::operator=(other);   // assign base part 
        fill = other.fill; 
        return *this;} 

    PointFilled & operator=(PointFilled && other) noexcept {
        Point::operator=(std::move(other)); 
        fill = std::move(other.fill); 
        return *this;} 

    // Setters
    void set_main(const Point & p) {Point::set(p);}
    void set_main(const float & xi, const float & yi, const Marker & m) { Point::set(xi, yi, m);}

    void set_fill(const Point & p) { fill.set(p); }
    void set_fill(const float & xi, const float & yi, const Marker & m) { fill.set(xi, yi, m); }

    // Drawing logic
    void fix_background(Pixel & pixel) { 
        Point::fix_background(pixel); 
        if (!fill.is_none()) fill.fix_background(pixel);}

    // Getters
    inline const Point & get_main() const { return *this; }
    inline const Point & get_fill() const { return fill; }
    inline Point & get_fill() { return fill; }
    inline bool no_fill() const {return fill.is_none();}

    // Bounds
    float get_xmin() const { return std::min(get_x(), fill.get_x()); }
    float get_xmax() const { return std::max(get_x(), fill.get_x()); }
    float get_ymin() const { return std::min(get_y(), fill.get_y()); }
    float get_ymax() const { return std::max(get_y(), fill.get_y()); }

    size_t get_two_lines_length(const PointFilled & p) const {return max(get_main().get_line_length(p.get_main()), get_fill().get_line_length(p.get_fill()));}

    Vector<PointFilled> get_two_lines(const PointFilled & p, const size_t & length, bool last = false) const {    
        //wcout << "!" << endl;    
        Vector<Point> main_line = get_main().get_line(p.get_main(), length, last);
        Vector<Point> fill_line = get_fill().get_line(p.get_fill(), length, last);

        //wcout << "sdasd" << length << flush << endl;
        // main_line.log(); 
        // fill_line.log(); nl(); 

        size_t size = main_line.get_length();
        Vector<PointFilled> out(length); 
        for (size_t i = 0; i < size; ++i) out.move_back(PointFilled(main_line.at(i), fill_line.at(i)));

        return out;}

    Vector<PointFilled> get_two_lines(const PointFilled & p, bool last = false) const { return get_two_lines(p, get_two_lines_length(p), last);}

    size_t get_filled_line_length() const {
        Point p1 = get_main(); Point p2 = get_fill();
        size_t count = p1.get_line_length(p2);
        return count;}


    Vector<Point> get_filled_line() const {
        Point p1 = get_main(); Point p2 = get_fill();
        //size_t count = get_filled_line_length();
        size_t count = p1.get_line_length(p2);
        //wcout << "sdasd " << count << flush << end
        return p1.get_line(p2, count, true);}


    bool is_close(const PointFilled & p){return Point::is_close(p.get_main()) and fill.is_close(p.get_fill());} 
    // // Transformations
    // void add_offset(const float & dx, const float & dy) noexcept {
    //     Point::add_offset(dx, dy);
    //     fill.add_offset(dx, dy);}

    void rescale_x(const std::pair<float, float> & xlim, const size_t & width, const float & delta) noexcept {
        Point::rescale_x(xlim, width, delta);
        fill.rescale_x(xlim, width, delta);}

    void rescale_y(const std::pair<float, float> & ylim, const size_t & height, const float & delta) noexcept {
        Point::rescale_y(ylim, height, delta);
        fill.rescale_y(ylim, height, delta);}

    void log_x() noexcept {
        Point::log_x();
        fill.log_x();}

    void log_y() noexcept {
        Point::log_y();
        fill.log_y();}

    void add_offset(const size_t & dx, const size_t & dy) noexcept {Point::add_offset(dx, dy); fill.add_offset(dx, dy); }


      // void update(const PointFilled & p) noexcept {
      //       if (!same_type(p)) set_type(p.get_type());

      //       if (!same_pixel(p)) {copy_pixel(p);}

      //       if (p.is_normal()) {copy_wcharacter(p);} 

      //       else {add_dot(p.get_x(), p.get_y());}}

    // Display
    wstring get_wstring(const bool & include_fill = true) const {
        std::wostringstream woss;
        woss << Point::get_wstring();
        if (include_fill) {woss << L" → " << fill.get_wstring();}
        return woss.str();}

    friend std::wostream& operator<<(std::wostream& os, const PointFilled& v) {
        os << v.get_wstring(true);
        return os;}

    inline void log(const bool & fill = true) const {
        // Logs the point with optional full details to standard output
        wcout << get_wstring(fill);}

};






extern "C" {
  Point * point_new(float x, float y, Marker * c) {return new PointFilled(x, y, *c);}
  //void point_set_fill(Point * point, bool fill, float x, float y) {point->set_fill(fill, x, y);}
  void point_delete(PointFilled * p) {delete p;}
  Marker * point_get_marker(PointFilled * p) {return new Marker(p->get_marker());}
  size_t point_get_col(PointFilled * c) noexcept {return c->get_col();}
  size_t point_get_row(PointFilled * c) noexcept {return c->get_row();}
  float point_get_x(PointFilled * c) noexcept {return c->get_x();}
  float point_get_y(PointFilled * c) noexcept {return c->get_y();}
  const wchar_t * point_get_wstring(PointFilled * c, bool fill) {return wstring_to_cstring(c->get_wstring(fill));}
}
