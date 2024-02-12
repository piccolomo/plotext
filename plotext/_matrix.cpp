#include <iostream>
#include <vector>

#ifdef _WIN32
    #include <Windows.h>
#endif

#include "_pixel.cpp"

using namespace std;

int get_displacement(int width, int ha){if (ha == -1) {return 0;} else if (ha == 0) {return - width / 2;} else {return 1 - width;}}


class String{
public:
  vector<Pixel> pixel;
  vector<wstring > string;

  String(size_t l = 0, Pixel p = Pixel()) {resize(l); fill(p);}
  
  String(wstring s, Pixel p = Pixel()) : String(s.length()) {
    insert(0, s, p);
    init_string();
    update_string(0);
    update_string(s.length());
  }
  
  String(const String & s) : pixel(s.pixel), string(s.string) {}
  
  ~String() {pixel.clear(); string.clear();}

  void fill(Pixel p = Pixel()){pixel.assign(width(), p); init_string();
      update_string(0);}

  void insert(size_t col, wstring s, Pixel p = Pixel()){
    size_t sl = s.length();
    for(size_t c = col; c < col + sl; c++){
      p.set_marker(s[c - col]);
      pixel.at(c) = p;
      string.at(c) = p.m;}
    update_string(col);
    update_string(col + sl);
  }
  
  void insert(size_t col, String s){
    size_t sl = s.width();
    for(size_t c = col; c < col + sl; c++){
      pixel.at(c) = s.pixel.at(c - col);
      string.at(c) = s.string.at(c - col); }
    update_string(col);
    update_string(col + sl);}

  bool insert_aligned(size_t col, String s, int ha = -1, bool check_spaces = true){
    int col_start = col + get_displacement(s.width(), ha);
    int col_end = col_start + s.width();
    bool col_ok = col_start >= 0 and col_end <= width();
    bool spaces_ok = (not check_spaces) or check(col_start - 1, col_end + 1);
    bool ok = col_ok and spaces_ok;
    if (ok){insert(col_start, s);}
    return ok;}

  bool insert_dynamic(size_t col, String s){
    int length = s.width();
    size_t left = length / 2; size_t right = length - left;
    size_t span = max(left, right) + 1;
    for (size_t delta = 0; delta < span; delta++){
      char directions [] = {-1, 1};
      for (size_t direction: directions){
   	int col_center = col + direction * delta;
	int col_left = col_center - left;
	int col_right = col_left + length;
   	if (col_left > col or col_right < col or col > width() - 1){continue;}
	//bool out = check(col_left, col_left + length);
	bool out = insert_aligned(col_center, s, 0);
	//if (out) {out = insert_aligned(col_center, s, 0);}
   	if (out){return true;}
   	else{continue;}}}
    return false;}


  void clear(){for (size_t i = 0; i < width(); i++){pixel.at(i).clear(); string.at(i).clear();}}

  void resize(size_t length) {pixel.resize(length); string.resize(length);}

  String hstack(String s){String n(width() + s.width());
    copy(this->pixel.begin(), this->pixel.end(), n.pixel.begin());
    copy(s.pixel.begin(), s.pixel.end(), n.pixel.begin() + width());
    n.init_string();
    n.update_string(0);
    return n;}

  void init_string(){
    for (size_t i = 0; i < width(); i++){string.at(i) = pixel.at(i).m;}}
  
  void update_string(size_t col){if(col != width() and new_color(col)){string.at(col) = pixel.at(col).get_string(2);}}
  
  bool new_color(size_t col){return col == 0 or pixel.at(col) != pixel.at(col - 1);}

  bool check(size_t col_start, size_t col_end){
    col_start = max(0, (int)col_start);
    col_end = min(col_end, width());
    if(width() == 0){col_end = 0;}
    bool res = true;
    for (size_t col = col_start; col < col_end; col++){res = res and pixel.at(col).check();}
    return res;}

  size_t width() const {return pixel.size();}

  String part(size_t col, size_t cols){
    size_t real_cols = min(cols, width() - col);
    String s(real_cols);
    for (size_t c = 0; c < real_cols; c++){s.pixel[c] = pixel[c + col];}
    s.init_string();
    s.update_string(col); s.update_string(s.width());
    return s;}
  
