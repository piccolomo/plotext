// Utility functions for string manipulation, encoding conversion and console output

// --- String Conversions ---

// Split a string into tokens by whitespace (spaces, tabs, newlines)
vector<string> split_string(const string & str) {
    vector<string> tokens;
    istringstream stream(str);
    string word;
    while (stream >> word) {tokens.push_back(word);}
    return tokens;}

// Split a wide string into lines based on new_line character
vector<wstring> split_wstring(const wstring & str) {
    vector<wstring> lines;
    size_t start = 0, end;
    while ((end = str.find(new_line, start)) != wstring::npos) {
        lines.push_back(str.substr(start, end - start));
        start = end + 1;} // Skip newline
    lines.push_back(str.substr(start)); // Add last line
    return lines;}

// Convert standard string to wide string
wstring_convert<codecvt_utf8_utf16<wchar_t>> converter;
inline wstring string_to_wstring(const string & str) noexcept {
    return converter.from_bytes(str);}

// Convert a wstring to a UTF-8 encoded string
inline std::string wstring_to_string(const std::wstring& wstr) {
    return converter.to_bytes(wstr);}

// Real (terminal-cell) width of a single wide character: 2 for East Asian wide / fullwidth / common emoji ranges, 1 otherwise. Used to size string-derived matrices so CJK and emoji glyphs (which the terminal renders in 2 cells) get 2 matrix columns.
inline size_t get_wchar_real_width(wchar_t c) noexcept {
    if (c < 0x1100) return 1;
    if (c >= 0x1100 && c <= 0x115F) return 2; // Hangul Jamo
    if (c >= 0x2E80 && c <= 0x303E) return 2; // CJK Radicals .. CJK Symbols and Punctuation
    if (c >= 0x3041 && c <= 0x33FF) return 2; // Hiragana .. CJK Compatibility
    if (c >= 0x3400 && c <= 0x4DBF) return 2; // CJK Extension A
    if (c >= 0x4E00 && c <= 0x9FFF) return 2; // CJK Unified Ideographs
    if (c >= 0xA000 && c <= 0xA4CF) return 2; // Yi
    if (c >= 0xAC00 && c <= 0xD7A3) return 2; // Hangul Syllables
    if (c >= 0xF900 && c <= 0xFAFF) return 2; // CJK Compatibility Ideographs
    if (c >= 0xFE30 && c <= 0xFE4F) return 2; // CJK Compatibility Forms
    if (c >= 0xFF00 && c <= 0xFF60) return 2; // Fullwidth Forms
    if (c >= 0xFFE0 && c <= 0xFFE6) return 2; // Fullwidth signs
    if (sizeof(wchar_t) >= 4) {
        if (c >= 0x1F300 && c <= 0x1FAFF) return 2; // Misc Pictographs / Emoticons / Transport / Geometric / Symbols & Pictographs Ext.
        if (c >= 0x20000 && c <= 0x2FFFD) return 2; // CJK Extensions B–F
        if (c >= 0x30000 && c <= 0x3FFFD) return 2; // CJK Extension G
    }
    return 1;
}

// Real (terminal-cell) width of a wide string: sum of per-character cell widths
inline size_t get_wstring_real_width(const wstring & s) noexcept {
    size_t w = 0;
    for (wchar_t c : s) w += get_wchar_real_width(c);
    return w;
}

// Get the width of the longest wide string in a vector (counted in terminal cells)
inline size_t get_width_strings(const vector<wstring> & str) noexcept {
    size_t length = 0;
    for (const wstring & s : str) {length = max(length, get_wstring_real_width(s));}
    return length;}

// Convert boolean to wide character ('1' or '0')
inline wchar_t bool_to_wchar(const bool & value) noexcept {return value ? L'1' : L'0';}


// --- Console Output Utilities ---

// Enable locale-based special characters
inline void enable_special_characters() noexcept {setlocale(LC_ALL, "");}

// Print new line(s)
inline void nl(size_t repeat = 1) {for (size_t i = 0; i < repeat; i++) {wcout << endl;}}

// Print spaces
inline void sp(size_t repeat = 1) {for (size_t i = 0; i < repeat; i++) {wcout << " ";}}

// Flush console output
inline void flush() {wcout << flush;}

// Write wide string to console, optionally with new line
inline void write(const wstring & s, bool new_line = 1) noexcept {wcout << s; if (new_line) {nl();}}

// Write standard string to console, optionally with new line
inline void write(const string & s, bool new_line = 1) noexcept {write(string_to_wstring(s), new_line);}
