class Matrix {
private:
    CharacterHD * data = nullptr; 
    size_t width = 0;
    size_t height = 0;

    constexpr inline size_t index(const size_t col, const size_t row) const noexcept { return row * width + col; }

public:
    // Constructors
    constexpr Matrix() noexcept = default;
    Matrix(const size_t w, const size_t h) noexcept : data(new CharacterHD[w * h]()), width(w), height(h) {}
    Matrix(const size_t w, const size_t h, const Pixel & p) noexcept : Matrix(w, h) { fill_pixel(p); }
    Matrix(const size_t w, const size_t h, const CharacterHD & c) noexcept : Matrix(w, h) { fill_character(c); }

    // Copy constructor
    Matrix(const Matrix & other) noexcept : width(other.width), height(other.height), data(new CharacterHD[other.width * other.height]) { copy_from(other); }

    // Destructor
    ~Matrix() noexcept { destroy(); }

    // Assignment
    Matrix & operator=(const Matrix & other) noexcept { destroy(); create(other.width, other.height); copy_from(other); return *this; }

    // Memory management
    void destroy() noexcept { delete[] data; data = nullptr; }
    void create(const size_t w, const size_t h) noexcept { data = new CharacterHD[w * h](); }
    void copy_from(const Matrix & other) noexcept { std::copy(other.data, other.data + width * height, data); }
    void clear() noexcept { for (size_t i = 0; i < width * height; i++) data[i].clear(); }

    // Accessors
    constexpr size_t get_width() const noexcept { return width; }
    constexpr size_t get_height() const noexcept { return height; }
    inline CharacterHD & get_character(const size_t col, const size_t row) noexcept { return data[index(col, row)]; }
    inline const CharacterHD & get_character(const size_t col, const size_t row) const noexcept { return data[index(col, row)]; }

    // Checks
    bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept {
        for (size_t r = row_start; r < row_stop; r++)
            for (size_t c = col_start; c < col_stop; c++)
                if (!get_character(c, r).is_empty()) return false;
        return true;}

    // Modifiers
    inline void set_character(const size_t col, const size_t row, const CharacterHD & c) noexcept { get_character(col, row) = c; }
    inline void set_wcharacter(const size_t col, const size_t row, const wchar_t & cs) noexcept { get_character(col, row).set_wcharacter(cs); }
    inline void set_pixel(const size_t col, const size_t row, const Pixel & p) noexcept { get_character(col, row).set_pixel(p); }

    void fill_pixel(const Pixel & p = Pixel()) noexcept { for (size_t i = 0; i < width * height; i++) data[i].set_pixel(p); }
    void fill_character(const CharacterHD & c) noexcept { for (size_t i = 0; i < width * height; i++) data[i] = c; }

    void resize(const size_t & w, const size_t & h) noexcept { Matrix temp(*this); destroy(); create(w, h); copy_from(temp); }

    // Stack operations
    Matrix vstack(const Matrix & m, const bool & adapt = false) noexcept {
        size_t w = adapt ? std::max(get_width(), m.get_width()) : get_width();
        Matrix out(w, get_height() + m.get_height());
        out.insert_matrix(0, 0, *this);
        out.insert_matrix(0, get_height(), m);
        return out;}

    Matrix hstack(const Matrix & m, const bool & adapt = false) noexcept {
        size_t h = adapt ? std::max(get_height(), m.get_height()) : get_height();
        Matrix out(get_width() + m.get_width(), h);
        out.insert_matrix(0, 0, *this);
        out.insert_matrix(get_width(), 0, m);
        return out;}

    // Matrix slicing
    inline Matrix part(const size_t & col_start, const size_t & col_stop, const size_t & row_start, const size_t & row_stop) const noexcept {
        const size_t new_height = std::min(row_stop - row_start, height);
        const size_t new_width = std::min(col_stop - col_start, width);
        Matrix m(new_width, new_height);
        for (size_t r = 0; r < new_height; r++)
            for (size_t c = 0; c < new_width; c++)
                m.get_character(c, r) = get_character(col_start + c, row_start + r);
        return m;}

