// Character family: NormalCharacter (Pixel + wchar), 4 X-Character builders (HD/FHD/Braille/Box) holding bits, MatrixCharacter (the matrix cell, NormalCharacter + kind + bits, with merge logic).

// NormalCharacter: a single wchar_t with inherited Pixel styling
class NormalCharacter : public Pixel {
private:
    wchar_t c = L' ';                                                       // displayed character (default space)

public:
    NormalCharacter() noexcept = default;
    NormalCharacter(wchar_t ch) noexcept                          : c(ch) {}
    NormalCharacter(wchar_t ch, const Pixel& p) noexcept          : Pixel(p), c(ch) {}
    NormalCharacter(const Pixel& p) noexcept                      : NormalCharacter(L' ', p) {}
    NormalCharacter(const NormalCharacter&) noexcept = default;
    NormalCharacter(NormalCharacter&&) noexcept = default;
    NormalCharacter& operator=(const NormalCharacter&) noexcept = default;
    NormalCharacter& operator=(NormalCharacter&&) noexcept = default;
    ~NormalCharacter() noexcept {}

    inline constexpr bool operator==(const NormalCharacter& o) const noexcept       { return c == o.c && Pixel::operator==(o); }
    inline constexpr bool operator!=(const NormalCharacter& o) const noexcept       { return !(*this == o); }
    inline constexpr bool same(const NormalCharacter& o) const noexcept             { return c == o.c && Pixel::operator==(o); }
    inline constexpr bool different_pixel(const NormalCharacter& o) const noexcept  { return !Pixel::operator==(o); }

    inline constexpr bool is_empty() const noexcept { return c == L' '; }
    inline void clear() noexcept { c = L' '; Pixel::clear(); }

    inline void    set_wcharacter(wchar_t ch) noexcept { c = ch; }
    inline wchar_t get_wcharacter() const noexcept { return c; }
    inline void    set_pixel(const Pixel& p) noexcept { Pixel::operator=(p); }

    inline void to_buffer(wchar_t* buf, size_t & pos, const bool & colorfull = true) const noexcept {
        if (colorfull) Pixel::to_buffer(buf, pos);
        wchar_to_buffer(c, buf, pos);
        if (colorfull) cstring_to_buffer(ansi_end, buf, pos); }

    inline wstring get_wstring() const {
        wchar_t buf[character_size_max + 1] = {};
        size_t pos = 0;
        to_buffer(buf, pos);
        return wstring(buf); }

    inline string get_string() const { return wstring_to_string(get_wstring()); }
    inline void   log()        const { wcout << L"Normal Character(" << get_wstring() << L")" << endl; }

    inline void stream(const bool & colorfull = false) const noexcept { if (colorfull) { wcout.write(ansi_end, 4); Pixel::stream(); } wcout.put(c); }   // colorfull=true → emit pixel transition before glyph; false → just glyph

    friend wostream & operator<<(wostream & os, const NormalCharacter & ch) noexcept { os << ch.get_wstring(); return os; }
    friend ostream  & operator<<(ostream  & os, const NormalCharacter & ch) noexcept { os << ch.get_string();  return os; }
};


// HDCharacter: 2×2 sub-cell dot grid (top-left = bit 3), 4-bit dot pattern in 1 byte
class HDCharacter : public Pixel {
private:
    static constexpr uint8_t cols = 2, rows = 2;
    uint8_t bits = 0;

public:
    HDCharacter() noexcept = default;
    HDCharacter(const Pixel & p) noexcept : Pixel(p) {}
    HDCharacter(const HDCharacter &) noexcept = default;
    HDCharacter(HDCharacter &&) noexcept = default;
    HDCharacter & operator=(const HDCharacter &) noexcept = default;
    HDCharacter & operator=(HDCharacter &&) noexcept = default;
    ~HDCharacter() noexcept {}

    inline void    add_dot(uint8_t col, uint8_t row) noexcept { bits |= get_dot_bit(col, row, cols, rows); }
    inline void    clear  ()                         noexcept { bits = 0; Pixel::clear(); }
    inline uint8_t get_code()       const noexcept { return bits; }
    inline wchar_t get_wcharacter() const noexcept { return hd_lookup[bits]; }

    inline NormalCharacter get_normal_character() const noexcept { return NormalCharacter(get_wcharacter(), *this); }
    inline void            log()                  const          { wcout << L"HD Character(" << get_wcharacter() << L", bits " << (int)bits << L")" << endl; }
};


