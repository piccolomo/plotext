// Orientation: horizontal / vertical layout direction for text and similar drawables

class Orientation {
private:
    bool horizontal = 1;
    bool vertical = 0;

public:
    // Constructor: 0 -> horizontal, anything else -> vertical
    Orientation(const int & i = 0) { clear(); if (i == 0) {horizontal = 1;} else {vertical = 1;} }

    // Clear all orientation flags
    void clear() { horizontal = vertical = 0; }

    // Queries
    bool is_horizontal() const noexcept { return horizontal; }
    bool is_vertical() const noexcept { return vertical; }

    // Integer representation: 0 horizontal, 1 vertical
    int get_integer() const noexcept { return horizontal ? 0 : 1; }
};
