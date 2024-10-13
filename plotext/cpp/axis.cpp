class Axis {
private:
  pair<float, float> lim;
  float fill_level;
  float delta = pow(10, -4);

public:
  inline void set_lim(const float & left, const float & right) noexcept {lim = make_pair(left, right);}
  inline void set_fill_level(const float & level) noexcept {fill_level = level;}
  inline void set_delta(const float & d) noexcept {delta = d;}
  
  inline constexpr pair<float, float> get_lim() const noexcept {return lim;}
  inline constexpr float get_fill_level() const noexcept {return fill_level;}
  inline constexpr float get_span() const noexcept {return lim.second - lim.first;}
  inline constexpr float get_delta() const noexcept {return delta;}
};