  wstring at(size_t col, bool colorless = false){if(colorless){return to_wstring(pixel.at(col).m);} else{return string.at(col);}}

  wstring get_string(bool colorless = false){wstring out = L"";
    if(not colorless){for(size_t col = 0; col < width(); col++){out.append(string.at(col));}}
    else{for (size_t col = 0; col < width(); col++){out.append(wstring(1, pixel.at(col).m));}}
    if(colorless){return out;} else{return out + ansi_end;};}

  void show() {wcout << get_string();}

  void show_new_color(){for(size_t col = 0; col < width(); col++){wcout << new_color(col);} wcout << endl;}
};


void print_wstring(wstring s) {
    wchar_t* result = new wchar_t[s.length() + 1];
    wcscpy(result, s.c_str());
    wcout << result << endl;
    delete[] result;}


class Matrix{
public:
  vector<String> line; 

  Matrix(size_t width = 0, size_t height = 0, Pixel p = Pixel()) {line.assign(height, String(width, p));}

  Matrix(const Matrix & m) : line(m.line) {}
  
  ~Matrix(){line.clear();}

  void insert_pixel(size_t col, size_t row, Pixel p = Pixel()){line.at(row).insert(col, wstring(1, p.m), p);}

  void insert_string(size_t col, size_t row, wstring s, Pixel p = Pixel()){
    line.at(row).insert(col, s, p);}

  void insert_matrix(size_t col, size_t row, Matrix m){
    for (size_t r = 0; r < m.height(); r++){line.at(row + r).insert(col, m.line.at(r));}}

  bool insert_aligned(size_t col, size_t row, Matrix m, int ha = -1, int va = -1, bool check_spaces = false){
    size_t row_start = row + get_displacement(m.height(), va);
    size_t row_end = row_start + m.height();
    bool row_ok = row_start >= 0 and row_end <= height();
    if (row_ok){for(size_t r = row_start; r < row_end; r++) {line.at(r).insert_aligned(col, m.line.at(r - row_start), ha, check_spaces);};}
    return row_ok;}

  bool insert_dynamic(size_t col, size_t row, String s){return line.at(row).insert_dynamic(col, s);}

  void fill(Pixel p = Pixel()){for (size_t row = 0; row < height(); row++){line.at(row).fill(p);}}
  
  void clear(){for (size_t row = 0; row < height(); row ++){line.at(row).clear();}}

  void resize(size_t width, size_t height, Pixel p = Pixel()){line.assign(height, String(width, p));}

  Matrix vstack(Matrix m){Matrix n(width(), height() + m.height()); copy(this->line.begin(), this->line.end(), n.line.begin()); copy(m.line.begin(), m.line.end(), n.line.begin() + height());return n;}

  Matrix hstack(Matrix m){
    Matrix n(width() + m.width(), height());
    for (size_t row = 0; row < height(); row ++){
      line.at(row).hstack(m.line.at(row));
      n.line.at(row).insert(0, line.at(row));
      n.line.at(row).insert(width(), m.line.at(row));}
    return n;}

  Matrix transpose(){Matrix t(height(), width());
    for (size_t col = 0; col < width(); col ++){
      for (size_t row = 0; row < height(); row ++){
	t.line.at(col).pixel.at(row) = line.at(row).pixel.at(col);}}
    return t;}
  
  size_t height() const {return line.size();}
  
  size_t width() const {if (height() == 0){return 0;}
    else {return line.at(0).width();}}

  Matrix part(size_t col, size_t row, size_t cols, size_t rows){
    size_t real_rows = min(rows, height() - row);
    size_t real_cols = min(cols, width() - col);
    Matrix m(real_cols, real_rows);
    for (size_t r = 0; r < real_rows; r++){m.line.at(r) = line.at(r + row).part(col, real_cols);} return m;}

  wstring at(size_t row, bool colorless){return line.at(row).get_string(colorless);}

  Pixel get_pixel(size_t col, size_t row){return line.at(row).pixel.at(col);}

  wstring get_string(bool colorless = false){
    wstring out = L"";
    size_t last_row = height() - 1;
    for (size_t row = 0; row < height(); row++){
      out.append(at(row, colorless));
      if(row < last_row){out += new_line;}}
    return out;}

  void show(){wcout << get_string() << endl;}

  Matrix& operator=(const Matrix& m) {line = m.line; return *this;}};
