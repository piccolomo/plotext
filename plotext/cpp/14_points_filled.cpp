class PointsFilled : public Vector<PointFilled> {
public:
    using Vector<PointFilled>::append; 
    using Vector<PointFilled>::at; 

    PointsFilled() = default;

    // Constructor with size reservation
    PointsFilled(const size_t & size) : Vector<PointFilled>(size) {}

    // Copy constructor 
    PointsFilled(const PointsFilled & p) : Vector<PointFilled>(p) {}

    // Move constructor 
    PointsFilled(PointsFilled && p) noexcept : Vector<PointFilled>(std::move(p)) {}

    ~PointsFilled() {}

    // Copy assignment
    PointsFilled & operator=(const PointsFilled & other) {
        Vector<PointFilled>::operator=(other);
        return *this;}

        // Copy assignment
    PointsFilled & operator=(const Vector<PointFilled> & other) {
        Vector<PointFilled>::operator=(other);
        return *this;}

    void clear() { Vector<PointFilled>::clear(); }

    // Add a filled point
    void append(const PointFilled & p) noexcept {Vector<PointFilled>::append(p);}

    // Append another PointsFilled collection
    void append(const Vector<PointFilled> & P) noexcept {Vector<PointFilled>::reserve(get_length() + P.get_length()); Vector<PointFilled>::append(P);}

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

    // // Get a point reference at a specific index 
    // PointFilled & at(const size_t & i) noexcept {return Vector<PointFilled>::at(i);}
    // const PointFilled & at(const size_t & i) const noexcept {return Vector<PointFilled>::at(i);}

    // Get minimum/maximum x and y across all points (including fills)
    float get_xmin(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmin = inf; 
        for (size_t i = 0; i < this->get_length(); i++)
            if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax)
                xmin = std::min(xmin, at(i).get_xmin());
        return xmin;} 

    float get_xmax(const float & ymin = -inf, const float & ymax = inf) const noexcept {
        float xmax = -inf; 
        for (size_t i = 0; i < this->get_length(); i++)
            if (at(i).get_ymin() >= ymin && at(i).get_ymax() <= ymax)
                xmax = std::max(xmax, at(i).get_xmax());
        return xmax;} 

    float get_ymin(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymin = inf; 
        for (size_t i = 0; i < this->get_length(); i++)
            if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax)
                ymin = std::min(ymin, at(i).get_ymin());
        return ymin;} 

    float get_ymax(const float & xmin = -inf, const float & xmax = inf) const noexcept {
        float ymax = -inf; 
        for (size_t i = 0; i < this->get_length(); i++)
            if (at(i).get_xmin() >= xmin && at(i).get_xmax() <= xmax)
                ymax = std::max(ymax, at(i).get_ymax());
        return ymax;} 

    // Transformations
    void log_x() { for (size_t i = 0; i < this->get_length(); i++) this->at(i).log_x(); }
    void log_y() { for (size_t i = 0; i < this->get_length(); i++) this->at(i).log_y(); }
    void rescale_x(const std::pair<float, float>& xlim, const size_t& width, const float& delta) { for (size_t i = 0; i < this->get_length(); i++) this->at(i).rescale_x(xlim, width, delta); }
    void rescale_y(const std::pair<float, float>& ylim, const size_t& height, const float& delta) { for (size_t i = 0; i < this->get_length(); i++) this->at(i).rescale_y(ylim, height, delta); }

    void add_offset(const size_t & dx, const size_t & dy) {for (size_t i = 0; i < get_length(); i++) at(i).add_offset(dx, dy); }

    void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<PointFilled> out(get_length());
        for(PointFilled & pf: *this) {if (pf.in_matrix(width, height)) out.append(pf);}
        *this = out;}

    // Create connected lines between multiple PointFilled
    Vector<PointFilled> get_lines(size_t method = 0) const {
        size_t total = 0;
        size_t length = get_length();

        Vector<Vector<PointFilled>> segments(get_length());  // temporary storage

        for (size_t i = 0; i < length - 1; ++i) {
            const PointFilled & p1 = at(i); 
            const PointFilled & p2 = at(i + 1); 
            //write(L"getting line " + p1.get_wstring() + p2.get_wstring());
            //wcout << "line " << i << " "; p1.log(1); p2.log(1); nl();
            bool last = (i == length - 2); 
            //last = 1;
            Vector<PointFilled> seg = p1.get_line(p2, last, method);
            //seg.log(); nl(); nl();
            total += seg.get_length();
            segments.move_back(move(seg));}

        Vector<PointFilled> result(total);
        for (Vector<PointFilled> & seg : segments) {result.move_back(move(seg));}

        return result;}

    inline size_t get_filled_length(bool method) const noexcept {size_t size = 0, length = get_length(); for (size_t i = 0; i < length; i++) {size += at(i).get_line_length(at(i).get_fill(), method);} return size; }

    inline Points get_filled_points(size_t method) const noexcept {
        size_t total = get_filled_length(method);
        Points result(total);
        size_t length = get_length();
        for (size_t i = 0; i < length; i++) {
            const PointFilled & pf = at(i); 
            //pf.log();nl(); 
            if (pf.no_fill()) {result.append(pf);} 
            else {
                //pf.log(); sp(2); pf.get_filled_line(method).log(); flush(); nl(2);
                result.append(pf.get_filled_line(method));}} 
        return result;}

    // Get string representation of all points
    std::wstring get_wstring(const bool & fill = false) const { 
        std::wostringstream woss; 
        size_t length = get_length(); 
        woss << L" Points " << length << " "; 
        for (size_t i = 0; i < length; ++i) {woss << at(i).get_wstring(fill); if (i != length - 1) {woss << ", ";}}
        return woss.str();} 

    // Log points to output
    void log(const bool & fill = false) const {std::wcout << get_wstring() << std::endl;}

    // Iterators
    const PointFilled * begin() const {return Vector<PointFilled>::begin(); }
    PointFilled * begin() { return Vector<PointFilled>::begin(); }

    const PointFilled * end() const {return Vector<PointFilled>::end(); }
    PointFilled * end() { return Vector<PointFilled>::end(); }

    // Copy container
    PointsFilled copy() const {PointsFilled newPoints(*this); return newPoints;}
};



