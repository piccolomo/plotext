class Colorize : public Pixel {
private:
    wchar_t * string;

public:
    Colorize(const size_t & length = 0, const Pixel & p = Pixel()) noexcept : Pixel(p) {create(length); }
    Colorize(const wstring & s, const Pixel & p = Pixel()) noexcept : Pixel(p) {string = wstring_to_cstring(s);}

    Colorize(const Colorize & o) noexcept : Pixel(o) {create(o.get_length()); copy_cstring(o.string, string);}
    Colorize(Colorize && o) noexcept : Pixel(move(o)), string(o.string) {o.destroy();}
    ~Colorize() {destroy();}

    Colorize & operator=(const Colorize & o) {destroy(); create(o.get_length()); copy_cstring(o.string, string); copy_pixel(o); return *this;}
    Colorize & operator=(Colorize && o) noexcept {destroy(); string = o.string; o.destroy(); copy_pixel(o); return *this;}
	inline bool operator==(const Colorize & c) noexcept {return Pixel::operator==(c) and same_cstrings(c.string, string);}

    inline void create(const size_t & size) noexcept {string = new wchar_t[size + 1]; wmemset(string, L'\0', size);}
    inline void destroy() noexcept {delete[] string; string = nullptr;}

    //inline void set_string(const wstring & s) {}

    // inline void set_char(const size_t & pos, wchar_t c) noexcept {string[pos] = c;}
    inline wchar_t get_char(const size_t & pos) const noexcept {return string[pos];}

	inline size_t get_length() const {return wcslen(string);}
	const wchar_t * get_cstring() const noexcept {return string;}
	inline wstring get_string() const {return wstring(string);}
	inline Pixel & get_pixel() {return *this;}
	//nline void set_pixel(const Pixel & p) noexcept {copy_pixel(p);}

	inline Colorize part(const size_t & start, const size_t & stop) const noexcept {size_t new_length = min(stop - start, get_length());
        Colorize s(new_length, *this); copy_part_cstring(string, s.string, start, stop); return s;}
	inline Colorize part(const size_t & stop) const noexcept {return part(0, stop);}

	virtual inline void to_buffer(wchar_t * buffer, size_t & length_buffer, const bool & colorless = false) const noexcept {
		vector<wstring> wstrings = split_string(get_string(), wstring(new_line));
		size_t height = wstrings.size();
		bool add_color = not (colorless or no_color());
		for (size_t row = 0; row < height; row++) {
			if (add_color) {Pixel::to_buffer(buffer, length_buffer);}
			cstring_to_buffer(wstrings.at(row).c_str(), buffer, length_buffer);
			if (add_color) {cstring_to_buffer(ansi_end, buffer, length_buffer);}
			if (row != height - 1) {cstring_to_buffer(new_line, buffer, length_buffer);}}}

	inline wstring get_wstring(const bool & colorless = false) const noexcept {
		size_t buffer_length = get_length(); if (not (colorless or no_color())) {buffer_length += (count_newlines(string) + 1) * pixel_size_max;}
		wchar_t buffer[buffer_length + 1]; buffer[0] = '\0'; size_t length = 0;
		to_buffer(buffer, length, colorless);
		wstring out(buffer);
		return out;}

	inline void show(const bool & colorless = false) const noexcept {wcout << get_wstring(colorless) << flush;}
};

	// inline wstring get_wstring(const bool & colorless = false) const noexcept {
	//     size_t buffer_size = character_size_max * get_width() * height + height;
	//     wchar_t buffer[buffer_size + 1]; buffer[0] = '\0'; size_t length = 0;
	//     to_buffer(buffer, length, colorless);
	//     wstring out(buffer);
	//     return out;}

 	//  inline void show(const bool & colorless = false) const noexcept {wcout << get_wstring(colorless) << endl;}
