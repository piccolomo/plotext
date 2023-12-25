#include <iostream>
#include <vector>

#ifdef _WIN32
    #include <Windows.h>
#endif


using namespace std;

wstring ansi_start = L"\x1b[";
wstring ansi_end = ansi_start + L"0m";
wstring ansi_full = ansi_start + L"38;";
wstring ansi_back = ansi_start + L"48;";
wstring new_line = L"\n";

enum ColorLevel {fullground, background};
enum ColorType {none, integer, rgb};


class Color{
public:
  ColorLevel level = fullground;
  ColorType type = none;
  unsigned char r = 0;
  unsigned char g = 0;
  unsigned char b = 0;
  
  Color(){};
  
  Color(ColorLevel l, ColorType t = none, size_t rs = 0, size_t gs = 0, size_t bs = 0){set_level(l); set_type(t); set_rgb(r, g, b);}
  
  Color(const Color & c): level(c.level), type(c.type), r(c.r), g(c.g), b(c.g) {}

  void set_level(ColorLevel l){level = l;}
  
  void set_type(ColorType t){type = t;}
  
  void set_rgb(size_t rs = 0, size_t gs = 0, size_t bs = 0){r = rs; g = gs; b = bs;}

  void clear(){type = none; r = g = b = 0;}
  
  wstring get_ansi(){
    if (type == none){return L"";}
    else if (type == integer){return get_ansi_level() + get_integer_code();}
    else {return get_ansi_level() + get_rgb_code();}}

  wstring get_ansi_level(){if (level == fullground){return ansi_full;} else {return ansi_back;}}
  
  wstring get_integer_code(){return L"5;" + to_wstring(r) + L"m";}
  
  wstring get_rgb_code(){return L"2;" + to_wstring(r) + L";" + to_wstring(g) + L";" + to_wstring(b) + L"m";}

  
  void log(){wcout << get_level() << L", " << get_type() << L", " << get_rgb() << endl;}

  wstring get_level(){if (level == fullground){return L"level: fullground";} else {return L"level: background";}}
  
  wstring get_type(){if (type == none){return L"type: none";} else if (type == integer) {return L"type: integer";} else {return L"type: rgb";}}
  
  wstring get_rgb(){return L"rgb(" + to_wstring(r) + L", " + to_wstring(g) + L", "+ to_wstring(b) + L")";}
  
  bool operator==(const Color& c) const {
    return level == c.level and type == c.type and ((type == none) or (type == integer and r == c.r) or (type == rgb and r == c.r and g == c.g and b == c.b));}
};



wstring style_code[8] =  {L"1", L"2", L"3", L"4", L"21", L"9", L"7", L"5"};
//"bold": 1, "dim": 2, "italic": 3, "underline": 4, "double-underline": 21, "strike": 9, "inverted": 7, "flash": 5

class Style{
public:
  bool code [8];

  Style(){clear();}
  
  Style(const Style & s) {for (size_t i = 0; i < 8; ++i) {code[i] = s.code[i];}}

  void set(size_t i, bool b = true){code[i] = b;}

  void clear(){for(bool & c: code){c = false;}}
  
  wstring get_ansi(){
    if (no_style()){return L"";}
    else {
      wstring out = L"";
      out += ansi_start;
      for(size_t i = 0; i < 8; i++){if(code[i]){out += style_code[i] + L";";}}
      out.pop_back(); return out + L"m";}}
  
  void log(){
    if (no_style()){wcout << L"no style" << endl;}
    else {wcout << L"style (";
      for (size_t i = 0; i < 8; i ++){wcout << code[i]; if(i != 7){wcout << L", ";}}
      wcout << L")" << endl;}}

  bool no_style(){bool res = true;
    for (size_t i = 0; i < 8; i ++){res = res and (not code[i]);} return res;}

  bool operator==(const Style& st) const {return equal(code, end(code), st.code);}
};



class Pixel{
public:
  wchar_t m = L' ';
  Color fg;
  Color bg;
  Style st;

  Pixel() {set_color_levels();}
  
  Pixel(wchar_t M, const Color & Fg = Color(), const Color & Bg = Color(), const Style & St = Style()) : m(M), fg(Fg), bg(Bg){}
  
  Pixel(const Pixel & p) : m(p.m), fg(p.fg), bg(p.bg), st(p.st) {}

  Pixel(Pixel && p) : m(p.m), fg(p.fg), bg(p.bg), st(p.st) {}

  void set_color_levels(){fg.set_level(fullground); bg.set_level(background);}
  
  void set_marker(wchar_t ms){m = ms;}
  
