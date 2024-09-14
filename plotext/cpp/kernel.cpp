using namespace std;

#include "header.h"
#include <chrono>



int main() {
String a(10, Pixel("red", "white"));
Colorize c(L"ciao", Pixel("red"));

a.insert_colorize_dynamically(5, c);
a.show();

return 1;}


extern "C" {

Pixel * pixel_new() {return new Pixel();}
void pixel_delete(Pixel * p) {delete p;}
void pixel_set_fullground_integer(Pixel * p, size_t r) {p->set_fullground(r);}
void pixel_set_fullground_rgb(Pixel * p, size_t r, size_t g, size_t b) {p->set_fullground(r, g, b);}
void pixel_set_fullground_code(Pixel * p, const char * code) {p->set_fullground(code);}
void pixel_set_background_integer(Pixel * p, size_t r) {p->set_background(r);}
void pixel_set_background_rgb(Pixel * p, size_t r, size_t g, size_t b) {p->set_background(r, g, b);}
void pixel_set_background_code(Pixel * p, const char * code) {p->set_background(code);}
void pixel_set_style_code(Pixel * p, const char * code) {p->set_style(code);}
void pixel_log(Pixel * p) {p->log();}
Pixel * pixel_copy(Pixel * c) {return new Pixel(*c);}

Canvas * canvas_new(size_t width, size_t height, Pixel * p) {return new Canvas(width, height, *p);}
void canvas_delete(Canvas * p) {delete p;}
void canvas_show(Canvas * canvas) {canvas->show();}
void canvas_set_xlim(Canvas * canvas, float left, float right) {canvas->set_xlim(left, right);}
void canvas_set_ylim(Canvas * canvas, float left, float right) {canvas->set_ylim(left, right);}
void canvas_set_fillx_level(Canvas * canvas, float level) {canvas->set_fillx_level(level);}
void canvas_set_filly_level(Canvas * canvas, float level) {canvas->set_filly_level(level);}
void canvas_draw(Canvas * canvas, Points * points) {canvas->draw(*points);}

Matrix * matrix_new(size_t width, size_t height, Pixel * p) {return new Matrix(width, height, *p);}
void matrix_delete(Matrix * p) {delete p;}
size_t matrix_get_width(Matrix * matrix) {return matrix->get_width();}
size_t matrix_get_height(Matrix * matrix) {return matrix->get_height();}
Matrix * matrix_vstack(Matrix * m1, Matrix * m2, bool adapt = 0) {return new Matrix(m1->vstack(*m2, adapt));}
Matrix * matrix_hstack(Matrix * m1, Matrix * m2, bool adapt = 0) {return new Matrix(m1->hstack(*m2, adapt));}
const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) {return wstring_to_cstring(m->get_wstring(colorless));}
void wstring_delete(wchar_t * wstr) {delete_cstring(wstr);}
Matrix * matrix_part(Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) {return new Matrix(m->part(col_start, col_stop, row_start, row_stop));}
bool matrix_is_empty(Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) {return m->is_empty(col_start, col_stop, row_start, row_stop);}

void matrix_show(Matrix * matrix, bool colorless) {matrix->show(colorless);}
Matrix * matrix_copy(Matrix * m) {return new Matrix(*m);}
bool matrix_insert(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va, bool adapt) {return m->insert(col, row, *mi, ha, va, adapt);}
bool matrix_insert_colorize(Matrix * m, size_t col, size_t row, Colorize * c, int ha, bool check_space) {return m->insert_colorize(col, row, *c, ha, check_space);}
bool matrix_insert_colorize_dynamically(Matrix * m, size_t col, size_t row, Colorize * c) {return m->insert_colorize_dynamically(col, row, *c);}



