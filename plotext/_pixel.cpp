#include <iostream>
#include <vector>

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
