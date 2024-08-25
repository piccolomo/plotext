class PointInfo : public FillInfo {
private: 
  bool lines = false;

public:
  inline constexpr PointInfo(const bool & ls = false, const bool & fx = false, const bool & fy = false) noexcept  : lines(ls), FillInfo(fx, fy) {};
  inline constexpr PointInfo(const FillInfo & fi) noexcept  : FillInfo(fi) {};
  //inline constexpr PointInfo operator|(const PointInfo & p) const noexcept {PointInfo r; FillInfo::operator|(r); r = r.set_lines(lines | p.lines); return r;}
  
  inline PointInfo(const PointInfo & other) noexcept : FillInfo(other), lines(other.lines) {}
  inline PointInfo(PointInfo && other) noexcept : FillInfo(std::move(other)), lines(other.lines) {}

  inline PointInfo & operator=(const PointInfo & p) noexcept {FillInfo::operator=(p); lines = p.lines; return *this;}


  inline constexpr void set_lines(const bool & l) noexcept {lines = l;}
  //inline constexpr void disable_lines(const bool & l) noexcept {lines = l;}
  inline constexpr bool get_lines() const noexcept {return lines;}

  inline void log() const noexcept {FillInfo::log(); wcout << L", lines " << bool_to_wchar(lines);}
};


  // inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
  //   cstring_to_buffer(L"lines ", buffer, length_buffer);
  //   wchar_to_buffer(bool_to_wchar(lines), buffer, length_buffer);
  //   cstring_to_buffer(L", ", buffer, length_buffer);
  //   FillInfo::to_buffer(buffer, length_buffer);}
