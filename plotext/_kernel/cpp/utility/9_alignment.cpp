// Alignment utilities: left/center/right anchoring used when placing text inside fixed-width cells

// --- Text Alignment Utilities ---

// Alignment: left (-1), center (0), right (1), or dynamic (2) anchor flags plus displacement helpers. Dynamic means "any alignment is OK, find a free spot", the matrix routes to insert_dynamically.
class Alignment {
private:
    bool left    = 0;
    bool center  = 0;
    bool right   = 0;
    bool dynamic = 0;

public:
    // Constructor: -1 -> left, 0 -> center, 1 -> right, 2 -> dynamic
    Alignment(const int & i = -1) { clear(); if (i == 0) center = 1; else if (i == 1) right = 1; else if (i == 2) dynamic = 1; else left = 1; }

    void clear() { left = center = right = dynamic = 0; }

    // The displacement of a static alignment, undefined when dynamic, so the caller checks is_dynamic() first; the width is cast to int, since the unsigned form underflows on the negations.
    int  get_displacement(const size_t & width) const { if (left) return 0; const int w = static_cast<int>(width); if (center) return -(w - 1) / 2; return 1 - w; }
    bool is_dynamic() const noexcept { return dynamic; }

    // Integer representation: -1 left, 0 center, 1 right, 2 dynamic
    int  get_integer() const noexcept { if (left) return -1; if (center) return 0; if (right) return 1; return 2; }
};

// Every displacement a dynamic alignment may try, in order, the closest to the center first.
inline Vector<int> get_dynamic_displacements(const size_t & width) {
    Alignment right(1), center(0);
    auto unsorted = range(right.get_displacement(width), 1);
    auto sorted = sort(unsorted, center.get_displacement(width));
    auto displacement = center.get_displacement(width);
    transform(sorted.begin(), sorted.end(), sorted.begin(), [displacement](int x){return x - displacement;});
    return sorted;}

// The displacements to try for an alignment, so that every alignment is handled by one loop: the centered search list when dynamic, the single static displacement otherwise.
inline Vector<int> get_displacements(const Alignment & a, size_t length) noexcept {
    if (a.is_dynamic()) {
        Vector<int> deltas = get_dynamic_displacements(length);
        const int c_disp = Alignment(0).get_displacement(length);
        for (size_t i = 0; i < deltas.get_length(); ++i) deltas.at(i) += c_disp;
        return deltas;
    }
    Vector<int> v(1); v.append(a.get_displacement(length));
    return v;
}
