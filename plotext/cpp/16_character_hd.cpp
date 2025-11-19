// Class to represent a character canvas, combining Marker and MatrixBool functionality.
class CharacterHD : public Marker, public MatrixBool {
public:
    using MatrixBool::set;
    using MatrixBool::get;
    using MatrixBool::get_code;

    // Constructor initializing with a Marker object (default or provided)
    CharacterHD(const Marker & m = Marker()) : MatrixBool(m.get_cols(), m.get_rows()), Marker(m) {}

    // Copy constructors
    CharacterHD(const CharacterHD & c) : Marker(c), MatrixBool(c) {}
    CharacterHD(const Character & c) : Marker(c.get_wcharacter(), c), MatrixBool(0, 0) {}

    // Assignment operators
    CharacterHD & operator=(const CharacterHD & c) { Marker::operator=(c); MatrixBool::operator=(c); return *this;}
    CharacterHD & operator=(const Character & c) { Marker::operator=(c); MatrixBool::zero(); return *this;}

    // Set the marker type, recreating matrix if type changes
    void set_type(const marker_type & type) noexcept { MarkerType::set(type); MatrixBool::set_size(Marker::get_cols(), Marker::get_rows());}
    constexpr marker_type get_type() const { return MarkerType::get(); }

    // Update from a Point
    void update(const Point & p) noexcept {
        if (!same_type(p)) set_type(p.get_type());
        if (!same_pixel(p)) copy_pixel(p);
        if (p.is_normal()) set_wcharacter(p.get_wcharacter());
        if (p.is_high_definition()) { add_dot(p.get_inner_col(), p.get_inner_row()); update_wcharacter(); } }

    // Get the character representation based on type/code
    inline wchar_t get_wcharacter() const noexcept {
        uint8_t code = MatrixBool::get_code();
        wchar_t out;
        if (is_normal()) out = Marker::get_wcharacter();
        if (is_hd()) out = hd_lookup[code];
        if (is_fhd()) out = fhd_lookup[code];
        if (is_braille()) out = braille_lookup[code];
        if (is_none()) out = L'?';
        return out; }

    inline void update_wcharacter() noexcept { set_wcharacter(get_wcharacter()); }

    // Write character and pixel data to buffer
    void to_buffer(wchar_t* buffer, size_t& length_buffer) const noexcept override { 
        Pixel::to_buffer(buffer, length_buffer);
        wchar_to_buffer(get_wcharacter(), buffer, length_buffer);
        cstring_to_buffer(ansi_end, buffer, length_buffer); }

    // Render to stdout
    void print() const noexcept {
        wchar_t buffer[character_size_max + 1] = {L'\0'};
        size_t length = 0;
        to_buffer(buffer, length);
        wcout.write(buffer, length); }

    // Wide string representation
    wstring get_wstring() const {
        wostringstream woss;
        woss << Marker::get_wstring();
        if (is_high_definition()) woss << L", " << MatrixBool::get_wstring();
        return woss.str(); }

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    inline void log() const { wcout << get_wstring() << flush; }
    inline void stream() const { Pixel::stream(); wcout.put(get_wcharacter()); }

    friend wostream & operator<<(wostream & os, const CharacterHD & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const CharacterHD & c) noexcept {os << c.get_string(); return os;}

};

 //using MatrixBool::get_code; // Expose get_code from MatrixBool.
