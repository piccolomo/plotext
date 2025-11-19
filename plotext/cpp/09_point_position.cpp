// PointPosition - lightweight 2D float position with fast integer conversion and marker helpers

class PointPosition {
private:
    float x = 0.0f;
    float y = 0.0f;

public:
    // ------------ lifecycle ------------
    constexpr PointPosition() noexcept = default;
    constexpr PointPosition(float xi, float yi) noexcept : x(xi), y(yi) {}

    // ------------ comparison ------------
    constexpr bool operator==(const PointPosition & p) const noexcept {return x == p.x && y == p.y;}
    constexpr bool operator!=(const PointPosition & p) const noexcept {return !(*this == p);}

    // ------------ getters ------------
    constexpr float  get_x() const noexcept {return x;}
    constexpr float  get_y() const noexcept {return y;}

    constexpr size_t get_col() const noexcept {return static_cast<size_t>(x);}   // integer part
    constexpr size_t get_row() const noexcept {return static_cast<size_t>(y);}   

    constexpr bool in_matrix(size_t width, size_t height) const noexcept {
        return x >= 0.0f && y >= 0.0f &&
               x < static_cast<float>(width) &&
               y < static_cast<float>(height); }

    // fractional part → inner marker cell
    constexpr unsigned char get_inner_col(size_t marker_cols) const noexcept {
        return static_cast<unsigned char>((x - get_col()) * marker_cols); }
    constexpr unsigned char get_inner_row(size_t marker_rows) const noexcept {
        return static_cast<unsigned char>((y - get_row()) * marker_rows); }

    // midpoint
    constexpr PointPosition get_middle(const PointPosition & p) const noexcept {
        return PointPosition(0.5f * x + 0.5f * p.x,
                             0.5f * y + 0.5f * p.y); }

    // ------------ setters ------------
    constexpr void set_x(float v) noexcept {x = v;}
    constexpr void set_y(float v) noexcept {y = v;}
    constexpr void set(float xi, float yi) noexcept {x = xi; y = yi;}

    // ------------ transformations ------------
    inline void rescale_x(const pair<float,float> & xlim, size_t width, float delta) noexcept {
        x = rescale_element(x, xlim, width, delta); }
    inline void rescale_y(const pair<float,float> & ylim, size_t height, float delta) noexcept {
        y = rescale_element(y, ylim, height, delta); }

    constexpr void add_offset(size_t dx, size_t dy) noexcept {
        x += static_cast<float>(dx);
        y += static_cast<float>(dy); }

    inline void log_x() noexcept {x = log10f(x);}
    inline void log_y() noexcept {y = log10f(y);}

    // ------------ debug helpers ------------
    // now includes parentheses "(x,y)"
    wstring get_wstring() const noexcept {
        wchar_t buf[40];
        swprintf(buf, 40, L"(%.4f,%.4f)", x, y);
        return wstring(buf); }

    inline string get_string() const {return wstring_to_string(get_wstring());}

    inline void log() const noexcept {wcout << get_wstring() << " ";}

    // ------------ stream operators ------------
    friend wostream & operator<<(wostream & os, const PointPosition & c) noexcept {
        os << c.get_wstring(); return os;}

    friend ostream & operator<<(ostream & os, const PointPosition & c) noexcept {
        os << c.get_string(); return os;}
};
