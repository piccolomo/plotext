// MarkerType class manages marker types.

class MarkerType {
private:
    marker_type type; // Enum representing the marker type (e.g., normal, hd, etc.)

public:
    // Constructor: Initializes the marker type to a default value (normal).
    MarkerType(const marker_type & t = normal) : type(t) {}

    // Copy constructor
    MarkerType(const MarkerType & other) : type(other.type) {}
 
    // Move constructor
    MarkerType(MarkerType && other) : type(other.type) {}

    // Assignment operator
    MarkerType & operator=(const MarkerType & m) {
        type = m.type;
        return *this;}

    // Reset the marker type to normal.
    void clear() {type = normal;}

    // Set a new marker type.
    void set(const marker_type & t = normal) {type = t;}

    // Get the current marker type.
    constexpr marker_type get() const {return type;}

    // Marker dimensions and resolution
    size_t get_rows() const {return get_marker_rows(type);}
    size_t get_cols() const {return get_marker_cols(type);}
    size_t get_resolution() const {return get_cols() * get_rows();}

    // Check if the marker type is normal.
    constexpr bool is_normal() const {return type == normal;}

    // Check if the marker type is not normal.
    constexpr bool is_hd() const {return type != normal;}

    // Copy the marker type's label into a buffer.
    virtual void to_buffer(wchar_t * buffer, size_t & length_buffer) const {
        string str = get_marker_label(type); // Convert marker type to string label
        cstring_to_buffer(string_to_wstring(str).c_str(), buffer, length_buffer);}
};