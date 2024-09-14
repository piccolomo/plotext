using namespace std;


class Alignment {
private:
    bool left = 0;
    bool center = 0;
    bool right = 0;

public:
    inline Alignment(const int & i) noexcept {clear(); if (i == 0) {center = 1;} else if (i == 1) {right = 1;} else {left = 1;}}
    inline void clear() noexcept {left = center = right = 0;}
    inline int get_displacement(const size_t & width) const noexcept {if (left) {return 0;} else if (center) {return - (width - 1) / 2;} else {return 1 - width;}}
};

inline vector<int> get_dynamic_displacements(const size_t & width) noexcept {
    Alignment right(1), center(0);
    vector<int> unsorted = range(right.get_displacement(width), 1);
    return sort(unsorted, center.get_displacement(width));}