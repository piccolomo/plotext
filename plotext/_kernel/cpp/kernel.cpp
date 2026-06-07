// FilledPoints with two 3×3 MatrixMarker entries (one green, one red) on a 100×30 white canvas. Stamp them, then draw a line between the two FilledPoints' anchors and stamp that too.

using namespace std;

#include "00_header.h"

int main() {
    setlocale(LC_ALL, "");

    // 3×3 MatrixMarker blocks, one green, one red.
    Matrix green_data(3, 3, MatrixCharacter(L'█', Pixel("green", "white")));
    Matrix red_data  (3, 3, MatrixCharacter(L'█', Pixel("red",   "white")));
    MatrixMarker green_mm(green_data, Alignment(0), Alignment(0));
    MatrixMarker red_mm  (red_data,   Alignment(0), Alignment(0));

    // Two FilledPoints at distinct anchors. fill defaults to (x, y) with no marker → no stem.
    FilledPoints fps(2);
    fps.append(FilledPoint(15.0f,  5.0f, &green_mm));
    fps.append(FilledPoint(80.0f, 22.0f, &red_mm));

    // Big white canvas.
    Pixel  white("white", "white");
    Matrix canvas(100, 30, MatrixCharacter(L' ', white));

    // 1) Stamp the FilledPoints (each renders just its main since no fill stem).
    canvas.insert(fps);

    // 2) Draw a line between FP[0]'s and FP[1]'s anchor positions. Intermediate points inherit FP[0]'s marker (green); the last point IS FP[1] (red).
    Vector<Point> line = fps.at(0).get_simple_line(fps.at(1), true);
    wcout << L"Line between FP[0] (15,5) and FP[1] (80,22): " << line.get_length() << L" points" << endl;
    for (size_t i = 0; i < line.get_length(); ++i) canvas.insert(line.at(i));

    canvas.stream(true, true);
    return 0;
}
