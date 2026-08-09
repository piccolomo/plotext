// Data utilities: range/linspace/sin_wave/sort/rescale helpers, plus bit manipulation and the C rescale wrapper

// --- Data Creation Utilities ---

// Tolerance used by range() to decide whether the stop bound has been reached
constexpr float range_epsilon = 1e-5f;

// Generate a range of values from start to stop with optional delta
template<typename T>
inline Vector<T> range(const T & start, const T & stop, const T & delta = 1) noexcept {
    Vector<T> out; if (delta == 0) {return out;} // avoid zero delta
    size_t size = (stop - start) / delta;
    out.reserve(size + 1);
    int sign = delta > 0 ? 1 : -1;
    T value = start;
    while ((stop - value) * sign > range_epsilon) {out.append(value); value += delta;}
    return out;}

// Generate linearly spaced values between start and stop
template<typename T>
inline Vector<T> linspace(const T & start, const T & stop, size_t num) noexcept {
    if (num < 2) return Vector<T>({start});
    T delta = (stop - start) / static_cast<T>(num - 1);
    return range(start, stop + delta / 2, delta);}


// Sort integers by proximity to a reference value
inline Vector<int> sort(const Vector<int> & unsorted, const int & reference) noexcept {
    Vector<int> sorted = unsorted;
    auto comparator = [reference](int a, int b) {return abs(a - reference) < abs(b - reference);};
    sort(sorted.begin(), sorted.end(), comparator);
    return sorted;}

// Rescale a float value to a discrete bin range with offsets
inline float rescale_element(const float & el, const pair<float, float> & lim, const size_t & bins, const float & delta) noexcept {
    float delta1 = delta + 0.0016585662f;
    float delta2 = delta + 0.001516152f;
    return delta1 + (bins - delta1 - delta2) * (el - lim.first) / (lim.second - lim.first);}


// --- Bit Manipulation Utilities ---



// C-callable wrapper for rescaling
extern "C" {
    // Rescale a value into the discrete bin range [0, bins) with the given limits and delta
    float rescale(float value, float min, float max, size_t bins, float delta) noexcept {
        return rescale_element(value, {min, max}, bins, delta);}
}
