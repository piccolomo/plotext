// Class to manage a collection of Dot objects, inheriting from DotsMap.

class Dots : public DotsMap {
private:
  vector<Dot> dots; // Vector to store Dot objects.

public:
  // Constructor to initialize the Dots container with reserved size.
  Dots(const size_t & size) {dots.reserve(size);}

  // Get the current number of dots.
  size_t get_length() const {return dots.size();}

  // Access a Dot object at a specific index.
  Dot & get(const size_t & i) {return dots.at(i);}

  // Add a Point to the collection, creating or updating a Dot.
  void add(const Point & p) {
    float x = p.get_x(), y = p.get_y(); // Get point coordinates.
    size_t c = p.get_col(), r = p.get_row(); // Get grid position.
    size_t index = get_index(c, r); // Get the index for this position.
    size_t length = get_length();

    bool no_previous_dot = (index == size_max); // Check if no dot exists at this position.
    if (no_previous_dot) {
      dots.emplace_back(p); // Create a new dot for the point.
      add_index(c, r, length);} // Update the index map.
    else {
      Dot & dot = get(index);
      dot.set_type(p.get_type()); 
      dot.copy_pixel(p); // Update the existing dot's pixel.
      if (p.is_normal()) {dot.set_wcharacter(p.get_wcharacter());}
      else {dot.add_dot(x, y);}
        }} // Add details if not normal.

  // // Add a Dot to the collection, creating or updating an existing Dot.
  // void add(const Dot & dot) {
  //   size_t c = dot.get_col(), r = dot.get_row(); // Get grid position.
  //   size_t index = get_index(c, r); // Get the index for this position.
  //   size_t length = get_length();

  //   bool no_previous_dot = (index == size_max); // Check if no dot exists at this position.
  //   if (no_previous_dot) {
  //     dots.emplace_back(dot); // Create a new dot.
  //     add_index(c, r, length);} // Update the index map.
  //   else {get(index).copy_pixel(dot); // Update the existing dot's pixel.
  //     if (get(index).is_hd()) {get(index).sum(dot);}
  //     }} // Combine dot details if not normal.

    // Get string representation of points
    std::wstring get_wstring() const {
        std::wostringstream woss;
        size_t length = get_length();
        woss << L"Dots [";
        for (size_t i = 0; i < length; i++) {
            woss << dots.at(i).get_wstring();
            if (i != length - 1) {woss << L", ";}}
        woss << L"]";
        return woss.str();}

    // Log points to output
    void log() const {
        std::wcout << get_wstring() << std::flush;}

  // Log the map representation of dots.
  void log_map() {DotsMap::log();}

  // Get a constant iterator to the beginning of the dots vector.
  vector<Dot>::const_iterator begin() const {return dots.begin();}

  // Get a constant iterator to the end of the dots vector.
  vector<Dot>::const_iterator end() const {return dots.end();}

};


extern "C" {
  Dots * dots_new(size_t size) noexcept {return new Dots(size);}
  void dots_delete(Dots * dots) noexcept {delete dots;}
  void dots_add(Dots * dots, Point * p) noexcept {dots->add(*p);}
  size_t dots_get_length(Dots * dots) noexcept {return dots->get_length();}
  Dot * dots_get(Dots * p, size_t i) noexcept {return new Dot(p->get(i));}
  const wchar_t * dots_get_wstring(Dots * c) noexcept {return wstring_to_cstring(c->get_wstring());}
  void dots_log(Dots * dots) noexcept {dots->log();}

}