  void set_fullground(ColorType t, size_t r = 0, size_t g = 0, size_t b = 0){fg.set_type(t); fg.set_rgb(r, g, b);}
  
  void set_background(ColorType t, size_t r = 0, size_t g = 0, size_t b = 0){bg.set_type(t); bg.set_rgb(r, g, b);}
  
  void set_style(size_t i, bool b = true){st.set(i, b);}

  void clear(){m = L' '; fg.clear(); bg.clear(); st.clear(); };
  
  bool check(){return m == L' ';}

  wstring get_ansi(){return fg.get_ansi() +  bg.get_ansi() + st.get_ansi();}

  wstring get_string(size_t type = 1){
    if (type == 1){return get_ansi() + m + ansi_end;}
    else {return ansi_end + get_ansi() + m;}}

  void show(){wcout << get_string(1) << endl;}
    
  void log(){wcout << "marker: " << get_string() << endl; fg.log(); bg.log(); st.log();}
  
  bool operator==(const Pixel& p) const {return ((fg == p.fg) and (bg == p.bg) and (st == p.st));}
  bool operator!=(const Pixel& p) const {return not (*this == p);}
  Pixel& operator=(const Pixel& p) {m = p.m; fg = p.fg; bg = p.bg; st = p.st; return *this;}
};


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

  void insert_pixel(size_t col, size_t row, Pixel p = Pixel()){line.at(row).insert(col, wstring(1,p.m), p);}

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

  wstring get_string(bool colorless = false){
    wstring out = L"";
    size_t last_row = height() - 1;
    for (size_t row = 0; row < height(); row++){
      out.append(at(row, colorless));
      if(row < last_row){out += new_line;}}
    return out;}

  void show(){wcout << get_string() << endl;}

  Matrix& operator=(const Matrix& m) {line = m.line; return *this;}};



class Marker{
public:
  wchar_t marker;
  vector<bool> code;

  Marker() {marker = L'X'; code = {0};};
  
  Marker(vector<bool> c, wchar_t m) : marker(m), code(c) {}

  void log(){
    size_t l = code.size();
    cout << "(";
    for (size_t i = 0; i < l; i ++) {cout << code[i]; if (i != l - 1){cout << ", ";};}
    cout << "): "; wcout << marker << endl;}

  bool operator==(Marker M) const {return marker == M.marker;}
  bool operator==(wchar_t m) const {return marker == m;}
  bool operator==(vector<bool> c) const {return code == c;}
};



vector<bool> sum_vectors(vector<bool> v1, vector<bool> v2){
  vector<bool> v;
  for (size_t i = 0; i < v1.size(); i++) {v.push_back(v1[i] or v2[i]);}
  return v;}


class Markers{
public:
  vector<Marker> markers;

  ~Markers() {markers.clear();}

  void add(vector<bool> c, wchar_t m){
    markers.push_back(Marker(c, m));}

  Marker get(wchar_t m){
    Marker M;
    for(Marker marker : markers){if(marker == m){M = marker;}}
    return M;}

  Marker get(vector<bool> c){
    Marker M;
    for(Marker marker : markers){if(marker == c){M = marker;}}
    return M;}

  vector<bool> get_vector(wchar_t m){return get(m).code;}

  wchar_t get_marker(vector<bool> c){return get(c).marker;}

  wchar_t sum(wchar_t m1, wchar_t m2) {return get_marker(sum_vectors(get_vector(m1), get_vector(m2)));}

  bool in(wchar_t m){bool res = false; Marker M = get(m); if(not (M == Marker())){res = true;} return res;}

  void log(){cout << "size: " << markers.size() << endl;
    for(Marker marker : markers) {marker.log();}}};



