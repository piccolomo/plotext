using namespace std;

#include "header.h"

int main() {
   enable_special_characters();

   auto c = Colorize(L"ciao"); c.print(); nl(); nl();
   auto m = Matrix(10, 20, Pixel("red", "white")); m.print(); nl(); nl();

   m.insert_colorized_aligned(0,0, c);

   m.print(); nl();

return 1;}