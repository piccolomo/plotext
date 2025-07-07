// Character class - Represents a single character with associated Pixel styling

class Character : public Pixel {
private:
    wchar_t c = L' '; // The character value, defaulting to a space

public:
    // Constructors
    Character() = default;
    Character(const wchar_t & cn) : c(cn) {}
    Character(const wchar_t & cn, const Pixel & p) : c(cn), Pixel(p) {}

    // Copy and Move constructors
    Character(const Character & p) : Pixel(p), c(p.c) {}
    Character(Character && p) noexcept : Pixel(std::move(p)), c(p.c) {}

    // Assignment operator
    Character & operator=(const Character& cn) {
        c = cn.c;
        Pixel::operator=(cn);
        return *this;}

    // Clear the character and its Pixel data
    void clear() noexcept {
        c = L' ';
        Pixel::clear();}

    // Setters
    void set_wcharacter(const wchar_t & cs) noexcept {c = cs;}
    void set_pixel(const Pixel & p) noexcept {Pixel::operator=(p);}

    // Getters
    wchar_t get_wcharacter() const noexcept {return c;}
    bool is_empty() const noexcept {return c == L' ';}

    // Compare Pixel attributes with another Character
    bool same(const Character & cn) const noexcept {return Pixel::operator==(cn);}
    bool different(const Character & cn) const noexcept {return !Pixel::operator==(cn);}

    // Convert Pixel and character to buffer
    void pixel_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        Pixel::to_buffer(buffer, length_buffer);}

    void character_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        wchar_to_buffer(c, buffer, length_buffer);}

    void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        pixel_to_buffer(buffer, length_buffer);
        character_to_buffer(buffer, length_buffer);
        cstring_to_buffer(ansi_end, buffer, length_buffer);}

    // Log the character with Pixel styling
    void print() const noexcept {
        wchar_t buffer[character_size_max + 1] = L""; // Initialize buffer
        size_t length = 0;
        to_buffer(buffer, length);
        wcout << buffer;}
};