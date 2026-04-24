// PointsFilled: collection of PointFilled objects built on Vector<PointFilled>, with bounds, transforms and line generation

class PointsFilled : public Vector<PointFilled> {
public:
    using Vector<PointFilled>::append;
    using Vector<PointFilled>::at;

    // ------------ lifecycle ------------

    // Default constructor
    PointsFilled() = default;

    // Construct with the given capacity
    PointsFilled(const size_t & size) : Vector<PointFilled>(size) {}

    // Copy constructor
    PointsFilled(const PointsFilled & p) : Vector<PointFilled>(p) {}

    // Move constructor
    PointsFilled(PointsFilled && p) noexcept : Vector<PointFilled>(std::move(p)) {}

    // Destructor
    ~PointsFilled() noexcept {}

    // ------------ assignment ------------

    // Copy assignment
    PointsFilled & operator=(const PointsFilled & other) { Vector<PointFilled>::operator=(other); return *this; }

    // Move assignment
    PointsFilled & operator=(PointsFilled && other) noexcept { Vector<PointFilled>::operator=(std::move(other)); return *this; }

    // Assign from a plain Vector<PointFilled>
    PointsFilled & operator=(const Vector<PointFilled> & other) { Vector<PointFilled>::operator=(other); return *this; }

    // Deep copy
    inline PointsFilled copy() const noexcept { return PointsFilled(*this); }

    // ------------ capacity / clear ------------

    // Clear every point
    inline void clear() noexcept { Vector<PointFilled>::clear(); }

    // ------------ append helpers ------------

    // Append a single PointFilled
    inline void append(const PointFilled & p) noexcept { Vector<PointFilled>::append(p); }

    // Append a PointFilled built from coordinates and a marker
    inline void append(const float & xi, const float & yi, const Marker & m = Marker()) noexcept { Vector<PointFilled>::append({xi, yi, m}); }

    // Append a batch of PointFilled, reserving capacity first
    void append(const Vector<PointFilled> & P) noexcept { this->reserve(this->get_length() + P.get_length()); Vector<PointFilled>::append(P); }

    // Append from an initializer list
    inline void append(std::initializer_list<PointFilled> list) noexcept { this->reserve(this->get_length() + list.size()); for (const auto & p : list) append(p); }

    // ------------ setters ------------

    // Replace the PointFilled at the given index
    inline void set_point(const size_t & index, const PointFilled & p) noexcept { this->at(index) = p; }

    // Update the main point at the given index
    inline void set_point(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept {
        this->at(index).set_main(xi, yi, m); }

    // Update the fill point at the given index
    inline void set_fill(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept { this->at(index).set_fill(xi, yi, m); }

    // ------------ drawing helpers ------------

    // Fix the background of every point against the given pixel
    inline void fix_background(const Pixel & pixel) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).fix_background(pixel); }

    // ------------ size / access ------------

    // Number of points
    inline size_t get_length() const noexcept { return Vector<PointFilled>::get_length(); }

    // ------------ bounds (min/max across points, optional axis filter) ------------

    // Minimum x across all points whose y is within [ymin, ymax]
    float get_xmin(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmin = inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax) xmin = std::min(xmin, at(i).get_xmin());
        return xmin;}

    // Maximum x across all points whose y is within [ymin, ymax]
    float get_xmax(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmax = -inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax) xmax = std::max(xmax, at(i).get_xmax());
        return xmax;}

    // Minimum y across all points whose x is within [xmin, xmax]
    float get_ymin(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymin = inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax) ymin = std::min(ymin, at(i).get_ymin());
        return ymin;}

    // Maximum y across all points whose x is within [xmin, xmax]
    float get_ymax(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymax = -inf; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax) ymax = std::max(ymax, at(i).get_ymax());
        return ymax;}

    // ------------ transformations ------------

    // Apply log10 to x of every point
    inline void log_x() noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).log_x(); }

    // Apply log10 to y of every point
    inline void log_y() noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).log_y(); }

    // Add (dx, dy) offset to every point
    inline void add_offset(const size_t & dx, const size_t & dy) noexcept { for (size_t i = 0; i < get_length(); ++i) at(i).add_offset(dx, dy); }

    // Rescale x of every point
    inline void rescale_x(const std::pair<float, float> & xlim, const size_t & width, const float & delta) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).rescale_x(xlim, width, delta); }

    // Rescale y of every point
    inline void rescale_y(const std::pair<float, float> & ylim, const size_t & height, const float & delta) noexcept { for (size_t i = 0; i < this->get_length(); ++i) this->at(i).rescale_y(ylim, height, delta); }

    // Keep only points whose main and fill both fall inside a matrix of the given size
    inline void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<PointFilled> out; out.reserve(get_length());
        for (auto & pf : *this) if (pf.in_matrix(width, height)) out.append(pf);
        *this = std::move(out); }

    // Create connected lines between consecutive PointFilled
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

    // Total length of all filled lines (main -> fill) combined
    inline size_t get_filled_length(bool method) const noexcept {
        size_t size = 0; size_t length = get_length();
        for (size_t i = 0; i < length; ++i) size += at(i).get_line_length(at(i).get_fill(), method);
        return size; }

    // Expand every PointFilled to its filled line of Points
    inline Points get_points(size_t method) const noexcept {
        size_t total = get_filled_length(method);
        Points result(total);
        size_t length = get_length();
        for (size_t i = 0; i < length; ++i) {
            const PointFilled & pf = at(i);
            if (pf.no_fill()) {result.append(pf);}
            else result.append(pf.get_filled_line(method));}
        return result; }

    // ------------ output / logging ------------

    // Get wide string summary "PointsFilled N: ..."
    std::wstring get_wstring(const bool & fill = false) const noexcept {
        std::wostringstream woss; size_t length = get_length();
        woss << L"PointsFilled " << length << L": ";
        for (size_t i = 0; i < length; ++i) { woss << at(i).get_wstring(fill); if (i + 1 < length) woss << L", "; }
        return woss.str(); }

    // Get narrow string summary
    inline std::string get_string(const bool & fill = false) const noexcept { return wstring_to_string(get_wstring(fill)); }

    // Log to wcout
    inline void log(const bool & fill = false) const noexcept { std::wcout << get_wstring(fill) << std::endl; }

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const PointsFilled & c) noexcept {os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const PointsFilled & c) noexcept {os << c.get_string(); return os;}
};
