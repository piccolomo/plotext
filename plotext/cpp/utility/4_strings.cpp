// This section contains utility functions for string manipulation

// String Conversions

// Split a string into tokens based on space char.
vector<string> split_string(const string & str) {
    vector<std::string> tokens;
    istringstream stream(str);
    string word;
    while (stream >> word) {tokens.push_back(word);}
    return tokens;}

// Split a string into tokens based on new line char.
vector<wstring> split_wstring(const wstring& str) {
    vector<wstring> lines;
    size_t start = 0;
    size_t end;

    while ((end = str.find(new_line, start)) != wstring::npos) {
        lines.push_back(str.substr(start, end - start));
        start = end + 1;} // Skip the newline character
    // Add the last line (if any) after the final newline
    lines.push_back(str.substr(start));
    return lines;}

// Convert a standard string to a wide string.
inline wstring string_to_wstring(const string &str) noexcept {
    wstring_convert<codecvt_utf8_utf16<wchar_t>> converter;
    return converter.from_bytes(str);}

// Get the width of the longest string in a vector of wide strings.
inline size_t get_width_strings(vector<wstring> & str) noexcept {
  size_t length = 0;
  for (wstring s: str) {length = max(length, s.size());}
  return length;}


// General Output Utility

// Enable special characters for locale-based formatting.
inline void enable_special_characters() noexcept {
    setlocale(LC_ALL, "");}

// Output a new line to the console.
inline void nl(size_t repeat = 1) {for (size_t i = 0; i < repeat; i++){wcout << endl;} }
inline void sp(size_t repeat = 1) {for (size_t i = 0; i < repeat; i++){wcout << " ";} }
inline void flush() { wcout << flush; }
inline void write(const std::wstring & s, bool new_line = 1) noexcept {std::wcout << s; if(new_line) {nl();}}
inline void write(const std::string & s, bool new_line = 1) noexcept {write(string_to_wstring(s), new_line);}

// String Conversions

// Convert a boolean value to a wide character ('1' or '0').
inline wchar_t bool_to_wchar(const bool &value) noexcept {return value ? L'1' : L'0';}

// Split a string into tokens based on a delimiter.
// template <typename T>
// std::vector<T> split_string(const T & s, const T & delimiter) {
//     std::vector<T> tokens;
//     typename T::size_type start = 0;
//     typename T::size_type end = 0;
//     T temp = s;
//     while ((end = temp.find(delimiter, start)) != T::npos) {
//         tokens.push_back(temp.substr(start, end - start));
//         start = end + delimiter.length();}
//     tokens.push_back(temp.substr(start));
//     return tokens;}
