using namespace std;

#include "header.h"


int main() {
enable_special_characters();

// Points Creation
size_t l = 500;
Points P(l); 
auto x = range((float) 0., (float) l);
auto y = sin(1, l, 1, 0, 0);
vector<Pixel> Px; for (size_t i = 0; i < l; i++) {Px.emplace_back(Fullground(((float) i / l) * 250), Background("white"));}//
for (size_t i = 0; i < l; i++) {P.add(x.at(i), -y.at(i), Marker(braille, Px.at(i)), {0, 1, 1});}

// Canvas Creation
Canvas c(100, 30, Pixel("", "white"));
c.set_fillx_level(0);
c.set_filly_level(l / 2);
c.set_xlim({0, l - 1});
c.set_ylim({-1, 1});

c.draw(P);
c.show();

return 1;}

/*auto start = chrono::high_resolution_clock::now();
size_t L = 0;
for(size_t i = 0; i < L; i++) {
	c.draw(P);
}
auto end = chrono::high_resolution_clock::now();
chrono::duration<double> duration = end - start;
wcout << L"Elapsed time: " << pow(10, 6)  * duration.count() / L << L" us" << endl;*/