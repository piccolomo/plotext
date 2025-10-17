class PointsFilled : public Vector<PointFilled> {
public:
    using Vector<PointFilled>::append;

    PointsFilled() = default;

    // Constructor with size reservation
    PointsFilled(const size_t & size) : Vector<PointFilled>(size) { }

    // Copy constructor
    PointsFilled(const PointsFilled & p) : Vector<PointFilled>(p) {}

    // Move constructor
    PointsFilled(PointsFilled && p) noexcept : Vector<PointFilled>(std::move(p)) {}

    ~PointsFilled() {}

    // Copy assignment
    PointsFilled & operator=(const PointsFilled & other) {
        Vector<PointFilled>::operator=(other);
        return *this;}

    void clear() { Vector<PointFilled>::clear(); }

    // Add a filled point
    void add_point(const PointFilled & p) noexcept { this->append(p); }

    // Append another PointsFilled collection
    void append(const Vector<PointFilled> & P) noexcept {for (size_t i = 0; i < P.get_length(); i++) append(P.at(i)); }

    //void append(const PointsFilled & P) noexcept { for (size_t i = 0; i < P.get_length(); i++) append(P.at(i)); }

    void append(std::initializer_list<PointFilled> list) noexcept { for (const auto& p : list) append(p);}

    // Set a filled point at a specific index
    void set_point(const size_t & index, const PointFilled & p) noexcept { this->at(index) = p; }

    void set_point(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept { this->at(index).set_main(xi, yi, m); }

    void set_fill(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept { this->at(index).set_fill(xi, yi, m); }

    // Fix background for all points using the given Pixel
    void fix_background(Pixel& pixel) {for (size_t i = 0; i < this->get_length(); i++) this->at(i).fix_background(pixel); }

    // Get the number of points
    size_t get_length() const noexcept { return Vector<PointFilled>::get_length(); }

    // Get a point at a specific index (copy)
    PointFilled get(const size_t & i) const noexcept { return this->at(i); }

    // Get a point reference at a specific index
    PointFilled & at(const size_t & i) noexcept { return Vector<PointFilled>::at(i); }
    const PointFilled & at(const size_t & i) const noexcept { return Vector<PointFilled>::at(i); }

    // Get minimum/maximum x and y across all points (including fills)
    float get_xmin() const noexcept {
        float xmin = std::numeric_limits<float>::max();
        for (size_t i = 0; i < this->get_length(); i++) xmin = std::min(xmin, this->at(i).get_xmin());
        return xmin; }

    float get_xmax() const noexcept {
        float xmax = std::numeric_limits<float>::lowest();
        for (size_t i = 0; i < this->get_length(); i++) xmax = std::max(xmax, this->at(i).get_xmax());
        return xmax; }

    float get_ymin() const noexcept {
        float ymin = std::numeric_limits<float>::max();
        for (size_t i = 0; i < this->get_length(); i++) ymin = std::min(ymin, this->at(i).get_ymin());
        return ymin; }

    float get_ymax() const noexcept {
        float ymax = std::numeric_limits<float>::lowest();
        for (size_t i = 0; i < this->get_length(); i++) ymax = std::max(ymax, this->at(i).get_ymax());
        return ymax; }

    // Transformations
    void log_x() { for (size_t i = 0; i < this->get_length(); i++) this->at(i).log_x(); }
    void log_y() { for (size_t i = 0; i < this->get_length(); i++) this->at(i).log_y(); }
    void rescale_x(const std::pair<float, float>& xlim, const size_t& width, const float& delta) { for (size_t i = 0; i < this->get_length(); i++) this->at(i).rescale_x(xlim, width, delta); }
    void rescale_y(const std::pair<float, float>& ylim, const size_t& height, const float& delta) { for (size_t i = 0; i < this->get_length(); i++) this->at(i).rescale_y(ylim, height, delta); }

    void add_offset(const size_t & dx, const size_t & dy) {for (size_t i = 0; i < get_length(); i++) at(i).add_offset(dx, dy); }


    // Create connected lines between multiple PointFilled
    Vector<PointFilled> get_lines() const {
        size_t total = 0;
        size_t length = get_length();

        Vector<Vector<PointFilled>> segments(get_length());  // temporary storage

        for (size_t i = 0; i < length - 1; ++i) {
            const PointFilled & p1 = at(i);
            const PointFilled & p2 = at(i + 1);
            bool last = (i == length - 2); 

            //p1.log(1); p2.log(1); nl();
            Vector<PointFilled> seg(p1.get_two_lines(p2, last));
            //nl();
            total += seg.get_length();
            segments.move_back(move(seg));}

        Vector<PointFilled> result(total + 1);
        for (auto & seg : segments) {result.move_back(move(seg));}

        return result;}

    // size_t get_filled_lines_length() const {
    //     size_t length = 0; for (auto & pf : *this) length += pf.get_filled_line_length();
    //     return length;}


    // Vector<Point> get_filled_lines() const {
    //     Vector<Vector<Point>> segments(get_length()); 
    //     for (auto & pf : *this) segments.move_back(pf.get_filled_line());

    //     size_t total_length = 0; for (auto & seg : segments) total_length += seg.get_length();

    //     Vector<Point> result(total_length); for (auto & seg : segments) {result.move_back(move(seg));}

    //     return result;}


    inline void plot() {
        Vector<PointFilled> out = get_lines();
        Vector<PointFilled>::operator=(out);}

    // Add a Point to the collection, creating or updating a Dot
    void squash(PointsMap & map) {
        Vector<PointFilled> out(get_length()); 

        for (PointFilled & pf: *this) {
            size_t c = pf.get_col(), r = pf.get_row();
            bool present = map.is_present(c, r);

            if (present) {
                size_t index = map.get_index(c, r);
                PointFilled & previous = out.at(index);
                bool close = pf.is_close(previous); 
                if (pf.is_close(previous)) {previous.set_type(none);}
            };    
            
            map.set_index(c, r, out.get_length());
            out.append(pf);};

        Vector<PointFilled>::clear();
        for (auto & el: out) if (not el.is_none()) append(el);
    }


    // inline void fill(Vector<Point> & points) const {
    //     Vector<Point> out = get_filled_lines(); 
    //     points.move_back(move(out));}

    // Get string representation of all points
    std::wstring get_wstring(const bool & fill = false) const { 
        std::wostringstream woss; 
        size_t length = get_length(); 
        woss << L" Points " << length << " "; 
        for (size_t i = 0; i < length; ++i) {woss << at(i).get_wstring(fill) << ", ";}
        return woss.str();} 

    // Log points to output
    void log(const bool & fill = false) const { std::wcout << get_wstring() << std::endl; }

    // Iterators
    const PointFilled * begin() const { return Vector<PointFilled>::begin(); }
    PointFilled * begin() { return Vector<PointFilled>::begin(); }

    const PointFilled * end() const { return Vector<PointFilled>::end(); }
    PointFilled * end() { return Vector<PointFilled>::end(); }

    // Copy container
    PointsFilled copy() const { PointsFilled newPoints(*this); return newPoints; }
};


// PointsFilled flatten(const Vector<PointsFilled> & signals) {
//     PointsFilled result;

//     // Precompute total length to avoid multiple reallocations
//     size_t total_length = 0;
//     for (const auto& signal : signals)
//         total_length += signal.get_length();
//     result.reserve(total_length);

//     // Append all points
//     for (const auto& signal : signals) {
//         for (const auto& pf : signal)
//             result.append(pf);  // copy each PointFilled
//     }

//     return result;
// }


