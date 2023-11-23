#include <iostream>
#include <vector>

#ifdef _WIN32
    #include <Windows.h>
#endif


using namespace std;

enum ColorLevel {fullground, background};
enum ColorType {none, integer, rgb};

wstring ansi_start = L"\x1b[";
wstring ansi_end = ansi_start + L"0m";
wstring ansi_full = ansi_start + L"38;";
wstring ansi_back = ansi_start + L"48;";
//"bold": 1, "dim": 2, "italic": 3, "underline": 4, "double-underline": 21, "strike": 9, "inverted": 7, "flash": 5


class Color{
public:
  ColorLevel level = fullground;
  ColorType type = none;
  unsigned char r = 0;
  unsigned char g = 0;
  unsigned char b = 0;
  
  Color(){};
  Color(ColorLevel l, ColorType t = none, int rs = 0, int gs = 0, int bs = 0){set_level(l); set_type(t); set_rgb(r, g, b);}
  Color(const Color & c): level(c.level), type(c.type), r(c.r), g(c.g), b(c.g) {}
  //~Color() {}

  void set_level(ColorLevel l){level = l;}
  void set_type(ColorType t){type = t;}
  void set_rgb(int rs = 0, int gs = 0, int bs = 0){r = rs; g = gs; b = bs;}
  //void set(const Color & c){level = c.level; type = c.type; r = c.r; g = c.g; b = c.b;}
  void reset(){level = fullground; type = none; r = 0; g = 0; b = 0;}

  wstring get_ansi(){
    if (type == none){return L"";}
    else if (type == integer){return get_ansi_level() + get_integer_code();}
    else {return get_ansi_level() + get_rgb_code();}}

  wstring get_ansi_level(){if (level == fullground){return ansi_full;} else {return ansi_back;}}
  wstring get_integer_code(){return L"5;" + to_wstring(r) + L"m";}
  wstring get_rgb_code(){return L"2;" + to_wstring(r) + L";" + to_wstring(g) + L";" + to_wstring(b) + L"m";}

  wstring get_type(){if (type == none){return L"type: none";} else if (type == integer) {return L"type: integer";} else {return L"type: rgb";}}
  wstring get_level(){if (level == fullground){return L"level: fullground";} else {return L"level: background";}}
  wstring get_rgb(){return L"rgb(" + to_wstring(r) + L", " + to_wstring(g) + L", "+ to_wstring(b) + L")";}
  
  void show_ansi(){wcout << get_ansi();}

  void log(){wcout << get_level() << L", " << get_type() << L", " << get_rgb() << endl;}


  bool operator==(const Color& c) const {
    return level == c.level and type == c.type and ((type == none) or (type == integer and r == c.r) or (type == rgb and r == c.r and g == c.g and b == c.b));}

  void clear(){type = none; r = g = b = 0;}
};

  

wstring style_code[8] =  {L"1", L"2", L"3", L"4", L"21", L"9", L"7", L"5"};
  
class Style{
public:
  bool code[8] = {false, false, false, false, false, false, false, false};

  Style(){}
  Style(const Style & s) {for (int i = 0; i < 8; ++i) {code[i] = s.code[i];}}

  void set(int i, bool b = true){code[i] = b;}
  
  wstring get_ansi(){
    if (no_style()){return L"";}
    else {
      wstring out = L"";
      out += ansi_start;
      for(int i = 0; i < 8; i++){if(code[i]){out += style_code[i] + L";";}}
      out.pop_back(); return out + L"m";}}

  bool no_style(){bool res = true;
    for (int i = 0; i < 8; i ++){res = res and (not code[i]);} return res;}

  void show_ansi(){wcout << get_ansi();}

  void log(){
    if (no_style()){wcout << L"no style" << endl;}
    else {wcout << L"style(";
      for (int i = 0; i < 8; i ++){cout << code[i]; if(i != 7){wcout << L", ";}}
      wcout << L")" << endl;}}

  bool operator==(const Style& st) const {return equal(code, end(code), st.code);}
  
  void clear(){for (int i = 0; i < 8; ++i){set(i, false);}}

};



class Pixel{
public:
  wchar_t m = ' ';
  Color fg;
  Color bg;
  Style st;
  bool novel = false; 

  Pixel() {set_levels();}
  Pixel(wchar_t M, const Color & Fg = Color(), const Color & Bg = Color(), const Style & St = Style()) : m(M), fg(Fg), bg(Bg), st(St){}
  Pixel(const Pixel & p) : m(p.m), fg(p.fg), bg(p.bg), st(p.st) {}

  void set_marker(wchar_t ms){m = ms;}
  void set_fullground(ColorType t, int r = 0, int g = 0, int b = 0){fg.set_type(t); fg.set_rgb(r, g, b);}
  void set_background(ColorType t, int r = 0, int g = 0, int b = 0){bg.set_type(t); bg.set_rgb(r, g, b);}
  void set_levels(){fg.set_level(fullground); bg.set_level(background);}
  void set_style(int i, bool b = true){st.set(i, b);}
  void set_novel(bool n){novel = n;}