Colorize * colorize_new(const wchar_t * string, Pixel * p) {return new Colorize(string, *p);}
size_t colorize_get_length(Colorize * c) {return c->get_length();}
Colorize * colorize_part(Colorize * m, size_t start, size_t stop) {return new Colorize(m->part(start, stop));}
const wchar_t * colorize_get_wstring(Colorize * c, bool colorless) {return wstring_to_cstring(c->get_wstring(colorless));}
Matrix * colorize_get_matrix(Colorize * c) {return new Matrix(colorize_to_matrix(*c));}
Pixel * colorize_get_pixel(Colorize * c) {return new Pixel(c->get_pixel());}
void colorize_set_pixel(Colorize * c, Pixel * p) {c->copy_pixel(*p);}
void colorize_show(Colorize * c, bool colorless) {c->show(colorless);}
Colorize * colorize_copy(Colorize * c) {return new Colorize(*c);}
void colorize_copy_from(Colorize * c, Colorize * c2) {*c = *c2;}
bool colorize_equals(Colorize * c, Colorize * c2) {return *c == *c2;}

Points * points_new(size_t size) {return new Points(size);}
void points_delete(Points * p) {delete p;}
void points_add_normal(Points * points, float x, float y, wchar_t c, Pixel * p, bool ln = 0, bool fx = 0, bool fy = 0) {points->add(x, y, Marker(c, *p), {ln, fx, fy});}
void points_add_hd(Points * points, float x, float y, marker_type c, Pixel * p, bool ln = 0, bool fx = 0, bool fy = 0) {points->add(x, y, Marker(c, *p), {ln, fx, fy});}
void points_log(Points * p, bool full = 0) {p->log(full);}
}

// Fullground * fullground_new() {return new Fullground();}
// void fullground_set_rgb(Fullground * fg, size_t r, size_t b, size_t g) {fg->set(r, g, b);}
// void fullground_set_code(Fullground * fg, const char * code) {wcout << string_to_wstring(code) << endl; fg->set(code);}

// Background * background_new() {return new Background();}
// void background_set_rgb(Background * fg, size_t r, size_t b, size_t g) {fg->set(r, g, b);}
// void background_set_code(Background * fg, const char * code) {fg->set(code);}

// Style * style_new() {return new Style();}
// void style_set_code(Style * fg, const char * code) {cout << code << endl; fg->set(code);}

// enable_special_characters();



// c.log(); nl();nl();

// c.get_matrix().show();

// String s(10, white_pixel); s.show();
// s.resize(5); s.fill_pixel(white_pixel); s.show(); 

// Matrix m1(10, 10, white_pixel); m1.show(); nl();

// Matrix m2(10, 15,Pixel("", "blue")); m2.show(); nl();

// m1.hstack(m2, 1).show();


// // m1.hstack(m2);
// // m1.show();

// // // Points Creation
// // size_t l = 1000;
// // Points P(l); 
// // auto x = range((float) 0., (float) l);
// // auto y = sin(1, l, -1, 0, 0);

// // vector<Pixel> Px; for (size_t i = 0; i < l; i++) {Px.emplace_back(Fullground(((float) i / l) * 250), Background("white"));}//
// // for (size_t i = 0; i < l; i++) {P.add(x.at(i), y.at(i), Marker(braille, Px.at(i)), {1, 1, 0});}
// // //P.log()

// // Points P2(l); 
// // auto y2 = sin(2, l, -0.5, 0, 0);
// // for (size_t i = 0; i < l; i++) {P2.add(x.at(i), y2.at(i), Marker('x', Pixel("blue", "white")), {0, 0, 0});}
// // //P2.log(1);

// // // Canvas Creation
// Canvas c(200, 60, Pixel("", "white"));
// // //Canvas c(247, 59, Pixel("", "white"));
// // c.set_fillx_level(0);
// // c.set_filly_level(l / 2);
// // c.set_xlim({0, l - 1});
// // c.set_ylim({-1, 1});

// // c.draw(P);
// // //c.draw(P2);

// // c.show();

// auto start = chrono::high_resolution_clock::now();
// size_t L = 0;
// for(size_t i = 0; i < L; i++) {
// 	c.get_matrix();
// 	//c.draw(P);
// 	//c.show();
// }
// auto end = chrono::high_resolution_clock::now();
// chrono::duration<double> duration = end - start;
// wcout << L"Elapsed time: " << pow(10, 6)  * duration.count() / L << L" us" << endl;
