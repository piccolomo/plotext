// Bit Manipulation

// Get the bit at a specific position.
constexpr bool get_bit(const size_t &number, const size_t &position) noexcept {
    return (number >> position) & 1;}

// Get the bit position for a specific row and column in a grid.
constexpr size_t get_bit_position(const size_t &col, const size_t &row, const size_t &cols, const size_t &rows) noexcept {
    return cols * (rows - row) - 1 - col;}