// Colorize: wide string paired with a Pixel (color + style); supports slicing, buffered rendering and printing

// A wide string with an associated Pixel used to render colored/styled text
class Colorize : public Pixel {
private:
    wchar_t * string; // Heap-allocated wide string (always null-terminated)

public:
    // Constructors
    Colorize(const size_t & length = 0, const Pixel & p = Pixel()) noexcept : Pixel(p) { create(length); }
    Colorize(const wstring & s, const Pixel & p = Pixel()) : Pixel(p) { string = wstring_to_cstring(s); }

    // Copy constructor
    Colorize(const Colorize & o) : Pixel(o) { create(o.get_length()); copy_cstring(o.string, string); }

    // Move constructor (transfer ownership; don't deallocate o's buffer)
    Colorize(Colorize && o) noexcept : Pixel(move(o)), string(o.string) { o.string = nullptr; }

    // Destructor
    ~Colorize() { destroy(); }

    // Assignment operators
    Colorize & operator=(const Colorize & o) { // Copy assignment (self-assignment safe)
        if (this != &o) {
            destroy(); create(o.get_length()); copy_cstring(o.string, string); copy_pixel(o); }
        return *this;}

    Colorize & operator=(Colorize && o) noexcept { // Move assignment (self-assignment safe, transfers ownership)
        if (this != &o) {
            destroy();
            string = o.string; o.string = nullptr;
            copy_pixel(o); }
        return *this;}

    // Equality operator
    inline bool operator==(const Colorize & c) const noexcept { return Pixel::operator==(c) && same_cstrings(c.string, string); }

    // Memory management
    inline void create(const size_t & size) noexcept { string = new wchar_t[size + 1]; wmemset(string, L'\0', size); }
    inline void destroy() noexcept { delete[] string; string = nullptr; }

    // Accessor methods
    inline wchar_t get_wcharacter(const size_t & pos) const noexcept { return string[pos]; }
    inline size_t get_length() const noexcept { return wcslen(string); }
    inline const wchar_t * get_cstring() const noexcept { return string; }
    inline wstring get_colorless_wstring() const noexcept { return wstring(string); }
    inline Pixel & get_pixel() noexcept { return *this; }

    // Return a substring as a new Colorize object
    Colorize part(const size_t & start, const size_t & stop) const noexcept {
        size_t new_length = min(stop - start, get_length());
        Colorize s(new_length, *this);
        copy_part_cstring(string, s.string, start, stop);
        return s;}
    inline Colorize part(const size_t & stop) const noexcept { return part(0, stop); }

    // Copy string and pixel to buffer
    void to_buffer(wchar_t * buffer, size_t & length_buffer, bool colorless = false) const noexcept {
        const bool add_color = !colorless && Pixel::has_color();
        const wchar_t * src = string;
        while (*src) {
            if (add_color) Pixel::to_buffer(buffer, length_buffer); // start color
            while (*src && *src != L'\n') buffer[length_buffer++] = *src++;
            if (add_color) cstring_to_buffer(ansi_end, buffer, length_buffer); // end color
            if (*src == L'\n') buffer[length_buffer++] = *src++;}
        buffer[length_buffer] = L'\0'; }

    // Return the string as wstring with optional color
    wstring get_wstring(bool colorless = false) const noexcept {
        size_t buffer_length = get_length();
        if (!(colorless || no_color())) buffer_length += (count_newlines(string) + 1) * pixel_size_max;
        wchar_t buffer[buffer_length + 1]; buffer[0] = L'\0'; size_t length = 0;
        to_buffer(buffer, length, colorless);
        return wstring(buffer);}

    // Return the string as std::string
    inline std::string get_string(bool colorless = false) const noexcept { return wstring_to_string(get_wstring(colorless)); }

    // Stream the colorized string to stdout
    inline void print(const bool colorless = false, const bool flushing = true) const noexcept {
        const bool colorfull = not colorless;
        if (colorfull) Pixel::stream();
        write_wide(get_cstring(), get_length(), false);
        if (colorfull) write_wide(ansi_end, 4, false);
        write_wide(new_line, 1, flushing);}


    inline void show() const noexcept { show_ansi_wstring(string); }

    friend wostream & operator<<(wostream & os, const Colorize & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Colorize & c) noexcept {os << c.get_string(); return os;}
};

extern "C" {

    // Create a new Colorize object from a wide string and Pixel
    Colorize * colorize_new(wchar_t * string, Pixel * p) noexcept {
        return new Colorize(string, *p); }

    // Delete a Colorize object
    void colorize_delete(Colorize * p) noexcept { delete p; }

    // Get the length of the Colorize string
    size_t colorize_get_length(Colorize * c) noexcept { return c->get_length(); }

    // Return a substring of Colorize as a new object
    Colorize * colorize_part(Colorize * c, size_t start, size_t stop) noexcept {
        return new Colorize(c->part(start, stop));}

    // Get the Colorize string as wide string (optionally colorless)
    const wchar_t * colorize_get_wstring(Colorize * c, bool colorless) noexcept {
        return wstring_to_cstring(c->get_wstring(colorless));}

    // Get a copy of the associated Pixel
    Pixel * colorize_get_pixel(Colorize * c) noexcept { return new Pixel(c->get_pixel()); }

    // Set the Pixel of a Colorize object
    void colorize_set_pixel(Colorize * c, Pixel * p) noexcept { c->copy_pixel(*p); }

    // Print the Colorize object (optionally colorless)
    void colorize_print(Colorize * c, bool colorless, bool flush) noexcept { c->print(colorless, flush); }

    // Copy a Colorize object
    Colorize * colorize_copy(Colorize * c) noexcept { return new Colorize(*c); }

    // Copy the contents of one Colorize into another
    void colorize_clone(Colorize * c, Colorize * c2) noexcept { *c = *c2; }

    // Compare two Colorize objects
    bool colorize_equals(Colorize * c, Colorize * c2) noexcept { return *c == *c2; }

    // Check if Background of Colorize is not set
    bool colorize_no_background(Colorize * c) noexcept { return c->no_background(); }

    // Copy Background from a Pixel into Colorize
    void colorize_copy_background(Colorize * c, Pixel * p) noexcept { c->copy_background(*p); }

    // Fix Background of Colorize using a Pixel if not set
    void colorize_fix_background(Colorize * c, Pixel * p) noexcept { c->fix_background(*p); }
    void colorize_fix(Colorize * c, Pixel * p) noexcept { c->fix(*p); }

}
