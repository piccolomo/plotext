class Points {
private:
    vector<pair<Point, FillPoint>> points; // Container to store points

public:
    Points() = default; // Default constructor

    // Constructor with size reservation
    Points(const size_t & size = 10) {points.reserve(size);} 

    // Copy constructor
    Points(const Points & p) : points(p.points) {} 

    ~Points() {}

    Points & operator=(const Points & other) {
        points = other.points; // Use vector's copy assignment operator
        return *this;}

    void clear() {points.clear();}

    // Add a new point from an existing point
    void add(const Point & p) noexcept {points.emplace_back(pair(p, FillPoint()));}

    void set_fill_point(const size_t & i, const Point & p) noexcept {FillPoint fp(p); fp.enable(); points.at(i).second = fp;}

    // Fix background for all dots using the given Pixel.
    void fix_background(Pixel & pixel) {
        for (size_t i = 0; i < get_length(); i++) {
        auto & P = points.at(i); P.first.fix_background(pixel); P.second.fix_background(pixel);}}

    // Get the number of points
    size_t get_length() const noexcept {return points.size();}

    // Get a point at a specific index
    Point get(const size_t & i) const noexcept {return points.at(i).first;}

    // Get minimum x-coordinate among points
    float get_xmin() const noexcept  {float xmin = std::numeric_limits<float>::max(); for (const auto& p : points) {xmin = std::min(xmin, p.first.get_x()); if(p.second.get_fill()){xmin = std::min(xmin, p.second.get_x());}} return xmin;}

    // Get maximum x-coordinate among points
    float get_xmax() const noexcept  {float xmin = std::numeric_limits<float>::min(); for (const auto& p : points) {xmin = std::max(xmin, p.first.get_x()); if(p.second.get_fill()){xmin = std::max(xmin, p.second.get_x());}} return xmin;}

    // Get minimum y-coordinate among points
    float get_ymin() const noexcept  {float xmin = std::numeric_limits<float>::max(); for (const auto& p : points) {xmin = std::min(xmin, p.first.get_y()); if(p.second.get_fill()){xmin = std::min(xmin, p.second.get_y());}} return xmin;}

    // Get maximum y-coordinate among points
    float get_ymax() const noexcept  {float xmin = std::numeric_limits<float>::min(); for (const auto& p : points) {xmin = std::max(xmin, p.first.get_y()); if(p.second.get_fill()){xmin = std::max(xmin, p.second.get_y());}} return xmin;}

    // Applies log10 transformation to the x-coordinate of each point in `points`.
    void log_x() {
        for (size_t i = 0; i < get_length(); i++) {
            auto & p = points.at(i);
            p.first.log_x();
            if (p.second.get_fill()) {p.second.log_x();}}}

    // Applies log10 transformation to the y-coordinate of each point in `points`.
    void log_y() {
        for (size_t i = 0; i < get_length(); i++) {
            auto & p = points.at(i);
            p.first.log_y();
            if (p.second.get_fill()) {p.second.log_y();}}}

    // Rescales the x-coordinate of each point in `points` based on the given width, limits, and delta.
    void rescale_x(const pair<float, float> & xlim, const size_t & width, const float & delta) {
        for (size_t i = 0; i < get_length(); i++) {
            auto & p = points.at(i);
            p.first.rescale_x(xlim, width, delta);
            if (p.second.get_fill()) {p.second.rescale_x(xlim, width, delta);}}}

    // Rescales the y-coordinate of each point in `points` based on the given width, limits, and delta.
    void rescale_y(const pair<float, float> & ylim, const size_t & height, const float & delta) {
        for (size_t i = 0; i < get_length(); i++) {
            auto & p = points.at(i);
            p.first.rescale_y(ylim, height, delta);
            if (p.second.get_fill()) {p.second.rescale_y(ylim, height, delta);}}}

    void add_offset(const float & dx, const float & dy)  {
        for (size_t i = 0; i < get_length(); i++) {
            auto & p = points.at(i);
            p.first.add_offset(dx, dy);
            if (p.second.get_fill()) {p.second.add_offset(dx, dy);}}}

    // Get filled points
    void fill() {
        size_t length = get_length();
        Points out(length * 10);

        for (size_t i = 0; i < length; i++) {
            Point p1(points.at(i).first);
            FillPoint p2(points.at(i).second);

            out.add(p1);

            if (p2.get_fill()){

            float x1 = p1.get_x(); 
            float y1 = p1.get_y();
            float x2 = p2.get_x(); 
            float y2 = p2.get_y();
            float Dx = x2 - x1;
            float Dy = y2 - y1;
            float s = Dy / Dx;
            float dx = 1; 
            float dy = 1; 
            if (p1.is_hd()) {dx /= p1.get_cols(); dy /= p1.get_rows();}
            float ds = dy / dx;
            float sx = Dx > 0 ? dx : -dx; 
            float sy = Dy > 0 ? dy : -dy; 

            if (abs(s / ds) < 1) {
                auto X = range(x1 + sx, x2, sx);
                for (auto & x : X) {
                    auto y = s * (x - x1) + y1;
                    out.add(Point(x, y, p1));}} 
            else {
                auto Y = range(y1 + sy, y2, sy);
                for (auto & y : Y) {
                    auto x = (y - y1) / s + x1;
                    out.add(Point(x, y, p1));}}
            out.add(p2);}}
       
        points = out.points;}

    // Get string representation of points
    std::wstring get_wstring() const {
        std::wostringstream woss;
        size_t length = get_length();
        woss << L"Points [";
        for (size_t i = 0; i < length; i++) {
            auto & P = points.at(i);
            woss << P.first.get_wstring();
            if (P.second.get_fill()){woss << "->" << P.second.get_wstring();}
            if (i != length - 1) {woss << L", ";}}
        woss << L"]";
        return woss.str();}

    // Log points to output
    void log() const {std::wcout << get_wstring() << std::flush;}

    // Iterator begin
    vector<pair<Point, FillPoint>>::const_iterator begin() const {return points.begin();}

    // Iterator end
    vector<pair<Point, FillPoint>>::const_iterator end() const {return points.end();}


    Points copy() const {
        Points newPoints(*this);
        return newPoints;}

};

