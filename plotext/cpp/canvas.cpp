class Canvas : public MatrixCanvas {
private:
  Axis xaxis;
  Axis yaxis;

public:
  inline Canvas(const size_t width, const size_t height) noexcept : MatrixCanvas(width, height) {}
  inline Canvas(const size_t width, const size_t height, const Character & c) noexcept : MatrixCanvas(width, height, c) {}
  inline Canvas(const size_t width, const size_t height, const Pixel & p) noexcept : MatrixCanvas(width, height, p) {}
  
  inline void set_xlim(const float & left, const float & right) noexcept {xaxis.set_lim(left, right);}
  inline void set_ylim(const float & lower, const float & upper) noexcept {yaxis.set_lim(lower, upper);}
  
  inline void set_fillx_level(const float & level) noexcept {xaxis.set_fill_level(level);}
  inline void set_filly_level(const float & level) noexcept {yaxis.set_fill_level(level);}
  
  inline void draw(Points points) noexcept {
    auto xlim = xaxis.get_lim();
    auto ylim = yaxis.get_lim();
    auto width = get_width();
    auto height = get_height();
    
    points.rescale_xy(width, height, xlim, ylim);
    points.add_lines();

    size_t fillx_level = rescale(xaxis.get_fill_level(), ylim, height);
    size_t filly_level = rescale(yaxis.get_fill_level(), xlim, width);

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