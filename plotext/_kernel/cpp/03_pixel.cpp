// Pixel: composite of Fullground, Background and Style used as the color/style carrier throughout the kernel

// Colored and styled pixel (multiply inherits from Fullground, Background and Style)
class Pixel : public Fullground, public Background, public Style {

public:
    // Default constructor
    constexpr Pixel() = default;

    // Construct from three style components
    Pixel(const Fullground & fg, const Background & bg = Background(), const Style & st = Style()) noexcept
        : Fullground(fg), Background(bg), Style(st) {}

    // Construct from three strings
    Pixel(const string & fg, const string & bg = "", const string & st = "") noexcept : Fullground(fg), Background(bg), Style(st) {}

    // Copy constructor
    constexpr Pixel(const Pixel & p) noexcept : Fullground(p), Background(p), Style(p) {}

    // Move constructor
    Pixel(Pixel && p) noexcept : Fullground(move(p)), Background(move(p)), Style(move(p)) {}

    // Virtual destructor for safe polymorphic deletion
    virtual ~Pixel() noexcept {}

    // Copy assignment (self-assignment safe)
    inline Pixel & operator=(const Pixel & p) noexcept {
        if (this != &p) {
            Fullground::operator=(p); Background::operator=(p); Style::operator=(p); }
        return *this;}

    // Equality comparison
    constexpr inline bool operator==(const Pixel & p) const noexcept {return Fullground::operator==(p) && Background::operator==(p) && Style::operator==(p);}

    // Inequality comparison
    inline bool operator!=(const Pixel & p) const noexcept {return !(*this == p);}

    // Clear all properties (color and style)
    inline void clear() noexcept { Fullground::clear(); Background::clear(); Style::clear(); }

    // Set RGB foreground color
    inline void set_fullground(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept { Fullground::set(r, g, b); }

    // Set foreground palette index
    inline void set_fullground(const unsigned char & r) noexcept { Fullground::set(r); }

    // Set foreground by name
    inline void set_fullground(const string & color) noexcept { Fullground::set(color); }

    // Set RGB background color
    inline void set_background(const unsigned char & r, const unsigned char & g, const unsigned char & b) noexcept { Background::set(r, g, b); }

    // Set background palette index
    inline void set_background(const unsigned char & r) noexcept { Background::set(r); }

    // Set background by name
    inline void set_background(const string & color) noexcept { Background::set(color); }

    // Set style from space-separated string
    inline void set_style(const string & style) noexcept { Style::set(style); }

    // Set all three properties from strings
    inline void set(const string & fs, const string & bs = "", const string & ss = "") noexcept {
        Fullground::set(fs); Background::set(bs); Style::set(ss);}

    // Copy another pixel's properties
    inline void copy_pixel(const Pixel & p) noexcept { *this = p; }

    // Copy only the foreground
    inline void copy_fullground(const Pixel & p) noexcept { Fullground::operator=(p); }

    // Copy only the background
    inline void copy_background(const Pixel & p) noexcept { Background::operator=(p); }

    // Copy only the style
    inline void copy_style(const Pixel & p) noexcept { Style::operator=(p); }

    // Swap fg and bg, patching each side's "3"/"4" prefix byte so the result remains a valid pixel for any colour representation.
    inline void swap() noexcept {
        Pixel saved = *this;
        Fullground::copy(static_cast<const Background&>(saved)); if (Fullground::length > 2) Fullground::code[2] = L'3';
        Background::copy(static_cast<const Fullground&>(saved)); if (Background::length > 2) Background::code[2] = L'4'; }

    // Apply another pixel's background only if this pixel has none
    inline void fix_background(const Pixel & pixel) noexcept { if (no_background()) copy_background(pixel); }

    // Apply another pixel's foreground only if this pixel has none
    inline void fix_fullground(const Pixel & pixel) noexcept { if (no_fullground()) copy_fullground(pixel); }

    // Apply another pixel's style only if this pixel has none
    inline void fix_style(const Pixel & pixel) noexcept { if (no_style()) copy_style(pixel); }

    // Fix foreground, background and style against another pixel, each taken only where this pixel has none
    inline void fix(const Pixel & pixel) noexcept { fix_background(pixel); fix_fullground(pixel); fix_style(pixel); }

    // True if no foreground is set
    inline bool no_fullground() const noexcept { return Fullground::no_color(); }

    // True if no background is set
    inline bool no_background() const noexcept { return Background::no_color(); }

    // True if no style is set
    inline bool no_style() const noexcept { return Style::no_style(); }

    // True if nothing is set (no color and no style)
    inline bool no_color() const noexcept { return no_fullground() && no_background() && no_style(); }

    // True if any color or style is set
    inline bool has_color() const noexcept { return !no_color(); }

    // Total ANSI code length (sum of the three components)
    inline size_t get_length() const noexcept { return Fullground::get_length() + Background::get_length() + Style::get_length(); }

    // Append the combined ANSI code (foreground + background + style) to a buffer
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        Fullground::to_buffer(buffer, length_buffer);
        Background::to_buffer(buffer, length_buffer);
        Style::to_buffer(buffer, length_buffer);}

