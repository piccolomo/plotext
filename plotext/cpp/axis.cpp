class Axis {
private:
  pair<float, float> lim;
  float fill_level;

public:
  inline void set_lim(const pair<float, float> & yl) noexcept {lim = yl;}
  inline void set_fill_level(const float & level) noexcept {fill_level = level;}
  
  inline constexpr pair<float, float> get_lim() const noexcept {return lim;}
  inline constexpr float get_fill_level() const noexcept {return fill_level;}
  inline constexpr float get_span() const noexcept {return lim.second - lim.first;}
};

