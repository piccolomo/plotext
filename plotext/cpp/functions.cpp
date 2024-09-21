// String, Char Manipulation

template <typename T>
std::vector<T> split_string(const T& s, const T& delimiter) {
    std::vector<T> tokens;
    typename T::size_type start = 0;
    typename T::size_type end = 0;
    T temp = s;
    while ((end = temp.find(delimiter, start)) != T::npos) {
        tokens.push_back(temp.substr(start, end - start));
        start = end + delimiter.length();}
    tokens.push_back(temp.substr(start));
    return tokens;}

inline size_t get_width_strings(vector<wstring> & str) noexcept {
  size_t length = 0;
  for (wstring s: str) {length = max(length, s.size());}
  for (wstring s: str) {}
  return length;}

inline wstring string_to_wstring(const string & str) noexcept {wstring_convert<codecvt_utf8_utf16<wchar_t>> converter; return converter.from_bytes(str);}

inline wstring str_round(const float & number, const size_t & precision) noexcept {wstringstream wss; wss << std::fixed << std::setprecision(precision) << number; return wss.str();}

inline wchar_t bool_to_wchar(const bool & value) noexcept {return value ? L'1' : L'0';}

inline void enable_special_characters() noexcept {setlocale(LC_ALL, "");}

inline void nl() {wcout << endl;}

inline wchar_t * wstring_to_cstring(const wstring & wstr) noexcept {wchar_t * cstr = new wchar_t[wstr.size() + 1]; wcscpy(cstr, wstr.c_str()); return cstr;}

inline void delete_cstring(wchar_t * cstr) noexcept {delete[] cstr;}

// Cstrings

inline bool same_cstrings(const wchar_t * code1, const wchar_t * code2) noexcept {return wcscmp(code1, code2) == 0;}

inline void copy_cstring(const wchar_t * source, wchar_t * destination) noexcept {wcscpy(destination, source);}

inline void copy_part_cstring(const wchar_t * source, wchar_t * destination, const size_t & start,  const size_t & stop) noexcept {wcsncpy(destination, source + start, stop - start); destination[stop - start] = L'\0';}


// String Buffer
inline void cstring_to_buffer(const wchar_t * string, wchar_t * buffer, size_t & length_buffer) noexcept {wcscpy(buffer + length_buffer, string); length_buffer += wcslen(string);}

inline constexpr void wchar_to_buffer(const wchar_t character, wchar_t * buffer, size_t & length_buffer) noexcept {
    buffer[length_buffer] = character;
    buffer[length_buffer + 1] = L'\0';
    length_buffer += 1;}

//inline size_t count_newlines(const wstring & str) {return count(str.begin(), str.end(), L'\n');}
inline size_t count_newlines(const wchar_t* str) {return count(str, str + std::wcslen(str), L'\n');}
// Color

inline void add_color_integer_ansi(wchar_t * buffer, const unsigned char & r) {
  swprintf(buffer, 7, L"5;%dm", r);}

inline void add_color_rgb_ansi(wchar_t * buffer, const unsigned char & r, const unsigned char & g, const unsigned char & b) {
  swprintf(buffer, 16, L"2;%d;%d;%dm", r, g, b); }

inline void add_color_ansi(wchar_t * buffer, const bool & is_fullground, const bool & is_integer, const unsigned char & r = 0, const unsigned char & g = 0, const unsigned char & b = 0) {
  if (is_fullground) {wcscpy(buffer, ansi_fullground);} else {wcscpy(buffer, ansi_background);}
  if (is_integer) {add_color_integer_ansi(buffer + 5, r);} else {add_color_rgb_ansi(buffer + 5, r, g, b);}}

inline void add_color_code(wchar_t * buffer, const bool & is_fullground, const string & color){
  unsigned char code = get_color_code(color);
  if (code == 100){buffer[0] = L'\0';} else {add_color_ansi(buffer, is_fullground, true, code);}}


// Style

inline vector<size_t> get_style_codes(const string & style){
  vector<size_t> codes;
  vector<string> styles = split_string(style, string(" "));
  for(const string & style : styles) {
    unsigned char code = get_style_code(style);
    if (code != 100){codes.push_back(code);}} return codes;}

inline void add_style_code(wchar_t * buffer, const string & style){
  vector<size_t> codes = get_style_codes(style);
  if(codes.size() != 0){wcscpy(buffer, ansi_start);}
  for(const size_t & code : codes) {swprintf(buffer + wcslen(buffer), 3, L"%d;", code);}
  if(codes.size() != 0){
    size_t len = wcslen(buffer);
    buffer[len - 1] = L'm';
    buffer[len] = L'\0';}}


// Bit Manipulation
inline constexpr bool get_bit(const size_t & number, const size_t & position) noexcept {return (number >> position) & 1;}
inline constexpr size_t get_bit_position(const size_t & col, const size_t & row, const size_t & cols, const size_t & rows) noexcept {return cols * (rows - row) - 1 - col;}


// Data Modification
const float delta = pow(10, -4);
inline float rescale(const float & el, const pair<float, float> & lim, const size_t & bins) noexcept {return delta + (bins - 2 * delta) * (el - lim.first) / (lim.second - lim.first);}

inline vector<int> sort(const vector<int> & unsorted, const int & reference) noexcept {
   vector<int> sorted = unsorted;
   auto comparator = [reference](int a, int b) {return abs(a - reference) < abs(b - reference);};
   sort(sorted.begin(), sorted.end(), comparator);
   return sorted;}


// Data Creation
template<typename T>
inline vector<T> range(const T & start, const T & stop, const T & delta = 1) noexcept {
	size_t size = (stop - start) / delta;
	vector<T> out; if (size <= 0 or delta == 0) {return out;} 
	out.reserve(size + 1); 
	int sign = delta > 0 ? 1 : -1;
	T value = start; while ((stop - value) * sign > pow(10, -5)) {out.push_back(value); value += delta;} return out;}
	
//inline vector<int> range(const int & stop) noexcept {return range(0, stop, 1);}

inline vector<float> sin(size_t periods = 2, size_t length = 200, float amplitude = 1, float phase = 0, float decay = 0, float delta = 1) noexcept {
    float f = 2 * M_PI * periods / (length - 1);
    phase *= M_PI;
    float d = decay / length;
    vector<float> result; result.reserve(length);
    for (int el = 0; el < length; el = el + delta) {result.push_back(amplitude * sin(f * el + phase) * exp(-d * el));}
    return result;};
	
	
//inline float round_up(const float & value, const size_t & precision) noexcept {float factor = pow(10.0, precision); return round(value * factor) / factor;}
//inline size_t to_size_t(const float & value) noexcept {return static_cast<size_t>(value);}



//inline float rescale(const float & el, const pair<float, float> & lim, const size_t & bins) noexcept {return 0.5 + delta + (bins - 1 - 2 * delta) * (el - lim.first) / (lim.second - lim.first);}

//inline wstring bool_to_wstring(const bool & value) noexcept {return value ? L"1" : L"0";}

// 
