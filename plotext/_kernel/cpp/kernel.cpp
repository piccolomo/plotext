// Kernel sandbox: stem plot via FilledPoints. Each FilledPoint is a sine-curve sample whose fill partner sits on the baseline — drawing it produces a vertical line of dots from the curve down to the baseline.

using namespace std;

#include "00_header.h"
#include <cmath>

int main() {
    setlocale(LC_ALL, "");

    const size_t W = 60, H = 14;
    Pixel bg("white", "black");
    Matrix m(W, H, MatrixCharacter(L' ', bg));

    BrailleMarker bm(Pixel("cyan",   "black"));
    BrailleMarker fm(Pixel("yellow", "black"));      // fill marker
    const float baseline = (H - 1) * 0.5f;            // mid-height

    const size_t N = 180;
    FilledPoints fps(N);
    for (size_t i = 0; i < N; ++i) {
        const float x       = static_cast<float>(W - 1) * i / (N - 1);
        const float y_main  = baseline * (1.0f - 0.9f * std::sin(2.0f * 3.1415926f * i / (N - 1)));
        const Point fill_pt(x, baseline, &fm);
        fps.append(FilledPoint(x, y_main, &bm, fill_pt));
    }

    fps.log();

    m.insert(fps);

    Text title(W / 2.0f, 0.0f, Colorize(L"stem plot", Pixel("magenta", "black")), Orientation(0), Alignment(0));
    m.insert(title);

    m.log();
    return 0;
}
