class Point : public PointPosition, public Marker, public PointInfo {
public:
  inline Point() noexcept = default;
  inline Point(const float & xi, const float & yi, const Marker & m, const PointInfo & mi = PointInfo()) noexcept : PointPosition(xi, yi), Marker(m), PointInfo(mi) {}
  inline Point(const float & xi, const float & yi, const Point & p, const PointInfo & mi = PointInfo()) noexcept : PointPosition(xi, yi), Marker(p.get_type(), p), PointInfo(mi) {if (p.is_normal()) {set_char(p.get_char());}}

  inline Point(const Point & other) noexcept : PointPosition(other), Marker(other), PointInfo(other) {}
  inline Point(Point && other) noexcept : PointPosition(move(other)), Marker(move(other)), PointInfo(move(other)) {}

  inline Point & operator=(const Point & p) noexcept {PointPosition::operator=(p); Marker::operator=(p); PointInfo::operator=(p);return *this;}

  inline wstring get_wstring(const bool & full = false) const noexcept {
    wostringstream woss;
    woss << L"(" << PointPosition::get_wstring() << L", " << Marker::get_wstring(); if (full) {woss << L", " << PointInfo::get_wstring();} 
    woss << L")";
    return woss.str();}

  inline void log(const bool & full = false) const noexcept {wcout << get_wstring(full) << flush;}

};

// inline void log(const bool & full = false) const noexcept {wcout << L"("; PointPosition::log(); wcout << L", "; Marker::log(); if (full) {wcout << L", "; PointInfo::log();} wcout << L")" << flush;}
//inline Point(const Point & p) noexcept : x(p.x), y(p.y), Marker(p), MarkerInfo(p) {}//wcout << "copy ";}
//inline Point(Point && p) noexcept : x(move(p.x)), y(move(p.y)), Marker(move(p)), MarkerInfo(move(p)) {}//wcout << "move ";}
// inline Point & operator=(const Point & p) {Marker::operator=(p); MarkerInfo::operator=(p); return *this;}
