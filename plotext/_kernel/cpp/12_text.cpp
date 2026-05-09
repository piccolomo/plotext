// Text: a Colorize string anchored at a (PointPosition) coordinate, with alignment and orientation. Inserted into a Matrix at its (col, row) — the matrix uses get_alignment + get_orientation to lay out the wchars row-wise (horizontal) or column-wise (vertical).

class Text : public PointPosition, public Colorize {
private:
    Orientation orientation = Orientation(0);   // 0 horizontal, 1 vertical
    Alignment   alignment   = Alignment(-1);    // -1 left, 0 center, 1 right

public:
    Text() noexcept = default;
    Text(float xi, float yi, const Colorize & c, const Orientation & o = Orientation(0), const Alignment & a = Alignment(-1)) : PointPosition(xi, yi), Colorize(c), orientation(o), alignment(a) {}
    Text(const Text & t) = default;
    Text(Text && t) noexcept = default;
    ~Text() {}

    Text & operator=(const Text & t) = default;
    Text & operator=(Text && t) noexcept = default;

    void set_position   (float xi, float yi)         noexcept { PointPosition::operator=(PointPosition(xi, yi)); }
    void set_alignment  (const Alignment   & a)      noexcept { alignment   = a; }
    void set_orientation(const Orientation & o)      noexcept { orientation = o; }

    const Alignment   & get_alignment()   const noexcept { return alignment; }
    const Orientation & get_orientation() const noexcept { return orientation; }

    wstring get_wstring() const noexcept {
        wostringstream woss;
        woss << L"Text(" << Colorize::get_wstring() << L", x=" << get_x() << L", y=" << get_y()
             << L", alignment=" << alignment.get_integer() << L", orientation=" << orientation.get_integer() << L")";
        return woss.str(); }

    inline void log() const { wcout << get_wstring() << endl; }
};


extern "C" {
    Text * text_new   (float x, float y, Colorize * c, int orientation, int alignment) noexcept { return new Text(x, y, *c, Orientation(orientation), Alignment(alignment)); }
    Text * text_copy  (Text * t) noexcept { return new Text(*t); }
    void   text_delete(Text * t) noexcept { delete t; }

    void   text_set_position   (Text * t, float x, float y) noexcept { t->set_position(x, y); }
    void   text_set_alignment  (Text * t, int a) noexcept { t->set_alignment(Alignment(a)); }
    void   text_set_orientation(Text * t, int o) noexcept { t->set_orientation(Orientation(o)); }

    float  text_get_x          (Text * t) noexcept { return t->get_x(); }
    float  text_get_y          (Text * t) noexcept { return t->get_y(); }
    int    text_get_alignment  (Text * t) noexcept { return t->get_alignment().get_integer(); }
    int    text_get_orientation(Text * t) noexcept { return t->get_orientation().get_integer(); }

    void   text_rescale_x(Text * t, float lo, float hi, size_t width,  float delta) noexcept { t->rescale_x({lo, hi}, width,  delta); }
    void   text_rescale_y(Text * t, float lo, float hi, size_t height, float delta) noexcept { t->rescale_y({lo, hi}, height, delta); }

    void   text_fix_background(Text * t, Pixel * p) noexcept { t->fix_background(*p); }

    const wchar_t * text_get_wstring(Text * t) noexcept { return wstring_to_cstring(t->get_wstring()); }
}