extern "C" {
  Pixel * pixel_create(){return new Pixel();}
  void pixel_destroy(Pixel * p){delete p;}
  
  void pixel_set_marker(Pixel * p, wchar_t m){p->set_marker(m);}

  void pixel_set_fullground(Pixel * p, size_t type, size_t r, size_t g, size_t b){
    if(type == 0){p->set_fullground(none);}
    else if (type == 1) {p->set_fullground(integer, r);}
    else {p->set_fullground(rgb, r, g, b);}}

  void pixel_set_background(Pixel * p, size_t type, size_t r, size_t g, size_t b){
    if(type == 0){p->set_background(none);}
    else if (type == 1) {p->set_background(integer, r);}
    else {p->set_background(rgb, r, g, b);}}
  
  void pixel_set_style(Pixel * p, size_t i){p->set_style(i, true);}
  
  void pixel_log(Pixel * p){p->log();}

  const wchar_t * pixel_get_string(Pixel * p){
    wstring s = p->get_string();
    return wcsdup(s.c_str());}
  
  Matrix * matrix_create(size_t width, size_t height, Pixel * p){return new Matrix(width, height, *p);}
  void matrix_destroy(Matrix * m){delete m;}

  void matrix_insert_pixel(Matrix * m, size_t col, size_t row, Pixel * p){m->insert_pixel(col, row, *p);}
  
  void matrix_insert_string(Matrix * m, size_t col, size_t row, wchar_t * s, Pixel * p){
    wstring ws(s);
    m->insert_string(col, row, ws, *p);}

  void matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * n){
    m->insert_matrix(col, row, *n);}
  
  bool matrix_insert_aligned(Matrix * m, size_t col, size_t row, Matrix * n, int ha = -1, int va = -1, bool check_spaces = false){
    return m->insert_aligned(col, row, *n, ha, va, check_spaces);}
  
  bool matrix_insert_dynamic(Matrix * m, size_t col, size_t row, Matrix * nm){return m->insert_dynamic(col, row, (*nm).line.at(0));}

  void matrix_fill(Matrix * m, Pixel * p) {m->fill(*p);}

  void matrix_clear(Matrix * m){m -> clear();}
  
  void matrix_resize(Matrix * m, size_t width, size_t height, Pixel * p){m -> resize(width, height, *p);}

  Matrix * matrix_hstack(Matrix * m, Matrix * n){return new Matrix(m->hstack(*n));}
  
  Matrix * matrix_vstack(Matrix * m, Matrix * n){return new Matrix(m->vstack(*n));}

  Matrix * matrix_transpose(Matrix * m){Matrix * nm = new Matrix(m->transpose()); return nm;}

  size_t matrix_height(Matrix * m){return m->height();}
  
  size_t matrix_width(Matrix * m){return m->width();}
  
  Matrix * matrix_part(Matrix * m, size_t col, size_t row, size_t cols, size_t rows) {return new Matrix(m->part(col, row, cols, rows)); }
  
  wchar_t * matrix_get_string(Matrix * m, bool colorless){
    wstring s = m->get_string(colorless);
    return wcsdup(s.c_str());}
  
  void string_free_memory(wchar_t * s){free(s);}
  
  void matrix_show(Matrix * m){m->show();}
  
  Matrix * matrix_copy(Matrix * m){Matrix * nm = new Matrix(*m); return nm;}

  Matrix * matrix_assign(Matrix * m1, Matrix * m2){*m1 = *m2; return m1;}

  Markers * markers_create(){return new Markers();}
  void markers_destroy(Markers * M){delete M;}
  
  void markers_add(Markers * M, bool * c, size_t c_size, wchar_t m){
    vector<bool> code(c, c + c_size);
    M->add(code, m);}
  
  wchar_t markers_sum(Markers * M, wchar_t m1, wchar_t m2){
    return M->sum(m1, m2);}
  
  bool markers_in(Markers * M, wchar_t m){return M->in(m);}

  void markers_log(Markers * M){M->log();}
};



int main(){
  Pixel p;
  p.set_marker(L' ');
  p.set_fullground(integer, 3);
  p.set_background(rgb, 110,134,156);
  p.set_style(1);

  Pixel p2;
  p2.set_marker(L'2');
  p2.set_fullground(integer, 5);
  p2.set_background(integer, 50);

  Matrix m1(100, 30, p);
  Matrix m2(100, 30, p2);
  //m1.insert_aligned(3, 0, m2, 0, -1, false);
  matrix_assign(&m1, &m2);
  //m1.show();

  String s(L"ciao", p);
  s.show();
  //Matrix(0, 0);

  return 0;
}

// #include <chrono>

  // int reps = 1 * pow(10, 3);
  // auto start = high_resolution_clock::now();
  // for (int i = 0; i < reps; ++i) {
  //   s.show();
  //   //print_wstring(s.get_string());
  // }
  // auto stop = high_resolution_clock::now();
  // auto duration = duration_cast<nanoseconds>(stop - start);
  // float time = duration.count() / reps;
  // wcout << "Elapsed time: " << time / pow(10, 6)  << " ms " << endl;



  // bool check(size_t col_start, size_t col_end, size_t row_start, size_t row_end){
  //   row_start = max(0, (int)row_start - 1);
  //   row_end = min(row_end + 1, height() - 1);
  //   bool res = true;
  //   for (size_t row = row_start; row < row_end; row++){res = res and line.at(row).check(col_start, col_end);}
  //   return res;}

// void print2(const std::wstring str) {
//    for (const wchar_t & ch : str) {
//         putwchar(ch);}
//     putwchar(L'\n'); // Add a newline after printing the string
// }