    // Append the combined CSS body (foreground + background + style) to a buffer
    inline void html_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        Fullground::html_to_buffer(buffer, length_buffer);
        Background::html_to_buffer(buffer, length_buffer);
        Style::html_to_buffer(buffer, length_buffer); }

    // Get the combined CSS body as a wstring
    inline wstring get_html() const {
        wchar_t buffer[512] = {L'\0'}; size_t len = 0;
        html_to_buffer(buffer, len);
        return wstring(buffer, len); }

    // Get combined ANSI code (caller owns the returned heap buffer, prefer get_wstring)
    inline const wchar_t * get_code() const {
        wchar_t * buffer = new wchar_t[pixel_size_max + 1]; buffer[0] = L'\0'; size_t len = 0;
        to_buffer(buffer, len); return buffer;}

    // Get Pixel as wide string (pixel code + "PlotextPixel()" label + reset)
    inline wstring get_wstring() const {
        wchar_t buffer[character_size_max + 14] = {L'\0'}; size_t len = 0;
        to_buffer(buffer, len);
        cstring_to_buffer(L"PlotextPixel()", buffer, len);
        if (has_color()) cstring_to_buffer(ansi_end, buffer, len);
        return wstring(buffer);}

    // Get Pixel as narrow string
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout
    inline void log() const noexcept { wcout << get_wstring() << endl; }

    // Show the three ANSI codes with indices
    inline void show() const noexcept { Fullground::show(); Background::show(); Style::show(); }

    // Stream the three ANSI codes to wcout
    inline void stream() const noexcept { Fullground::stream(); Background::stream(); Style::stream(); }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Pixel & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Pixel & c) noexcept {os << c.get_string(); return os;}
};


extern "C" {

    // Create a new Pixel
    Pixel * pixel_new() noexcept { return new Pixel(); }

    // Delete a Pixel
    void pixel_delete(Pixel * p) noexcept { delete p; }

    // Clear the pixel's color and style
    void pixel_clear(Pixel * p) noexcept {p->clear(); }

    // Set foreground to a palette index
    void pixel_set_fullground_integer(Pixel * p, size_t r) noexcept { p->set_fullground(static_cast<unsigned char>(r)); }

    // Set foreground to an RGB triplet
    void pixel_set_fullground_rgb(Pixel * p, size_t r, size_t g, size_t b) noexcept {
        p->set_fullground(static_cast<unsigned char>(r), static_cast<unsigned char>(g), static_cast<unsigned char>(b));}

    // Set foreground by name
    void pixel_set_fullground_code(Pixel * p, const char * code) noexcept {
        p->set_fullground(string(code)); }

    // Set background to a palette index
    void pixel_set_background_integer(Pixel * p, size_t r) noexcept { p->set_background(static_cast<unsigned char>(r)); }

    // Set background to an RGB triplet
    void pixel_set_background_rgb(Pixel * p, size_t r, size_t g, size_t b) noexcept {
        p->set_background(static_cast<unsigned char>(r), static_cast<unsigned char>(g), static_cast<unsigned char>(b)); }

    // Set background by name
    void pixel_set_background_code(Pixel * p, const char * code) noexcept {p->set_background(string(code));}

    // Set style from space-separated string
    void pixel_set_style_code(Pixel * p, const char * code) noexcept { p->set_style(string(code)); }

    // Copy all properties from src into dest
    void pixel_clone(Pixel * dest, const Pixel * src) noexcept { dest->copy_pixel(*src); }

    // Copy only the background from src into dest
    void pixel_copy_background(Pixel * dest, const Pixel * src) noexcept { dest->copy_background(*src); }

    // Copy only the foreground from src into dest (verbatim, preserves color type)
    void pixel_copy_fullground(Pixel * dest, const Pixel * src) noexcept { dest->copy_fullground(*src); }

    // True iff a and b match on fg + bg + style (full pixel equality)
    bool pixel_equals(const Pixel * a, const Pixel * b) noexcept { return *a == *b; }

    // Swap the pixel's fg and bg (preserving each side's ansi prefix)
    void pixel_swap(Pixel * p) noexcept { p->swap(); }

    // Fix both foreground and background of dest using src
    void pixel_fix(Pixel * dest, const Pixel * src) noexcept { dest->fix(*src); }

    // Fix only the background of dest using src
    void pixel_fix_background(Pixel * dest, const Pixel * src) noexcept { dest->fix_background(*src); }

    // True if no background is set
    bool pixel_no_background(const Pixel * p) noexcept { return p->no_background(); }

    // The foreground and the background as one packed number, red times 65536 plus green times 256 plus blue, and -1 when the color is not set
    int pixel_get_foreground(const Pixel * p) noexcept {
        const Fullground & color = *p;
        if (color.no_color()) return -1;
        unsigned char r, g, b; color.get_rgb(r, g, b);
        return (r << 16) | (g << 8) | b; }

    int pixel_get_background(const Pixel * p) noexcept {
        const Background & color = *p;
        if (color.no_color()) return -1;
        unsigned char r, g, b; color.get_rgb(r, g, b);
        return (r << 16) | (g << 8) | b; }

    // Log the pixel to wcout
    void pixel_log(const Pixel * p) noexcept { p->log(); }

    // Return the rendered wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t * pixel_get_wstring(const Pixel * p) noexcept {
        return wstring_to_cstring(p->get_wstring()); }

    // Return the pixel's HTML CSS body as a wide string (caller owns the buffer, free with wstring_delete)
    const wchar_t * pixel_get_html(const Pixel * p) noexcept {
        return wstring_to_cstring(p->get_html()); }

    // Deep copy of the pixel
    Pixel * pixel_copy(const Pixel * p) noexcept { return new Pixel(*p); }

}