    // Insert operations
    inline void insert_matrix(const size_t & col, const size_t & row, const Matrix & m) noexcept {
        const size_t h = std::min(m.get_height(), height - row);
        const size_t w = std::min(m.get_width(), width - col);
        for (size_t r = 0; r < h; ++r) {
            const size_t dest_index = (row + r) * width + col;
            const size_t src_index = r * m.get_width();
            for (size_t c = 0; c < w; ++c)
                data[dest_index + c] = m.data[src_index + c];}}

    inline void insert_matrix_aligned(const size_t & col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1) noexcept {
        const int v_disp = va.get_displacement(m.get_height());
        const int h_disp = ha.get_displacement(m.get_width());
        row += v_disp;
        const size_t aligned_col = col + h_disp;
        const size_t max_r = std::min(m.get_height(), height - row);
        const size_t max_c = std::min(m.get_width(), width - aligned_col);
        for (size_t r = 0; r < max_r; ++r) {
            const size_t dest_index = (row + r) * width + aligned_col;
            const size_t src_index = r * m.get_width();
            for (size_t c = 0; c < max_c; ++c)
                data[dest_index + c] = m.data[src_index + c];}}

    void insert_wstring(const size_t col, const size_t row, const wstring & s) noexcept {
        for (size_t i = 0; i < s.size(); i++) get_character(col + i, row).set_wcharacter(s[i]);}

    inline bool insert_colorized_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, const bool & check_space = false, const bool & change_color = true) noexcept {
        if (row >= height || col >= width) return false;
        const int c = static_cast<int>(col) + ha.get_displacement(s.get_length());
        const size_t start = std::max(0, c - 1);
        const size_t stop = std::min(width, c + s.get_length() + 1);
        if (check_space && (c < 0 || c + s.get_length() > width || !is_empty(start, stop, row, row + 1))) return false;
        for (size_t i = 0; i < s.get_length(); ++i) {
            auto & ch = get_character(c + i, row);
            ch.set_wcharacter(s.get_wcharacter(i));
            if (change_color) ch.set_pixel(s);}
        return true;}

    inline int insert_colorized_dynamically(const size_t & col, const size_t & row, const Colorize & s) noexcept {
        if (row >= height) return -1;
        for (int delta : get_dynamic_displacements(s.get_length()))
            if (insert_colorized_aligned(col + delta, row, s, 0, true, true)) return static_cast<int>(col) + delta;
        return -1;}

    inline void insert_point(const Point & p) noexcept { get_character(p.get_col(), p.get_row()).update(p); }
    inline void insert_points(const Points & points) noexcept { for (const Point & p : points) insert_point(p); }

    // Rendering / Output
    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        for (size_t i = 0; i < width * height; ++i) {
            data[i].to_buffer(buffer, length_buffer);
            if ((i + 1) % width == 0 && (i + 1) != width * height) buffer[length_buffer++] = L'\n';}}

    inline void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        for (size_t i = 0; i < width * height; ++i) {
            wchar_to_buffer(data[i].get_wcharacter(), buffer, length_buffer);
            if ((i + 1) % width == 0 && (i + 1) != width * height) buffer[length_buffer++] = L'\n';}}

    wstring get_wstring(const bool colorless = false) const noexcept {
        wchar_t buffer[character_size_max * width * height + height + 1] = {0};
        size_t length = 0;
        if (colorless) to_colorless_buffer(buffer, length);
        else to_buffer(buffer, length);
        return wstring(buffer);}

    inline string get_string() const { return wstring_to_string(get_wstring()); }

    const wchar_t * get_cstring(const bool colorless = false) const noexcept {
        size_t required_size = character_size_max * width * height + height + 1;
        wchar_t * buffer = new wchar_t[required_size]; size_t length = 0;
        if (colorless) to_colorless_buffer(buffer, length);
        else to_buffer(buffer, length);
        buffer[length] = L'\0';
        return buffer;}

    inline void print(const bool colorless = false) const noexcept {
        const size_t total = width * height;
        for (size_t i = 0; i < total; ++i) {
            data[i].stream();
            if (not data[i].same_pixel(data[i + 1])) {wcout.write(ansi_end, 4);}
            if ((i + 1) % width == 0) {wcout.write(ansi_end, 4); if ((i + 1) != total) wcout.put(L'\n');}} // Add newline after each row (except the last one)
        wcout.flush();}

    friend wostream & operator<<(wostream & os, const Matrix & c) noexcept {os << c.get_wstring(); return os;}
    friend ostream & operator<<(ostream & os, const Matrix & c) noexcept {os << c.get_string(); return os;}

};



