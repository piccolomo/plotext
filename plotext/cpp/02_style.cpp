// Style class for managing multiple text styles (e.g., bold, underlined).


class Style {
private:
  wchar_t code[19]; // Buffer to store the style code.
  size_t length;

public:
  // Default constructor: Clears the style code.
  constexpr Style() noexcept : code{L'\0'}, length(0) {}

  // Constructor that sets the style based on a string.
  Style(const string & style) {clear(); set(style);}

  // Copy constructor (defaulted).
  Style(const Style & st) = default;

  // Move constructor (defaulted).
  Style(Style && st) = default;

  // Equality operator: Compares style codes for equality.
  bool operator==(const Style& st) const {return length == st.length and same_cstrings(code, st.get_code(), length);}

  // Assignment operator: Copies the style code from another Style object.
  Style & operator=(const Style& st) {
    length = st.length;
    copy_cstring(st.get_code(), code, length);
    return *this;} 

  // Clears the style code.
  void clear() {code[0] = L'\0'; length = 0;}

  // Sets the style based on a string (e.g., "bold", "underline").
  inline void set(const string & style) {

    // Split the input style string into individual styles (e.g., "bold underline").
    vector<string> styles = split_string(style);
    vector<unsigned char> style_codes; 
    style_codes.reserve(styles.size());

     for (const string & style : styles) {
        unsigned char style_code = get_style_code(style); // Get the ANSI code for the style.
        if (style_code != 100){style_codes.push_back(style_code);}} 

    // If there are any styles, start the ANSI escape code sequence.
    if (style_codes.size() != 0) {wcscpy(code, ansi_start);} // Initialize with the ANSI escape start sequence.
    
    // Iterate through the styles and append the corresponding style code to the buffer.
    for (const unsigned char & style_code : style_codes) {swprintf(code + wcslen(code), 3, L"%d;", style_code);} // Append the code with a semicolon.
    
    // If any styles were added, finalize the ANSI escape sequence by replacing the last semicolon with 'm'.
    if (style_codes.size() != 0) {
        size_t len = wcslen(code);   // Find the length of the current code.
        code[len - 1] = L'm';        // Replace the last char with 'm'.
        code[len] = L'\0'; } // Null-terminate the string.

    length = wcslen(code);}

  // Returns the length of the style code.
  size_t get_length() const {return length;}

  // Returns the current style code.
  const wchar_t * get_code() const {return code;}

  void show_code() const {show_ansi_wstring(get_code());}

  // Checks if no style is set (empty code).
  bool no_style() const {return length == 0;}
  bool has_style() const { return length != 0; }

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
      if (has_style()) {  // only copy if style is set
          cstring_to_buffer(code, length, buffer, length_buffer);}}
        
  // Logs the current style code.
  void log() const {wcout << code << L"style" << ansi_end << endl;}

  inline void stream() const {wcout.write(code, length);} 

};



