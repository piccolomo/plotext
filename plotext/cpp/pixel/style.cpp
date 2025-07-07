// Style class for managing multiple text styles (e.g., bold, underlined).


class Style {
private:
  wchar_t code[19]; // Buffer to store the style code.

public:
  // Default constructor: Clears the style code.
  Style() {clear();}

  // Constructor that sets the style based on a string.
  Style(const string & style) {clear(); set(style);}

  // Copy constructor (defaulted).
  Style(const Style & st) = default;

  // Move constructor (defaulted).
  Style(Style && st) = default;

  // Equality operator: Compares style codes for equality.
  bool operator==(const Style& st) const {return same_cstrings(code, st.get_code());}

  // Assignment operator: Copies the style code from another Style object.
  Style & operator=(const Style& st) {
    copy_cstring(st.get_code(), code);
    return *this;}

  // Clears the style code.
  void clear() {code[0] = L'\0';}

  // Sets the style based on a string (e.g., "bold", "underline").
  void set(const string & style) {

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
  }   

  // Returns the length of the style code.
  size_t get_length() const {return wcslen(code);}

  // Returns the current style code.
  const wchar_t * get_code() const {return code;}

  void show_code() const {show_ansi_wstring(get_code());}

  // Checks if no style is set (empty code).
  bool no_style() const {return code[0] == L'\0';}

  // Converts the style code to a buffer for terminal output.
  void to_buffer(wchar_t * buffer, size_t & length_buffer) const {
    if (!no_style()) {cstring_to_buffer(code, buffer, length_buffer);}}

  // Logs the current style code.
  void log() const {wcout << code << L"style" << ansi_end << endl;}
};



