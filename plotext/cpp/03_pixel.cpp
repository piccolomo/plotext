// Pixel class: Combines Fullground, Background, and Style for colored/styled pixels.

class Pixel : public Fullground, public Background, public Style {

public:
    // Constructors
    constexpr Pixel() = default; // Default constructor
    Pixel(const Fullground & fg, const Background & bg = Background(), const Style & st = Style()) noexcept 
        : Fullground(fg), Background(bg), Style(st) {} // With objects
    Pixel(const string & fg, const string & bg = "", const string & st = "") noexcept 
        : Fullground(fg), Background(bg), Style(st) {} // With strings

    // Copy / Move constructors
    constexpr Pixel(const Pixel & p) noexcept : Fullground(p), Background(p), Style(p) {}
    Pixel(Pixel && p) noexcept : Fullground(move(p)), Background(move(p)), Style(move(p)) {}

    // Assignment operator
    inline Pixel & operator=(const Pixel & p) noexcept {
        Fullground::operator=(p); Background::operator=(p); Style::operator=(p);
        return *this;}

    // Equality / Inequality
    constexpr inline bool operator==(const Pixel & p) const noexcept {return Fullground::operator==(p) && Background::operator==(p) && Style::operator==(p);}
    inline bool operator!=(const Pixel & p) const noexcept {return !(*this == p);}

    // Clear all properties
    inline void clear() noexcept { Fullground::clear(); Background::clear(); Style::clear(); }

    // Setters
    inline void set_fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept { Fullground::set(r, g, b); }
    inline void set_fullground(const unsigned char & r) noexcept { Fullground::set(r); }
    inline void set_fullground(const string & color) noexcept { Fullground::set(color); }

    inline void set_background(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept { Background::set(r, g, b); }
    inline void set_background(const unsigned char & r) noexcept { Background::set(r); }
    inline void set_background(const string & color) noexcept { Background::set(color); }

    inline void set_style(const string & style) noexcept { Style::set(style); }

    inline void set(const string & fs, const string & bs = "", const string & ss = "") noexcept {
        Fullground::set(fs); Background::set(bs); Style::set(ss);}

    // Copy / fix methods
    inline void copy_pixel(const Pixel & p) noexcept { *this = p; }
    inline void copy_fullground(const Pixel & p) noexcept { Fullground::operator=(p); }
    inline void copy_background(const Pixel & p) noexcept { Background::operator=(p); }
    inline void fix_background(const Pixel & pixel) noexcept { if (no_background()) copy_background(pixel); }
    inline void fix_fullground(const Pixel & pixel) noexcept { if (no_fullground()) copy_fullground(pixel); }
    inline void fix(const Pixel & pixel) noexcept { fix_background(pixel); fix_fullground(pixel); }

    // Checks
    inline bool no_fullground() const noexcept { return Fullground::no_color(); }
    inline bool no_background() const noexcept { return Background::no_color(); }
    inline bool no_style() const noexcept { return Style::no_style(); }
    inline bool no_color() const noexcept { return no_fullground() && no_background() && no_style(); }
    inline bool has_color() const noexcept { return !no_color(); }

    // Length / codes
    inline size_t get_length() const noexcept { return Fullground::get_length() + Background::get_length() + Style::get_length(); }
    inline const unsigned char get_fullground_integer_code() const noexcept { return Fullground::get_integer_code(); }

    // Buffer operations
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        Fullground::to_buffer(buffer, length_buffer);
        Background::to_buffer(buffer, length_buffer);
        Style::to_buffer(buffer, length_buffer);}

    // Get combined ANSI code
    inline const wchar_t * get_code() const {
        wchar_t * buffer = new wchar_t[pixel_size_max + 1]; buffer[0] = L'\0'; size_t len = 0;
        to_buffer(buffer, len); return buffer;}

    // Get Pixel as wide string
    inline wstring get_wstring() const {
        wchar_t buffer[character_size_max + 5] = {L'\0'}; size_t len = 0;
        to_buffer(buffer, len);
        cstring_to_buffer(L"Pixel", buffer, len);
        if (has_color()) cstring_to_buffer(ansi_end, buffer, len);
        return wstring(buffer);}

    // Get Pixel as string
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Print / show
    inline void log() const noexcept { wcout << get_wstring() << endl; }
    inline void show() const noexcept { Fullground::show(); Background::show(); Style::show(); }

    inline void stream() const noexcept { Fullground::stream(); Background::stream(); Style::stream(); }

    friend wostream & operator<<(wostream & os, const Pixel & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Pixel & c) noexcept {os << c.get_string(); return os;}

};


extern "C" {

    // Create / delete Pixel
    Pixel * pixel_new() noexcept { return new Pixel(); }
    void pixel_delete(Pixel * p) noexcept { delete p; }

    // Set Fullground color
    void pixel_set_fullground_integer(Pixel * p, size_t r) noexcept { p->set_fullground(static_cast<unsigned char>(r)); }
    void pixel_set_fullground_rgb(Pixel * p, size_t r, size_t g, size_t b) noexcept { 
        p->set_fullground(static_cast<unsigned char>(r), static_cast<unsigned char>(g), static_cast<unsigned char>(b));}
    void pixel_set_fullground_code(Pixel * p, const char * code) noexcept { 
        p->set_fullground(string(code)); }

    // Set Background color
    void pixel_set_background_integer(Pixel * p, size_t r) noexcept { p->set_background(static_cast<unsigned char>(r)); }
    void pixel_set_background_rgb(Pixel * p, size_t r, size_t g, size_t b) noexcept { 
        p->set_background(static_cast<unsigned char>(r), static_cast<unsigned char>(g), static_cast<unsigned char>(b)); }
    void pixel_set_background_code(Pixel * p, const char * code) noexcept {p->set_background(string(code));}

    // Style operations
    void pixel_set_style_code(Pixel * p, const char * code) noexcept { p->set_style(string(code)); }

    // Copy / fix operations
    void pixel_copy_pixel(Pixel * dest, const Pixel * src) noexcept { dest->copy_pixel(*src); }
    void pixel_copy_background(Pixel * dest, const Pixel * src) noexcept { dest->copy_background(*src); }
    void pixel_fix(Pixel * dest, const Pixel * src) noexcept { dest->fix(*src); }
    void pixel_fix_background(Pixel * dest, const Pixel * src) noexcept { dest->fix_background(*src); }

    // Queries
    bool pixel_no_background(const Pixel * p) noexcept { return p->no_background(); }
    unsigned char pixel_get_code(const Pixel * p) noexcept { return p->get_fullground_integer_code(); }

    // Output
    void pixel_log(const Pixel * p) noexcept { p->log(); }
    const wchar_t * pixel_get_wstring(const Pixel * p) noexcept { 
        return wstring_to_cstring(p->get_wstring()); }

    // Copy constructor
    Pixel * pixel_copy(const Pixel * p) noexcept { return new Pixel(*p); }

}
