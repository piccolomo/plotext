class PointPosition {
private:
  float x, y;

public:
  inline PointPosition() noexcept = default;
  inline PointPosition(const float & xi, const float & yi) noexcept : x(xi), y(yi) {}

  inline PointPosition(const PointPosition & other) noexcept : x(other.x), y(other.y) {}
  inline PointPosition(PointPosition && other) noexcept : x(other.x), y(other.y) {}

  inline PointPosition & operator=(const PointPosition & p) noexcept {x = p.x; y = p.y; return *this;}

  inline constexpr float get_x() const {return x;}
  inline constexpr float get_y() const {return y;}

  inline constexpr float get_col() const {return static_cast<size_t>(x);}
  inline constexpr float get_row() const {return static_cast<size_t>(y);}

  inline void set_x(const float & el) {x = el;}
  inline void set_y(const float & el) {y = el;}

  inline wstring get_wstring() const noexcept {
    wostringstream woss;
    woss << fixed << setprecision(2) << get_x() << L", " << get_y();
    return woss.str();}

  inline void log() const noexcept {wcout << get_wstring() << flush;}
};

  //inline Point(const Point & p) noexcept : x(p.x), y(p.y), Marker(p), MarkerInfo(p) {}//wcout << "copy ";}
  //inline Point(Point && p) noexcept : x(move(p.x)), y(move(p.y)), Marker(move(p)), MarkerInfo(move(p)) {}//wcout << "move ";}
 // inline Point & operator=(const Point & p) {Marker::operator=(p); MarkerInfo::operator=(p); return *this;}
