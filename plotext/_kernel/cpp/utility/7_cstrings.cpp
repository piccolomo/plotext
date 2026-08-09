// C-style wide string and buffer utilities (raw wchar_t* operations and append-to-buffer helpers)

// --- C-style Wide String Utilities ---

// Convert a wide string to a C-style wide string (wchar_t*)
inline wchar_t * wstring_to_cstring(const wstring & wstr) noexcept {
    wchar_t * cstr = new wchar_t[wstr.size() + 1];
    wcscpy(cstr, wstr.c_str());
    return cstr;}

// Delete a C-style wide string
inline void delete_cstring(wchar_t * cstr) noexcept {delete[] cstr;}

// Compare two wide strings knowing their length
inline bool same_cstrings(const wchar_t * code1, const wchar_t * code2, size_t length) noexcept {
    return length == 0 || memcmp(code1, code2, length * sizeof(wchar_t)) == 0;}

// Compare two null-terminated C-style wide strings
inline bool same_cstrings(const wchar_t * code1, const wchar_t * code2) noexcept {return wcscmp(code1, code2) == 0;}

// Copy a wide string knowing its length (keeps null-terminated)
inline void copy_cstring(const wchar_t * source, wchar_t * destination, size_t length) noexcept {
    if (length == 0) {destination[0] = L'\0'; return;}
    memcpy(destination, source, length * sizeof(wchar_t));
    destination[length] = L'\0';}

// Copy a null-terminated C-style wide string
inline void copy_cstring(const wchar_t * source, wchar_t * destination) noexcept {wcscpy(destination, source);}

// Copy part of a C-style wide string (from start to stop) to destination
inline void copy_part_cstring(const wchar_t * source, wchar_t * destination, const size_t & start, const size_t & stop) noexcept {
    wcsncpy(destination, source + start, stop - start);
    destination[stop - start] = L'\0';}

// Count the number of newline characters in a C-style wide string
inline size_t count_newlines(const wchar_t * str) noexcept {
    return count(str, str + wcslen(str), L'\n');}

// Debug: show wide string with indices (ANSI style)
inline void show_ansi_wstring(const wchar_t * code) {
    for (size_t i = 0; i < wcslen(code); i++) {wcout << i << space << code[i] << ansi_end << endl;}}


// --- Buffer Utilities ---

// Append a null-terminated C-style wide string to a buffer and update length
inline void cstring_to_buffer(const wchar_t * string, wchar_t * buffer, size_t & length_buffer) noexcept {
    wcscpy(buffer + length_buffer, string);
    length_buffer += wcslen(string);}

// Append a C-style wide string of known length to a buffer and update length
inline void cstring_to_buffer(const wchar_t * string, size_t string_length, wchar_t * buffer, size_t & length_buffer) noexcept {
    memcpy(buffer + length_buffer, string, string_length * sizeof(wchar_t));
    length_buffer += string_length;
    buffer[length_buffer] = L'\0';}

// Append a single wide character to a buffer and update length
inline constexpr void wchar_to_buffer(const wchar_t character, wchar_t * buffer, size_t & length_buffer) noexcept {
    buffer[length_buffer] = character;
    buffer[length_buffer + 1] = L'\0';
    length_buffer += 1;}


extern "C" {
    // Delete a wchar_t buffer produced by wstring_to_cstring
    void wstring_delete(wchar_t * wstr) noexcept { delete_cstring(wstr); }

}
