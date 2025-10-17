// Class to represent a character canvas, combining Marker and MatrixBool functionality.

class CharacterHD : public Marker, public MatrixBool {
public:
  using MatrixBool::set; 
  using MatrixBool::get; 

  // Constructor initializing with a Marker object (default or provided).
  CharacterHD(const Marker & m = Marker()) : MatrixBool(m.get_cols(), m.get_rows()), Marker(m) {}

  // Copy constructor.
  CharacterHD(const CharacterHD & c) : Marker(c), MatrixBool(c) {}

  // Copy constructor.
  CharacterHD(const Character & c) : Marker(c.get_wcharacter(), c), MatrixBool(0, 0) {}

  // Assignment operator.
  CharacterHD & operator=(const CharacterHD & c) {
    Marker::operator=(c); 
    MatrixBool::operator=(c); 
    return *this;}

  CharacterHD & operator=(const Character & c) {
    Marker::operator=(c); 
    MatrixBool::zero(); // just zero instead of recreating
    return *this;}

  // Method to set the marker type, clearing and recreating the matrix if the type changes.
  void set_type(const marker_type & type) noexcept {MarkerType::set(type); MatrixBool::set_size(Marker::get_cols(), Marker::get_rows());}

  constexpr marker_type get_type() const {return MarkerType::get();}

  //void set_wcharacter(const wchar_t & cs) noexcept {Marker::set_wcharacter(cs); }

  void update(const Point & p) noexcept {
    if (!same_type(p)) {set_type(p.get_type());}
    if (!same_pixel(p)) {copy_pixel(p);}
    if (p.is_normal()) {set_wcharacter(p.get_wcharacter());}
    if (p.is_high_definition()) {add_dot(p.get_inner_col(), p.get_inner_row()); update_wcharacter();}}

  // Get the character representation based on type or code.
  //inline wchar_t get_wcharacter() const noexcept {return Marker::get_wcharacter();} 

  // Get the character representation based on type or code.
  inline wchar_t get_wcharacter() const noexcept {
    uint8_t code = MatrixBool::get_code();
    wchar_t out;

    if (is_normal()) {out = Marker::get_wcharacter();}
    if (is_hd()) {out = hd_lookup[code];}
    if (is_fhd()) {out = fhd_lookup[code];}
    if (is_braille()) {out = braille_lookup[code];}
    if (is_none()) {out = L'?';}

    return out;}    

  inline void update_wcharacter() noexcept {set_wcharacter(get_wcharacter());}
  // Get a Character object based on the current state.
  //Character get_character() const {return Character(get_wcharacter(), *this);}

  // Write character and pixel data to buffer.
  void to_buffer(wchar_t* buffer, size_t& length_buffer) const noexcept override  { 
    Pixel::to_buffer(buffer, length_buffer); // Add pixel data to buffer.
    wchar_to_buffer(get_wcharacter(), buffer, length_buffer);
    cstring_to_buffer(ansi_end, buffer, length_buffer);} // Add ANSI end string.
  
  void print() const noexcept {
      wchar_t buffer[character_size_max + 1] = {L'\0'}; // Buffer for rendering
      size_t length = 0;
      to_buffer(buffer, length);                         // Fill buffer
      wcout.write(buffer, length);                       // Write entire buffer at once
      //wcout.flush();                                     // Flush to ensure output
      }
    
  wstring get_wstring() const {
    // Returns a wide string representation of the point
    wostringstream woss;
    woss << Marker::get_wstring();
    if(is_high_definition()) {woss << L", " <<  MatrixBool::get_wstring();}
    return woss.str();}

  inline void log() const {
    // Logs the point to standard output
    wcout << get_wstring() << flush;}

  inline void stream() const {Pixel::stream(); wcout.put(get_wcharacter());} 


};

 //using MatrixBool::get_code; // Expose get_code from MatrixBool.
