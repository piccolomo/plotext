// FilledPoints: a collection of FilledPoint built on Vector. Provides flatten-to-Points helper for matrix insertion.

class FilledPoints : public Vector<FilledPoint> {
public:
    using Vector<FilledPoint>::append;                                          // bring inherited append(FilledPoint) overload back into scope (the FilledPoints overload below would otherwise hide it)

    FilledPoints() noexcept : Vector<FilledPoint>() {}
    explicit FilledPoints(size_t capacity) : Vector<FilledPoint>(capacity) {}

    // Append every FilledPoint from another FilledPoints. Reserves up-front so the inherited Vector::append loop never trips set_length's capacity assert.
    inline void append(const FilledPoints & other) noexcept {
        reserve(get_length() + other.get_length());
        Vector<FilledPoint>::append(other); }

    // Flatten every FilledPoint to its filled line of Points. Two-pass: first count total samples, then allocate exactly + fill.
    inline Vector<Point> get_points() const noexcept {
        const size_t n = get_length();
        size_t total = 0;
        for (size_t i = 0; i < n; ++i) total += at(i).has_fill() ? at(i).get_line_size(at(i).get_fill()) : 1;

        Vector<Point> out(total);
        for (size_t i = 0; i < n; ++i) {
            Vector<Point> seg = at(i).get_filled_line();
            for (size_t j = 0; j < seg.get_length(); ++j) out.append(seg.at(j)); }
        return out; }

    inline void log() const {
        wcout << L"FilledPoints (" << get_length() << L"):" << endl;
        for (size_t i = 0; i < get_length(); ++i) { wcout << L"  "; at(i).log(); } }
};


// Stamp every FilledPoint in the collection. Declared inside Matrix's class body in 07_matrix.cpp; defined here because FilledPoints must be fully declared first.
inline void Matrix::insert(const FilledPoints & fps) noexcept {
    for (size_t i = 0; i < fps.get_length(); ++i) insert(fps.at(i)); }
