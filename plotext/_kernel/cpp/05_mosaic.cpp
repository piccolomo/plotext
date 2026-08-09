// Mosaic: a boolean matrix of at most 3 by 3, packed into one byte, the top left cell taking the highest bit

class Mosaic {
private:
    uint8_t bits = 0;                  // packed bits
    size_t  rows = 1;
    size_t  cols = 1;

    // Reverse-order linear index
    constexpr size_t get_index(const size_t & col, const size_t & row) const noexcept {
        return (rows * cols - 1) - (row * cols + col); }

public:
    // Constructor taking the number of columns and rows
    constexpr Mosaic(const size_t & c = 1, const size_t & r = 1) noexcept
        : bits(0), rows(r), cols(c) {}

    // Copy constructor
    constexpr Mosaic(const Mosaic &) noexcept = default;

    // Move constructor
    constexpr Mosaic(Mosaic &&) noexcept = default;

    // Virtual destructor for safe polymorphic deletion
    virtual ~Mosaic() noexcept {}

    // Copy assignment
    Mosaic & operator=(const Mosaic &) noexcept = default;              // constexpr on a defaulted assignment is allowed only from C++23

    // Move assignment
    Mosaic & operator=(Mosaic &&) noexcept = default;

    // Number of columns
    constexpr size_t get_cols() const noexcept {return cols;}

    // Number of rows
    constexpr size_t get_rows() const noexcept {return rows;}

    // Copy only the size (cols and rows) from another Mosaic
    inline void copy_size(const Mosaic & ch) noexcept {rows = ch.rows; cols = ch.cols;}

    // Copy only the packed bits
    inline void copy_code(const Mosaic & ch) noexcept {bits = ch.bits;}

    // Copy both size and bits
    inline void copy(const Mosaic & ch) noexcept {copy_size(ch); copy_code(ch);}

    // Set dimensions (keeps bits as they are)
    inline void set_size(const size_t & new_cols, const size_t & new_rows) noexcept {
        cols = new_cols; rows = new_rows;}

    // Clear all bits to 0
    inline void zero() noexcept {bits = 0;}

    // Set or clear bit at (col,row)
    inline void set(const size_t & col, const size_t & row, const bool & value) noexcept {
        const uint8_t mask = uint8_t(1) << get_index(col, row);
        bits = value ? (bits | mask) : (bits & ~mask); }

    // Enable (set to 1) bit at (col, row)
    inline void enable (const size_t & col, const size_t & row) noexcept {set(col, row, true);}

    // Disable (set to 0) bit at (col, row)
    inline void disable(const size_t & col, const size_t & row) noexcept {set(col, row, false);}

    // Check the value of bit at (col, row)
    inline bool get(const size_t & col, const size_t & row) const noexcept {
        return bits & (uint8_t(1) << get_index(col, row)); }

    // Add a dot (enables the bit) from float coordinates (truncated to size_t)
    inline void add_dot(const float & col, const float & row) noexcept {enable(col, row);}

    // OR-accumulate another Mosaic's bits into this one
    inline void sum(const Mosaic & other) noexcept {bits |= other.bits;}

    // OR-accumulate a raw byte of bits into this one
    inline void sum(uint8_t code) noexcept {bits |= code;}

    // Return the raw packed bits
    constexpr uint8_t get_code() const noexcept {return bits;}

    // Convert to wide string (e.g. "101 010 001")
    wstring get_wstring() const {
        wostringstream log;
        for (size_t r = 0; r < rows; r++) {
            for (size_t c = 0; c < cols; c++) log << (get(c, r) ? L'1' : L'0');
            if (r < rows - 1) log << L" "; }
        return log.str(); }

    // Convert to narrow string
    inline string get_string() const {return wstring_to_string(get_wstring());}

    // Print to wcout (no trailing newline)
    inline void log() const {wcout << get_wstring();}

    // Wide-stream output
    friend wostream & operator<<(wostream & os, const Mosaic & c) noexcept {
        os << c.get_wstring(); return os;}

    // Narrow-stream output
    friend ostream & operator<<(ostream & os, const Mosaic & c) noexcept {
        os << c.get_string(); return os;}
};
