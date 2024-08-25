class DotPosition {
private:
  size_t col, row;

public:
  inline DotPosition() noexcept {col = 0; row = 0;}

  inline DotPosition(const size_t & col, const size_t & row) noexcept : col(col), row(row) {}
  inline DotPosition(const Point & p) noexcept : DotPosition(p.get_col(), p.get_row()) {}

  inline DotPosition & operator=(const DotPosition & d) noexcept {col = d.col; row = d.row; return *this;}

  inline void set_row(const float & el) {row = el;}
  inline void set_col(const float & el) {col = el;}

  constexpr inline size_t get_col() const noexcept {return col;}
  constexpr inline size_t get_row() const noexcept {return row;}

  inline void log() const noexcept {wcout << get_col() << L", " << get_row();}
};