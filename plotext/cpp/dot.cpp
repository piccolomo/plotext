class Dot : public Marker, public DotMatrix, public DotPosition {

public:
  //inline Dot() noexcept : Marker(), DotMatrix(0, 0), DotPosition() {}

  //inline Dot(const size_t & col, const size_t & row, const CharacterCanvas & ch) noexcept : col(col), row(row), CharacterCanvas(ch) {}
  inline Dot(const Point & p) noexcept : Marker(p), DotMatrix(p), DotPosition(p) {}

  inline Dot(const Dot & p) noexcept : Marker(p), DotMatrix(p), DotPosition(p) {}


  inline Dot & operator=(const Dot & d) noexcept {Marker::operator=(d); DotMatrix::operator=(d); DotPosition::operator=(d); return *this;}
  //inline Dot & operator=(Dot && d) noexcept {Marker::operator=(move(d)); DotMatrix::operator=(move(d)); DotPosition::operator=(move(d)); return *this;}

  inline CharacterCanvas get_character_canvas() const noexcept {CharacterCanvas out(*this); out.copy_matrix(*this); return out;}

  inline void log(const bool & full = false) const noexcept {wcout << L"("; DotPosition::log(); wcout << ", "; get_character_canvas().log(); if(full) {wcout << L", "; DotMatrix::log();} wcout << L")";}
};