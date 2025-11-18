// Marker class combines manages either a normal character or hd types

class Marker : public Character, public MarkerType {
public:
    // Constructors
    constexpr Marker() noexcept = default; // Default constructor
    Marker(const wchar_t & c, const Pixel & p = Pixel()) noexcept : Character(c, p), MarkerType(normal) {}

    Marker(const marker_type & t, const Pixel & p = Pixel()) noexcept : MarkerType(t), Character(space, p) {}


    // Copy & move constructors
    Marker(const Marker & m) noexcept = default;
    Marker(Marker && m) noexcept = default;

    // Assignment operators
    Marker & operator=(const Marker & m) noexcept {clone(m);
        return *this;}

    Marker & operator=(const Character & m) noexcept {
        Character::operator=(m);
        MarkerType::set(normal);
        return *this;}

    void clone(const Marker & m) noexcept {
        Character::operator=(m);
        MarkerType::operator=(m);
    }

     // Equality operators
    bool operator==(const Marker & other) const noexcept {return Character::operator==(other) && MarkerType::operator==(other);}
    bool operator!=(const Marker & other) const noexcept { return !(*this == other); }

    // Clear both character and marker type
    void clear() noexcept {
        Character::clear();
        MarkerType::clear();}

    void set_type(const marker_type & t = normal) noexcept { MarkerType::set(t); }

    bool same_type(const Marker & m) const noexcept { return MarkerType::operator==(m); }

    void set_wcharacter(const wchar_t & cs) noexcept {MarkerType::set(normal); Character::set_wcharacter(cs);}

    wchar_t get_model() const noexcept {
        marker_type type = MarkerType::get(); 
        wchar_t ch; if(type == normal) {return Character::get_wcharacter();} else {return get_marker_model(type);}}

    Pixel get_pixel() const noexcept {return *this;}

    // Render the marker to a buffer
    virtual void to_buffer(wchar_t* buffer, size_t & length_buffer) const noexcept override {
        Pixel::to_buffer(buffer, length_buffer); // Add pixel attributes
        if (is_normal()) {wchar_to_buffer(get_wcharacter(), buffer, length_buffer);} // Render as a character if normal
        else {MarkerType::to_buffer(buffer, length_buffer);} // Use marker type rendering
        if (get_length() > 0) cstring_to_buffer(ansi_end, buffer, length_buffer);}

    // Get the marker as a wide string
    wstring get_wstring() const {
        wchar_t buffer[marker_size_max + 1] = {L'\0'}; // Buffer for rendering 
        size_t length = 0;
        to_buffer(buffer, length);
        return wstring(buffer);}

    // Print the marker to the console
    void log() const noexcept {wcout.write(get_wstring().c_str(), get_wstring().size());}

};


extern "C" {
    Marker * marker_new_normal(wchar_t c, Pixel * p) noexcept {return new Marker(c, *p);}
    Marker * marker_new_type(marker_type t, Pixel * p) noexcept {return new Marker(t, *p);}

    void marker_delete(Marker * m) noexcept {delete m;}
    Marker * marker_copy(Marker * m) noexcept {return new Marker(*m);}
    const wchar_t * marker_get_wstring(Marker * c) noexcept {return wstring_to_cstring(c->get_wstring());}
    wchar_t marker_get_model(Marker * cs) noexcept {return cs->get_model();}
    Pixel * marker_get_pixel(Marker * cs) noexcept {return new Pixel(cs->get_pixel());}
    void marker_fix(Marker * p, Marker * pixel) noexcept {p->fix(*pixel);}
}
