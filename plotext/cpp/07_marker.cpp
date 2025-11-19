// Marker class combines manages either a normal character or hd types

// Marker - combines Character (wchar + styling) with MarkerType (resolution mode)

class Marker : public Character, public MarkerType {
public:
    // -------------------- lifecycle --------------------
    constexpr Marker() noexcept = default;

    constexpr Marker(wchar_t ch, const Pixel & p = Pixel())
        noexcept : Character(ch, p), MarkerType(normal) {}

    constexpr Marker(marker_type t, const Pixel & p = Pixel())
        noexcept : Character(L' ', p), MarkerType(t) {}

    Marker(const Marker&) noexcept = default;
    Marker(Marker&&) noexcept = default;

    // -------------------- assignment --------------------
    Marker& operator=(const Marker& m) noexcept {
        if (this == &m) return *this;
        Character::operator=(m);
        MarkerType::operator=(m);
        return *this;}

    Marker& operator=(const Character& ch) noexcept {
        Character::operator=(ch);
        MarkerType::set(normal);
        return *this;}

    // -------------------- comparison --------------------
    constexpr bool operator==(const Marker& o) const noexcept {
        return Character::operator==(o) && MarkerType::operator==(o);}
    constexpr bool operator!=(const Marker& o) const noexcept { return !(*this == o); }
    constexpr bool same_type(const Marker& o) const noexcept { return MarkerType::operator==(o); }

    // -------------------- state --------------------
    void clear() noexcept { Character::clear(); MarkerType::clear(); }
    void set_type(marker_type t = normal) noexcept { MarkerType::set(t); }

    // Setting character forces normal mode (semantic choice)
    void set_wcharacter(wchar_t ch) noexcept {
        MarkerType::set(normal);
        Character::set_wcharacter(ch);}

    // Model character: actual displayed char in normal mode, or representative char otherwise
    wchar_t get_model() const noexcept {
        return is_normal() ? Character::get_wcharacter() : get_marker_model(get());}

    Pixel get_pixel() const noexcept { return static_cast<Pixel>(*this); }

    // -------------------- rendering --------------------
    void to_buffer(wchar_t* buf, size_t& pos) const noexcept {
        Pixel::to_buffer(buf, pos);                          // apply styling
        if (is_normal()) wchar_to_buffer(get_wcharacter(), buf, pos);        // single char
        else MarkerType::to_buffer(buf, pos);                    // e.g. "HD", "FHD"
        if (pos > 0) cstring_to_buffer(ansi_end, buf, pos); }    // reset ANSI

    wstring get_wstring() const {
        wchar_t buf[marker_size_max + 1] = {};
        size_t pos = 0;
        to_buffer(buf, pos);
        return wstring(buf, pos);}

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    void log() const noexcept {wcout << get_wstring() << endl;}

    friend wostream& operator<<(wostream & os, const Marker & m) noexcept {os << m.get_wstring(); return os; }

    friend ostream& operator<<(ostream & os, const Marker & m) noexcept {os << m.get_string(); return os; }

};


extern "C" {
    Marker* marker_new_normal(wchar_t c, const Pixel* p) noexcept { return new Marker(c, *p); }
    Marker* marker_new_type(marker_type t, const Pixel* p) noexcept { return new Marker(t, *p); }
    void    marker_delete(Marker* m) noexcept { delete m; }
    Marker* marker_copy(const Marker* m) noexcept { return new Marker(*m); }

    const wchar_t* marker_get_wstring(const Marker* m) noexcept { return wstring_to_cstring(m->get_wstring()); }
    wchar_t        marker_get_model(const Marker* m) noexcept { return m->get_model(); }
    Pixel*         marker_get_pixel(const Marker* m) noexcept { return new Pixel(m->get_pixel()); }

    void marker_fix(Marker * p, Marker * pixel) noexcept {p->fix(*pixel);}
}