Matrix colorize_to_matrix(const Colorize & c) noexcept {
    // Split the colorless string by newline
    vector<wstring> wstrings = split_wstring(c.get_colorless_wstring());
    
    // Determine maximum width and height
    size_t height = wstrings.size();
    size_t width = 0;
    for (const auto & line : wstrings) width = std::max(width, line.size());

    Matrix out(width, height); // Create matrix

    // Insert each line as Colorize into the matrix
    for (size_t row = 0; row < height; ++row) {
        const wstring & line = wstrings[row];
        Colorize cs(line, c); // preserve coloring
        out.insert_colorized_aligned(0, row, cs, -1, false, true);}

    return out;}


extern "C" {

    Matrix * matrix_new(size_t width, size_t height, Pixel * p) noexcept { return new Matrix(width, height, *p); }
    void matrix_clear(Matrix * m) noexcept { m->clear(); }
    void matrix_delete(Matrix * m) noexcept { delete m; }

    size_t matrix_get_width(Matrix * m) noexcept { return m->get_width(); }
    size_t matrix_get_height(Matrix * m) noexcept { return m->get_height(); }
    bool matrix_is_empty(Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept {
        return m->is_empty(col_start, col_stop, row_start, row_stop);}

    void matrix_resize(Matrix * m, size_t width, size_t height) noexcept { m->resize(width, height); }
    void matrix_fill_pixel(Matrix * m, Pixel * p) noexcept { m->fill_pixel(*p); }

    const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) noexcept { return wstring_to_cstring(m->get_wstring(colorless)); }
    void wstring_delete(wchar_t * wstr) noexcept { delete_cstring(wstr); }

    Matrix * matrix_vstack(Matrix * m1, Matrix * m2, bool adapt = 0) noexcept { return new Matrix(m1->vstack(*m2, adapt)); }
    Matrix * matrix_hstack(Matrix * m1, Matrix * m2, bool adapt = 0) noexcept { return new Matrix(m1->hstack(*m2, adapt)); }
    Matrix * matrix_part(const Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept { return new Matrix(m->part(col_start, col_stop, row_start, row_stop)); }
    Matrix * matrix_copy(const Matrix * m) noexcept { return new Matrix(*m); }

    void matrix_set_wcharacter(Matrix * m, size_t col, size_t row, wchar_t cs) noexcept { m->set_wcharacter(col, row, cs); }
    void matrix_set_pixel(Matrix * m, size_t col, size_t row, Pixel * p) noexcept { m->set_pixel(col, row, *p); }

    void matrix_insert_wstring(Matrix * m, size_t col, size_t row, wchar_t * s) noexcept { m->insert_wstring(col, row, s); }
    void matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * mi) noexcept { m->insert_matrix(col, row, *mi); }
    void matrix_insert_matrix_aligned(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va) noexcept { m->insert_matrix_aligned(col, row, *mi, ha, va); }

    bool matrix_insert_colorized_aligned(Matrix * m, size_t col, size_t row, Colorize * c, int ha, bool check_space, bool change_color) noexcept {return m->insert_colorized_aligned(col, row, *c, ha, check_space, change_color);}

    int matrix_insert_colorized_dynamically(Matrix * m, size_t col, size_t row, const Colorize * c) noexcept { return m->insert_colorized_dynamically(col, row, *c); }
    void matrix_insert_points(Matrix * m, Points * points) noexcept { m->insert_points(*points); }

    void matrix_print(Matrix * m, bool colorless) noexcept { m->print(colorless); }

    Matrix * colorize_get_matrix(Colorize * c) noexcept { return new Matrix(colorize_to_matrix(*c)); }

    void fast_print() { std::ios::sync_with_stdio(false); std::wcout.tie(nullptr); }

}

