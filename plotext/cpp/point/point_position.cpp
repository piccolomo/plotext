// A class to represent and manipulate the position of a point in the plot canvas.

class PointPosition {
private:
  float x, y; // Coordinates of the point

public:
  PointPosition() = default; // Default constructor
  PointPosition(const float & xi, const float & yi) : x(xi), y(yi) {} // Constructor with x and y

  PointPosition(const PointPosition & other) : x(other.x), y(other.y) {} // Copy constructor
  PointPosition(PointPosition && other) : x(other.x), y(other.y) {} // Move constructor

  PointPosition & operator=(const PointPosition & p) {x = p.x; y = p.y; return *this;} // Assignment operator

  float get_x() const noexcept {return x;} // Get x-coordinate
  float get_y() const noexcept {return y;} // Get y-coordinate

  float get_col() const noexcept {return static_cast<size_t>(x);} // Get column (as size_t)
  float get_row() const noexcept {return static_cast<size_t>(y);} // Get row (as size_t)

  void set_x(const float & el) noexcept {x = el;} // Set x-coordinate
  void set_y(const float & el) noexcept {y = el;} // Set y-coordinate
  void set(const float & xi, const float & yi) noexcept {x = xi; y = yi;}
  void add_offset(const float & dx, const float & dy) noexcept {x += dx; y += dy;}

  void rescale_x(const pair<float, float> & xlim, const size_t & width, const float & delta) noexcept {x = rescale_element(x, xlim, width, delta);}
  void rescale_y(const pair<float, float> & ylim, const size_t & height, const float & delta) noexcept {y = rescale_element(y, ylim, height, delta);}

  void log_x() noexcept {x = log10(x);} 
  void log_y() noexcept {y = log10(y);} 

  wstring get_wstring() const noexcept { 
    // Returns a wide string representation of the point
    wostringstream woss; 
    woss << fixed << setprecision(3) << get_x() << L", " << get_y(); 
    return woss.str();
  }

  void log() const {wcout << get_wstring() << flush;} // Logs the point to standard output
};