// MarkerType class manages marker types.

class MarkerType {
private:
    marker_type type = normal;          // default marker resolution

public:
    // -------------------- lifecycle --------------------
    constexpr MarkerType(marker_type t = normal) noexcept : type(t) {}
    constexpr MarkerType(const MarkerType&) noexcept = default;
    constexpr MarkerType(MarkerType&&) noexcept = default;
    constexpr MarkerType& operator=(const MarkerType&) noexcept = default;

    // -------------------- comparison --------------------
    constexpr bool operator==(const MarkerType& o) const noexcept { return type == o.type; }
    constexpr bool operator!=(const MarkerType& o) const noexcept { return type != o.type; }

    // -------------------- state --------------------
    constexpr void clear() noexcept { type = normal; }
    constexpr void set(marker_type t = normal) noexcept { type = t; }

    // -------------------- getters --------------------
    constexpr marker_type get() const noexcept { return type; }

    size_t get_rows()   const noexcept { return get_marker_rows(type); }
    size_t get_cols()   const noexcept { return get_marker_cols(type); }
    size_t get_resolution() const noexcept { return get_rows() * get_cols(); }

    // -------------------- type checks --------------------
    constexpr bool is_none()     const noexcept { return type == none; }
    constexpr bool is_normal()   const noexcept { return type == normal; }
    constexpr bool is_hd()       const noexcept { return type == hd; }
    constexpr bool is_fhd()      const noexcept { return type == fhd; }
    constexpr bool is_braille()  const noexcept { return type == braille; }
    constexpr bool is_high_definition() const noexcept { return !is_none() && !is_normal(); }

    // -------------------- output --------------------
    // Append marker label (e.g. "HD", "FHD") to buffer
    virtual inline void to_buffer(wchar_t* buf, size_t& pos) const noexcept {
        cstring_to_buffer(get_marker_label(type), buf, pos);}

    // -------------------- display & logging --------------------
    inline wstring get_wstring() const {
        return get_marker_label(type); }

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    inline void log() const { wcout << get_wstring() << endl; }

    friend wostream& operator<<(wostream& os, const MarkerType& m) noexcept {
        os << m.get_wstring(); return os; }

    friend ostream& operator<<(ostream& os, const MarkerType& m) noexcept {
        os << m.get_string(); return os; }

};