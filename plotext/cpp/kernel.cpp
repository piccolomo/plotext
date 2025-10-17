using namespace std;

#include "header.h"

int main() {
   enable_special_characters();

   Style s("bold");
   s.log();
   s.set("italic");
   s.log();
   Pixel f("blue");
   f.set_background("red");
   f.print();

   return 1; }