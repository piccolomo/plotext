class MiniDot {
private: 
  bool dot;

public:
  inline MiniDot() noexcept {dot = false;} 
  inline MiniDot operator|(const MiniDot & di) const noexcept {MiniDot r; r.dot = (this->dot | di.dot); return r;}
  inline MiniDot & operator=(const MiniDot & di) noexcept {dot = di.dot; return *this;}

  inline constexpr void set_dot(const bool & d) noexcept {dot = d;}
  inline constexpr void enable_dot() noexcept {dot = true;}
  inline constexpr bool get_dot() const noexcept {return dot;}

  inline void log() const noexcept {wcout << "dot " << bool_to_wchar(dot);}
};
