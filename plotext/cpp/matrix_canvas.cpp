class MatrixCanvas {
private:
  StringCanvas * strings; 
  size_t height;

public:
  inline MatrixCanvas(const size_t & w, const size_t & h) noexcept : strings(new StringCanvas[h]), height(h) {for (int row = 0; row < height; row++) {StringCanvas * address = &strings[row]; new(address) StringCanvas(w);}}
  inline MatrixCanvas(const size_t & w, const size_t & h, const Pixel & p) noexcept : MatrixCanvas(w, h) {fill_pixel(p);}
  inline MatrixCanvas(const size_t & w, const size_t & h, const CharacterCanvas & c) noexcept : MatrixCanvas(w, h) {fill_character(c);}

  inline ~MatrixCanvas() noexcept {delete [] strings; strings = nullptr;}
  
  inline constexpr size_t get_height() const {return height;}
  inline constexpr size_t get_width() const {if (height == 0){return 0;} else {return strings[0].get_width();}}
  inline CharacterCanvas & get_character(const size_t & col,const size_t & row) const noexcept {return strings[row].get_character(col);}
  inline Matrix get_matrix() noexcept {Matrix m(get_width(), height);
    for (size_t i = 0; i < height; i++) {m.insert(0, i, strings[i].get_string());} return m;}

  inline constexpr void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t row = 0; row < height; row++){strings[row].fill_pixel(p);}}
  inline constexpr void fill_character(const CharacterCanvas & c) noexcept {for (size_t row = 0; row < height; row++){strings[row].fill_character(c);}}

  inline void insert(const size_t & col, const size_t & row, const CharacterCanvas & c) noexcept {strings[row].insert(col, c);} 
};

// Matrix vstack(Matrix & m1, MatrixCanvas & m2, bool & adapt = 0) {
  


// }