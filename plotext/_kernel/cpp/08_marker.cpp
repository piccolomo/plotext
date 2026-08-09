// Marker: abstract polymorphic base for things you can plot at a position. Each subclass owns its own MatrixCharacter construction via get_matrix_character.

class Marker {
public:
    virtual ~Marker() noexcept = default;
    virtual uint8_t         get_type()    const noexcept = 0;                                                              // marker_normal / marker_hd / marker_fhd / marker_braille / marker_box
    // (orientation virtual: meaningful only for BoxMarker, pure h/v subset)
    virtual wstring         get_wstring() const = 0;                                                                       // single-line representation (no newline)
    virtual size_t          get_xres()    const noexcept { return 1; }                                                      // sub-cell horizontal resolution (dot columns per character cell)
    virtual size_t          get_yres()    const noexcept { return 1; }                                                      // sub-cell vertical resolution (dot rows per character cell)
    virtual MatrixCharacter get_matrix_character(uint8_t subcell_col = 0, uint8_t subcell_row = 0) const = 0;               // produce the cell contribution this marker draws at the given sub-cell coords
    virtual const Pixel &   get_pixel()   const noexcept = 0;                                                               // every Marker subclass IS-A Pixel; expose it
    virtual void            fix(const Pixel & p) noexcept = 0;                                                              // forward to Pixel::fix
    virtual void            fix_background(const Pixel & p) noexcept = 0;                                                   // forward to Pixel::fix_background
    virtual void            set_pixel(const Pixel & p) noexcept = 0;                                                        // overwrite the marker's internal pixel
    virtual Marker *        copy()        const = 0;                                                                        // polymorphic deep copy
    virtual bool            get_orientation() const noexcept { return false; }                                              // only meaningful for BoxMarker, default false for the others
    virtual wchar_t         get_model_character() const noexcept { return get_symbol_model(get_type()); }                   // glyph used to represent this marker in the legend; subclasses can override (NormalMarker exposes its actual character; others use the type-based lookup glyph)
    virtual bool            is_matrix_marker() const noexcept { return false; }                                             // MatrixMarker overrides to true. Lets Point::stamp pick the multi-cell branch without dynamic_cast / RTTI.
    virtual void            merge(const Marker & other) noexcept { (void)other; }                                           // default: no merging (later overwrites earlier); BoxMarker overrides so crossings render as ┼/┤/├ instead of overwriting.
    inline  void            log() const { wcout << get_wstring() << endl; }
};


// NormalMarker: inherits NormalCharacter (gets wchar + pixel) and the polymorphic Marker interface.
class NormalMarker : public NormalCharacter, public Marker {
public:
    NormalMarker() noexcept = default;
    NormalMarker(wchar_t ch, const Pixel& p = {}) noexcept : NormalCharacter(ch, p) {}

    uint8_t         get_type()             const noexcept override { return marker_normal; }
    wchar_t         get_model_character()  const noexcept override { return get_wcharacter(); }
    wstring         get_wstring() const override { wstring s = L"PlotextMarker("; s.push_back(get_wcharacter()); s.push_back(L')'); return s; }
    MatrixCharacter get_matrix_character(uint8_t, uint8_t) const override { return MatrixCharacter(marker_normal, *this, get_wcharacter()); }
    const Pixel &   get_pixel()   const noexcept override { return *this; }
    void            fix(const Pixel & p) noexcept override { Pixel::fix(p); }
    void            fix_background(const Pixel & p) noexcept override { Pixel::fix_background(p); }
    void            set_pixel(const Pixel & p) noexcept override { Pixel::operator=(p); }
    Marker *        copy()        const override { return new NormalMarker(*this); }
};


// HDMarker: 2×2 sub-cell point. Pixel only, sub-cell position comes from the Point.
class HDMarker : public Pixel, public Marker {
public:
    HDMarker() noexcept = default;
    HDMarker(const Pixel& p) noexcept : Pixel(p) {}

    uint8_t         get_type()    const noexcept override { return marker_hd; }
    wstring         get_wstring() const override { return L"PlotextMarker(hd)"; }
    size_t          get_xres()    const noexcept override { return 2; }
    size_t          get_yres()    const noexcept override { return 2; }
    MatrixCharacter get_matrix_character(uint8_t dc, uint8_t dr) const override {
        MatrixCharacter mc(marker_hd, *this);
        mc.set_bits(get_dot_bit(dc, dr, 2, 2));
        return mc; }
    const Pixel &   get_pixel()   const noexcept override { return *this; }
    void            fix(const Pixel & p) noexcept override { Pixel::fix(p); }
    void            fix_background(const Pixel & p) noexcept override { Pixel::fix_background(p); }
    void            set_pixel(const Pixel & p) noexcept override { Pixel::operator=(p); }
    Marker *        copy()        const override { return new HDMarker(*this); }
};


// FHDMarker: 2×3 sub-cell point.
class FHDMarker : public Pixel, public Marker {
public:
    FHDMarker() noexcept = default;
    FHDMarker(const Pixel& p) noexcept : Pixel(p) {}

