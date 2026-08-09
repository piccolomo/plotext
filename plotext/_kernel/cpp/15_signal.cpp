// Signal: a FilledPoints with plotting metadata (xside/yside, label, marker, fill_method, line_method). The user-facing handle the plotter pipeline operates on. All transformations (rescale/log/add_offset/fix_background/select_in_matrix) walk both main + fill of every FilledPoint.

class Signal : public FilledPoints {
private:
    bool          xside       = false;     // false = lower x axis, true = upper
    bool          yside       = false;     // false = left y axis,  true = right
    Matrix      * label       = nullptr;   // owned, destroyed in ~Signal, deep-copied on set/copy
    Marker      * marker      = nullptr;   // owned, destroyed in ~Signal, deep-copied on set/copy
    bool          fill_method = false;     // false = simple, true = full
    bool          line_method = false;     // false = simple, true = full

public:
    Signal() noexcept : FilledPoints() {}
    Signal(size_t capacity) noexcept : FilledPoints(capacity) {}
    ~Signal() noexcept { delete label; delete marker; }

    Signal(const Signal & o) noexcept
        : FilledPoints(o), xside(o.xside), yside(o.yside),
          label(o.label ? new Matrix(*o.label) : nullptr),
          marker(o.marker ? o.marker->copy() : nullptr),
          fill_method(o.fill_method), line_method(o.line_method) {}
    Signal(Signal && o) noexcept
        : FilledPoints(std::move(o)), xside(o.xside), yside(o.yside), label(o.label),
          marker(o.marker), fill_method(o.fill_method), line_method(o.line_method) { o.label = nullptr; o.marker = nullptr; }
    Signal & operator=(const Signal & o) noexcept {
        if (this != &o) {
            FilledPoints::operator=(o);
            xside = o.xside; yside = o.yside;
            delete label; label = o.label ? new Matrix(*o.label) : nullptr;
            delete marker; marker = o.marker ? o.marker->copy() : nullptr;
            fill_method = o.fill_method; line_method = o.line_method; }
        return *this; }
    Signal & operator=(Signal && o) noexcept {
        if (this != &o) {
            FilledPoints::operator=(std::move(o));
            xside = o.xside; yside = o.yside;
            delete label; label = o.label; o.label = nullptr;
            delete marker; marker = o.marker; o.marker = nullptr;
            fill_method = o.fill_method; line_method = o.line_method; }
        return *this; }

    void clear() noexcept { FilledPoints::clear(); xside = false; yside = false; delete label; label = nullptr; delete marker; marker = nullptr; }

    // ---- field accessors ----

    bool             get_xside()       const noexcept { return xside; }
    bool             get_yside()       const noexcept { return yside; }
    Matrix *         get_label()       const noexcept { return label; }
    Marker *         get_marker_ptr()  const noexcept { return marker; }
    bool             get_fill_method() const noexcept { return fill_method; }
    bool             get_line_method() const noexcept { return line_method; }

    void set_xside       (bool v)              noexcept { xside = v; }
    void set_yside       (bool v)              noexcept { yside = v; }
    void set_label       (Matrix * m)          noexcept { delete label; label = m ? new Matrix(*m) : nullptr; }
    void set_marker      (Marker * m)          noexcept { delete marker; marker = m ? m->copy() : nullptr; }
    void set_fill_method (bool v)              noexcept { fill_method = v; }
    void set_line_method (bool v)              noexcept { line_method = v; }

    // ---- index-style point setters ----

    void set_main      (size_t i, float x, float y, Marker * m) noexcept { at(i).set_main(x, y, m); }
    void set_fill_point(size_t i, float x, float y, Marker * m) noexcept { at(i).set_fill(x, y, m); }
    void set_connected (size_t i, bool v)                       noexcept { at(i).set_connected(v); }
    bool is_connected  (size_t i)                         const noexcept { return at(i).is_connected(); }

    // ---- per-Signal transforms (apply main + fill of every FilledPoint) ----

    void add_offset(size_t dx, size_t dy) noexcept {
        for (size_t i = 0; i < get_length(); ++i) { at(i).add_offset(dx, dy); at(i).get_fill().add_offset(dx, dy); } }

    void log_x() noexcept { for (size_t i = 0; i < get_length(); ++i) { at(i).log_x(); at(i).get_fill().log_x(); } }
    void log_y() noexcept { for (size_t i = 0; i < get_length(); ++i) { at(i).log_y(); at(i).get_fill().log_y(); } }

    void rescale_x(const pair<float, float> & lim, size_t width,  float delta) noexcept {
        for (size_t i = 0; i < get_length(); ++i) { at(i).rescale_x(lim, width,  delta); at(i).get_fill().rescale_x(lim, width,  delta); } }
    void rescale_y(const pair<float, float> & lim, size_t height, float delta) noexcept {
        for (size_t i = 0; i < get_length(); ++i) { at(i).rescale_y(lim, height, delta); at(i).get_fill().rescale_y(lim, height, delta); } }

