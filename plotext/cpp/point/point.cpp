// A class to represent a 2D point with position, marker, and fill attributes.
// Inherits from PointPosition, Marker, and PointFill.

class Point : public PointPosition, public Marker {
public:

  Point() = default; // Default constructor

  Point(const float & xi, const float & yi, const Marker & m = Marker()) 
    : PointPosition(xi, yi), Marker(m) {} // Constructor with position, marker, and fill

  Point(const float & xi, const float & yi, const Point & p)  
    : PointPosition(xi, yi), Marker(p.get(), p) {if (p.is_normal()) {set_wcharacter(p.get_wcharacter());}} // Copy marker character if normal

  Point(const Point & point) : PointPosition(point), Marker(point) {} // Copy constructor

  Point(Point && point) : PointPosition(move(point)), Marker(move(point)) {} // Move constructor

  Point & operator=(const Point & p) {
    // Assignment operator
    PointPosition::operator=(p); 
    Marker::operator=(p); 
    //fill = p.fill; 
    return *this;}

  constexpr marker_type get_type() const {return MarkerType::get();}

  //Marker get_marker() const {return Marker(*this);}

  wstring get_wstring() const {
    // Returns a wide string representation of the point
    wostringstream woss;
    woss << L"(" << PointPosition::get_wstring() << L", " << Marker::get_wstring() << L")";
    return woss.str();}

  inline void log() const {
    // Logs the point with optional full details to standard output
    wcout << get_wstring() << flush;}
};


class FillPoint: public Point {
private:
  bool fill;

public:
  using Point::Point;
  FillPoint(const Point & point) : Point(point) {disable();}
  FillPoint(const FillPoint & point) : Point(point) {fill = point.fill;}


  bool get_fill() const noexcept {return fill;}
  void set_fill(const bool & f) noexcept {fill = f;}
  void enable() noexcept {fill = true;}
  void disable() noexcept {fill = false;}

};


extern "C" {
  Point * point_new(float x, float y, Marker * c) {return new Point(x, y, *c);}
  //void point_set_fill(Point * point, bool fill, float x, float y) {point->set_fill(fill, x, y);}
  void point_delete(Point * p) {delete p;}
  Marker * point_get_marker(Point * p) {return new Marker(*p);}
  float point_get_col(Point * c) noexcept {return c->get_col();}
  float point_get_row(Point * c) noexcept {return c->get_row();}

  const wchar_t * point_get_wstring(Point * c) {return wstring_to_cstring(c->get_wstring());}}