  wstring get_ansi(){return ansi_end + fg.get_ansi() + bg.get_ansi() + st.get_ansi();}
  wchar_t get_marker(){return m;}
  wstring get_colored_marker(){return get_ansi() + get_marker() + ansi_end;}
  
  void show(){wcout << get_colored_marker() << endl;}
  void log(){log_marker(); fg.log(); bg.log(); st.log(); log_novel(); }
  
  void log_marker(){wcout << "marker: " << m << endl;}
  void log_novel(){wcout << "novel " << novel << endl;}
  
  bool operator==(const Pixel& p) const {return ((fg == p.fg) and (bg == p.bg) and (st == p.st));}
  bool operator!=(const Pixel& p) const {return not (*this == p);}

  void clear(){m = L' '; fg.clear(); bg.clear(); st.clear();};

  bool check(){return get_marker() == L' ';}

};



class String{
public:
  vector<Pixel> pixel;

  String(int l = 0) {pixel.resize(l); init_novel();}
  String(wstring s, const Pixel & p = Pixel()) : String(s.length()) {insert(0, s, p);}
  String(const String & s) : pixel(s.pixel) {}
  ~String() {pixel.clear();}

  void fill(const Pixel & p = Pixel()){for(int i = 0; i < length(); i++){pixel.at(i) = p;} init_novel();}
  
  void insert(int i, wstring s, const Pixel & p = Pixel()){
    int sl = s.length();
    for(int j = 0; j < sl; j++){
      Pixel pn(p);
      pn.set_marker(s[j]);
      pixel.at(i + j) = pn;}
    set_novels(i, sl);}
  
  void insert(int i, const String & s){
    int sl = s.length();
    for(int j = 0; j < sl; j++){pixel.at(i + j) = s.pixel.at(j);}
    set_novels(i, sl);}

  void set_novel(int i){
    if (length() > 0 and i == 0){pixel[i].set_novel(true);}
    else if (i < length()) {pixel[i].set_novel(get(i) != get(i - 1));}}
  void set_novels(int i, int l){set_novel(i); if(l > 0){set_novel(i + l - 0);};}
  void init_novel(){set_novels(0, length());}

  bool check(int i, int length){bool res = true;
    for (int l = 0; l < length; l++){res = res and pixel.at(i + l).check();}
    return res;}
  
  int length() const {return pixel.size();}
  Pixel & get(int i){return pixel[i];}

  bool get_novel(int i){return get(i).novel;}
  wchar_t get_marker(int i){return get(i).get_marker();};
  wstring get_ansi(int i){return get(i).get_ansi();}

  wstring get_string(bool colorless = false){
    wstring out = L"";
    for (int i = 0; i < length(); i++){
      if (not colorless and get_novel(i)){out += get_ansi(i);}
      out += get_marker(i);}
    if(not colorless and length() > 0){out += ansi_end;}
  return out;}

  void show(){wcout << get_string(); if(length() > 0){wcout << "\n";}}

  void clear(){for (int i = 0; i < length(); i++){pixel.at(i).clear();}}
};



class Matrix{
public:
  vector<String> line; 

  // Matrix() {}
  
  Matrix(int cols, int rows, const Pixel & p = Pixel()) {for (int i = 0; i < rows; i++){line.push_back(String(cols));} fill(p);}

  Matrix(const Matrix & m) : line(m.line) {}
  ~Matrix(){line.clear();}

  void fill(const Pixel & p = Pixel()){for (int row = 0; row < rows(); row++){line.at(row).fill(p);}}
  
  void insert_h(int col, int row, wstring s, const Pixel & p = Pixel()){
    line.at(row).insert(col, s, p);}

  void insert_v(int col, int row, wstring s, const Pixel & p = Pixel()){
    for (int r = 0; r < s.length(); r++){insert_h(col, row + r, s.substr(r, 1), p);}}

  void insert_m(int col, int row, const Matrix & m){
    for (int r = 0; r < m.rows(); r++){line.at(row + r).insert(col, m.line[r]);}}

  bool insert_d(int col, int row, wstring s, const Pixel & p = Pixel()){
    int length = s.length();
    int left = length / 2; int right = length - left;
    int span = max(left, right);
    int directions [] = {-1, 1};
    for (int delta = 0; delta < span; delta++){
      for (int direction: directions){
	int col_new = col + direction * delta;
        int col_real = col_new - left;
	if (col_real < col - length or col_real > col){continue;}
	bool all_spaces = line.at(row).check(col_real - 1, length + 2);
	if (all_spaces){insert_h(col_real, row, s, p); return true;}
	else{continue;}}}
    return false;}

  bool check(int col, int row, int cols, int rows){bool res = true;
    for (int r = 0; r < rows; r++){res = res and line.at(row + r).check(col, cols);}
    return res;}


  wstring get_string(bool colorless = false){
    wstring out = L"";
    for (int row = 0; row < rows(); row++){
      out += line.at(row).get_string(colorless);
      if(row < rows() - 1){out += L"\n";}}
    return out;}

