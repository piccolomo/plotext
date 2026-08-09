// Color: stores the ANSI escape sequence for a foreground or background color; base class for Fullground and Background

// Single ANSI color code (foreground or background) with name/integer/RGB setters
class Color {
protected:
    wchar_t code[color_size_max]; // ANSI color code storage
    size_t length = 0;            // Cache length

public:
    // Default constructor
    constexpr Color() noexcept : code{}, length(0) {}

    // String constructor (color name)
    Color(bool is_fullground, const string & color) { clear(); set(is_fullground, color); }

    // Integer or RGB constructor
    Color(bool is_fullground, bool is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
        clear(); set(is_fullground, is_integer, r, g, b);}

    // Copy constructor
    Color(const Color & c) = default;

    // Move constructor
    Color(Color && c) = default;

    // Virtual destructor for safe polymorphic deletion
    virtual ~Color() noexcept {}

    // Compare two colors (length and code equal)
    constexpr inline bool same(const Color & c) const noexcept { return length == c.length and same_cstrings(code, c.get_code(), c.length); }

    // Copy another color's code into this one
    inline void copy(const Color & c) noexcept { copy_cstring(c.get_code(), code, c.length); length = c.length; }

    // Clear the color (empty code)
    inline void clear() noexcept { code[0] = L'\0'; length = 0; }

    // Refresh the cached length from the code buffer
    inline void update_length() noexcept { length = wcslen(code); }

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

    // Parse the integer code from the stored ANSI sequence (returns 20 if not found). `val` is `int` because `%d` writes sizeof(int) bytes, using `unsigned char` here is UB and stack-smashes.
    inline unsigned char get_integer_code() const noexcept {
        const wchar_t * p = wcsstr(code, L"5;");
        if (p) { int val = 0; if (swscanf(p + 2, L"%dm", &val) == 1) return static_cast<unsigned char>(val); }
        return 20; }

    // Cached code length
    constexpr size_t get_length() const noexcept { return length; }

    // Access the raw ANSI code
    constexpr const wchar_t * get_code() const noexcept { return code; }

    // True if no color is set
    constexpr bool no_color() const noexcept { return length == 0; }

    // True if a color is set
    constexpr bool has_color() const noexcept { return length != 0; }

    // Append the ANSI code to a buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (has_color()) { cstring_to_buffer(code, length, buffer, length_buffer); } }

    // Append the CSS property name to a buffer (overridden by Fullground = "color", Background = "background")
    virtual inline void css_name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { cstring_to_buffer(L"color", 5, buffer, length_buffer); }

    // Decode this color's ANSI code into an RGB triplet (palette form via rgb_lookup, rgb form by parsing)
    inline void get_rgb(unsigned char & r, unsigned char & g, unsigned char & b) const noexcept {
        if (code[5] == L'5') { unsigned char idx = get_integer_code(); r = rgb_lookup[idx][0]; g = rgb_lookup[idx][1]; b = rgb_lookup[idx][2]; }
        else { unsigned int rr = 0, gg = 0, bb = 0; swscanf(code + 7, L"%u;%u;%um", &rr, &gg, &bb); r = (unsigned char)rr; g = (unsigned char)gg; b = (unsigned char)bb; } }

    // Append the CSS declaration for this color to a buffer (e.g. "color:rgb(229,229,16);")
    inline void html_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (no_color()) return;
        unsigned char r, g, b; get_rgb(r, g, b);
        css_name_to_buffer(buffer, length_buffer);
        wchar_t tmp[24] = {L'\0'};
        int n = swprintf(tmp, 24, L":rgb(%u,%u,%u);", r, g, b);
        if (n > 0) cstring_to_buffer(tmp, (size_t)n, buffer, length_buffer); }

    // Append the class name label to a buffer (overridden by Fullground / Background)
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

    // Log to wcout
    inline void log() const { wcout << get_wstring() << endl; }

    // Show the ANSI code with indices
    inline void show() const { show_ansi_wstring(code); }

    // Stream the raw ANSI code to wcout
    inline void stream() const { wcout.write(code, length); }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Color & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Color & c) noexcept {os << c.get_string(); return os;}

};


// Fullground: foreground color (ANSI \x1b[38;...)
class Fullground : public Color {
public:
    // Default constructor
    constexpr Fullground() = default;

    // String constructor (color name)
    Fullground(const string & color) : Color(true, color) {}

    // Integer constructor (palette index)
    Fullground(const unsigned char & r) : Color(true, true, r) {}

    // RGB constructor
    Fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(true, false, r, g, b) {}

    // Copy constructor
    Fullground(const Fullground & c) = default;

    // Move constructor
    Fullground(Fullground && c) = default;

    // Destructor
    ~Fullground() noexcept {}

    // Compare foreground colors
    constexpr inline bool operator==(const Fullground & fg) const noexcept { return Color::same(fg); }

    // Copy assignment (self-assignment safe)
    inline Fullground & operator=(const Fullground & fg) noexcept {
        if (this != &fg) Color::copy(fg);
        return *this; }


    // RGB setter
    inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) { Color::set(true, false, r, g, b); }

    // Palette-index setter
    inline void set(const unsigned char & r) { Color::set(true, true, r); }

    // Name setter
    inline void set(const string & color) { Color::set(true, color); }

    // Append class name label "Fullground" to a buffer
    inline void name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override { cstring_to_buffer(L"Fullground", 10, buffer, length_buffer); }

    // Append the CSS property name "color" to a buffer
    inline void css_name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override { cstring_to_buffer(L"color", 5, buffer, length_buffer); }
};


// Background: background color (ANSI \x1b[48;...)
class Background : public Color {
public:
    // Default constructor
    constexpr Background() = default;

    // String constructor (color name)
    Background(const string & color) : Color(false, color) {}

    // Integer constructor (palette index)
    Background(const unsigned char & r) : Color(false, true, r) {}

    // RGB constructor
    Background(const unsigned char & r, const unsigned char & g, const unsigned char & b) : Color(false, false, r, g, b) {}

    // Copy constructor
    Background(const Background & c) = default;

    // Move constructor
    Background(Background && c) = default;

    // Destructor
    ~Background() noexcept {}

    // Compare background colors
    inline bool operator==(const Background & bg) const noexcept { return Color::same(bg); }

    // Copy assignment (self-assignment safe)
    inline Background & operator=(const Background & bg) noexcept {
        if (this != &bg) Color::copy(bg);
        return *this; }

    // RGB setter
    inline void set(const unsigned char & r, const unsigned char & g, const unsigned char & b) { Color::set(false, false, r, g, b); }

    // Palette-index setter
    inline void set(const unsigned char & r) { Color::set(false, true, r); }

    // Name setter
    inline void set(const string & color) { Color::set(false, color); }

    // Append class name label "Background" to a buffer
    inline void name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override { cstring_to_buffer(L"Background", 10, buffer, length_buffer); }

    // Append the CSS property name "background" to a buffer
    inline void css_name_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept override { cstring_to_buffer(L"background", 10, buffer, length_buffer); }
};