// FHDCharacter: 2×3 sub-cell dot grid (top-left = bit 5), 6-bit dot pattern in 1 byte
class FHDCharacter : public Pixel {
private:
    static constexpr uint8_t cols = 2, rows = 3;
    uint8_t bits = 0;

public:
    FHDCharacter() noexcept = default;
    FHDCharacter(const Pixel & p) noexcept : Pixel(p) {}
    FHDCharacter(const FHDCharacter &) noexcept = default;
    FHDCharacter(FHDCharacter &&) noexcept = default;
    FHDCharacter & operator=(const FHDCharacter &) noexcept = default;
    FHDCharacter & operator=(FHDCharacter &&) noexcept = default;
    ~FHDCharacter() noexcept {}

    inline void    add_dot(uint8_t col, uint8_t row) noexcept { bits |= get_dot_bit(col, row, cols, rows); }
    inline void    clear  ()                         noexcept { bits = 0; Pixel::clear(); }
    inline uint8_t get_code()       const noexcept { return bits; }
    inline wchar_t get_wcharacter() const noexcept { return fhd_lookup[bits]; }

    inline NormalCharacter get_normal_character() const noexcept { return NormalCharacter(get_wcharacter(), *this); }
    inline void            log()                  const          { wcout << L"FHD Character(" << get_wcharacter() << L", bits " << (int)bits << L")" << endl; }
};


// BrailleCharacter: 2×4 sub-cell dot grid (top-left = bit 7), 8-bit dot pattern fills the byte
class BrailleCharacter : public Pixel {
private:
    static constexpr uint8_t cols = 2, rows = 4;
    uint8_t bits = 0;

public:
    BrailleCharacter() noexcept = default;
    BrailleCharacter(const Pixel & p) noexcept : Pixel(p) {}
    BrailleCharacter(const BrailleCharacter &) noexcept = default;
    BrailleCharacter(BrailleCharacter &&) noexcept = default;
    BrailleCharacter & operator=(const BrailleCharacter &) noexcept = default;
    BrailleCharacter & operator=(BrailleCharacter &&) noexcept = default;
    ~BrailleCharacter() noexcept {}

    inline void    add_dot(uint8_t col, uint8_t row) noexcept { bits |= get_dot_bit(col, row, cols, rows); }
    inline void    clear  ()                           noexcept { bits = 0; Pixel::clear(); }
    inline uint8_t get_code()       const noexcept { return bits; }
    inline wchar_t get_wcharacter() const noexcept { return braille_lookup[bits]; }

    inline NormalCharacter get_normal_character() const noexcept { return NormalCharacter(get_wcharacter(), *this); }
    inline void            log()                  const          { wcout << L"Braille Character(" << get_wcharacter() << L", bits " << (int)bits << L")" << endl; }
};


// BoxStyle: shared "drawable line config", style + pixel. Owned state for BoxCharacter and BoxMarker; arms (shape) live in BoxCharacter.
class BoxStyle : public Pixel {
private:
    uint8_t style = box_normal;

public:
    BoxStyle() noexcept = default;
    BoxStyle(uint8_t s, const Pixel & p) noexcept : Pixel(p), style(s) {}

    inline uint8_t get_style()       const noexcept { return style; }
    inline void    set_style(uint8_t s) noexcept    { style = s; }
    inline const Pixel & get_pixel() const noexcept { return *this; }
    inline void    set_pixel(const Pixel & p) noexcept { Pixel::operator=(p); }
};


// BoxCharacter: arms (low nibble) + BoxStyle (style + pixel). get_code() repacks arms+style on demand for the matrix path.
class BoxCharacter : public BoxStyle {
private:
    uint8_t arms = 0;

public:
    BoxCharacter() noexcept = default;
    BoxCharacter(bool up, bool down, bool left, bool right, uint8_t style = box_normal, const Pixel & p = Pixel()) noexcept : BoxStyle(style, p) {
        if (up)    arms |= box_n;
        if (right) arms |= box_e;
        if (down)  arms |= box_s;
        if (left)  arms |= box_w; }
    BoxCharacter(const BoxCharacter &) noexcept = default;
    BoxCharacter(BoxCharacter &&) noexcept = default;
    BoxCharacter & operator=(const BoxCharacter &) noexcept = default;
    BoxCharacter & operator=(BoxCharacter &&) noexcept = default;
    ~BoxCharacter() noexcept {}

    inline void    clear() noexcept { arms = 0; set_style(box_normal); Pixel::clear(); }
    inline uint8_t get_code()       const noexcept { return get_box_code(arms, get_style()); }
    inline uint8_t get_arms()       const noexcept { return arms; }
    inline void    merge(const BoxCharacter & o) noexcept { arms |= o.arms; }                     // merge another BoxCharacter's arms into this one (used by Points::squash to keep box-line crossings as ┼/┤/├ instead of overwriting)
    inline wchar_t get_wcharacter() const noexcept { return get_box_glyph(get_code()); }