    uint8_t         get_type()    const noexcept override { return marker_fhd; }
    wstring         get_wstring() const override { return L"PlotextMarker(fhd)"; }
    size_t          get_xres()    const noexcept override { return 2; }
    size_t          get_yres()    const noexcept override { return 3; }
    MatrixCharacter get_matrix_character(uint8_t dc, uint8_t dr) const override {
        MatrixCharacter mc(marker_fhd, *this);
        mc.set_bits(get_dot_bit(dc, dr, 2, 3));
        return mc; }
    const Pixel &   get_pixel()   const noexcept override { return *this; }
    void            fix(const Pixel & p) noexcept override { Pixel::fix(p); }
    void            fix_background(const Pixel & p) noexcept override { Pixel::fix_background(p); }
    void            set_pixel(const Pixel & p) noexcept override { Pixel::operator=(p); }
    Marker *        copy()        const override { return new FHDMarker(*this); }
};


// BrailleMarker: 2×4 sub-cell point.
class BrailleMarker : public Pixel, public Marker {
public:
    BrailleMarker() noexcept = default;
    BrailleMarker(const Pixel& p) noexcept : Pixel(p) {}

    uint8_t         get_type()    const noexcept override { return marker_braille; }
    wstring         get_wstring() const override { return L"PlotextMarker(braille)"; }
    size_t          get_xres()    const noexcept override { return 2; }
    size_t          get_yres()    const noexcept override { return 4; }
    MatrixCharacter get_matrix_character(uint8_t dc, uint8_t dr) const override {
        MatrixCharacter mc(marker_braille, *this);
        mc.set_bits(get_dot_bit(dc, dr, 2, 4));
        return mc; }
    const Pixel &   get_pixel()   const noexcept override { return *this; }
    void            fix(const Pixel & p) noexcept override { Pixel::fix(p); }
    void            fix_background(const Pixel & p) noexcept override { Pixel::fix_background(p); }
    void            set_pixel(const Pixel & p) noexcept override { Pixel::operator=(p); }
    Marker *        copy()        const override { return new BrailleMarker(*this); }
};


// BoxMarker: a BoxCharacter (packed arms + style + Pixel) wearing the polymorphic Marker interface. State lives entirely in the BoxCharacter base, no duplicate fields.
class BoxMarker : public BoxCharacter, public Marker {
public:
    BoxMarker() noexcept = default;

    // Simple orientation ctor: 0 = horizontal (left+right arms), 1 = vertical (up+down arms).
    BoxMarker(bool orientation, uint8_t style = box_normal, const Pixel & p = {}) noexcept
        : BoxCharacter(orientation, orientation, !orientation, !orientation, style, p) {}

    // Full-arms ctor: each bool toggles the corresponding arm. Used internally for ticks/corners/grid intersections.
    BoxMarker(bool up, bool down, bool left, bool right, uint8_t style, const Pixel & p) noexcept
        : BoxCharacter(up, down, left, right, style, p) {}

    // Heuristic, meaningful only for pure h/v markers. Any N or S arm reports as vertical.
    bool get_orientation() const noexcept override { return (get_arms() & (box_n | box_s)) != 0; }

    uint8_t         get_type()    const noexcept override { return marker_box; }
    void            merge(const Marker & other) noexcept override {
        if (other.get_type() == marker_box) BoxCharacter::merge(static_cast<const BoxMarker &>(other)); }
    wchar_t         get_model_character() const noexcept override { return BoxCharacter::get_wcharacter(); }   // legend shows the actual arm shape (│ ─ ┼ etc.) instead of the type-default glyph
    wstring         get_wstring() const override { return get_orientation() ? L"PlotextMarker(box, vertical)" : L"PlotextMarker(box, horizontal)"; }
    MatrixCharacter get_matrix_character(uint8_t, uint8_t) const override {
        MatrixCharacter mc(marker_box, *this);
        mc.set_bits(get_code());
        return mc; }
    const Pixel &   get_pixel()                     const noexcept override { return *this; }
    void            fix(const Pixel & p)                  noexcept override { Pixel::fix(p); }
    void            fix_background(const Pixel & p)       noexcept override { Pixel::fix_background(p); }
    void            set_pixel(const Pixel & p)            noexcept override { Pixel::operator=(p); }
    Marker *        copy()                          const          override { return new BoxMarker(*this); }
};


