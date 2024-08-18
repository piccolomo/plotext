using namespace std;

// Color

inline unsigned char get_color_code(const string & color) noexcept {
    auto pair = color_codes.find(color);
    if (pair != color_codes.end()) {return pair->second;}
    else {return 100;}};


// Style

inline unsigned char get_style_code(const string & style) {
    auto pair = style_codes.find(style);
    if (pair != style_codes.end()) {return pair->second;}
    else {return 100;}};


// Marker

inline wchar_t string_to_character(const string & code) {
    auto it = marker_codes.find(code);
    if (it != marker_codes.end()){return it->second;} else {return code[0];}}

inline unsigned char get_marker_rows(const MarkerType & type) {
    auto it = marker_rows.find(type);
    if (it != marker_rows.end()) {return it->second;} else {return 0;}}

inline unsigned char get_marker_cols(const MarkerType & type) {
    auto it = marker_cols.find(type);
    if (it != marker_cols.end()) {return it->second;} else {return 0;}}

inline string get_marker_label(const MarkerType & type) {
    for (const auto & pair: marker_labels) {if (pair.first == type) {return pair.second;}} return "normal";}

inline wchar_t code_to_hd_character(const unsigned char & code) {
    auto it = hd_codes.find(code);
    if (it != hd_codes.end()){return it->second;} else {return L'H';}}
   
inline wchar_t code_to_fhd_character(const unsigned char & code) {
    auto it = fhd_codes.find(code);
    if (it != fhd_codes.end()){return it->second;} else {return L'F';}}

inline wchar_t code_to_braille_character(const unsigned char & code) {
    auto it = braille_codes.find(code);
    if (it != braille_codes.end()){return it->second;} else {return L'B';}}
    

const unordered_map<MarkerType, function<wchar_t(const unsigned char &)>> marker_converters = {
  {hd, code_to_hd_character},
  {fhd, code_to_fhd_character},
  {braille, code_to_braille_character}};

inline function<wchar_t(const unsigned char &)> get_marker_converter(const MarkerType & type) noexcept {
    auto it = marker_converters.find(type);
    if (it != marker_converters.end()) {return it->second;} else {return [](const unsigned char &) { return L'N'; };}};


// Placement

// inline signed char get_ha_code(const string & code) {
//     auto pair = ha_codes.find(code);
//     if (pair != ha_codes.end()) {return pair->second;}
//     else {return -1;}};

// inline signed char get_va_code(const std::string & code) {
//     auto pair = va_codes.find(code);
//     if (pair != va_codes.end()) {
//         return pair->second;} else {return -1;}}

