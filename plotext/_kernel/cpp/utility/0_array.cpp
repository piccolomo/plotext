// Array: owning dynamic-length buffer used throughout the kernel

template <typename T>
class Array {
private:
    T * data = nullptr;
    size_t length = 0;

public:
    // --- Constructors ---

    // Default constructor
    Array() noexcept = default;

    // Length constructor (allocates without filling)
    explicit Array(const size_t& len) { allocate(len);}

    // Fill constructor (allocates and fills with value)
    Array(const size_t& len, const T& value) {
        allocate(len);
        fill(value); }

    // Initializer list constructor
    Array(std::initializer_list<T> init) {
        allocate(init.size());
        copy_from(init.begin(), init.size()); }

    // Copy constructor
    Array(const Array<T> & other) {
        allocate(other.get_length());
        copy_from(other); }

    // Move constructor
    Array(Array<T> && other) noexcept : data(other.data), length(other.length) {
        other.data = nullptr;
        other.length = 0;}

    // Destructor
    ~Array() {destroy();}

    // --- Iterators ---

    // Iterator begin
    T * begin() {return data;}

    // Const iterator begin
    const T* begin() const {return data;}

    // Iterator end
    T * end() {return data + length;}

    // Const iterator end
    const T* end() const {return data + length;}

    // --- Assignment ---

    // Copy assignment (self-assignment safe)
    Array& operator=(const Array& other) {
        if (this != &other) clone(other);
        return *this; }

    // Move assignment
    Array& operator=(Array&& other) noexcept {
        if (this != &other) {
            destroy();
            data = other.data;
            length = other.length;
            other.data = nullptr;
            other.length = 0; }
        return *this; }

    // --- Comparison ---

    // Equality comparison
    bool operator==(const Array<T>& other) const {
        if (length != other.get_length()) return false;
        for (size_t i = 0; i < length; ++i)
            if (!(data[i] == other.at(i))) return false;
        return true; }

    // Inequality comparison
    bool operator!=(const Array<T>& other) const { return !(*this == other); }

    // --- Memory Management ---

    // Release ownership of the underlying buffer (caller becomes responsible for deleting it)
    T * release_data() noexcept {
        T * temp = data;
        data = nullptr;
        length = 0;
        return temp; }

    // Delete the underlying buffer and reset state
    void destroy() noexcept { delete[] release_data(); }

    // Allocate a new buffer of the given length (zero-initialized)
    void allocate(const size_t & new_length) {
        data = new T[new_length]();
        length = new_length; }

    // Reallocate to a new length (discards current contents)
    void reallocate(const size_t & new_length) {
        destroy();
        allocate(new_length);}

    // Clear the array (reallocate to length 0)
    void clear() {reallocate(0);}

    // Resize the array; shrinking truncates, growing zero-fills the extra slots
    void set_size(const size_t & new_length){
        Array<T> temp(*this);
        reallocate(new_length);
        copy_from(temp.begin(), std::min(temp.get_length(), new_length));}

    // Overwrite a single element at the given index
    inline void insert(size_t index, const T & value) noexcept {assert(index < length); data[index] = value;}

    // Overwrite a run of elements starting at index with values from another Array
    inline void insert(size_t index, const Array<T>& other) noexcept {size_t i = 0; for (auto & el: other) data[index + (i++)] = el;}

    // --- Accessors ---

    // Number of elements in the array
    size_t get_length() const noexcept { return length; }

    // Element access (mutable)
    T & at(size_t i) noexcept { return data[i]; }

    // Element access (const)
    const T& at(size_t i) const noexcept { return data[i]; }

    // Indexing operator (mutable)
    T & operator[](size_t i) noexcept {return data[i];}

    // Indexing operator (const)
    const T & operator[](size_t i) const noexcept {return data[i];}

    // Check if an element exists in the array
    bool is_in(const T& el) const { for (size_t i = 0; i < length; ++i) if (data[i] == el) return true; return false; }

    // Check if every element equals the given value
    bool is_constant(const T & value) const noexcept {
        for (size_t i = 0; i < length; ++i) {if (not (at(i) == value)) return false;}
        return true;}

    // --- Modifiers ---

    // Fill the array with a value
    void fill(const T& value) { for (size_t i = 0; i < length; ++i) data[i] = value; }

    // Reverse the elements in place
    void reverse() { for (size_t i = 0; i < length / 2; ++i) std::swap(data[i], data[length - 1 - i]); }

    // --- Utilities ---

    // Copy source_length elements from a raw pointer into this array at offset. Early return on empty source, keeps the compiler from warning when source happens to be a freshly-constructed (empty, possibly-null) buffer.
    void copy_from(const T* source, size_t source_length, size_t offset = 0) {
        if (source_length == 0) return;
        for (size_t i = 0; i < source_length; ++i)
            data[offset + i] = source[i];}

    // Copy every element of another Array into this array (starting at index 0)
    void copy_from(const Array<T> & other) { copy_from(other.begin(), other.get_length()); }

    // Return a deep copy of the array
    Array<T> copy() const {
        Array<T> new_array(length);
        new_array.copy_from(*this);
        return new_array; }

    // Replace this array's contents with a deep copy of another
    void clone(const Array<T> & other) {
        reallocate(other.length);
        copy_from(other);}

    // Return a slice [i1, i2) as a new Array
    Array part(size_t i1, size_t i2) const {
        size_t len = i2 - i1;
        Array out(len);
        out.copy_from(data + i1, len);
        return out;}

    // Return a new Array formed by concatenating this array with another
    Array<T> stack(const Array<T>& other) const {
        Array<T> result(length + other.length);
        result.copy_from(data, length, 0);
        result.copy_from(other.data, other.length, length);
        return result;}

    // --- Output ---

    // Wide-stream output
    friend wostream& operator<<(wostream& os, const Array<T>& v) {
        os << L"[";
        for (size_t i = 0; i < v.length; ++i) {
            os << v.data[i];
            if (i + 1 < v.length) os << L", "; }
        os << L"]";
        return os; }

    // Narrow-stream output
    friend ostream& operator<<(ostream& os, const Array<T>& v) {
        os << "[";
        for (size_t i = 0; i < v.length; ++i) {
            os << v.data[i];
            if (i + 1 < v.length) os << ", "; }
        os << "]";
        return os; }

    // Convert to narrow string
    string get_string() const {
        stringstream ss;
        ss << *this;
        return ss.str(); }

    // Convert to wide string
    std::wstring get_wstring() const {
        std::wstringstream ss;
        ss << *this;
        return ss.str();}

    // Print to wcout
    void log() const { wcout << *this << endl; }
};
