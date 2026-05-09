// PointPosition: lightweight 2D float position with fast integer conversion and marker-cell helpers

class PointPosition {
private:
    float x = 0.0f;
    float y = 0.0f;

public:
    // ------------ lifecycle ------------

    // Default constructor (origin)
    constexpr PointPosition() noexcept = default;

    // Construct from x and y
    constexpr PointPosition(float xi, float yi) noexcept : x(xi), y(yi) {}

    // Copy constructor
    constexpr PointPosition(const PointPosition &) noexcept = default;

    // Move constructor
    constexpr PointPosition(PointPosition &&) noexcept = default;

    // Virtual destructor for safe polymorphic deletion (Point inherits)
    virtual ~PointPosition() noexcept {}

    // Copy assignment
    constexpr PointPosition & operator=(const PointPosition &) noexcept = default;

    // Move assignment
    constexpr PointPosition & operator=(PointPosition &&) noexcept = default;

    // ------------ comparison ------------

    // Equality comparison (both coordinates match)
    constexpr bool operator==(const PointPosition & p) const noexcept {return x == p.x && y == p.y;}

    // Inequality comparison
    constexpr bool operator!=(const PointPosition & p) const noexcept {return !(*this == p);}

    // ------------ getters ------------

    // Get the x coordinate
    constexpr float  get_x() const noexcept {return x;}

    // Get the y coordinate
    constexpr float  get_y() const noexcept {return y;}

    // Integer column (truncated x)
    constexpr size_t get_col() const noexcept {return static_cast<size_t>(x);}

    // Integer row (truncated y)
    constexpr size_t get_row() const noexcept {return static_cast<size_t>(y);}

    // True if (x, y) lies inside a matrix of the given width and height
    constexpr bool in_matrix(size_t width, size_t height) const noexcept {
        return x >= 0.0f && y >= 0.0f &&
               x < static_cast<float>(width) &&
               y < static_cast<float>(height); }

    // Return the midpoint between this position and another
    PointPosition get_middle(const PointPosition & p) const noexcept {
        return PointPosition(0.5f * x + 0.5f * p.x,
                             0.5f * y + 0.5f * p.y); }

    // ------------ setters ------------

    // Set the x coordinate
    constexpr void set_x(float v) noexcept {x = v;}

    // Set the y coordinate
    constexpr void set_y(float v) noexcept {y = v;}

    // Set both coordinates
    constexpr void set(float xi, float yi) noexcept {x = xi; y = yi;}

    // ------------ transformations ------------

    // Rescale x to discrete bins using rescale_element
    inline void rescale_x(const pair<float,float> & xlim, size_t width, float delta) noexcept {
        x = rescale_element(x, xlim, width, delta); }

    // Rescale y to discrete bins using rescale_element
    inline void rescale_y(const pair<float,float> & ylim, size_t height, float delta) noexcept {
        y = rescale_element(y, ylim, height, delta); }

    // Add an integer offset to both coordinates
    constexpr void add_offset(size_t dx, size_t dy) noexcept {
        x += static_cast<float>(dx);
        y += static_cast<float>(dy); }

    // Apply log10 to the x coordinate
    inline void log_x() noexcept {x = log10f(x);}

    // Apply log10 to the y coordinate
    inline void log_y() noexcept {y = log10f(y);}

    // ------------ debug helpers ------------

    // Get wide string "(x, y)"
    wstring get_wstring() const noexcept {
        wchar_t buf[40];
        swprintf(buf, 40, L"(%.4f, %.4f)", x, y);
        return wstring(buf); }

    // Get narrow string "(x, y)"
    inline string get_string() const {return wstring_to_string(get_wstring());}

    // Print to wcout followed by a space
    inline void log() const noexcept {wcout << get_wstring() << " ";}

    // ------------ stream operators ------------

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const PointPosition & c) noexcept {
        os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const PointPosition & c) noexcept {
        os << c.get_string(); return os;}
};
