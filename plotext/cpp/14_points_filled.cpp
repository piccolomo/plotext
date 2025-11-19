// PointsFilled - manages a collection of PointFilled objects with utilities and output helpers
class PointsFilled : public Vector<PointFilled> {
public:
    using Vector<PointFilled>::append;
    using Vector<PointFilled>::at;

    // lifecycle
    PointsFilled() = default;
    PointsFilled(const size_t & size) : Vector<PointFilled>(size) {}
    PointsFilled(const PointsFilled & p) : Vector<PointFilled>(p) {}
    PointsFilled(PointsFilled && p) noexcept : Vector<PointFilled>(std::move(p)) {}
    ~PointsFilled() = default;

    // assignment
    PointsFilled & operator=(const PointsFilled & other) { Vector<PointFilled>::operator=(other); return *this; }
    PointsFilled & operator=(const Vector<PointFilled> & other) { Vector<PointFilled>::operator=(other); return *this; }

    inline PointsFilled copy() const noexcept { return PointsFilled(*this); }

    // capacity / clear
    inline void clear() noexcept { Vector<PointFilled>::clear(); } // clear all

    // append helpers
    inline void append(const PointFilled & p) noexcept { Vector<PointFilled>::append(p); } // add one
    void append(const Vector<PointFilled> & P) noexcept { this->reserve(this->get_length() + P.get_length()); Vector<PointFilled>::append(P); } // add many
    inline void append(std::initializer_list<PointFilled> list) noexcept { this->reserve(this->get_length() + list.size()); for (const auto & p : list) append(p); } // init-list

    // setters
    inline void set_point(const size_t & index, const PointFilled & p) noexcept { this->at(index) = p; }
    inline void set_point(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept { this->at(index).set_main(xi, yi, m); }
    inline void set_fill(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept { this->at(index).set_fill(xi, yi, m); }

    // drawing helpers
    inline void fix_background(Pixel & pixel) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).fix_background(pixel); } // fix bg

    // size / access
    inline size_t get_length() const noexcept { return Vector<PointFilled>::get_length(); } // number of points

    // bounds (min/max across points, optional axis filter)
    float get_xmin(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmin = inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax) xmin = std::min(xmin, at(i).get_xmin());
        return xmin;}
    float get_xmax(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmax = -inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax) xmax = std::max(xmax, at(i).get_xmax());
        return xmax;}
    float get_ymin(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymin = inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax) ymin = std::min(ymin, at(i).get_ymin());
        return ymin;}
    float get_ymax(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymax = -inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax) ymax = std::max(ymax, at(i).get_ymax());
        return ymax;}

    // transformations
    inline void log_x() noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).log_x(); }
    inline void log_y() noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).log_y(); }
    inline void add_offset(const size_t & dx, const size_t & dy) noexcept { for (size_t i = 0; i < get_length(); ++i) at(i).add_offset(dx, dy); }

    inline void rescale_x(const std::pair<float, float> & xlim, const size_t & width, const float & delta) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).rescale_x(xlim, width, delta); }
    inline void rescale_y(const std::pair<float, float> & ylim, const size_t & height, const float & delta) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).rescale_y(ylim, height, delta); }

    // filter points inside matrix
    inline void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<PointFilled> out; out.reserve(get_length());
        for (auto & pf : *this) if (pf.in_matrix(width, height)) out.append(pf);
        *this = std::move(out); }

    // create connected lines between consecutive PointFilled
    Vector<PointFilled> get_lines(size_t method = 0) const {
        size_t length = get_length();
        if (length < 2) return Vector<PointFilled>(0);
        Vector<Vector<PointFilled>> segments(length); size_t total = 0;
        for (size_t i = 0; i < length - 1; ++i) {
            bool last = (i == length - 2);
            Vector<PointFilled> seg = at(i).get_line(at(i + 1), last, method);
            total += seg.get_length();
            segments.move_back(std::move(seg)); }
        Vector<PointFilled> result(total);
        for (Vector<PointFilled> & seg : segments) result.move_back(std::move(seg));
        return result; }

    // filled-length and points
    inline size_t get_filled_length(bool method) const noexcept {
        size_t size = 0; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) size += at(i).get_line_length(at(i).get_fill(), method);
        return size; }

    inline Points get_filled_points(size_t method) const noexcept {
        size_t total = get_filled_length(method); Points result(total);
        size_t length = get_length();
        for (size_t i = 0; i < length; ++i) {
            const PointFilled & pf = at(i);
            if (pf.no_fill()) result.append(pf);
            else result.append(pf.get_filled_line(method));}
        return result; }

    // output / logging
    std::wstring get_wstring(const bool & fill = false) const noexcept {
        std::wostringstream woss; size_t length = get_length();
        woss << L" Points " << length << L" ";
        for (size_t i = 0; i < length; ++i) { woss << at(i).get_wstring(fill); if (i + 1 < length) woss << L", "; }
        return woss.str(); }
    inline std::string get_string(const bool & fill = false) const noexcept { return wstring_to_string(get_wstring(fill)); }
    inline void log(const bool & fill = false) const noexcept { std::wcout << get_wstring(fill) << std::endl; }
    friend wostream & operator<<(wostream & os, const PointsFilled & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const PointsFilled & c) noexcept {os << c.get_string(); return os;}


};