// MatrixMarker: a Matrix-shaped marker with per-axis alignment, but no position of its own. Position is provided by the Point that carries it, same contract as single-cell markers, just with a multi-cell character footprint. Separates "what to draw" (here) from "where to draw it" (Point). get_xres/get_yres return 1 (sub-cell resolution, matches NormalMarker so line generators don't over-densify); the multi-cell footprint is accessed via Matrix::get_width/get_height for the stamping path. The stamp() override delegates to Matrix::insert(col, row, Matrix, ha, va) with the marker's per-axis alignments.
class MatrixMarker : public Matrix, public Marker {
private:
    Alignment halignment = Alignment(-1);   // -1 left, 0 center, 1 right
    Alignment valignment = Alignment(-1);   // -1 top,  0 center, 1 bottom

public:
    MatrixMarker() noexcept = default;
    MatrixMarker(const Matrix & m, const Alignment & ha = Alignment(-1), const Alignment & va = Alignment(-1)) : Matrix(m), halignment(ha), valignment(va) {}
    MatrixMarker(const MatrixMarker &) = default;
    MatrixMarker(MatrixMarker &&) noexcept = default;
    ~MatrixMarker() = default;
    MatrixMarker & operator=(const MatrixMarker &) = default;
    MatrixMarker & operator=(MatrixMarker &&) noexcept = default;

    // Per-axis alignment
    const Alignment & get_halignment() const noexcept { return halignment; }
    const Alignment & get_valignment() const noexcept { return valignment; }

    // Marker interface
    uint8_t get_type()    const noexcept override { return marker_normal; }
    size_t  get_xres()    const noexcept override { return 1; }
    size_t  get_yres()    const noexcept override { return 1; }
    wstring get_wstring() const override {
        wostringstream w;
        w << L"MatrixMarker(" << get_width() << L"x" << get_height()
          << L", ha=" << halignment.get_integer()
          << L", va=" << valignment.get_integer() << L")";
        return w.str(); }
    // Legacy single-cell fallback: returns the top-left cell. Real multi-cell rendering goes through stamp() -> Matrix::insert + alignment, not through this method.
    MatrixCharacter get_matrix_character(uint8_t, uint8_t) const override {
        return get_size() == 0 ? MatrixCharacter() : Array2D<MatrixCharacter>::at(0); }
    // Representative pixel: the top-left cell's Pixel (each MatrixCharacter is-a Pixel). Empty-matrix safety via a static fallback.
    const Pixel & get_pixel() const noexcept override {
        static const Pixel empty;
        return get_size() == 0 ? empty : Array2D<MatrixCharacter>::at(0); }
    // Pixel transforms apply cell-wise, multi-cell markers don't have a single owned pixel. fix_background / set_pixel forward to Matrix's existing per-cell iterators.
    void fix           (const Pixel & p) noexcept override { for (size_t i = 0; i < get_size(); ++i) at(i).fix(p); }
    void fix_background(const Pixel & p) noexcept override { Matrix::fix_background(p); }
    void set_pixel     (const Pixel & p) noexcept override { Matrix::set_pixel(p); }
    Marker * copy()                            const override { return new MatrixMarker(*this); }
    wchar_t  get_model_character()        const noexcept override {
        return get_size() == 0 ? get_symbol_model(marker_normal) : Array2D<MatrixCharacter>::at(0).get_wcharacter(); }
    bool     is_matrix_marker()           const noexcept override { return true; }   // self-identify so Point::stamp routes to the multi-cell branch.
};


extern "C" {
    Marker * marker_new_normal (wchar_t c, Pixel * p) noexcept { return new NormalMarker (c, *p); }
    Marker * marker_new_hd     (Pixel * p) noexcept { return new HDMarker     (*p); }
    Marker * marker_new_fhd    (Pixel * p) noexcept { return new FHDMarker    (*p); }
    Marker * marker_new_braille(Pixel * p) noexcept { return new BrailleMarker(*p); }
    Marker * marker_new_box      (bool up, bool down, bool left, bool right, uint8_t style, Pixel * p) noexcept { return new BoxMarker(up, down, left, right, style, *p); }
    Marker * marker_new_code   (const char * code, Pixel * p) noexcept { return new NormalMarker(get_symbol(string(code)), *p); }
    Marker * marker_new_matrix (Matrix * m, int ha, int va) noexcept { return new MatrixMarker(*m, Alignment(ha), Alignment(va)); }
    void     marker_delete     (Marker * m) noexcept { delete m; }

    const wchar_t * marker_get_wstring(Marker * m) noexcept { return wstring_to_cstring(m->get_wstring()); }
    const wchar_t * marker_get_model  (Marker * m) noexcept { return wstring_to_cstring(wstring(1, m->get_model_character())); }
    Pixel  *        marker_get_pixel  (Marker * m) noexcept { return new Pixel(m->get_pixel()); }
    void            marker_fix        (Marker * m, Pixel * p) noexcept { m->fix(*p); }
    void            marker_set_pixel  (Marker * m, Pixel * p) noexcept { m->set_pixel(*p); }
    Marker *        marker_copy       (Marker * m) noexcept { return m->copy(); }
    bool            marker_get_orientation(Marker * m) noexcept { return m->get_orientation(); }
    // Returns the line style (0 = normal, 1 = double, 2 = heavy, 3 = dotted, 4 = rounded). Only meaningful for BoxMarker; other kinds return 0.
    uint8_t         marker_get_style(Marker * m) noexcept { return m->get_type() == marker_box ? static_cast<BoxMarker*>(m)->get_style() : 0; }
}
