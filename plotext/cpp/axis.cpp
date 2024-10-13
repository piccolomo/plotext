enum axis_scale {normal_scale, log_scale};

class Axis {
private:
  pair<float, float> lim;
  float fill_level;
  float delta = pow(10, -4);
  axis_scale scale;

public:
  inline void set_lim(const float & left, const float & right) noexcept {lim = make_pair(left, right);}
  inline void set_fill_level(const float & level) noexcept {fill_level = level;}
  inline void set_delta(const float & d) noexcept {delta = d;}
  inline void set_scale(const axis_scale & s) noexcept {scale = s;}
  
  inline constexpr pair<float, float> get_lim() const noexcept {if (scale == log_scale) {return make_pair(log10(lim.first), log10(lim.second));} else {return lim;}}
  inline constexpr float get_fill_level() const noexcept {if (scale == log_scale) {return log10(fill_level);} else {return fill_level;}}
  inline constexpr float get_span() const noexcept {return lim.second - lim.first;}
  inline constexpr float get_delta() const noexcept {return delta;}
  inline constexpr axis_scale get_scale() const noexcept {return scale;}

};

