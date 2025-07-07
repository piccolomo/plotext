//C Strings

// Convert a wide string to a C-style wide string (wchar_t*)
inline wchar_t * wstring_to_cstring(const wstring & wstr) noexcept {
    wchar_t *cstr = new wchar_t[wstr.size() + 1];
    wcscpy(cstr, wstr.c_str());
    return cstr;}

// Delete a C-style wide string
inline void delete_cstring(wchar_t *cstr) noexcept {
    delete[] cstr;}

// Compare two C-style wide strings.
inline bool same_cstrings(const wchar_t * code1, const wchar_t * code2) noexcept {
    return wcscmp(code1, code2) == 0;}

// Copy a C-style wide string to another C-style wide string.
inline void copy_cstring(const wchar_t * source, wchar_t * destination) noexcept {
    wcscpy(destination, source);}

// Copy part of a C-style wide string to another C-style wide string.
inline void copy_part_cstring(const wchar_t *source, wchar_t *destination, const size_t &start, const size_t &stop) noexcept {
    wcsncpy(destination, source + start, stop - start);
    destination[stop - start] = L'\0';}

// Count the number of newlines in a C-style wide string.
inline size_t count_newlines(const wchar_t * str) noexcept {
    return count(str, str + std::wcslen(str), L'\n');}

inline void show_ansi_wstring(const wchar_t * code){for (size_t i = 0; i < wcslen(code); i++){wcout << i << space <<code[i] << ansi_end << endl;}}

//Buffer

// Append a C-style wide string to a buffer and update the buffer length.
inline void cstring_to_buffer(const wchar_t * string, wchar_t * buffer, size_t &length_buffer) noexcept {
    wcscpy(buffer + length_buffer, string);
    length_buffer += wcslen(string);}

// Append a wide character to a buffer and update the buffer length.
inline constexpr void wchar_to_buffer(const wchar_t character, wchar_t *buffer, size_t &length_buffer) noexcept {
    buffer[length_buffer] = character;
    buffer[length_buffer + 1] = L'\0';
    length_buffer += 1;}
