class Dots : public MatrixMap {
private:
  vector<Dot> dots;

public:
  inline Dots(const size_t & size) noexcept {dots.reserve(size);}

  inline size_t get_length() const noexcept {return dots.size();}
  inline Dot & at(const size_t & i) noexcept {return dots.at(i);}

  inline void add(const Point & p) noexcept {
    float x = p.get_x(); float y = p.get_y(); 
    size_t c = p.get_col(); size_t r = p.get_row(); 
    size_t index = get_index(c, r);
    size_t length = get_length();
    
    bool no_previous_dot = (index == size_max);
    if (no_previous_dot) {dots.emplace_back(p); add_index(c, r, length);}
    else {at(index).copy_pixel(p); at(index).add_dot(x, y, p);}}
 
  inline void add(const Dot & dot) noexcept {
    size_t c = dot.get_col(); size_t r = dot.get_row(); 
    size_t index = get_index(c, r);
    size_t length = get_length();
    bool no_previous_dot = (index == size_max);
    if (no_previous_dot) {dots.emplace_back(dot); add_index(c, r, length);}
    else {at(index).copy_pixel(dot); at(index).sum_matrix(dot);}}

  inline void fill(const bool xaxis, const size_t & level) noexcept {
    size_t length = get_length();
    for(size_t i = 0; i < length; i++) {
      if (not at(i).get_fill(xaxis)) {continue;}
      Dot & dot = at(i); size_t pos; if (xaxis) {pos = dot.get_row();} else {pos = dot.get_col();}
      bool forward = pos < level;
      if (xaxis) {dot.fill_cols(forward);} else {dot.fill_rows(forward);}
      Dot dot_filled = dot;
      if (xaxis) {dot_filled.fill_cols(not forward);} else {dot_filled.fill_rows(not forward);}
      size_t start = pos + 1; size_t end = level; if (not forward) {start = level; end = pos;}
      for(size_t p = start; p < end; p++) {if (xaxis) {dot_filled.set_row(p);} else {dot_filled.set_col(p);} add(dot_filled);}}}

  inline void log() noexcept {size_t length = get_length(); wcout << L"Dots ["; for(size_t i = 0; i < length; i++) {at(i).log(); if (i != length - 1) {wcout << ", ";}} wcout << L"]" << endl;}

  inline vector<Dot>::const_iterator begin() const noexcept {return dots.begin();}
  inline vector<Dot>::const_iterator end() const noexcept {return dots.end();}
};