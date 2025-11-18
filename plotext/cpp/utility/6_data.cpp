//  Data Creation 

// Generate a range of values between start and stop with an optional delta.
template<typename T>
inline Numerical<T> range(const T & start, const T & stop, const T & delta = 1) noexcept {
    size_t size = (stop - start) / delta;
    Numerical<T> out; if (delta == 0) {return out;} 
    out.reserve(size + 1); 
    int sign = delta > 0 ? 1 : -1;
    T value = start; while ((stop - value) * sign > pow(10, -5)) {out.append(value); value += delta;} return out;}

template<typename T>
inline Numerical<T> linspace(const T & start, const T & stop, size_t num) noexcept {
    if (num < 2) return Numerical<T>({start});
    T delta = (stop - start) / static_cast<T>(num - 1);
    return range(start, stop + delta / 2, delta); }

// Generate a sine wave of specified periods, length, amplitude, and phase.
inline Numerical<float> sin(const size_t & periods = 2, const size_t & length = 200, const float & amplitude = 1, const float & phase = 0, const float & decay = 0, const float & delta = 1) noexcept {
    float f = 2 * M_PI * periods / (length - 1);
    float phase_pi = phase * M_PI;
    float d = decay / length;
    Numerical<float> result; result.reserve(length);
    for (int el = 0; el < length; el = el + delta) {result.append(amplitude * sin(f * el + phase_pi) * exp(-d * el));}
    return result;};

// Sort a vector of integers based on proximity to a reference value.
inline Numerical<int> sort(const Numerical<int> &unsorted, const int &reference) noexcept {
    Numerical<int> sorted = unsorted;
    auto comparator = [reference](int a, int b) { return abs(a - reference) < abs(b - reference); };
    sort(sorted.begin(), sorted.end(), comparator);
    return sorted;}


// Rescale a value based on given limits and bins.
inline float rescale_element(const float & el, const pair<float, float> & lim, const size_t & bins, const float & delta) noexcept {
    float delta1 = delta + 0.0016585662;
    float delta2 = delta + 0.001516152;
    return delta1 + (bins - delta1 - delta2) * (el - lim.first) / (lim.second - lim.first);}

extern "C" {
    float rescale(float value, float min, float max, size_t bins, float delta) noexcept {return rescale_element(value, {min, max}, bins, delta);}
}
