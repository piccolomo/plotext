// Vector and Numerical classes: dynamic array container and numeric extensions
// Implements dynamic resizing, numeric operations, and utility functions

template <typename T>
class Vector {
private:
    T * data;          // pointer to dynamic array
    size_t capacity;   // allocated memory size
    size_t length;     // number of elements stored

public:
    // --- Constructors ---
    Vector() : capacity(0), length(0), data(nullptr) {}
    Vector(const size_t & capacity): capacity(capacity), length(0) {data = new T[capacity];}
    Vector(const size_t & capacity, const T & value): Vector(capacity) {init(value);}
    Vector(std::initializer_list<T> init) : Vector(init.size()) {for (const auto& elem : init) append(elem);}
    Vector(const Vector & other) : capacity(other.capacity), length(other.length) {
        data = new T[capacity]; for (size_t i = 0; i < length; ++i) {data[i] = other.data[i];}}
    Vector(Vector && other) noexcept : Vector(other) {other.destroy();}

    // --- Destructor ---
    ~Vector() {destroy();}

    // --- Assignment operator ---
    Vector & operator=(const Vector & other) {
        if (this == &other) return *this; // self-assignment check
        destroy();
        capacity = other.capacity;
        length = other.length;
        data = new T[capacity];
        for (size_t i = 0; i < length; ++i) {data[i] = other.data[i];}
        return *this;}

    // --- Comparison ---
    bool operator==(const Vector<T>& other) const {
        if (length != other.length) return false;
        for (size_t i = 0; i < length; ++i) {if (!(data[i] == other.data[i])) return false;}
        return true;}
    bool operator!=(const Vector<T>& other) const {return !(*this == other);}

    // --- Accessors ---
    size_t get_length() const {return length;}
    size_t get_capacity() const {return capacity;}
    T & at(size_t i) {return data[i];}
    const T & at(size_t i) const {return data[i];}
    T & last() {return data[length - 1];} // get last element

    // --- Iterators ---
    T * begin() {return data;}   // Iterator begin
    const T* begin() const {return data;}
    T * end() {return data + length;}  // Iterator end
    const T* end() const {return data + length;}

    // --- Modifiers ---
    void append(const T & value) {if (length >= capacity) reserve(capacity > 0 ? capacity * 2 : 1); data[length++] = value;}
    void append(const Vector<T> & other) {for (size_t i = 0; i < other.length; ++i) {append(other.data[i]);}}
    void move_back(T && value) {if (length >= capacity) reserve(capacity > 0 ? capacity * 2 : 1); data[length++] = move(value);}
    void move_back(Vector<T> && other) {if (length + other.length > capacity) reserve(length + other.length); std::move(other.data, other.data + other.length, data + length); length += other.length; other.clear();}
    void pop() {if (length > 0) length--;}
    void clear() {length = 0;}
    void set_length(const size_t & l) {length = l;}

    // --- Memory management ---
    void destroy() noexcept {delete[] data; data = nullptr; clear(); capacity = 0;}
    void reserve(const size_t & new_capacity) {if (new_capacity <= capacity) return; T * new_data = new T[new_capacity]; for (size_t i = 0; i < length; ++i) {new_data[i] = std::move(data[i]);} delete[] data; data = new_data; capacity = new_capacity;}
    void minimize() {reserve(length);}
    void grow() {if (length >= capacity) reserve(capacity > 0 ? capacity * 2 : 1);}
    void init(const T & value) {for (size_t i = 0; i < capacity; ++i) {data[i] = value;}}
    void fill(const T & value) {for (size_t i = 0; i < length; ++i) {data[i] = value;}}

    // --- Utilities ---
    bool is_in(const T & el) const {for (size_t i = 0; i < length; ++i) if (data[i] == el) return true; return false;}
    Vector<T> get_unique() const {Vector<T> unique; for (size_t i = 0; i < length; ++i) if (!unique.is_in(data[i])) {unique.append(data[i]);} return unique;}
    Vector<T> copy() const {Vector<T> newVector; newVector.reserve(length); for (size_t i = 0; i < length; ++i) {newVector.append(data[i]);} return newVector;}
    void reverse() {for (size_t i = 0; i < length / 2; ++i) std::swap(data[i], data[length - 1 - i]);}
    void stretch(const size_t & size) { // eg: [1,2,3] -> [1,1,2,2,3,3]
        size_t old_length = get_length(); if (old_length == 0 || size <= old_length) return;
        Vector<T> temp(*this); set_length(size);
        for (size_t i = 0; i < size; ++i) {size_t idx = static_cast<size_t>(std::floor((float)i * old_length / size)); if (idx >= old_length) idx = old_length - 1; at(i) = temp.at(idx);}}

    // --- Output ---
    friend wostream & operator<<(std::wostream & os, const Vector<T> & v) {size_t size = v.get_length(); os << "Vector ["; for (size_t i = 0; i < size; ++i) {os << v.at(i); if (i + 1 < size) os << ", ";} os << "]"; return os;}
    friend ostream & operator<<(std::ostream & os, const Vector<T> & v) {size_t size = v.get_length(); os << "["; for (size_t i = 0; i < size; ++i) {os << v.at(i); if (i + 1 < size) os << ", ";} os << "]"; return os;}
    string get_string() const {stringstream ss; ss << *this; return ss.str();}
    wstring get_wstring() const {wstringstream ss; ss << *this; return ss.str();}
    void log() const {wcout << *this << endl;}
};


template <typename T>
class Numerical : public Vector<T> {
public:
    using Vector<T>::Vector;
    using Vector<T>::get_length;
    using Vector<T>::at;
    using Vector<T>::append;

    void multiply(const T & factor) {for (size_t i = 0; i < get_length(); ++i) at(i) *= factor;}
    void add(const T & factor) {for (size_t i = 0; i < get_length(); ++i) at(i) += factor;}
    void invert() {multiply(-1);}
    void sort() {std::sort(data, data + get_length());}

    T get_closest(const T & value) const {T best = at(0); float min_diff = std::abs(best - value); for (size_t i = 1; i < get_length(); ++i) {float diff = abs(at(i) - value); if (diff < min_diff) {min_diff = diff; best = at(i);}} return best;}
    bool is_sorted() const {for (size_t i = 1; i < get_length(); ++i) if (at(i) < at(i - 1)) return false; return true;}
};
