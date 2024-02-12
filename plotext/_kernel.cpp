#include <iostream>
#include <vector>

#ifdef _WIN32
    #include <Windows.h>
#endif

#include "_matrix.cpp"
#include "_marker.cpp"

using namespace std;

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
  
  Pixel * pixel_assign(Pixel * m1, Pixel * m2){*m1 = *m2; return m1;}

  
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
  
  Pixel * matrix_get_pixel(Matrix * m, size_t col, size_t row) {return new Pixel(m->get_pixel(col, row));}
  
  wchar_t * matrix_get_string(Matrix * m, bool colorless){
    wstring s = m->get_string(colorless);
    return wcsdup(s.c_str());}
  
  void string_free_memory(wchar_t * s){free(s);}
  
  void matrix_show(Matrix * m){m->show();}
  
  Matrix * matrix_copy(Matrix * m){Matrix * nm = new Matrix(*m); return nm;}

  Matrix * matrix_assign(Matrix * m1, Matrix * m2){*m1 = *m2; return m1;}

  HDmarkers * hd_markers_create(){return new HDmarkers();}
  void hd_markers_destroy(HDmarkers * M){delete M;}
  
  void hd_markers_add(HDmarkers * M, bool * c, size_t c_size, wchar_t m){
    vector<bool> code(c, c + c_size);
    M->append_marker(code, m);}
  
  wchar_t hd_markers_sum(HDmarkers * M, wchar_t m1, wchar_t m2){
    return M->sum(m1, m2);}
  
  bool hd_markers_in(HDmarkers * M, wchar_t m){return M->in(m);}

  void hd_markers_log(HDmarkers * M){M->log();}

};


// int main(){
//   Pixel p;
//   p.set_marker(L' ');
//   p.set_fullground(integer, 3);
//   p.set_background(rgb, 110,134,156);
//   p.set_style(1);

//   Pixel p2;
//   p2.set_marker(L'2');
//   p2.set_fullground(integer, 5);
//   p2.set_background(integer, 50);

//   Matrix m(100, 30, p);
//   m.show();

//   return 0;
// }


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




