// CharacterHD: a Marker + a MatrixBool that together render a high-definition glyph (hd / fhd / braille)

class CharacterHD : public Marker, public MatrixBool {
public:
    using MatrixBool::set;
    using MatrixBool::get;
    using MatrixBool::get_code;

    // Construct from a Marker (defaults to a normal marker)
    CharacterHD(const Marker & m = Marker(normal)) : Marker(m), MatrixBool(m.get_cols(), m.get_rows()) {}

    // Copy constructor
    CharacterHD(const CharacterHD & c) : Marker(c), MatrixBool(c) {}

    // Move constructor
    CharacterHD(CharacterHD && c) noexcept : Marker(std::move(c)), MatrixBool(std::move(c)) {}

    // Construct from a plain Character (forces normal mode, 0x0 dot grid)
    CharacterHD(const Character & c) : Marker(c.get_wcharacter(), c), MatrixBool(0, 0) {}

    // Construct from a Pixel (empty character, normal mode)
    CharacterHD(const Pixel & c) : CharacterHD(Marker(L' ', c)) {}

    // Destructor
    ~CharacterHD() noexcept {}

    // Copy assignment
    CharacterHD & operator=(const CharacterHD & c) { Marker::operator=(c); MatrixBool::operator=(c); return *this;}

    // Move assignment
    CharacterHD & operator=(CharacterHD && c) noexcept { Marker::operator=(std::move(c)); MatrixBool::operator=(std::move(c)); return *this;}

    // Assign from a plain Character (zeroes the dot grid)
    CharacterHD & operator=(const Character & c) { Marker::operator=(c); MatrixBool::zero(); return *this;}

    // Set the marker type and resize the dot grid accordingly
    void set_type(const marker_type & type) noexcept { MarkerType::set(type); MatrixBool::set_size(Marker::get_cols(), Marker::get_rows());}

    // Get the current marker type
    constexpr marker_type get_type() const { return MarkerType::get(); }

    // Update this cell from a Point (type, pixel, character, dot)
    void update(const Point & p) noexcept {
        if (!same_type(p)) set_type(p.get_type());
        if (!same_pixel(p)) copy_pixel(p);
        if (p.is_normal()) set_wcharacter(p.get_wcharacter());
        if (p.is_high_definition()) { add_dot(p.get_inner_col(), p.get_inner_row()); update_wcharacter(); } }

    // Get the glyph character for the current type/code
    inline wchar_t get_wcharacter() const noexcept {
        const uint8_t code = MatrixBool::get_code();
        wchar_t out = L'?';
        if (is_normal())      out = Marker::get_wcharacter();
        else if (is_hd())     out = hd_lookup[code];
        else if (is_fhd())    out = fhd_lookup[code];
        else if (is_braille()) out = braille_lookup[code];
        return out; }

    // Sync the Marker's stored character to the computed glyph
    inline void update_wcharacter() noexcept { set_wcharacter(get_wcharacter()); }

    // Append styled glyph + reset to a buffer
    inline void to_buffer(wchar_t* buf, size_t & pos) const noexcept {
        Pixel::to_buffer(buf, pos);                 // apply foreground/bg/attrs
        wchar_to_buffer(get_wcharacter(), buf, pos);               // write character itself
        cstring_to_buffer(ansi_end, buf, pos);}      // reset ANSI codes

    // Append glyph to a matrix buffer (optionally including color codes)
    inline void to_matrix_buffer(wchar_t* buf, size_t & pos, const bool & colorfull = true) const noexcept {
        if (colorfull) cstring_to_buffer(ansi_end, buf, pos);// reset ANSI codes
        if (colorfull) Pixel::to_buffer(buf, pos);                 // apply foreground/bg/attrs
        wchar_to_buffer(get_wcharacter(), buf, pos);}               // write character itself

    // Render to stdout
    void print() const noexcept {
        wchar_t buffer[character_size_max + 1] = {L'\0'};
        size_t length = 0;
        to_buffer(buffer, length);
        wcout.write(buffer, length);}

    // Get wide string for display (marker + dot grid when in HD mode)
    wstring get_wstring() const {
        wostringstream woss;
        woss << Marker::get_wstring();
        if (is_high_definition()) woss << L", " << MatrixBool::get_wstring();
        return woss.str(); }

    // Get narrow string for display
    inline string get_string() const { return wstring_to_string(get_wstring()); }

    // Log to wcout (no newline)
    inline void log() const { wcout << get_wstring() << flush; }

    // Stream directly to wcout (optionally including color codes)
    inline void stream(const bool & colorfull = false) const { if (colorfull) {wcout.write(ansi_end, 4); Pixel::stream();} wcout.put(get_wcharacter()); }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const CharacterHD & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const CharacterHD & c) noexcept {os << c.get_string(); return os;}

};
