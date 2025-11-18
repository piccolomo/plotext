class Points : public Vector<Point> {
public:
    using Vector<Point>::append;

    // Constructor with size reservation
    Points(const size_t & size) : Vector<Point>(size) {}

    // Copy constructor 
    Points(const Points & p) : Vector<Point>(p) {}

    // Move constructor 
    Points(Points && p) noexcept : Vector<Point>(std::move(p)) {}

    ~Points() {}

    // Copy assignment
    Points & operator=(const Points & other) {
        Vector<Point>::operator=(other);
        return *this;}

    // Assignment from a Vector<Point>
    Points & operator=(const Vector<Point> & other) {
        Vector<Point>::operator=(other);
        return *this;}

    // Clear all points
    void clear() { Vector<Point>::clear(); }

    // Append a single Point
    void append(const Point & p) noexcept { Vector<Point>::append(p); }

    // Append another vector of Points
    void append(const Vector<Point> & P) noexcept {
        Vector<Point>::reserve(get_length() + P.get_length());
        Vector<Point>::append(P);}

    // // Append from initializer list
    // void append(std::initializer_list<Point> list) noexcept {
    //     for (const auto & p : list) append(p);}

    // // Set a point at a given index
    // void set_point(const size_t & index, const Point & p) noexcept { this->at(index) = p; }

    // // Set directly with coordinates and marker
    // void set_point(const size_t & index, const float & xi, const float & yi, const Marker & m) noexcept {
    //     this->at(index).set_main(xi, yi, m);}

    // Fix background of all points using a Pixel
    void fix_background(Pixel & pixel) {
        for (size_t i = 0; i < this->get_length(); i++)
            this->at(i).fix_background(pixel);}

    // Get the number of points
    size_t get_length() const noexcept { return Vector<Point>::get_length(); }

    // // Get point reference by index
    // Point & at(const size_t & i) noexcept { return Vector<Point>::at(i); }
    // const Point & at(const size_t & i) const noexcept { return Vector<Point>::at(i); }

   
     void add_offset(const size_t & dx, const size_t & dy) noexcept {
        for (size_t i = 0; i < get_length(); i++) at(i).add_offset(dx, dy);}

    // Select points within matrix bounds
    void select_in_matrix(const size_t & width, const size_t & height) noexcept {
        Vector<Point> out(get_length());
        for (const Point & p : *this)
            if (p.in_matrix(width, height))
                out.append(p);
        *this = out;}

    // // Create connected lines between multiple Points
    // Vector<Point> get_lines(size_t method = 0) const {
    //     size_t total = 0;
    //     size_t length = get_length();

    //     Vector<Vector<Point>> segments(get_length());  // temporary storage

    //     for (size_t i = 0; i < length - 1; ++i) {

    //         const Point & p1 = at(i); 
    //         const Point & p2 = at(i + 1); 
    //         wprintf(L"getting line\n ", p1.get_wstring(), p2.get_wstring());
    //         bool last = (i == length - 2); 
    //         Vector<Point> seg = p1.get_line(p2, last, method);
    //         total += seg.get_length();
    //         segments.move_back(std::move(seg));}

    //     Vector<Point> result(total);
    //     for (Vector<Point> & seg : segments)
    //         result.move_back(std::move(seg));

    //     return result;}

    // Add a Point to the collection, creating or updating a Dot
    void squash(PointsMap & map) {
        Vector<Point> out(get_length()); 

        for (Point & current: *this) {
            size_t c = current.get_col(), r = current.get_row();
            bool is_present = map.is_present(c, r);

            if (is_present) {
                size_t index = map.get_index(c, r);
                Point & previous = out.at(index); 
                //current.log(); previous.log(); nl(); flush();
                bool close = current.is_close(previous); 
                if (close) {previous.set_type(none);}
            };    

            map.set_index(c, r, out.get_length()); // set map to current
            out.append(current);};


        Vector<Point>::clear();
        for (auto & el: out) if (not el.is_none()) {append(el);}}

    // String representation
    std::wstring get_wstring() const { 
        std::wostringstream woss; 
        size_t length = get_length(); 
        woss << L" Points " << length << " ["; 
        at(get_length() - 1).log();
        for (size_t i = 0; i < length; i++){woss << at(i).get_wstring() ; if (i != length - 1) {woss << ", ";}} 
        woss << "]";
        return woss.str();}

    // Log points to output
    void log() const { std::wcout << get_wstring() << std::endl; }

    // Iterators
    const Point * begin() const { return Vector<Point>::begin(); }
    Point * begin() { return Vector<Point>::begin(); }

    const Point * end() const { return Vector<Point>::end(); }
    Point * end() { return Vector<Point>::end(); }

    // Copy container
    Points copy() const { Points newPoints(*this); return newPoints; }
};



extern "C" {

    // --- Creation / Destruction ---
    Points * points_new(size_t n) noexcept { return new Points(n); }
    void points_delete(Points * p) noexcept { delete p; }
    void points_clear(Points * p) noexcept { p->clear(); }

    // --- Append operations ---
    void points_append_point(Points * p, const Point * point) noexcept { p->append(*point); }
    void points_append_points(Points * p, const Points * P) noexcept { p->append(*P); }

    // --- Getters ---
    Point * points_get_point(const Points * p, size_t index) noexcept { return new Point(p->at(index)); }
    size_t points_get_length(const Points * p) noexcept { return p->get_length(); }

    void points_fix_background(Points* s, Pixel* p) noexcept { s->fix_background(*p); }
    void points_add_offset(Points * p, size_t dx, size_t dy) noexcept { p->add_offset(dx, dy); }

    void points_select_in_matrix(Points * p, size_t width, size_t height) noexcept { p->select_in_matrix(width, height); }

    // --- Derived Data ---
    void points_squash(Points * s, PointsMap * map) noexcept {s->squash(*map); }


    void points_log(const Points * p) noexcept { p->log(); }

    // --- Copying ---
    Points * points_copy(const Points * p) noexcept { return new Points(p->copy()); }

}

