// Class to represent a character canvas, combining Marker and MatrixBool functionality.

class CharacterHD : public Marker, public MatrixBool {
public:
  using MatrixBool::set;
  using MatrixBool::get;
  
  // Constructor initializing with a Marker object (default or provided).
  CharacterHD(const Marker & m = Marker()) 
    : MatrixBool(m.get_cols(), m.get_rows()), Marker(m) {}

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
    MatrixBool(0, 0); 
    return *this;}

  void set_wcharacter(const wchar_t & cs) noexcept {Marker::set_wcharacter(cs); zero(); }

  // Get the character representation based on type or code.
  wchar_t get_wcharacter() const {
    if (is_normal()) {return Marker::get_wcharacter();} 
    else {return get_marker_converter(MarkerType::get())(MatrixBool::get_code());}}

  // Get a Character object based on the current state.
  Character get_character() const {return Character(get_wcharacter(), *this);}

  // Convert character to buffer.
  void character_to_buffer(wchar_t* buffer, size_t& length_buffer) const { 
    wchar_to_buffer(get_wcharacter(), buffer, length_buffer);}

  // Write character and pixel data to buffer.
  void to_buffer(wchar_t* buffer, size_t& length_buffer) const override { 
    pixel_to_buffer(buffer, length_buffer); // Add pixel data to buffer.
    character_to_buffer(buffer, length_buffer); // Add character data to buffer.
    cstring_to_buffer(ansi_end, buffer, length_buffer);} // Add ANSI end string.
  
  // Log the current character canvas state.
  void print() const { 
    wchar_t buffer[character_size_max + 1] = {'\0'}; // Initialize buffer.
    size_t length = 0; 
    to_buffer(buffer, length); 
    wcout << buffer;}

};

 //using MatrixBool::get_code; // Expose get_code from MatrixBool.
