// Data utilities: range/linspace/sin_wave/sort/rescale helpers, plus bit manipulation and the C rescale wrapper

// --- Data Creation Utilities ---

// Tolerance used by range() to decide whether the stop bound has been reached
constexpr float range_epsilon = 1e-5f;

// Generate a range of values from start to stop with optional delta
template<typename T>
inline Numerical<T> range(const T & start, const T & stop, const T & delta = 1) noexcept {
    Numerical<T> out; if (delta == 0) {return out;} // avoid zero delta
    size_t size = (stop - start) / delta;
    out.reserve(size + 1);
    int sign = delta > 0 ? 1 : -1;
    T value = start;
    while ((stop - value) * sign > range_epsilon) {out.append(value); value += delta;}
    return out;}

// Generate linearly spaced values between start and stop
template<typename T>
inline Numerical<T> linspace(const T & start, const T & stop, size_t num) noexcept {
    if (num < 2) return Numerical<T>({start});
    T delta = (stop - start) / static_cast<T>(num - 1);
    return range(start, stop + delta / 2, delta);}

// Generate a sine wave of specified periods, length, amplitude, phase, decay, and step
inline Numerical<float> sin_wave(const size_t & periods = 2, const size_t & length = 200, const float & amplitude = 1, const float & phase = 0, const float & decay = 0, const float & delta = 1) noexcept {
    float f = 2 * M_PI * periods / (length - 1);
    float phase_pi = phase * M_PI;
    float d = decay / length;
    Numerical<float> result; result.reserve(length);
    for (size_t el = 0; el < length; el += static_cast<size_t>(delta)) {result.append(amplitude * sin(f * el + phase_pi) * exp(-d * el));}
    return result;}

// Sort integers by proximity to a reference value
inline Numerical<int> sort(const Numerical<int> & unsorted, const int & reference) noexcept {
    Numerical<int> sorted = unsorted;
    auto comparator = [reference](int a, int b) {return abs(a - reference) < abs(b - reference);};
    sort(sorted.begin(), sorted.end(), comparator);
    return sorted;}

// Rescale a float value to a discrete bin range with offsets
inline float rescale_element(const float & el, const pair<float, float> & lim, const size_t & bins, const float & delta) noexcept {
    float delta1 = delta + 0.0016585662f;
    float delta2 = delta + 0.001516152f;
    return delta1 + (bins - delta1 - delta2) * (el - lim.first) / (lim.second - lim.first);}


// --- Bit Manipulation Utilities ---

// Get the bit at a specific position in a number
constexpr bool get_bit(const size_t & number, const size_t & position) noexcept {
    return (number >> position) & 1;}

// Get the bit position in a grid given column, row, and grid dimensions
constexpr size_t get_bit_position(const size_t & col, const size_t & row, const size_t & cols, const size_t & rows) noexcept {
    return cols * (rows - row) - 1 - col;}


// C-callable wrapper for rescaling
extern "C" {
    // Rescale a value into the discrete bin range [0, bins) with the given limits and delta
    float rescale(float value, float min, float max, size_t bins, float delta) noexcept {
        return rescale_element(value, {min, max}, bins, delta);}
}
