// Color Management: Handles ANSI foreground/background color codes.

class Color {
private:
    wchar_t code[color_size_max]; // ANSI color code storage
    size_t length = 0;            // Cache length

public:
    constexpr Color() noexcept : code{}, length(0) {} // Default constructor

    Color(bool is_fullground, const string & color) { clear(); set(is_fullground, color); } // String constructor

    Color(bool is_fullground, bool is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
        clear(); set(is_fullground, is_integer, r, g, b);} // RGB or integer constructor

    Color(const Color & c) = default; // Copy constructor
    Color(Color && c) = default;      // Move constructor

    constexpr inline bool same(const Color & c) const noexcept { return length == c.length and same_cstrings(code, c.get_code(), c.length); } // Compare colors

    inline void copy(const Color & c) noexcept { copy_cstring(c.get_code(), code, c.length); length = c.length; } // Copy color

    inline void clear() noexcept { code[0] = L'\0'; length = 0; } // Clear color

    inline void update_length() noexcept { length = wcslen(code); } // Update cached length

    // Set color using fullground flag, integer flag, and RGB values
    inline void set(bool is_fullground, bool is_integer, const unsigned char r = 0, const unsigned char g = 0, const unsigned char b = 0) {
        if (is_fullground) { wcscpy(code, ansi_fullground); } 
        else { wcscpy(code, ansi_background); }
        if (is_integer) { swprintf(code + 5, 7, L"5;%dm", r); } 
        else { swprintf(code + 5, 16, L"2;%d;%d;%dm", r, g, b); }
        update_length(); }

    // Set color using string name
    inline void set(bool is_fullground, const string & color) {
        unsigned char color_code = get_color_code(color);
        if (color_code == 100) { clear(); } 
        else { set(is_fullground, true, color_code); } }

    inline const unsigned char get_integer_code() const noexcept {
        const wchar_t * p = wcsstr(code, L"5;");
        if (p) { unsigned char val = 0; if (swscanf(p + 2, L"%dm", &val) == 1) return val; }
        return 20; } // Default if not found

    constexpr size_t get_length() const noexcept { return length; } // Cached length
    constexpr const wchar_t * get_code() const noexcept { return code; } // Access code
    constexpr bool no_color() const noexcept { return length == 0; } // No color
    constexpr bool has_color() const noexcept { return length != 0; } // Has color

    // Write code to buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (has_color()) { cstring_to_buffer(code, length, buffer, length_buffer); } }

    // Write name to buffer (virtual)
    virtual inline void name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { cstring_to_buffer(L"Color", 5, buffer, length_buffer); }

    // Get wide string for display
    inline wstring get_wstring() const {
        wchar_t buffer[color_size_max + 10] = {L'\0'}; 
        size_t len = 0;
        to_buffer(buffer, len);
        name_to_buffer(buffer, len);
        if (has_color()) { cstring_to_buffer(ansi_end, buffer, len); }
        return wstring(buffer); }

    // Get standard string for display
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    inline void log() const { wcout << get_wstring() << endl; } // Log to console
    inline void show() const { show_ansi_wstring(code); }       // Show code

    inline void stream() const { wcout.write(code, length); } // Stream raw ANSI

    friend wostream & operator<<(wostream & os, const Color & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Color & c) noexcept {os << c.get_string(); return os;}

};


// Fullground: Foreground color
class Fullground : public Color {
public:
    constexpr Fullground() = default; // Default constructor
    Fullground(const string & color) : Color(true, color) {} // String constructor
    Fullground(const unsigned char & r) : Color(true, true, r) {} // Integer constructor
    Fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(true, false, r, g, b) {} // RGB constructor
    Fullground(const Fullground & c) = default; // Copy
    Fullground(Fullground && c) = default;      // Move

    constexpr inline bool operator==(const Fullground & fg) const noexcept { return Color::same(fg); } // Compare
    inline Fullground & operator=(const Fullground & fg) noexcept { Color::copy(fg); return *this; } // Assign

    inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) { Color::set(true, false, r, g, b); } // RGB
    inline void set(const unsigned char & r) { Color::set(true, true, r); } // Single int
    inline void set(const string & color) { Color::set(true, color); } // Name

    inline void name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { cstring_to_buffer(L"Fullground", 10, buffer, length_buffer); } // Override name
};


// Background: Background color
class Background : public Color {
public:
    constexpr Background() = default; // Default constructor
    Background(const string & color) : Color(false, color) {} // String
    Background(const unsigned char & r) : Color(false, true, r) {} // Integer
    Background(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(false, false, r, g, b) {} // RGB
    Background(const Background & c) = default; // Copy
    Background(Background && c) = default;      // Move

    inline bool operator==(const Background & bg) const noexcept { return Color::same(bg); } // Compare
    inline Background & operator=(const Background & bg) noexcept { Color::copy(bg); return *this; } // Assign

    inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) { Color::set(false, false, r, g, b); } // RGB
    inline void set(const unsigned char & r) { Color::set(false, true, r); } // Single int
    inline void set(const string & color) { Color::set(false, color); } // Name

    inline void name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { cstring_to_buffer(L"Background", 10, buffer, length_buffer); } // Override name
};
