// Colorize class: Manages a colorized string with associated Pixel

class Colorize : public Pixel {
private:
    wchar_t * string; // Holds the string of characters

public:
    // Constructors
    Colorize(const size_t & length = 0, const Pixel & p = Pixel()) : Pixel(p) {create(length);}
    Colorize(const wstring & s, const Pixel & p = Pixel()) : Pixel(p) {string = wstring_to_cstring(s);}

    // Copy and Move constructors
    Colorize(const Colorize & o) : Pixel(o) {create(o.get_length()); copy_cstring(o.string, string);}
    Colorize(Colorize && o) noexcept : Pixel(move(o)), string(o.string) {o.destroy();}

    // Destructor
    ~Colorize() {destroy();}

    // Assignment operators
    Colorize& operator=(const Colorize & o) {
        destroy(); create(o.get_length()); copy_cstring(o.string, string); copy_pixel(o); return *this;}

    Colorize& operator=(Colorize&& o) noexcept {
        destroy(); string = o.string; o.destroy(); copy_pixel(o); return *this;}

    // Equality operator
    bool operator==(const Colorize& c) const noexcept {
        return Pixel::operator==(c) && same_cstrings(c.string, string);}

    // Memory management for the string
    void create(const size_t& size) noexcept {
        string = new wchar_t[size + 1]; wmemset(string, L'\0', size);}

    void destroy() noexcept {
        delete[] string; string = nullptr;}

    // Accessor methods
    wchar_t get_wcharacter(const size_t& pos) const noexcept {return string[pos];}
    size_t get_length() const {return wcslen(string);}
    const wchar_t* get_cstring() const noexcept {return string;}
    wstring get_string() const {return wstring(string);}
    Pixel & get_pixel() {return *this;}

    // Returns a part of the Colorize object
    Colorize part(const size_t & start, const size_t & stop) const noexcept {
        size_t new_length = min(stop - start, get_length());
        Colorize s(new_length, *this); copy_part_cstring(string, s.string, start, stop);
        return s;}

    Colorize part(const size_t & stop) const noexcept {return part(0, stop);}

    // Convert the object to a buffer (useful for displaying the string with color)
    void to_buffer(wchar_t * buffer, size_t & length_buffer, const bool & colorless = false) const noexcept {
        vector<wstring> wstrings = split_wstring(get_string());
        size_t height = wstrings.size();
        bool add_color = !(colorless || no_color());
        for (size_t row = 0; row < height; row++) {
            if (add_color) { Pixel::to_buffer(buffer, length_buffer); }
            cstring_to_buffer(wstrings.at(row).c_str(), buffer, length_buffer);
            if (add_color) { cstring_to_buffer(ansi_end, buffer, length_buffer); }
            if (row != height - 1) { cstring_to_buffer(new_line, buffer, length_buffer);}}}

    // Return the string as a wstring with optional color stripping
    wstring get_wstring(const bool& colorless = false) const noexcept {
        size_t buffer_length = get_length();
        if (!(colorless || no_color())) {
            buffer_length += (count_newlines(string) + 1) * pixel_size_max;}
        wchar_t buffer[buffer_length + 1]; buffer[0] = '\0'; size_t length = 0;
        to_buffer(buffer, length, colorless);
        return wstring(buffer);}

    // Display the Colorize object to standard output
    void print(const bool& colorless = false) const noexcept {
        wcout << get_wstring(colorless) << flush;}
};

extern "C" {
    Colorize * colorize_new(wchar_t * string, Pixel * p) noexcept {return new Colorize(string, *p);}
    void colorize_delete(Colorize * p) noexcept {delete p;}
    size_t colorize_get_length(Colorize * c) noexcept {return c->get_length();}
    Colorize * colorize_part(Colorize * m, size_t start, size_t stop) noexcept {return new Colorize(m->part(start, stop));}
    const wchar_t * colorize_get_wstring(Colorize * c, bool colorless) noexcept {return wstring_to_cstring(c->get_wstring(colorless));}
    Pixel * colorize_get_pixel(Colorize * c) noexcept {return new Pixel(c->get_pixel());}
    void colorize_set_pixel(Colorize * c, Pixel * p) noexcept {c->copy_pixel(*p);}
    void colorize_print(Colorize * c, bool colorless) noexcept {c->print(colorless);}
    Colorize * colorize_copy(Colorize * c) noexcept {return new Colorize(*c);}
    void colorize_copy_from(Colorize * c, Colorize * c2) noexcept {*c = *c2;}
    bool colorize_equals(Colorize * c, Colorize * c2) noexcept {return *c == *c2;}
    bool colorize_no_background(Colorize * p) noexcept {return p->no_background();}
    void colorize_copy_background(Colorize * p, Pixel * p2) noexcept {p->copy_background(*p2);}
    void colorize_fix_background(Colorize * p, Pixel * p2) noexcept {p->fix_background(*p2);}
    //void colorize_fix(Colorize * p, Pixel * pixel) noexcept {p->fix(*pixel);}

}