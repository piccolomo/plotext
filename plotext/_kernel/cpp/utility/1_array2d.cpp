// Array2D: 2D wrapper around Array<T> with (col, row) access and stack/insert helpers

template <typename T>
class Array2D : private Array<T> {
private:
    size_t width = 0;
    size_t height = 0;

    // Compute linear index
    constexpr inline size_t index(size_t col, size_t row) const noexcept {return row * width + col;}

public:
    using Array<T>::begin;
    using Array<T>::end;
    using Array<T>::at;

    // Re-expose the global Array template so derived classes (e.g. Matrix) can write `Array<wchar_t>` without the `::` qualifier, the private inheritance above otherwise shadows the global name during unqualified lookup.
    template <typename U> using Array = ::Array<U>;

    // --- Constructors ---

    // Default constructor
    Array2D() noexcept = default;

    // Construct an empty 2D array with the given width and height
    Array2D(size_t w, size_t h) : Array<T>(w * h), width(w), height(h) {}

    // Construct a 2D array filled with a value
    Array2D(size_t w, size_t h, const T & value) : Array<T>(w * h, value), width(w), height(h) {}

    // Copy constructor
    Array2D(const Array2D<T> & other) : Array<T>(other), width(other.width), height(other.height) {}

    // Move constructor
    Array2D(Array2D<T> && other) noexcept : Array<T>(std::move(other)), width(other.width), height(other.height) {
        other.width = 0;
        other.height = 0;}

    // Destructor
    ~Array2D() {width = 0; height = 0; Array<T>::destroy();}

    // Copy assignment (self-assignment safe)
    Array2D & operator=(const Array2D<T> & other) {
        if (this != &other) clone(other);
        return *this;}

    // Move assignment
    Array2D & operator=(Array2D<T> && other) noexcept {
        if (this != &other) {
            Array<T>::operator=(std::move(other));
            width = other.width;
            height = other.height;
            other.width = 0;
            other.height = 0; }
        return *this;}

    // Equality comparison
    bool operator==(const Array2D<T>& other) const {return width == other.width and height == other.height and Array<T>::operator==(other); }

    // Inequality comparison
    bool operator!=(const Array2D<T>& other) const {return !(*this == other); }

    // --- Accessors ---

    // Number of columns
    size_t get_width() const noexcept { return width; }

    // Number of rows
    size_t get_height() const noexcept { return height; }

    // Total number of cells (width * height)
    size_t get_size() const noexcept { return width * height; }

    // Element access at (col, row), mutable
    T & at(size_t col, size_t row) noexcept { return Array<T>::at(index(col, row)); }

    // Element access at (col, row), const
    const T & at(size_t col, size_t row) const noexcept { return Array<T>::at(index(col, row)); }

    // Set dimensions (does not reallocate)
    void set_size(size_t new_width, size_t new_height) {width = new_width; height = new_height;}

    // Overwrite a single cell
    inline void insert(size_t col, size_t row, const T & value) noexcept {Array<T>::insert(index(col,row), value);}

    // Insert another Array2D at (col, row), cell by cell
    inline void insert(size_t col, size_t row, const Array2D<T>& other) noexcept {
        assert(col + other.get_width() <= width and row + other.get_height() <= height);
        for (size_t r = 0; r < other.get_height(); ++r)
            for (size_t c = 0; c < other.get_width(); ++c)
                at(col + c, row + r) = other.at(c, r);}

    // Copy cols x rows from a raw pointer (row-major)
    void copy_from(const T * source, size_t cols, size_t rows) {
        for (size_t col = 0; col < cols; ++col)
            for (size_t row = 0; row < rows; ++row)
                at(col, row) = source[row * cols + col];}

    // Copy the overlapping region from another Array2D
    void copy_from(const Array2D<T> & other) { copy_from(other.begin(), min(other.get_width(), get_width()), min(other.get_height(), get_height()));}

    // Replace contents with a deep copy of another Array2D
    void clone(const Array2D<T> & other) {
        set_size(other.width, other.height);
        Array<T>::clone(other);}

    // Resize, preserving existing cells where possible
    void resize(size_t cols, size_t rows) {
        Array2D<T> old(*this);  // copy old data
        set_size(cols, rows);
        Array<T>::reallocate(cols * rows);
        copy_from(old);}

    // Return a deep copy
    Array2D<T> copy() const {Array2D<T> new_array(*this); return new_array;}

    // Extract a sub-rectangle [col1, col2) x [row1, row2) as a new Array2D.
    // Copied cell-by-cell via at() so the original row stride is respected:
    // raw-pointer + reshaped-stride approaches break when the source is a
    // view into a wider array (off-by-width bug).
    Array2D<T> part(size_t col1, size_t col2, size_t row1, size_t row2) const {
        size_t new_cols = col2 - col1;
        size_t new_rows = row2 - row1;
        Array2D out(new_cols, new_rows);
        for (size_t r = 0; r < new_rows; ++r)
            for (size_t c = 0; c < new_cols; ++c)
                out.at(c, r) = at(col1 + c, row1 + r);
        return out;}

    // Stack this Array2D above another (optionally widen to the max width)
    inline Array2D<T> vstack(const Array2D<T> & m, bool adapt = false) noexcept {
        size_t w_out = adapt ? std::max(get_width(), m.get_width()) : get_width();
        Array2D<T> out(w_out, get_height() + m.get_height());
        out.insert(0, 0, *this);
        out.insert(0, get_height(), m);
        return out;}

    // Stack this Array2D next to another (optionally heighten to the max height)
    inline Array2D<T> hstack(const Array2D<T> & m, bool adapt = false) noexcept {
        size_t h_out = adapt ? std::max(get_height(), m.get_height()) : get_height();
        Array2D<T> out(get_width() + m.get_width(), h_out);
        out.insert(0, 0, *this);
        out.insert(get_width(), 0, m);
        return out;}


    // Narrow-stream output
    friend std::ostream& operator<<(std::ostream& os, const Array2D<T>& m) {
        os << "[\n";
        for (size_t r = 0; r < m.height; ++r) {
            os << "  [";
            for (size_t c = 0; c < m.width; ++c) {
                os << m.at(c, r);
                if (c + 1 < m.width) os << ", ";}
            os << "]";
            if (r + 1 < m.height) os << "\n";}
        os << "\n]";
        return os;}

    // Wide-stream output
    friend std::wostream& operator<<(std::wostream& os, const Array2D<T>& m) {
        os << L"[\n";
        for (size_t r = 0; r < m.height; ++r) {
            os << L"  [";
            for (size_t c = 0; c < m.width; ++c) {
                os << m.at(c, r);
                if (c + 1 < m.width) os << L", ";}
            os << L"]";
            if (r + 1 < m.height) os << L"\n";}
        os << L"\n]";
        return os;}
};
