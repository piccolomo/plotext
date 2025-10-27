// A class to represent and manipulate the position of a point in the plot canvas.

class PointPosition {
private:
    float x = 0.0f;
    float y = 0.0f;

public:
    // Constructors
    constexpr PointPosition() noexcept = default;
    constexpr PointPosition(float xi, float yi) noexcept : x(xi), y(yi) {}
    constexpr PointPosition(const PointPosition& other) noexcept = default;
    constexpr PointPosition(PointPosition&& other) noexcept = default;

    // Assignment operator
    constexpr PointPosition& operator=(const PointPosition& p) noexcept = default;

    // Equality operator
    constexpr bool operator==(const PointPosition& p) const noexcept { return x == p.x && y == p.y; }
    constexpr bool operator!=(const PointPosition& p) const noexcept { return !(*this == p); }

    // Getters
    constexpr float get_x() const noexcept { return x; }
    constexpr float get_y() const noexcept { return y; }

    // Convert to integer coordinates
    constexpr size_t get_col() const noexcept { return static_cast<size_t>(x); }
    constexpr size_t get_row() const noexcept { return static_cast<size_t>(y); }

    constexpr bool in_matrix(const size_t & width, const size_t & height) const noexcept { return x >= 0 and y >= 0 and x < width and y < height; }


    // Inner position within a marker cell
    constexpr unsigned char get_inner_col(const size_t marker_cols) const noexcept {return static_cast<unsigned char>((x - get_col()) * marker_cols); }

    constexpr unsigned char get_inner_row(const size_t marker_rows) const noexcept {return static_cast<unsigned char>((y - get_row()) * marker_rows); }

    // Setters
    constexpr void set_x(float el) noexcept { x = el; }
    constexpr void set_y(float el) noexcept { y = el; }
    constexpr void set(float xi, float yi) noexcept { x = xi; y = yi; }

    // Rescaling
    void rescale_x(const pair<float, float>& xlim, size_t width, float delta) noexcept { 
        x = rescale_element(x, xlim, width, delta); }

    void rescale_y(const pair<float, float>& ylim, size_t height, float delta) noexcept { 
        y = rescale_element(y, ylim, height, delta); }

    // Offset addition
    constexpr void add_offset(size_t dx, size_t dy) noexcept { x += static_cast<float>(dx); y += static_cast<float>(dy); }

    // Logarithmic transformation
    void log_x() noexcept { x = log10f(x); }
    void log_y() noexcept { y = log10f(y); }

    // Fast string representation without stringstreams
    wstring get_wstring() const noexcept {
        wchar_t buffer[32]; // enough for two floats with precision
        swprintf(buffer, sizeof(buffer)/sizeof(wchar_t), L"%.2f, %.2f", x, y);
        return wstring(buffer);}

    void log() const noexcept { wcout << get_wstring() << flush; }
};
