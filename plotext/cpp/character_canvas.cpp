class CharacterCanvas: public Marker, public MiniDotMatrix {

public:
  inline CharacterCanvas(const Marker & m = Marker()) noexcept : MiniDotMatrix(m.get_cols(), m.get_rows()), Marker(m) {}
  inline CharacterCanvas(const CharacterCanvas & c) : Marker(c), MiniDotMatrix(c) {}
  using MiniDotMatrix::get_code;

  inline CharacterCanvas & operator=(const CharacterCanvas & c) noexcept {Marker::operator=(c); MiniDotMatrix::operator=(c); return *this;}

  inline wchar_t get_char() const noexcept override {if (is_normal()) {return Marker::get_char();} else {return get_marker_converter(get_type())(get_code());}}
  inline Character get_character() const noexcept {return Character(get_char(), *this);}

  inline void character_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {wchar_to_buffer(get_char(), buffer, length_buffer);}
 
  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override {
      pixel_to_buffer(buffer, length_buffer);
      character_to_buffer(buffer, length_buffer);
      cstring_to_buffer(ansi_end, buffer, length_buffer);}
      
  inline void log() const noexcept {
      wchar_t buffer[character_size_max + 1]; buffer[0] = '\0';  size_t length = 0;
      to_buffer(buffer, length);
      wcout << buffer;}
	};


    //inline ~CharacterCanvas() noexcept {clear_matrix(); matrix = nullptr;}
