class Style {
private:
  wchar_t code [19];

public:
  inline Style() noexcept {clear();};
  inline Style(const string style) noexcept {clear(); set(style);}
  
  inline constexpr Style(const Style & st) noexcept = default;
  inline constexpr Style(Style && st) noexcept = default;

  inline bool operator==(const Style & st) const noexcept {return same_cstrings(code, st.get_code());}
  inline Style & operator=(const Style & st) noexcept {copy_cstring(st.get_code(), code); return *this;}
  
  inline constexpr void clear() noexcept {code[0] = L'\0';}
  inline void set(const string style) noexcept {add_style_code(code, style);}

  inline const size_t get_length() const noexcept {return wcslen(code);}
  inline constexpr const wchar_t * get_code() const noexcept {return code;}
  inline constexpr bool no_style() const noexcept {return code[0] == L'\0';}

  inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {if(not no_style()) {cstring_to_buffer(code, buffer, length_buffer);}}
  inline void log() const noexcept {wcout << code << L"style" << ansi_end << endl;}
};
