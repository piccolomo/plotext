class Point : public Marker, public MarkerInfo {
private: 
  float x, y;

public:
  inline Point() noexcept = default;
  inline Point(const float & xi, const float & yi, const Marker & m, const MarkerInfo & mi = MarkerInfo()) noexcept : x(xi), y(yi), Marker(m), MarkerInfo(mi) {}

  inline Point(const float & xi, const float & yi, const Point & p, const MarkerInfo & mi = MarkerInfo()) noexcept : x(xi), y(yi), Marker(p.get_type(), p), MarkerInfo(mi) {if (p.is_normal()) {set_char(p.get_char());}}

  inline constexpr float get_x() const {return x;}
  inline constexpr float get_y() const {return y;}

  inline constexpr float get_col() const {return static_cast<size_t>(x);}
  inline constexpr float get_row() const {return static_cast<size_t>(y);}

  inline void set_x(const float & el) {x = el;}
  inline void set_y(const float & el) {y = el;}
  
  inline void log(const bool & full = false) const noexcept {
  	wcout << L"(" + str_round(x, 2) + L", " + str_round(y, 2) + L", ";
  	Marker::log(); wcout << L")";}
};

  //inline Point(const Point & p) noexcept : x(p.x), y(p.y), Marker(p), MarkerInfo(p) {}//wcout << "copy ";}
  //inline Point(Point && p) noexcept : x(move(p.x)), y(move(p.y)), Marker(move(p)), MarkerInfo(move(p)) {}//wcout << "move ";}
 // inline Point & operator=(const Point & p) {Marker::operator=(p); MarkerInfo::operator=(p); return *this;}
