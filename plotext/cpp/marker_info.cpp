class FillInfo {
private: 
  bool fillx = false;
  bool filly = false;

public:
  inline constexpr FillInfo(const bool & fx = false, const bool & fy = false) noexcept : fillx(fx), filly(fy) {};
  inline constexpr FillInfo & operator=(const FillInfo & other) noexcept {fillx = other.fillx; filly = other.filly; return *this;}
  inline constexpr FillInfo operator|(const FillInfo & fi) const noexcept {FillInfo r; r.set_fillx(get_fillx() | fi.get_fillx()); r.set_filly(get_filly() | fi.get_filly()); return r;}

  inline constexpr void set_fillx(const bool & f) noexcept {fillx = f;}
  inline constexpr void set_filly(const bool & f) noexcept {filly = f;}
  
  inline constexpr bool get_fillx() const noexcept {return fillx;}
  inline constexpr bool get_filly() const noexcept {return filly;}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    cstring_to_buffer(L"fillx ", buffer, length_buffer);
    wchar_to_buffer(bool_to_wchar(fillx), buffer, length_buffer);
    cstring_to_buffer(L", filly ", buffer, length_buffer);
    wchar_to_buffer(bool_to_wchar(filly), buffer, length_buffer);}
      
};


class MarkerInfo : public FillInfo {
private: 
  bool lines = false;

public:
  inline constexpr MarkerInfo(const bool & ls = false, const bool & fx = false, const bool & fy = false) noexcept  : lines(ls), FillInfo(fx, fy) {};
  //inline constexpr MarkerInfo operator|(const MarkerInfo & p) const noexcept {MarkerInfo r; FillInfo::operator|(r); r = r.set_lines(lines | p.lines); return r;}
  
  inline constexpr void set_lines(const bool & l) noexcept {lines = l;}

  inline constexpr bool get_lines() const noexcept {return lines;}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    cstring_to_buffer(L"lines ", buffer, length_buffer);
    wchar_to_buffer(bool_to_wchar(lines), buffer, length_buffer);
    cstring_to_buffer(L", ", buffer, length_buffer);
    FillInfo::to_buffer(buffer, length_buffer);}

  inline void log() const noexcept {
      wchar_t buffer[30 + 1]; buffer[0] = '\0';  size_t length = 0;
      to_buffer(buffer, length);
      wcout << buffer;}
};


class DotInfo : public FillInfo {
private: 
  bool dot = false;

public:
  inline constexpr DotInfo() = default; 
  inline constexpr DotInfo operator|(const FillInfo & fi) const noexcept {DotInfo r; static_cast<FillInfo&>(r) = static_cast<const FillInfo&>(*this) | fi; return r;}
  inline constexpr DotInfo operator|(const DotInfo & di) const noexcept {DotInfo r; r = (*this) | static_cast<const FillInfo&>(di); r.dot = this->dot | di.dot; return r;}
  inline constexpr DotInfo & operator=(const DotInfo& other) noexcept {FillInfo::operator=(other); dot = other.dot; return *this;}

  inline constexpr void set_dot(const bool & d) noexcept {dot = d;}
  inline constexpr bool get_dot() const noexcept {return dot;}
  inline constexpr FillInfo get_fill_info() const noexcept {return *this;}

};