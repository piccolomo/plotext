// MarkerType class manages marker types.

class MarkerType {
private:
    marker_type type = normal; // Default to normal

public:
    // Constructors
    constexpr MarkerType(marker_type t = normal) noexcept : type(t) {}
    MarkerType(const MarkerType &) noexcept = default;
    MarkerType(MarkerType &&) noexcept = default;

    // Assignment
    MarkerType & operator=(const MarkerType &) noexcept = default;

    // Equality
    constexpr bool operator==(const MarkerType & m) const noexcept { return type == m.type; }
    constexpr bool operator!=(const MarkerType & m) const noexcept { return type != m.type; }

    // Reset / Set
    constexpr void clear() noexcept { type = normal; }
    constexpr void set(marker_type t = normal) noexcept { type = t; }

    // Getters
    constexpr marker_type get() const noexcept { return type; }
    size_t get_rows() const noexcept { return get_marker_rows(type); }
    size_t get_cols() const noexcept { return get_marker_cols(type); }
    size_t get_resolution() const noexcept { return get_rows() * get_cols(); }

    // Type checks
    constexpr bool is_none() const noexcept { return type == none; }
    constexpr bool is_normal() const noexcept { return type == normal; }
    constexpr bool is_hd() const noexcept { return type == hd; }
    constexpr bool is_fhd() const noexcept { return type == fhd; }
    constexpr bool is_braille() const noexcept { return type == braille; }
    constexpr bool is_high_definition() const noexcept { return !is_none() && !is_normal(); }


    // Copy the marker type's label into a buffer.
    virtual void to_buffer(wchar_t * buffer, size_t & length_buffer) const {
        const wchar_t * str = get_marker_label(type); // Convert marker type to string label
        cstring_to_buffer(str, buffer, length_buffer);}
};