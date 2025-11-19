// Character - single wchar_t with inherited Pixel styling (foreground/background/attributes)

class Character : public Pixel {
private:
    wchar_t c = L' ';                   // displayed character (default space)

public:
    // -------------------- lifecycle --------------------
    constexpr Character() noexcept = default;
    constexpr Character(wchar_t ch) noexcept : c(ch) {}
    constexpr Character(wchar_t ch, const Pixel& p) noexcept : Pixel(p), c(ch) {}

    Character(const Character&) noexcept = default;
    Character(Character&&) noexcept = default;

    Character& operator=(const Character&) noexcept = default;

    // -------------------- comparison --------------------
    inline constexpr bool operator==(const Character& o) const noexcept { return c == o.c && Pixel::operator==(o); }
    inline constexpr bool operator!=(const Character& o) const noexcept { return !(*this == o); }

    inline constexpr bool same(const Character& o) const noexcept      { return c == o.c && Pixel::operator==(o); }
    inline constexpr bool same_pixel(const Character& o) const noexcept{ return Pixel::operator==(o); }
    inline constexpr bool different(const Character& o) const noexcept { return !Pixel::operator==(o); }

    // -------------------- state --------------------
    inline constexpr bool is_empty() const noexcept { return c == L' '; }
    inline void clear() noexcept { c = L' '; Pixel::clear(); }

    // -------------------- setters/getters --------------------
    inline constexpr void set_wcharacter(wchar_t ch) noexcept { c = ch; }
    inline wchar_t get_wcharacter() const noexcept           { return c; }

    inline void set_pixel(const Pixel& p) noexcept { Pixel::operator=(p); }
    inline void copy_wcharacter(const Character& o) noexcept { c = o.c; }

    // -------------------- output --------------------
    // Append styled character + reset to wchar_t buffer
    inline void to_buffer(wchar_t* buf, size_t& pos) const noexcept {
        Pixel::to_buffer(buf, pos);                 // apply foreground/bg/attrs
        wchar_to_buffer(c, buf, pos);               // write character itself
        cstring_to_buffer(ansi_end, buf, pos);}      // reset ANSI codes

    // Same as to_buffer but guarantees final reset (some callers prefer explicit double-reset)
    inline void to_buffer_full(wchar_t* buf, size_t& pos) const noexcept {
        to_buffer(buf, pos);
        cstring_to_buffer(ansi_end, buf, pos);}

    // Get wide string for display
    inline wstring get_wstring() const {
        wchar_t buf[character_size_max + 1] = {};
        size_t pos = 0;
        to_buffer_full(buf, pos);
        return wstring(buf);}

    // Get standard string for display
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    inline void log() const { wcout << get_wstring() << endl; } // Log to console

    // Stream directly (faster, no buffer)
    inline void stream() const noexcept {
        Pixel::stream();
        wcout.put(c);}

    friend wostream & operator<<(wostream & os, const Character & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Character & c) noexcept {os << c.get_string(); return os;}
};