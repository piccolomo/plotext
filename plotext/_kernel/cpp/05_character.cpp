// Character: a single wchar_t with inherited Pixel styling (foreground / background / attributes)

class Character : public Pixel {
private:
    wchar_t c = L' ';                   // displayed character (default space)

public:
    // -------------------- lifecycle --------------------

    // Default constructor
    constexpr Character() noexcept = default;

    // Construct from a wchar_t
    constexpr Character(wchar_t ch) noexcept : c(ch) {}

    // Construct from a wchar_t and a Pixel
    constexpr Character(wchar_t ch, const Pixel& p) noexcept : Pixel(p), c(ch) {}

    // Construct from a Pixel only (character defaults to space)
    constexpr Character(const Pixel& p) noexcept : Character(L' ', p) {}

    // Copy constructor
    Character(const Character&) noexcept = default;

    // Move constructor
    Character(Character&&) noexcept = default;

    // Copy assignment
    Character& operator=(const Character&) noexcept = default;

    // Move assignment
    Character& operator=(Character&&) noexcept = default;

    // Destructor (no dynamic memory)
    ~Character() noexcept {}

    // -------------------- comparison --------------------

    // Equality comparison (same character and same pixel)
    inline constexpr bool operator==(const Character& o) const noexcept { return c == o.c && Pixel::operator==(o); }

    // Inequality comparison
    inline constexpr bool operator!=(const Character& o) const noexcept { return !(*this == o); }

    // True if character and pixel both match
    inline constexpr bool same(const Character& o) const noexcept      { return c == o.c && Pixel::operator==(o); }

    // True if only the pixel matches
    inline constexpr bool same_pixel(const Character& o) const noexcept{ return Pixel::operator==(o); }

    // True if the pixel differs
    inline constexpr bool different_pixel(const Character& o) const noexcept { return !Pixel::operator==(o); }

    // -------------------- state --------------------

    // True if this character is a blank space
    inline constexpr bool is_empty() const noexcept { return c == L' '; }

    // Reset character and pixel to defaults
    inline void clear() noexcept { c = L' '; Pixel::clear(); }

    // -------------------- setters/getters --------------------

    // Set the displayed character
    inline constexpr void set_wcharacter(wchar_t ch) noexcept { c = ch; }

    // Get the displayed character
    inline wchar_t get_wcharacter() const noexcept           { return c; }

    // Copy a pixel onto this character
    inline void set_pixel(const Pixel& p) noexcept { Pixel::operator=(p); }

    // Copy only the character from another Character
    inline void copy_wcharacter(const Character& o) noexcept { c = o.c; }

    // -------------------- output --------------------

    // Append styled character + reset to a wchar_t buffer
    inline void to_buffer(wchar_t* buf, size_t & pos, const bool & colorfull = true) const noexcept {
        if (colorfull) Pixel::to_buffer(buf, pos);                 // apply foreground/bg/attrs
        wchar_to_buffer(c, buf, pos);               // write character itself
        if (colorfull) cstring_to_buffer(ansi_end, buf, pos);}      // reset ANSI codes


    // Get wide string for display
    inline wstring get_wstring() const {
        wchar_t buf[character_size_max + 1] = {};
        size_t pos = 0;
        to_buffer(buf, pos);
        return wstring(buf);}

    // Get standard string for display
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout
    inline void log() const { wcout << get_wstring() << endl; }

    // Stream directly (faster, no buffer)
    inline void stream(const bool & colorless = false) const noexcept {
        if (not colorless) Pixel::stream();
        wcout.put(c);
        if (not colorless) wcout.write(ansi_end, 4);}

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Character & ch) noexcept {os << ch.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Character & ch) noexcept {os << ch.get_string(); return os;}
};
