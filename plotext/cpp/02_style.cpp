// Style Management: Handles multiple text styles (bold, underline, etc.)

class Style {
private:
    wchar_t code[19]; // Buffer to store ANSI style code
    size_t length;    // Cached length

public:
    constexpr Style() noexcept : code{L'\0'}, length(0) {} // Default constructor
    Style(const string & style) { clear(); set(style); }   // String constructor
    Style(const Style & st) = default;                    // Copy constructor
    Style(Style && st) = default;                         // Move constructor

    inline bool operator==(const Style & st) const noexcept { return length == st.length and same_cstrings(code, st.get_code(), length); } // Compare

    inline Style & operator=(const Style & st) noexcept { length = st.length; copy_cstring(st.get_code(), code, length); return *this; } // Assign

    inline void clear() noexcept { code[0] = L'\0'; length = 0; } // Clear style

    // Set style from string (e.g., "bold underline")
    inline void set(const string & style) {
        vector<string> styles = split_string(style); // Split input
        vector<unsigned char> style_codes; 
        style_codes.reserve(styles.size());

        for (const string & s : styles) {
            unsigned char style_code = get_style_code(s); 
            if (style_code != 100) { style_codes.push_back(style_code); }} // Only valid codes

        if (!style_codes.empty()) { wcscpy(code, ansi_start); } // Start sequence
        for (const unsigned char & sc : style_codes) { swprintf(code + wcslen(code), 3, L"%d;", sc); } // Append codes
        if (!style_codes.empty()) { code[wcslen(code) - 1] = L'm'; code[wcslen(code)] = L'\0'; } // Terminate
        length = wcslen(code); }

    constexpr size_t get_length() const noexcept { return length; }  // Cached length
    constexpr const wchar_t * get_code() const noexcept { return code; } // Access code
    constexpr bool no_style() const noexcept { return length == 0; } // Empty
    constexpr bool has_style() const noexcept { return length != 0; } // Set

    // Write style to buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        if (has_style()) { cstring_to_buffer(code, length, buffer, length_buffer); } }

    // Get wide string representation
    inline wstring get_wstring() const {
        wchar_t buffer[30] = { L'\0' };
        size_t len = 0;
        to_buffer(buffer, len);
        cstring_to_buffer(L"Style", 5, buffer, len);
        if (has_style()) { cstring_to_buffer(ansi_end, buffer, len); }
        return wstring(buffer);}

    // Get std::string version
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Show style code in console
    inline void show() const noexcept { show_ansi_wstring(code); }

    inline void log() const { wcout << get_wstring () << endl; } // Log
    inline void stream() const { wcout.write(code, length); }                   // Stream raw ANSI

    friend wostream & operator<<(wostream & os, const Style & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Style & c) noexcept {os << c.get_string(); return os;}

};