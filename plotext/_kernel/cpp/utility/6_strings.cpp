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

// Get the width of the longest wide string in a vector
inline size_t get_width_strings(const vector<wstring> & str) noexcept {
    size_t length = 0;
    for (const wstring & s : str) {length = max(length, s.size());}
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
