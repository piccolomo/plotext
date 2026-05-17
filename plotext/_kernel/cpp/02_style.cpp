// Style: stores the ANSI escape sequence for one or more text styles (bold, underline, italic, etc.)

// Composite ANSI style code built from space-separated style names
class Style {
private:
    wchar_t code[style_size_max]; // ANSI style code storage
    size_t length;                // Cached length

public:
    // Default constructor
    constexpr Style() noexcept : code{L'\0'}, length(0) {}

    // Build from a space-separated style name string (e.g. "bold italic")
    Style(const string & style) { clear(); set(style); }

    // Copy constructor
    Style(const Style & st) = default;

    // Move constructor
    Style(Style && st) = default;

    // Destructor
    ~Style() noexcept {}

    // Compare styles (length and code equal)
    inline bool operator==(const Style & st) const noexcept { return length == st.length and same_cstrings(code, st.get_code(), length); }

    // Copy assignment (self-assignment safe)
    inline Style & operator=(const Style & st) noexcept {
        if (this != &st) { length = st.length; copy_cstring(st.get_code(), code, length); }
        return *this; }

    // Clear the style (empty code)
    inline void clear() noexcept { code[0] = L'\0'; length = 0; }

    // Set style from a space-separated string (e.g. "bold underline")
    inline void set(const string & style) {
        vector<string> styles = split_string(style);
        vector<unsigned char> style_codes;
        style_codes.reserve(styles.size());

        for (const string & s : styles) {
            unsigned char style_code = get_style_code(s);
            if (style_code != 100) { style_codes.push_back(style_code); }} // Only valid codes

        if (!style_codes.empty()) { wcscpy(code, ansi_start); } // Start sequence
        for (const unsigned char & sc : style_codes) { swprintf(code + wcslen(code), 3, L"%d;", sc); } // Append codes
        if (!style_codes.empty()) { code[wcslen(code) - 1] = L'm'; code[wcslen(code)] = L'\0'; } // Terminate
        length = wcslen(code); }

    // Cached code length
    constexpr size_t get_length() const noexcept { return length; }

    // Access the raw ANSI code
    constexpr const wchar_t * get_code() const noexcept { return code; }

    // True if no style is set
    constexpr bool no_style() const noexcept { return length == 0; }

    // True if a style is set
    constexpr bool has_style() const noexcept { return length != 0; }

    // Append the ANSI code to a buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (has_style()) { cstring_to_buffer(code, length, buffer, length_buffer); } }

    // Append the CSS declarations for this style to a buffer (e.g. "font-weight:bold;font-style:italic;"). Re-parses the cached ANSI code to recover individual style integers, then looks up each in style_html_codes.
    inline void html_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (no_style()) return;
        const wchar_t * p = code + 2; // skip "\x1b["
        while (*p && *p != L'm') {
            unsigned int sc = 0;
            while (*p >= L'0' && *p <= L'9') { sc = sc * 10 + (*p - L'0'); ++p; }
            auto it = style_html_codes.find((unsigned char)sc);
            if (it != style_html_codes.end()) cstring_to_buffer(it->second.c_str(), it->second.length(), buffer, length_buffer);
            if (*p == L';') ++p; } }

    // Get wide string representation
    inline wstring get_wstring() const {
        wchar_t buffer[style_size_max + 11] = { L'\0' };
        size_t len = 0;
        to_buffer(buffer, len);
        cstring_to_buffer(L"Style", 5, buffer, len);
        if (has_style()) { cstring_to_buffer(ansi_end, buffer, len); }
        return wstring(buffer);}

    // Get narrow string representation
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Show style code in console
    inline void show() const noexcept { show_ansi_wstring(code); }

    // Log to wcout
    inline void log() const { wcout << get_wstring() << endl; }

    // Stream the raw ANSI code to wcout
    inline void stream() const noexcept { wcout.write(code, length); }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Style & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Style & c) noexcept {os << c.get_string(); return os;}
};
