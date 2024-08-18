class Dot : public CharacterCanvas {
private:
  size_t col, row;

public:
  inline Dot() noexcept : CharacterCanvas() {col = 0; row = 0;}

  inline Dot(const size_t & col, const size_t & row, const CharacterCanvas & ch) noexcept : col(col), row(row), CharacterCanvas(ch) {}
  inline Dot(const Point & p) noexcept : Dot(p.get_col(), p.get_row(), p) {add_dot(p.get_x(), p.get_y(), p);}

  inline Dot & operator=(const Dot & d) noexcept {CharacterCanvas::operator=(d); col = d.col; row = d.row; return *this;}

  inline void set_row(const float & el) {row = el;}
  inline void set_col(const float & el) {col = el;}

  constexpr inline size_t get_col() const noexcept {return col;}
  constexpr inline size_t get_row() const noexcept {return row;}

  inline void log() const noexcept {
  	wcout << L"(" + to_wstring(col) + L", " + to_wstring(row) + L", ";
  	CharacterCanvas::log(); wcout << L")";}
};