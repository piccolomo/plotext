// Character class - Represents a single character with associated Pixel styling

class Character : public Pixel {
private:
    wchar_t c = L' '; // The character value, defaulting to a space

public:
    // Constructors
    constexpr Character() = default;
    Character(const wchar_t & cn) noexcept : c(cn) {}
    Character(const wchar_t & cn, const Pixel & p) noexcept : c(cn), Pixel(p) {}

    // Copy and Move constructors
    Character(const Character & p) noexcept : Pixel(p), c(p.c) {}
    Character(Character && p) noexcept : Pixel(std::move(p)), c(move(p.c)) {}

    // Assignment operator
    Character & operator=(const Character& cn) noexcept {
        c = cn.c;
        Pixel::operator=(cn);
        return *this;}

    // Equality operators
    bool operator==(const Character & other) const noexcept {return c == other.c and Pixel::operator==(other);}

    bool operator!=(const Character & other) const noexcept {return not operator==(other);}

    // Clear the character and its Pixel data
    void clear() noexcept {
        c = L' ';
        Pixel::clear();}

    // Setters
    void set_wcharacter(const wchar_t & cs) noexcept {c = cs;}
    void set_pixel(const Pixel & p) noexcept {Pixel::operator=(p);}
    void copy_wcharacter(const Character & p) noexcept {c = p.c;}

    // Getters
    wchar_t get_wcharacter() const noexcept {return c;}
    bool is_empty() const noexcept {return c == L' ';}

    // Compare Pixel attributes with another Character
    bool same_pixel(const Character & cn) const noexcept {return Pixel::operator==(cn);}
    bool same(const Character & cn) const noexcept {return Pixel::operator==(cn) and c == cn.c;}
    bool different(const Character & cn) const noexcept {return !Pixel::operator==(cn);}

    // // Convert Pixel and character to buffer
    // void pixel_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    //     Pixel::to_buffer(buffer, length_buffer);}

    // void character_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    //     wchar_to_buffer(c, buffer, length_buffer);}

    // void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    //     pixel_to_buffer(buffer, length_buffer);
    //     character_to_buffer(buffer, length_buffer);
    //     cstring_to_buffer(ansi_end, buffer, length_buffer);}

    // Buffer conversion: use noexcept, remove extra function call
    void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        Pixel::to_buffer(buffer, length_buffer);
        wchar_to_buffer(c, buffer, length_buffer);
        cstring_to_buffer(ansi_end, buffer, length_buffer);}

    void to_buffer_full(wchar_t * buffer, size_t & length_buffer) const noexcept {
        to_buffer(buffer, length_buffer);
        cstring_to_buffer(ansi_end, buffer, length_buffer);}

    // Log the character with Pixel styling
    void print() const noexcept {
        wchar_t buffer[character_size_max + 1] = L""; // Initialize buffer
        size_t length = 0;
        to_buffer_full(buffer, length);
        wcout.write(buffer, length);}

  inline void stream() const {Pixel::stream(); wcout.put(c);} 

};