class PointInfo : public FillInfo {
private: 
  bool lines = false;

public:
  inline constexpr PointInfo(const bool & ls = false, const bool & fx = false, const bool & fy = false) noexcept  : lines(ls), FillInfo(fx, fy) {};
  inline constexpr PointInfo(const FillInfo & fi) noexcept  : FillInfo(fi) {};
  //inline constexpr PointInfo operator|(const PointInfo & p) const noexcept {PointInfo r; FillInfo::operator|(r); r = r.set_lines(lines | p.lines); return r;}
  
  inline PointInfo(const PointInfo & o) noexcept : FillInfo(o), lines(o.lines) {}
  inline PointInfo(PointInfo && o) noexcept : FillInfo(std::move(o)), lines(o.lines) {}

  inline PointInfo & operator=(const PointInfo & p) noexcept {FillInfo::operator=(p); lines = p.lines; return *this;}

  inline constexpr void set_lines(const bool & l) noexcept {lines = l;}
  //inline constexpr void disable_lines(const bool & l) noexcept {lines = l;}
  inline constexpr bool get_lines() const noexcept {return lines;}

  inline wstring get_wstring() const noexcept {wostringstream woss; woss << FillInfo::get_wstring() <<  L", lines " << bool_to_wchar(lines); return woss.str();}

  inline void log() const noexcept {wcout << get_wstring() << flush;}
};


  // inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
  //   cstring_to_buffer(L"lines ", buffer, length_buffer);
  //   wchar_to_buffer(bool_to_wchar(lines), buffer, length_buffer);
  //   cstring_to_buffer(L", ", buffer, length_buffer);
  //   FillInfo::to_buffer(buffer, length_buffer);}
