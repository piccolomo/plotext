// Vector: dynamic-length container built on top of Array (capacity vs logical length)

template <typename T>
class Vector : private Array<T> {
private:
    size_t length = 0; // logical number of elements (capacity lives in Array<T>)

public:
    using Array<T>::at;
    using Array<T>::begin;

    // --- Constructors ---

    // Default constructor
    Vector() noexcept : Array<T>(), length(0) {}

    // Construct with the given capacity
    explicit Vector(size_t capacity) : Array<T>(capacity) {}

    // Construct with the given capacity, filled with a value
    Vector(size_t capacity, const T & value) : Vector(capacity) {fill(value); }

    // Construct from an initializer list
    Vector(std::initializer_list<T> init) : Array<T>(init), length(init.size()) {}

    // Copy constructor
    Vector(const Vector<T> & other) : Array<T>(other.get_capacity()), length(other.length) {copy_from(other);}

    // Move constructor
    Vector(Vector<T> && other) noexcept : Array<T>(std::move(other)), length(other.length) {other.set_length(0);}

    // Destructor
    ~Vector() = default;

    // Copy assignment (self-assignment safe)
    Vector & operator=(const Vector<T> & other) {
        if (this != &other) clone(other);
        return *this;}

    // Move assignment
    Vector & operator=(Vector<T> && other) noexcept {
        if (this != &other) {
            Array<T>::operator=(std::move(other));
            length = other.length;
            other.length = 0; }
        return *this;}

    // Equality comparison
    bool operator==(const Vector<T>& other) const {
        if (get_length() != other.get_length()) return false;
        for (size_t i = 0; i < get_length() ; ++i)
            if (not (at(i) == other.at(i))) return false;
        return true; }

    // Inequality comparison
    bool operator!=(const Vector<T> & other) const { return !(*this == other); }

    // Iterator end (mutable)
    T * end() {return begin() + length;}

    // Iterator end (const)
    const T* end() const {return begin() + length;}

    // Logical number of elements
    size_t get_length() const {return length;}

    // Allocated capacity
    size_t get_capacity() const {return Array<T>::get_length();}

    // Return a plain Array<T> containing the logical elements (exact size)
    Array<T> get_array() const {
        Array<T> result(get_length());
        result.copy_from(begin(), get_length());
        return result;}

    // Resize the capacity, preserving as many elements as fit. Empty case (length==0) skips the copy round-trip, saves work AND silences a GCC bounds-analysis warning when reserving on a freshly-empty vector.
    void set_capacity(const size_t & new_capacity) {
        if (length == 0) { Array<T>::reallocate(new_capacity); return; }
        Vector<T> temp(*this);                      // copy the data
        Array<T>::reallocate(new_capacity);          // allocate new array
        set_length(min(new_capacity, length));
        copy_from(temp);}

    // Convenience: reserve capacity
    void reserve(size_t capacity) {set_capacity(capacity);}


    // Double the capacity (at least 1)
    void grow() {size_t cap = get_capacity(); if (length >= cap) set_capacity(cap > 0 ? cap * 2 : 1);}

    // Grow if the logical length reached capacity
    void check_and_grow() {if (length >= get_capacity()) grow();}

    // Set the logical length (must not exceed capacity)
    void set_length(const size_t & new_length){
        assert(new_length <= get_capacity());
        length = new_length; }

    // Increase (or decrease) the logical length by a delta
    void increase_length(const int & delta) {set_length(length + delta);}

    // Reset logical length to 0
    void clear() { this->set_length(0); }


    // Fill the logical region with a value
    void fill(const T & value) {for (size_t i = 0; i < length; ++i) {at(i) = value;}}

    // Copy source_length elements from a raw pointer into the logical region
    void copy_from(const T * source, size_t source_length) {
        for (size_t i = 0; i < source_length; ++i)
            at(i) = source[i];}

    // Copy the overlapping prefix from another Vector
    void copy_from(const Vector<T> & other) {Array<T>::copy_from(other.begin(), min(other.get_length(), get_length())); }

    // Replace contents with a deep copy of another Vector
    void clone(const Vector<T> & other) {
        Array<T>::reallocate(other.get_capacity());
        set_length(other.get_length());
        copy_from(other);
    }

    // Return a deep copy
    Vector<T> copy() const {
        Vector<T> new_array(get_capacity());
        new_array.set_length(get_length());
        new_array.copy_from(*this);
        return new_array;}


    // Append a single element
    void append(const T & value) {size_t l = get_length(); increase_length(1); at(l) = value;}

    // Append every element of another Vector
    void append(const Vector<T> & other) {for (size_t i = 0; i < other.get_length(); ++i) {append(other.at(i));}}

    // Move-append a single rvalue
    void move_back(T && value) {size_t l = get_length(); increase_length(1); at(l) = move(value);}

    // Move-append every element of another Vector (leaves other cleared)
    void move_back(Vector<T>&& other) {
        const auto other_len = other.get_length();
        const auto old_len   = get_length();

        increase_length(other_len);

        std::move(other.begin(), other.begin() + other_len, Array<T>::begin() + old_len);

        other.clear();}

    // True if an element equals el
    bool is_in(const T & el) const {for (size_t i = 0; i < length; ++i) if (at(i) == el) return true; return false;}


    // --- Stretch (specific to Vector) ---

    // Resample the vector to the requested larger size, repeating existing values
    void stretch(size_t size) {
        size_t old_length = this->get_length();
        if (old_length == 0 || size <= old_length) return;
        Vector<T> temp(*this);
        this->reserve(size);
        this->set_length(size);
        for (size_t i = 0; i < size; ++i) {
            size_t idx = i * old_length / size;
            if (idx >= old_length) idx = old_length - 1;
            this->at(i) = temp.at(idx);}}
};
