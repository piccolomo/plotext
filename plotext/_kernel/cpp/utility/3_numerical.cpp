// Numerical: Vector<T> extended with scalar arithmetic, sorting and nearest-value lookup

template <typename T>
class Numerical : public Vector<T> {
public:
    using Vector<T>::Vector;
    using Vector<T>::get_length;
    using Vector<T>::at;
    using Vector<T>::append;
    using Vector<T>::begin;
    using Vector<T>::end;

    // Multiply every element by a scalar factor
    void multiply(const T & factor) {for (size_t i = 0; i < get_length(); ++i) at(i) *= factor;}

    // Add a scalar to every element
    void add(const T & factor) {for (size_t i = 0; i < get_length(); ++i) at(i) += factor;}

    // Negate every element in place
    void invert() {multiply(-1);}

    // Sort elements in ascending order
    void sort() {std::sort(begin(), begin() + get_length());}

    // Return the element closest to the given value (ties resolved by earlier index)
    T get_closest(const T & value) const {
        T best = at(0);
        auto min_diff = std::abs(best - value);
        for (size_t i = 1; i < get_length(); ++i) {
            auto diff = abs(at(i) - value);
            if (diff < min_diff) {
                min_diff = diff;
                best = at(i); }
        }
        return best;}

    // Check if elements are in ascending order
    bool is_sorted() const {for (size_t i = 1; i < get_length(); ++i) if (at(i) < at(i - 1)) return false; return true;}
};
