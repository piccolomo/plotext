class Canvas : public MatrixCanvas {
private:
  pair<Axis, Axis> xaxis;
  pair<Axis, Axis> yaxis;

public:
  inline Canvas(const size_t width, const size_t height) noexcept : MatrixCanvas(width, height) {}
  inline Canvas(const size_t width, const size_t height, const Character & c) noexcept : MatrixCanvas(width, height, c) {}
  inline Canvas(const size_t width, const size_t height, const Pixel & p) noexcept : MatrixCanvas(width, height, p) {}

  inline Axis & get_xaxis(const bool & side) noexcept {if (side) {return xaxis.second;} else {return xaxis.first;} }
  inline Axis & get_yaxis(const bool & side) noexcept {if (side) {return yaxis.second;} else {return yaxis.first;} }
  inline Axis & get_axis(const bool & axis, const bool & side) noexcept {if (axis) {return get_yaxis(side);} else {return get_xaxis(side);} }
  
  inline void set_lim(const bool & axis, const bool & side, const float & left, const float & right) noexcept {get_axis(axis, side).set_lim(left, right);}
  
  inline pair<float, float> get_lim(const bool & axis, const bool & side) noexcept {return get_axis(axis, side).get_lim();}
  
  inline void set_fill_level(const bool & axis, const bool & side, const float & level) noexcept {get_axis(axis, side).set_fill_level(level);}

  inline float get_fill_level(const bool & axis, const bool & side) noexcept {return get_axis(axis, side).get_fill_level();}

  inline void set_delta(const bool & axis, const bool & side, const float & delta) noexcept {get_axis(axis, side).set_delta(delta);}

  inline float get_delta(const bool & axis, const bool & side) noexcept {return get_axis(axis, side).get_delta();}

  
  inline void draw(Points points, const bool & xside = 0, const bool & yside = 0) noexcept {
    auto xlim = get_lim(0, xside);
    auto ylim = get_lim(1, yside);
    auto width = get_width();
    auto height = get_height();

    auto xdelta = get_delta(0, xside);
    auto ydelta = get_delta(1, yside);

    points.rescale_x(width, xlim, xdelta);
    points.rescale_y(height, ylim, ydelta);

    points.add_lines();

    size_t fillx_level = rescale(get_fill_level(0, xside), ylim, height, xdelta);
    size_t filly_level = rescale(get_fill_level(1, yside), xlim, width, ydelta);

    size_t length = points.get_length();
    Dots dots(length); for(size_t i = 0; i < length; i++) {dots.add(points.at(i));}
    //dots.log(1);

    dots.fill(1, fillx_level);
    dots.fill(0, filly_level);

    length = dots.get_length(); for(size_t i = 0; i < length; i++) {Dot & dot = dots.at(i); insert(dot.get_col(), dot.get_row(), dot.get_character_canvas());}
    //dots.log_map();
    }
    	
    inline void show() noexcept {MatrixCanvas::get_matrix().show();}
};



