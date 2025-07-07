// Class to handle text alignment: left, center, or right alignment

class Alignment {
private:
    bool left = 0;   // Alignment flag for left
    bool center = 0; // Alignment flag for center
    bool right = 0;  // Alignment flag for right

public:
    // Constructor: Sets alignment based on input value
    Alignment(const int & i) { 
        clear(); 
        if (i == 0) {center = 1;} 
        else if (i == 1) {right = 1;} 
        else {left = 1;}}

    // Clears all alignment flags
    void clear() { left = center = right = 0; }

    // Calculates displacement based on alignment
    int get_displacement(const size_t & width) const { 
        if (left) { return 0; } 
        else if (center) { return - (width - 1) / 2; } 
        else { return 1 - width;}}

    int get_integer() const noexcept {if(left) {return -1;} if (center) {return 0;} else {return 1;}}
};

// Function to generate dynamic displacements based on width
vector<int> get_dynamic_displacements(const size_t & width) {
    Alignment right(1), center(0); // Define right and center alignments
    auto unsorted = range(right.get_displacement(width), 1); // Generate unsorted range
    auto sorted = sort(unsorted, center.get_displacement(width)); // Sort based on center displacement
    auto displacement = center.get_displacement(width); // Calculate center displacement
    // Adjust sorted displacements relative to center
    transform(sorted.begin(), sorted.end(), sorted.begin(), [displacement](int x) { return x - displacement; });
    return sorted;}
