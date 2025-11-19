// MatrixBool - ultra-compact boolean matrix (max 3x3 → 9 bits in 1 byte)
// Bits stored in reverse order (top-left = highest bit)

class MatrixBool {
private:
    uint8_t bits = 0;                  // packed bits
    size_t  rows = 1;
    size_t  cols = 1;

    // Reverse-order linear index
    constexpr size_t get_index(const size_t & col, const size_t & row) const noexcept {
        return (rows * cols - 1) - (row * cols + col); }

public:
    // Constructor
    constexpr MatrixBool(const size_t & c = 1, const size_t & r = 1) noexcept
        : bits(0), rows(r), cols(c) {}

    // Size getters
    constexpr size_t get_cols() const noexcept {return cols;}
    constexpr size_t get_rows() const noexcept {return rows;}

    // Copy helpers
    inline void copy_size(const MatrixBool & ch) noexcept {rows = ch.rows; cols = ch.cols;}
    inline void copy_code(const MatrixBool & ch) noexcept {bits = ch.bits;}
    inline void copy(const MatrixBool & ch) noexcept {copy_size(ch); copy_code(ch);}    

    // Set dimensions (keeps bits as they are)
    inline void set_size(const size_t & new_cols, const size_t & new_rows) noexcept {
        cols = new_cols; rows = new_rows;}

    // Clear bits
    inline void zero() noexcept {bits = 0;}

    // Set or clear bit at (col,row)
    inline void set(const size_t & col, const size_t & row, const bool & value) noexcept {
        const uint8_t mask = uint8_t(1) << get_index(col, row);
        bits = value ? (bits | mask) : (bits & ~mask); }

    // Shortcuts
    inline void enable (const size_t & col, const size_t & row) noexcept {set(col, row, true);}
    inline void disable(const size_t & col, const size_t & row) noexcept {set(col, row, false);}

    // Check bit value
    inline bool get(const size_t & col, const size_t & row) const noexcept {
        return bits & (uint8_t(1) << get_index(col, row)); }

    // Add dot (keep original behavior)
    inline void add_dot(const float & col, const float & row) noexcept {enable(col, row);}

    // OR-accumulate
    inline void sum(const MatrixBool & other) noexcept {bits |= other.bits;}

    // Return raw bits
    constexpr uint8_t get_code() const noexcept {return bits;}

    // Convert to wstring (ex: "101 010 001")
    wstring get_wstring() const {
        wostringstream log;
        for (size_t r = 0; r < rows; r++) {
            for (size_t c = 0; c < cols; c++) log << (get(c, r) ? L'1' : L'0');
            if (r < rows - 1) log << L" "; }
        return log.str(); }

    // Convert to string
    inline string get_string() const {return wstring_to_string(get_wstring());}

    // Print to wcout
    inline void log() const {wcout << get_wstring();}

    // Stream operators
    friend wostream & operator<<(wostream & os, const MatrixBool & c) noexcept {
        os << c.get_wstring(); return os;}

    friend ostream & operator<<(ostream & os, const MatrixBool & c) noexcept {
        os << c.get_string(); return os;}
};