    inline NormalCharacter get_normal_character() const noexcept { return NormalCharacter(get_wcharacter(), *this); }

    inline const wchar_t * get_style_name() const noexcept {                              // "normal"/"double"/"heavy"/"dotted"/"rounded"
        const uint8_t s = get_style();
        if (s == box_double)  return L"double";
        if (s == box_heavy)   return L"heavy";
        if (s == box_dotted)  return L"dotted";
        if (s == box_rounded) return L"rounded";
        return L"normal"; }

    inline void log() const { wcout << L"Line Character(" << get_wcharacter() << L", arms " << (int)get_arms() << L", style " << get_style_name() << L")" << endl; }
};


// Free helpers used by MatrixCharacter::merge, bit-level merge rules
inline void merge_dot_bits (uint8_t & bits, uint8_t other) noexcept { bits |= other; }                                                    // HD/FHD/Braille: OR dot bits
inline void merge_box_bits(uint8_t & bits, uint8_t other) noexcept {                                                                      // Line: OR arms, heavier style wins
    const uint8_t merged_arms   = get_box_arms (bits) | get_box_arms (other);
    const uint8_t heavier_style = get_box_style(other) > get_box_style(bits) ? get_box_style(other) : get_box_style(bits);
    bits = get_box_code(merged_arms, heavier_style); }


// MatrixCharacter: the matrix cell. NormalCharacter + (kind, bits) so successive Points at the same (col, row) merge, HD/FHD/Braille accumulate dots, Line accumulates arms + heaviest style.
class MatrixCharacter : public NormalCharacter {
private:
    uint8_t kind = marker_normal;             // which marker kind currently owns this cell
    uint8_t bits = 0;                        // dot bits / packed line code; unused for marker_normal

public:
    MatrixCharacter() noexcept = default;
    MatrixCharacter(wchar_t ch, const Pixel & p = {}) noexcept : NormalCharacter(ch, p) {}
    MatrixCharacter(const NormalCharacter & nc) noexcept : NormalCharacter(nc) {}
    // Construct with kind + pixel (and optional cached glyph). Bits stay 0, caller sets them via set_bits if needed.
    MatrixCharacter(uint8_t k, const Pixel & p, wchar_t ch = L' ') noexcept : NormalCharacter(ch, p), kind(k) {}

    inline uint8_t get_kind() const noexcept { return kind; }
    inline void    set_bits(uint8_t b) noexcept { bits = b; }

    inline void clear() noexcept { kind = marker_normal; bits = 0; NormalCharacter::clear(); }

    // Refresh the cached glyph from (kind, bits). Normal kind keeps whatever wchar is already there.
    inline void update_wcharacter() noexcept {
        switch (kind) {
            case marker_hd:      set_wcharacter(hd_lookup     [bits]); return;
            case marker_fhd:     set_wcharacter(fhd_lookup    [bits]); return;
            case marker_braille: set_wcharacter(braille_lookup[bits]); return;
            case marker_box:    set_wcharacter(get_box_glyph(bits)); return;
            default:           return; } }

    // Refresh the cached glyph, then delegate to NormalCharacter::stream, the matrix loop calls this per cell, so glyphs always reflect the latest (kind, bits) at render time.
    inline void stream(const bool & colorfull = false) noexcept { update_wcharacter(); NormalCharacter::stream(colorfull); }

    // Merge another MatrixCharacter into this one. Different kind → adopt new kind (reset bits). Normal kind overwrites entirely. Cached glyph stays stale until update_wcharacter() runs.
    inline void merge(const MatrixCharacter & o) noexcept {
        if (o.kind == marker_normal) { *this = o; return; }
        if (kind != o.kind) { kind = o.kind; bits = 0; }
        if (o.kind == marker_box) merge_box_bits(bits, o.bits);
        else                     merge_dot_bits (bits, o.bits);
        set_pixel(o); }

    inline void log() const { wcout << L"Matrix Character(kind " << (int)kind << L", bits " << (int)bits << L", glyph " << get_wcharacter() << L")" << endl; }
};


extern "C" {
    BoxStyle * box_style_new       (uint8_t style, Pixel * p)   noexcept { return new BoxStyle(style, *p); }
    void       box_style_delete    (BoxStyle * b)               noexcept { delete b; }

    uint8_t    box_style_get_style (BoxStyle * b)               noexcept { return b->get_style(); }
    void       box_style_set_style (BoxStyle * b, uint8_t s)    noexcept { b->set_style(s); }

    Pixel *    box_style_get_pixel (BoxStyle * b)               noexcept { return new Pixel(b->get_pixel()); }
    void       box_style_set_pixel (BoxStyle * b, Pixel * p)    noexcept { b->set_pixel(*p); }
}