    void fix_background(const Pixel & p) noexcept {
        for (size_t i = 0; i < get_length(); ++i) { Marker * m = at(i).get_marker(); if (m) m->fix_background(p); } }

    void select_in_matrix(size_t width, size_t height) noexcept {
        FilledPoints kept(get_length());
        for (size_t i = 0; i < get_length(); ++i) if (at(i).in_matrix(width, height)) kept.append(at(i));
        FilledPoints::operator=(std::move(kept)); }

    // ---- bounds (filter by orthogonal range; returns 0 if no points match) ----

    float get_xmin(float ymin = -inf, float ymax = inf) const noexcept {
        float v = inf;
        for (size_t i = 0; i < get_length(); ++i)
            if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax)
                v = std::min(v, at(i).get_xmin());
        return v == inf ? 0 : v; }
    float get_xmax(float ymin = -inf, float ymax = inf) const noexcept {
        float v = -inf;
        for (size_t i = 0; i < get_length(); ++i)
            if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax)
                v = std::max(v, at(i).get_xmax());
        return v == -inf ? 0 : v; }
    float get_ymin(float xmin = -inf, float xmax = inf) const noexcept {
        float v = inf;
        for (size_t i = 0; i < get_length(); ++i)
            if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax)
                v = std::min(v, at(i).get_ymin());
        return v == inf ? 0 : v; }
    float get_ymax(float xmin = -inf, float xmax = inf) const noexcept {
        float v = -inf;
        for (size_t i = 0; i < get_length(); ++i)
            if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax)
                v = std::max(v, at(i).get_ymax());
        return v == -inf ? 0 : v; }

    // ---- append helpers ----

    void append(float x, float y, Marker * m) noexcept {
        FilledPoint fp(x, y, m);
        if (get_length() == 0) set_marker(m);         // remember the first marker as the signal's default
        FilledPoints::append(fp); }

    void append(const Signal & other) noexcept {
        if (!marker && other.marker) set_marker(other.marker);   // inherit the other signal's master marker if we don't already have one
        FilledPoints::append(other); }

    // ---- plotting ----

    // plot(): expand consecutive FilledPoints into a denser line (current minimal version: ignores connected flag, ignores method flag).
    void plot() noexcept {
        const size_t n = get_length();
        if (n < 2) return;
        size_t total = 1;
        for (size_t i = 1; i < n; ++i) {
            if (at(i).is_connected()) {
                const size_t main_n = at(i - 1).get_line_size(at(i), line_method);
                const size_t fill_n = at(i - 1).get_fill().get_line_size(at(i).get_fill(), fill_method);
                total += std::max(main_n, fill_n) - 1; }
            else
                total += 1; }
        FilledPoints out(total);
        out.append(at(0));
        for (size_t i = 1; i < n; ++i) {
            if (at(i).is_connected()) {
                Vector<Point> main_line = at(i - 1).get_line(at(i), true, line_method);
                Vector<Point> fill_line = at(i - 1).get_fill().get_line(at(i).get_fill(), true, fill_method);
                const size_t k = std::max(main_line.get_length(), fill_line.get_length());
                if (main_line.get_length() < k) main_line.stretch(k);
                if (fill_line.get_length() < k) fill_line.stretch(k);
                for (size_t j = 1; j < k; ++j) out.append(FilledPoint(main_line.at(j), fill_line.at(j))); }
            else
                out.append(at(i)); }
        FilledPoints::operator=(std::move(out)); }

    // get_points(): flatten every FilledPoint to its filled line of Points. Two-pass: first count total samples, then allocate exactly + fill (mirrors FilledPoints::get_points and the legacy implementation). Honors fill_method so each main↔fill segment is densified the same way the user asked for.
    Points get_points() const noexcept {
        const size_t n = get_length();
        size_t total = 0;
        for (size_t i = 0; i < n; ++i) total += at(i).has_fill() ? at(i).get_line_size(at(i).get_fill(), fill_method) : 1;
        Points out(total);
        for (size_t i = 0; i < n; ++i) {
            Vector<Point> seg = at(i).get_filled_line(fill_method);
            for (size_t j = 0; j < seg.get_length(); ++j) out.append(seg.at(j)); }
        return out; }

    // ---- output / logging ----

    // The label as one line of plain text, its trailing new line dropped, for the log line below
    wstring get_label_wstring() const noexcept {
        if (label == nullptr)
            return L"no label";
        wstring out = label->get_wstring(true);
        while (!out.empty() && out.back() == L'\n')
            out.pop_back();
        return L"label " + out; }

    wstring get_wstring(bool full = false) const noexcept {
        wostringstream os;
        os << L"Plotext signal: length " << get_length()
           << L", xside " << (xside ? L"upper" : L"lower")
           << L", yside " << (yside ? L"right" : L"left")
           << L", " << get_label_wstring()
           << L", line method " << (line_method ? L"full" : L"simple")
           << L", fill method " << (fill_method ? L"full" : L"simple");
        if (full)
            for (size_t i = 0; i < get_length(); ++i)
                os << L"\n  " << i << L" " << (i > 0 && at(i).is_connected() ? L"↑" : L" ")
                   << L" " << at(i).get_wstring();
        return os.str(); }

    inline void log() const noexcept { wcout << get_wstring() << endl; }
};