  int rows() const {return line.size();}
  int cols() const {
    if (rows() == 0){return 0;}
    else {return line.at(0).length();}}
  
  void show(){wcout << get_string(); if(rows() > 0){wcout << "\n";}}

  Matrix part(int start, int end){
    int rows = end - start;
    Matrix m(cols(), rows);
    for (int row = 0; row < rows; row++) {m.line.at(row) = line.at(row + start);}
    return m;}

  void clear(){for (int row = 0; row < rows(); row ++){line.at(row).clear();}}
};


class Marker{
public:
  wchar_t marker;
  vector<bool> code;

  Marker() {marker = L'X'; code = {0};};
  Marker(vector<bool> c, wchar_t m) : marker(m), code(c) {}

  void log(){
    int l = code.size();
    cout << "(";
    for (int i = 0; i < l; i ++) {cout << code[i]; if (i != l - 1){cout << ", ";};}
    cout << "): "; wcout << marker << endl;}

  bool operator==(Marker M) const {return marker == M.marker;}
  bool operator==(wchar_t m) const {return marker == m;}
  bool operator==(vector<bool> c) const {return code == c;}
};



vector<bool> sum_vectors(vector<bool> v1, vector<bool> v2){
  vector<bool> v;
  for (int i = 0; i < v1.size(); i++) {v.push_back(v1[i] or v2[i]);}
  return v;}


class Markers{
public:
  vector<Marker> markers;

  //Markers() {markers.resize(0);}
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
    for(Marker marker : markers) {marker.log();}}
};



int main(){
  return 0;
};


extern "C" {
  Pixel * pixel_create(){return new Pixel();}
  
  void pixel_set_marker(Pixel * p, wchar_t m){p->set_marker(m);}

  void pixel_set_fullground(Pixel * p, int type, int r, int g, int b){
    if(type == 0){p->set_fullground(none);}
    else if (type == 1) {p->set_fullground(integer, r);}
    else {p->set_fullground(rgb, r, g, b);}}

  void pixel_set_background(Pixel * p, int type, int r, int g, int b){
    if(type == 0){p->set_background(none);}
    else if (type == 1) {p->set_background(integer, r);}
    else {p->set_background(rgb, r, g, b);}}
  
  void pixel_set_style(Pixel * p, int i){p->set_style(i, true);}
  
  void pixel_log(Pixel * p){p->log();}
  
  void pixel_show(Pixel * p){p->show();}
  
  void pixel_destroy(Pixel * p){delete p;}

  String * string_create(int l){return new String(l);}
  
  void string_destroy(String * s){delete s;}

  Matrix * matrix_create(int cols, int rows, Pixel * p){return new Matrix(cols, rows, *p);}

  void matrix_insert_h(Matrix * m, int col, int row, wchar_t * s, Pixel * p){
    wstring ws(s);
    m->insert_h(col, row, ws, *p);}

  bool matrix_insert_d(Matrix * m, int col, int row, wchar_t * s, Pixel * p){
    wstring ws(s);
    return m->insert_d(col, row, ws, *p);}
  
  void matrix_insert_v(Matrix * m, int col, int row, wchar_t * s, Pixel * p){
    wstring ws(s);
    m->insert_v(col, row, ws, *p);}

  void matrix_insert_m(Matrix * m, int col, int row, Matrix * nm){m->insert_m(col, row, *nm);}

  bool matrix_check(Matrix * m, int col, int row, int cols, int rows){return m->check(col, row, cols, rows);}

  // Matrix * matrix_hstack(Matrix * m1, Matrix * m2){Matrix * m = new Matrix(m1->hstack(*m2)); return m;}

  // Matrix *  matrix_vstack(Matrix * m1, Matrix * m2){Matrix * m = new Matrix(m1->vstack(*m2)); return m;}

  wchar_t * matrix_get_string(Matrix * m, bool colorless){
    wstring s = m->get_string(colorless);
    return wcsdup(s.c_str());}
  
  void string_free_memory(wchar_t * s){free(s);}
  
  void matrix_show(Matrix * m){m->show();}
  void matrix_destroy(Matrix * m){delete m;}
  Matrix * matrix_copy(Matrix * m){Matrix * nm = new Matrix(*m); return nm;}

  int matrix_rows(Matrix * m){return m->rows();}
  int matrix_cols(Matrix * m){return m->cols();}

  Matrix * matrix_part(Matrix * m, int start, int end) {return new Matrix(m->part(start, end)); }

  void matrix_clear(Matrix * m){m -> clear();}

  void matrix_fill(Matrix * m, Pixel * p) {m->fill(*p);}

  
  Markers * markers_create(){return new Markers();}
  
  void markers_add(Markers * M, bool * c, int c_size, wchar_t m){
    vector<bool> code(c, c + c_size);
    M->add(code, m);}
  
  wchar_t markers_sum(Markers * M, wchar_t m1, wchar_t m2){
    return M->sum(m1, m2);}
  
  bool markers_in(Markers * M, wchar_t m){return M->in(m);}

  void markers_log(Markers * M){M->log();}
    
  void markers_destroy(Markers * M){delete M;}

  
};