extern "C" {
    Points * points_new(size_t size) noexcept {return new Points(size);}
    void points_delete(Points * p) noexcept {delete p;}
    void points_clear(Points * p) noexcept {p->clear();}
    void points_add(Points * points, const Point * point) noexcept {points->add(*point);}
    void points_set_fill_point(Points * points, size_t i, const Point * point) noexcept {points->set_fill_point(i, *point);}
    void points_fix_background(Points * p, Pixel * pixel) noexcept {p->fix_background(*pixel);}
    void points_fill(Points * p1) noexcept {p1->fill();}
    const wchar_t * points_get_wstring(const Points * c) noexcept {return wstring_to_cstring(c->get_wstring());}
    Point * points_get(const Points * p, size_t i) noexcept {return new Point(p->get(i));}
    size_t points_get_length(const Points * p) noexcept {return p->get_length();}
    void points_assign(Points * p1, const Points * p2) noexcept {*p1 = *p2;}

    // float points_get_x(const Points * p, size_t index) noexcept {return p->get(index).get_x();}

    float points_get_xmin(Points * p) noexcept {return p->get_xmin();}
    float points_get_xmax(Points * p) noexcept {return p->get_xmax();}

    float points_get_ymin(Points * p) noexcept {return p->get_ymin();} 
    float points_get_ymax(Points * p) noexcept {return p->get_ymax();} 

    void points_log_x(Points * p) noexcept {p->log_x();}
    void points_log_y(Points * p) noexcept {p->log_y();}

    void points_rescale_x(Points * p, float lower, float higher, size_t bins, float delta) noexcept {p->rescale_x({lower, higher}, bins, delta);}
    void points_rescale_y(Points * p, float lower, float higher, size_t bins, float delta) noexcept {p->rescale_y({lower, higher}, bins, delta);}

    void points_add_offset(Points * p, float dx, float dy) noexcept {p->add_offset(dx, dy);}

    Points * points_copy(const Points * p) noexcept {return new Points(*p);}

}
