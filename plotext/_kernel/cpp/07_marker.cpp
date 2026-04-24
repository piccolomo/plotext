// Marker: combines Character (wchar + styling) with MarkerType (resolution mode: normal / hd / fhd / braille)

class Marker : public Character, public MarkerType {
public:
    // -------------------- lifecycle --------------------

    // Default constructor
    constexpr Marker() noexcept = default;

    // Construct from a character and optional pixel (normal marker type)
    constexpr Marker(wchar_t ch, const Pixel & p = Pixel()) noexcept : Character(ch, p), MarkerType(normal) {}

    // Construct from a marker type and optional pixel (character defaults to space)
    constexpr Marker(marker_type t, const Pixel & p = Pixel()) noexcept : Character(L' ', p), MarkerType(t) {}

    // Construct from a pixel only (type defaults to none)
    constexpr Marker(const Pixel & p) noexcept : Marker(none, p) {}

    // Copy constructor
    Marker(const Marker&) noexcept = default;

    // Move constructor
    Marker(Marker&&) noexcept = default;

    // Destructor
    ~Marker() noexcept {}

    // -------------------- assignment --------------------

    // Copy assignment (self-assignment safe)
    Marker& operator=(const Marker& m) noexcept {
        if (this == &m) return *this;
        Character::operator=(m);
        MarkerType::operator=(m);
        return *this;}

    // Move assignment
    Marker& operator=(Marker&& m) noexcept {
        if (this == &m) return *this;
        Character::operator=(std::move(m));
        MarkerType::operator=(std::move(m));
        return *this;}

    // Assign from a plain Character (forces normal mode)
    Marker& operator=(const Character& ch) noexcept {
        Character::operator=(ch);
        MarkerType::set(normal);
        return *this;}

    // -------------------- comparison --------------------

    // Equality comparison
    constexpr bool operator==(const Marker& o) const noexcept {
        return Character::operator==(o) && MarkerType::operator==(o);}

    // Inequality comparison
    constexpr bool operator!=(const Marker& o) const noexcept { return !(*this == o); }

    // True if markers share the same type
    constexpr bool same_type(const Marker& o) const noexcept { return MarkerType::operator==(o); }

    // -------------------- state --------------------

    // Reset character, pixel and marker type
    void clear() noexcept { Character::clear(); MarkerType::clear(); }

    // Set the marker type
    void set_type(marker_type t = normal) noexcept { MarkerType::set(t); }

    // Set the displayed character (switches the marker type to normal)
    void set_wcharacter(wchar_t ch) noexcept {
        MarkerType::set(normal);
        Character::set_wcharacter(ch);}

    // Representative character: the actual char in normal mode, or a model glyph otherwise
    wchar_t get_model() const noexcept {
        return is_normal() ? Character::get_wcharacter() : get_marker_model(get());}

    // Return the pixel (color + style) as a detached copy
    Pixel get_pixel() const noexcept { return static_cast<Pixel>(*this); }

    // -------------------- rendering --------------------

    // Append styled character (or marker label in HD modes) to buffer
    void to_buffer(wchar_t* buf, size_t& pos) const noexcept {
        Pixel::to_buffer(buf, pos);                          // apply styling
        if (is_normal()) wchar_to_buffer(get_wcharacter(), buf, pos);        // single char
        else MarkerType::to_buffer(buf, pos);                    // e.g. "HD", "FHD"
        if (pos > 0) cstring_to_buffer(ansi_end, buf, pos); }    // reset ANSI

    // Get wide string for display
    wstring get_wstring() const {
        wchar_t buf[marker_size_max + 1] = {};
        size_t pos = 0;
        to_buffer(buf, pos);
        return wstring(buf, pos);}

    // Get narrow string for display
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout
    void log() const noexcept {wcout << get_wstring() << endl;}

    // Wide-stream output
    friend wostream& operator<<(wostream & os, const Marker & m) noexcept {os << m.get_wstring(); return os; }

    // Narrow-stream output
    friend ostream& operator<<(ostream & os, const Marker & m) noexcept {os << m.get_string(); return os; }

};


extern "C" {
    // Create a new normal marker from a character and pixel
    Marker* marker_new_normal(wchar_t c, const Pixel* p) noexcept { return new Marker(c, *p); }

    // Create a new HD/FHD/braille marker from a type and pixel
    Marker* marker_new_hd(marker_type t, const Pixel* p) noexcept { return new Marker(t, *p); }

    // Create a new normal marker from a named character code (e.g. "dot"),
    // resolved to a wchar_t via get_marker() from utility/5_maps.cpp.
    Marker* marker_new_code(const char* code, const Pixel* p) noexcept {
        return new Marker(get_marker(string(code)), *p); }

    // Delete a marker
    void marker_delete(Marker* m) noexcept { delete m; }

    // Deep copy of a marker
    Marker* marker_copy(const Marker* m) noexcept { return new Marker(*m); }

    // Return the rendered wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t* marker_get_wstring(const Marker* m) noexcept { return wstring_to_cstring(m->get_wstring()); }

    // Return the representative model character
    wchar_t        marker_get_model(const Marker* m) noexcept { return m->get_model(); }

    // Return a heap-allocated copy of the marker's pixel
    Pixel*         marker_get_pixel(const Marker* m) noexcept { return new Pixel(m->get_pixel()); }

    // Fix this marker's colors against another marker's pixel
    void marker_fix(Marker * p, Marker * pixel) noexcept {p->fix(*pixel);}
}
