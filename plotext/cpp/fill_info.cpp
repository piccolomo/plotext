class FillInfo {
private: 
  bool fillx = false;
  bool filly = false;

public:
  inline constexpr FillInfo(const bool & fx = false, const bool & fy = false) noexcept : fillx(fx), filly(fy) {};
  inline constexpr FillInfo & operator=(const FillInfo & other) noexcept {fillx = other.fillx; filly = other.filly; return *this;}
  inline constexpr FillInfo operator|(const FillInfo & fi) const noexcept {FillInfo r; r.fillx = (fillx | fi.fillx); r.filly = (filly | fi.filly); return r;}

  inline constexpr FillInfo(const FillInfo & other) noexcept : fillx(other.fillx), filly(other.filly) {}
  inline constexpr FillInfo(FillInfo && other) noexcept: fillx(other.fillx), filly(other.filly) {}

  inline constexpr void set_fillx(const bool & f) noexcept {fillx = f;}
  inline constexpr void set_filly(const bool & f) noexcept {filly = f;}

  inline constexpr void enable_fillx() noexcept {fillx = true;}
  inline constexpr void enable_filly() noexcept {filly = true;}
  
  inline constexpr bool get_fillx() const noexcept {return fillx;}
  inline constexpr bool get_filly() const noexcept {return filly;}

  inline bool get_fill(const bool & xaxis = 1) const noexcept {if (xaxis) {return get_fillx();} else {return get_filly();}}

  inline void log() const noexcept {wcout << L"fillx " << bool_to_wchar(fillx) <<  L", filly " << bool_to_wchar(filly);}
};

  // inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
  //   cstring_to_buffer(L"fillx ", buffer, length_buffer);
  //   wchar_to_buffer(bool_to_wchar(fillx), buffer, length_buffer);
  //   cstring_to_buffer(L", filly ", buffer, length_buffer);
  //   wchar_to_buffer(bool_to_wchar(filly), buffer, length_buffer);}    