// MarkerType: classification of a marker (none / normal / hd / fhd / braille) with size and label lookups

class MarkerType {
private:
    marker_type type = normal;          // default marker resolution

public:
    // -------------------- lifecycle --------------------

    // Constructor with an explicit marker type (defaults to none)
    constexpr MarkerType(marker_type t = none) noexcept : type(t) {}

    // Copy constructor
    constexpr MarkerType(const MarkerType &) noexcept = default;

    // Move constructor
    constexpr MarkerType(MarkerType &&) noexcept = default;

    // Virtual destructor for safe polymorphic deletion via base
    virtual ~MarkerType() noexcept {}

    // Copy assignment
    constexpr MarkerType& operator=(const MarkerType &) noexcept = default;

    // Move assignment
    constexpr MarkerType& operator=(MarkerType &&) noexcept = default;

    // -------------------- comparison --------------------

    // Equality comparison
    constexpr bool operator==(const MarkerType & o) const noexcept { return type == o.type; }

    // Inequality comparison
    constexpr bool operator!=(const MarkerType & o) const noexcept { return type != o.type; }

    // -------------------- state --------------------

    // Reset to the normal marker type
    constexpr void clear() noexcept { type = normal; }

    // Set the marker type
    constexpr void set(marker_type t = normal) noexcept { type = t; }

    // -------------------- getters --------------------

    // Return the marker type enum
    constexpr marker_type get() const noexcept { return type; }

    // Number of sub-rows in the marker
    size_t get_rows()   const noexcept { return get_marker_rows(type); }

    // Number of sub-columns in the marker
    size_t get_cols()   const noexcept { return get_marker_cols(type); }

    // Total number of sub-cells in the marker (rows * cols)
    size_t get_resolution() const noexcept { return get_rows() * get_cols(); }

    // -------------------- type checks --------------------

    // True if marker type is none
    constexpr bool is_none()     const noexcept { return type == none; }

    // True if marker type is normal
    constexpr bool is_normal()   const noexcept { return type == normal; }

    // True if marker type is hd
    constexpr bool is_hd()       const noexcept { return type == hd; }

    // True if marker type is fhd
    constexpr bool is_fhd()      const noexcept { return type == fhd; }

    // True if marker type is braille
    constexpr bool is_braille()  const noexcept { return type == braille; }

    // True if marker type is any of hd / fhd / braille
    constexpr bool is_high_definition() const noexcept { return !is_none() && !is_normal(); }

    // -------------------- output --------------------

    // Append marker label (e.g. "HD", "FHD") to buffer
    virtual inline void to_buffer(wchar_t* buf, size_t & pos) const noexcept {
        cstring_to_buffer(get_marker_label(type), buf, pos);}

    // -------------------- display & logging --------------------

    // Get wide string (the marker label)
    inline wstring get_wstring() const {
        return get_marker_label(type); }

    // Get narrow string
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout
    inline void log() const { wcout << get_wstring() << endl; }

    // Wide-stream output
    friend wostream& operator<<(wostream& os, const MarkerType& m) noexcept {
        os << m.get_wstring(); return os; }

    // Narrow-stream output
    friend ostream& operator<<(ostream& os, const MarkerType& m) noexcept {
        os << m.get_string(); return os; }

};