extern "C" {
    Signal * signal_new   (size_t length) noexcept { return new Signal(length); }
    void     signal_delete(Signal * s) noexcept { delete s; }
    Signal * signal_copy  (Signal * s) noexcept { return s ? new Signal(*s) : nullptr; }
    void     signal_clear (Signal * s) noexcept { s->clear(); }

    bool             signal_get_xside       (Signal * s) noexcept { return s->get_xside(); }
    bool             signal_get_yside       (Signal * s) noexcept { return s->get_yside(); }
    Matrix *         signal_get_label       (Signal * s) noexcept { Matrix * m = s->get_label(); return m ? new Matrix(*m) : nullptr; }
    Marker *         signal_get_marker      (Signal * s) noexcept { Marker * m = s->get_marker_ptr(); return m ? m->copy() : nullptr; }
    bool             signal_get_fill_method (Signal * s) noexcept { return s->get_fill_method(); }
    bool             signal_get_line_method (Signal * s) noexcept { return s->get_line_method(); }

    void signal_set_xside       (Signal * s, bool v)             noexcept { s->set_xside(v); }
    void signal_set_yside       (Signal * s, bool v)             noexcept { s->set_yside(v); }
    void signal_set_label       (Signal * s, Matrix * m)         noexcept { s->set_label(m); }
    void signal_set_marker      (Signal * s, Marker * m)         noexcept { s->set_marker(m); }
    void signal_set_fill_method (Signal * s, bool v)             noexcept { s->set_fill_method(v); }
    void signal_set_line_method (Signal * s, bool v)             noexcept { s->set_line_method(v); }

    void signal_append_point  (Signal * s, float x, float y, Marker * m)              noexcept { s->append(x, y, m); }
    void signal_append        (Signal * s, Signal * other)                            noexcept { s->append(*other); }
    void signal_set_point     (Signal * s, size_t i, float x, float y, Marker * m)    noexcept { s->set_main(i, x, y, m); }
    void signal_set_fill_point(Signal * s, size_t i, float x, float y, Marker * m)    noexcept { s->set_fill_point(i, x, y, m); }
    void signal_set_connected (Signal * s, size_t i, bool v)                          noexcept { s->set_connected(i, v); }
    bool signal_is_connected  (Signal * s, size_t i)                                  noexcept { return s->is_connected(i); }

    FilledPoint * signal_get_point     (Signal * s, size_t i) noexcept { return new FilledPoint(s->at(i)); }
    Point       * signal_get_fill_point(Signal * s, size_t i) noexcept { return new Point(s->at(i).get_fill()); }

    void signal_fix_background (Signal * s, Pixel * p)                                  noexcept { s->fix_background(*p); }
    void signal_log_x          (Signal * s)                                             noexcept { s->log_x(); }
    void signal_log_y          (Signal * s)                                             noexcept { s->log_y(); }
    void signal_rescale_x      (Signal * s, float l, float h, size_t b, float d)        noexcept { s->rescale_x({l, h}, b, d); }
    void signal_rescale_y      (Signal * s, float l, float h, size_t b, float d)        noexcept { s->rescale_y({l, h}, b, d); }
    void signal_add_offset     (Signal * s, size_t dx, size_t dy)                       noexcept { s->add_offset(dx, dy); }
    void signal_select_in_matrix(Signal * s, size_t w, size_t h)                        noexcept { s->select_in_matrix(w, h); }

    float signal_get_xmin(Signal * s, float ymin, float ymax) noexcept { return s->get_xmin(ymin, ymax); }
    float signal_get_xmax(Signal * s, float ymin, float ymax) noexcept { return s->get_xmax(ymin, ymax); }
    float signal_get_ymin(Signal * s, float xmin, float xmax) noexcept { return s->get_ymin(xmin, xmax); }
    float signal_get_ymax(Signal * s, float xmin, float xmax) noexcept { return s->get_ymax(xmin, xmax); }

    void   signal_assign     (Signal * s, Signal * other) noexcept { *s = *other; }
    void   signal_plot       (Signal * s)                  noexcept { s->plot(); }
    Points*signal_get_points (Signal * s)                  noexcept { return new Points(s->get_points()); }
    size_t signal_get_length (Signal * s)                  noexcept { return s->get_length(); }
    const wchar_t * signal_get_wstring(Signal * s, bool fill) noexcept { return wstring_to_cstring(s->get_wstring(fill)); }
}
