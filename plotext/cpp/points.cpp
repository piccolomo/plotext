class Points {
private:
  vector<Point> points;

public:
  inline Points() noexcept = default;
  inline Points(const size_t & size) noexcept {points.reserve(size * 50);};

  inline size_t get_length() const noexcept {return points.size();}
  inline Point & at(const size_t & i) noexcept {return points.at(i);}

  inline void add(const float & xi, const float & yi, const Marker & m, const PointInfo & mi = PointInfo()) noexcept {points.emplace_back(xi, yi, m, mi);}

  inline void rescale_xy(const size_t & width, const size_t & height, const pair<float, float> & xlim, const pair<float, float> & ylim) {
    for(size_t i = 0; i < get_length(); i++) {
      Point & p = points.at(i);
      float c = rescale(p.get_x(), xlim, width);
      float r = rescale(p.get_y(), ylim, height);
      p.set_x(c); p.set_y(r);}}

  inline void add_lines() noexcept {
 		size_t length = get_length();
 		vector<Point> P; P.reserve(get_length() * 50);
  	for(size_t i = 0; i < length - 1; i++){
      if (not at(i).get_lines()) {continue;}
	    float x1 = at(i).get_x(); float y1 = at(i).get_y(); 
	    float x2 = at(i + 1).get_x(); float y2 = at(i + 1).get_y(); 
    	float Dx = x2 - x1; float Dy = y2 - y1; float s = Dy / Dx;
      float dx = 1; float dy = 1; 
      if (at(i).is_not_normal()) {dx /= at(i).get_cols(); dy /= at(i).get_rows();}
      float ds = dy / dx;
    	float sx = Dx > 0 ? dx : -dx; float sy = Dy > 0 ? dy : -dy; 
    	PointInfo mi(at(i));
    	if   (abs(s / ds) < 1) {auto X = range(x1 + sx, x2, sx); for (auto & x: X) {auto y = s * (x - x1) + y1; P.emplace_back(x, y, at(i), mi);}}
    	else                   {auto Y = range(y1 + sy, y2, sy); for (auto & y: Y) {auto x = (y - y1) / s + x1; P.emplace_back(x, y, at(i), mi);}}
   		at(i).set_lines(0);}
   		if (length > 0) {at(length - 1).set_lines(0);}
   		points.insert(points.begin(), P.begin(), P.end());
    }

  inline void log(const bool & full = false) const noexcept {
    size_t length = get_length();
    wcout << L"Points ["; for(size_t i = 0; i < length; i++){points.at(i).log(full); if (i != length - 1){wcout << ", ";}} wcout << L"]" << endl;}
    
  inline vector<Point>::const_iterator begin() const noexcept {return points.begin();}
  inline vector<Point>::const_iterator end() const noexcept {return points.end();}
 };


/*  inline vector<float> get_x() const noexcept {
    size_t length = get_length();
    vector<float> x(length);
    for(size_t i = 0; i < length; i ++){x.push_back(points.at(i).get_x());} return x;}
  
  inline vector<float> get_y() const noexcept {
    size_t length = get_length();
    vector<float> y(length);
    for(size_t i = 0; i < length; i ++){y.push_back(points.at(i).get_y());} return y;}*/

/*  inline pair<float, float> get_xlim() const noexcept {
    vector<float> x = get_x();
    float min = *min_element(x.begin(), x.end());
    float max = *max_element(x.begin(), x.end());
    return make_pair(min, max);}

  inline pair<float, float> get_ylim() const noexcept {
    vector<float> y = get_y();
    float min = *min_element(y.begin(), y.end());
    float max = *max_element(y.begin(), y.end());
    return make_pair(min, max);}*/