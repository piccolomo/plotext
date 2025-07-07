// Class representing a Dot, which is a rescaled Point within a plot canvas

class Dot : public Marker, public MatrixBool, public DotPosition {

public:
  // Constructor that initializes Marker, MatrixBool, and DotPosition with a point.
  Dot(const Point & p) noexcept : Marker(p), MatrixBool(p.get_cols(), p.get_rows()), DotPosition(p) 
    {if (p.is_hd()) {add_dot(p.get_x(), p.get_y());}}

  // Copy constructor initializing from another Dot object.
  Dot(const Dot & d) noexcept : Marker(d), MatrixBool(d), DotPosition(d) {}

  // Assignment operator copying values from another Dot.
  Dot & operator=(const Dot & d) noexcept {
    Marker::operator=(d);  // Assign Marker part 
    MatrixBool::operator=(d);  // Assign MatrixBool part 
    DotPosition::operator=(d);  // Assign DotPosition part 
    return *this;}
  
  // Method to set the marker type, clearing and recreating the matrix if the type changes.
  void set_type(const marker_type & t) noexcept {
    auto type_old = MarkerType::get(); // Get the current marker type.
    if (type_old != t) {clear_matrix();} // If the type is different, clear the matrix.
    MarkerType::set(t); // Set the new marker type.
    if (type_old != t) {create_matrix();}}  // If the type was changed, recreate the matrix.

constexpr marker_type get_type() const {return MarkerType::get();}
  
// Returns a CharacterHD object, copying the matrix from the current Dot.
  CharacterHD get_character_hd() const noexcept {
    CharacterHD out(*this);
    out.copy_matrix(*this);  // Copy matrix into the CharacterCanvas.
    return out;}

  wstring get_wstring() const {
    // Returns a wide string representation of the point
    wostringstream woss;
    woss << L"(" << DotPosition::get_wstring() << L", " << Marker::get_wstring();
    if(is_hd()) {woss << L", " <<  MatrixBool::get_wstring();}
    woss << L")";
    return woss.str();}

  inline void log() const {
    // Logs the point to standard output
    wcout << get_wstring() << flush;}

};

extern "C" {
  Dot * dot_new(const Point * p) noexcept {return new Dot(*p);}
  void dot_delete(Dot * p) noexcept {delete p;}
  const wchar_t * dot_get_wstring(Dot * c) noexcept {return wstring_to_cstring(c->get_wstring());}

}