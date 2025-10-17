template <typename T>
class Vector {
private:
    T * data;          // pointer to dynamic array
    size_t capacity;  // allocated memory size
    size_t length;    // number of elements stored

public:
    Vector() : capacity(0), length(0), data(nullptr) {}

    // constructor
    Vector(const size_t & capacity): capacity(capacity), length(0) {data = new T[capacity];}

    Vector(const size_t & capacity, const T & value): Vector(capacity) {init(value);}

    // copy constructor
    Vector(const Vector & other) : capacity(other.capacity), length(other.length) {
        data = new T[capacity];
        for (size_t i = 0; i < length; ++i) {data[i] = other.data[i];}}

    // initializer_list constructor
    Vector(std::initializer_list<T> init) : Vector(init.size()) {
        //reserve(init.size());
        for (const auto& elem : init)
            push_back(elem);}

    // destructor
    ~Vector() {destroy();}

    // assignment operator
    Vector & operator=(const Vector & other) {
        clear();
        capacity = other.capacity;
        length = other.length;
        data = new T[capacity];
        for (size_t i = 0; i < length; ++i) {data[i] = other.data[i];}
        return *this;}

    // Equality operator
    bool operator==(const Vector<T>& other) const {
        if (length != other.length) return false; // different sizes
        for (size_t i = 0; i < length; ++i) {if (!(data[i] == other.data[i])) return false;}
        return true;}

    // Inequality operator
    bool operator!=(const Vector<T>& other) const {return !(*this == other);}

    // size
    size_t get_length() const {return length;}

    // capacity
    size_t get_capacity() const {return capacity; }

    // clear
    void clear() {length = 0;}

        // Full destroy: deallocates memory and resets vector
    void destroy() noexcept {
        delete[] data;
        data = nullptr;
        clear();
        capacity = 0;}

    void fill(const T & value) {for (size_t i = 0; i < length; ++i) {data[i] = value;}}
    void init(const T & value) {for (size_t i = 0; i < capacity; ++i) {data[i] = value;}}

    void resize(const size_t & l) {length = l;}

    // Reserve capacity
    void reserve(const size_t & new_capacity) {
        if (new_capacity <= capacity) {return;}
        T * new_data = new T[new_capacity];
        for (size_t i = 0; i < length; ++i) {new_data[i] = std::move(data[i]);}
        delete[] data;
        data = new_data;
        capacity = new_capacity;}

    // Function to automatically grow the capacity if needed
    void grow() {
        if (length >= capacity) {
            wcout<<"---------- grow ------------"<< endl;
            size_t new_capacity = (capacity > 0) ? capacity * 2 : 1;
            reserve(new_capacity);}}

    // Access element (non-const)
    T & at(size_t i) {return data[i];}

    // Access element (const)
    const T & at(size_t i) const {return data[i]; }


    // Add a single element at the end
    void append(const T & value) {
        //grow();
        data[length++] = value;}

    // Optionally, also support move semantics
    void move_back(T && value) {
        //grow();
        data[length++] = move(value);}



    // Append all elements from another Vector
    void append(const Vector<T> & other) {
        for (size_t i = 0; i < other.length; ++i) {data[length++] = other.data[i];}}

    // // Optionally, a move version to avoid copies
    // void append(Vector<T> && other) {
    //     for (size_t i = 0; i < other.length; ++i) {data[length++] = move(other.data[i]);} other.clear();}

    void move_back(Vector<T> && other) {
        //reserve(length + other.length);
        std::move(other.data, other.data + other.length, data + length);
        length += other.length;
        //other.clear();
        }


    Vector<T> copy() const {
        Vector<T> newVector;
        newVector.reserve(length);        // pre-allocate memory
        for (size_t i = 0; i < length; ++i) {newVector.emplace_back(data.at(i));}
        return newVector;}

    // Iterator begin
    T * begin() { return data; } 
    const T* begin() const { return data; }

    // Iterator end
    T * end() { return data + length; }
    const T* end() const { return data + length; }

        // << operator as friend so it can access private members
    friend wostream & operator<<(std::wostream & os, const Vector<T> & v) {
        size_t size = v.get_length();
        os << "[";
        for (size_t i = 0; i < size; ++i) {
            os << v.at(i);
            if (i + 1 < size) os << ", ";}
        os << "]";
        return os; }

    friend std::ostream& operator<<(std::ostream & os, const Vector<T> & v) {
        size_t size = v.get_length();
        os << "[";
        for (size_t i = 0; i < size; ++i) {
            os << v.at(i);
            if (i + 1 < size) os << ", ";}
        os << "]";
        return os;}

        // --- get_wstring ---
    wstring get_wstring() const {
        std::wstringstream ss;
        ss << *this;
        return ss.str();}

    void log() const { std::wcout << get_wstring() << std::endl; }

};


// template <typename T>
// class Vector : public std::vector<T> {
// public:
//     // Inherit constructors
//     using std::vector<T>::vector; // inherit constructors

//     // Append a single element
//     void append(const T& value) {
//         this->push_back(value);
//     }

//     // Append another vector
//     void append(const Vector<T>& other) {
//         // use std::vector<T>'s begin() and end(), not our T* versions
//         std::vector<T>::insert(
//             std::vector<T>::end(),
//             other.std::vector<T>::begin(),
//             other.std::vector<T>::end()
//         );
//     }


//     // Get length of vector
//     size_t get_length() const {
//         return this->size();
//     }

//     // Pointer-based begin/end
//     T* begin() {
//         return this->data();
//     }

//     T* end() {
//         return this->data() + this->size();
//     }

//     // Const pointer-based begin/end
//     const T* begin() const {
//         return this->data();
//     }

//     const T* end() const {
//         return this->data() + this->size();
//     }

//     // Log contents to stdout
//     void log() const {
//         std::wcout << "Vector(" << this->size() << "): [";
//         for (size_t i = 0; i < this->size(); ++i) {
//             std::wcout << (*this)[i];
//             if (i + 1 < this->size())
//                 std::wcout << ", ";
//         }
//         std::wcout << "]" << std::endl;
//     }

// };

//     //     // operator[]
//     // T& operator[](size_t index) {
//     //     if (index >= length) {
//     //         throw std::out_of_range("Index out of range");}
//     //     return data[index];}

//     // const T& operator[](size_t index) const {
//     //     if (index >= length) {
//     //         throw std::out_of_range("Index out of range");}
//     //     return data[index];}