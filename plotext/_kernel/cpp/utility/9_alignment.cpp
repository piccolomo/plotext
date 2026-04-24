// Alignment utilities: left/center/right anchoring used when placing text inside fixed-width cells

// --- Text Alignment Utilities ---

// Alignment: left (-1), center (0), or right (1) anchor flags plus displacement helpers
class Alignment {
private:
    bool left = 0;   // Left alignment flag
    bool center = 0; // Center alignment flag
    bool right = 0;  // Right alignment flag

public:
    // Constructor: 0 -> center, 1 -> right, anything else -> left
    Alignment(const int & i) {clear(); if (i == 0) {center = 1;} else if (i == 1) {right = 1;} else {left = 1;}}

    // Clear all alignment flags
    void clear() {left = center = right = 0;}

    // Calculate displacement for a given width
    int get_displacement(const size_t & width) const {if (left) {return 0;} else if (center) {return -(width - 1) / 2;} else {return 1 - width;}}

    // Return integer representation: -1 left, 0 center, 1 right
    int get_integer() const noexcept {if (left) {return -1;} if (center) {return 0;} else {return 1;}}
};

// Generate a vector of dynamic displacements based on width
inline Vector<int> get_dynamic_displacements(const size_t & width) {
    Alignment right(1), center(0);                        // Right and center alignment objects
    auto unsorted = range(right.get_displacement(width), 1); // Unsorted range of displacements
    auto sorted = sort(unsorted, center.get_displacement(width)); // Sort relative to center
    auto displacement = center.get_displacement(width);  // Center displacement
    transform(sorted.begin(), sorted.end(), sorted.begin(), [displacement](int x){return x - displacement;}); // Adjust to center
    return sorted;}
