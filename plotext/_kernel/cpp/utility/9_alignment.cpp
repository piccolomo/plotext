// Alignment utilities: left/center/right anchoring used when placing text inside fixed-width cells

// --- Text Alignment Utilities ---

// Alignment: left (-1), center (0), right (1), or dynamic (2) anchor flags plus displacement helpers. Dynamic means "any alignment is OK, find a free spot" — the matrix routes to insert_dynamically.
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

    // Static-mode displacement (left/center/right). Undefined when dynamic — caller must check is_dynamic() first.
    // Cast to int up-front: with size_t (unsigned) the negations and 1-width underflow, then the cast back to int is implementation-defined and was producing -1 for center at width=2 (bug).
    int  get_displacement(const size_t & width) const { if (left) return 0; const int w = static_cast<int>(width); if (center) return -(w - 1) / 2; return 1 - w; }
    bool is_dynamic() const noexcept { return dynamic; }

    // Integer representation: -1 left, 0 center, 1 right, 2 dynamic
    int  get_integer() const noexcept { if (left) return -1; if (center) return 0; if (right) return 1; return 2; }
};

// Generate a vector of dynamic displacements based on width
inline Vector<int> get_dynamic_displacements(const size_t & width) {
    Alignment right(1), center(0);                        // Right and center alignment objects
    auto unsorted = range(right.get_displacement(width), 1); // Unsorted range of displacements
    auto sorted = sort(unsorted, center.get_displacement(width)); // Sort relative to center
    auto displacement = center.get_displacement(width);  // Center displacement
    transform(sorted.begin(), sorted.end(), sorted.begin(), [displacement](int x){return x - displacement;}); // Adjust to center
    return sorted;}

// Build a delta sequence for an Alignment: dynamic → centred search list (get_dynamic_displacements shifted by the center displacement so the first try is the centred placement, mirroring Text's dynamic-insert semantics), static → a one-element sequence with the static displacement. Lets callers handle every alignment combination through a single uniform loop where each delta is the absolute offset to add to the anchor.
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
