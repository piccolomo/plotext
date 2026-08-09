// Normal marker maps: symbol name -> glyph, marker-kind tags, representative glyph per kind

const unordered_map<string, wchar_t> symbol_codes = {
  {"full",         L'█'},
  {"brick",        L'▇'},
  {"dot",          L'•'},
  {"dollar",       L'$'},
  {"euro",         L'€'},
  {"bitcoin",      L'฿'},
  {"at",           L'@'},
  {"heart",        L'♥'},
  {"smile",        L'☺'},
  {"shamrock",     L'☘'},
  {"atom",         L'⚛'},
  {"snowflake",    L'❄'},
  {"sun",          L'☀'},
  {"cloud",        L'☁'},
  {"umbrella",     L'☂'},
  {"zigzag",       L'↯'},
  {"star",         L'❋'},
  {"emptystar",    L'☆'},
  {"flower",       L'❁'},
  {"queen",        L'♕'},
  {"king",         L'♔'},
  {"cross",        L'♰'},
  {"yinyang",      L'☯'},
  {"om",           L'ॐ'},
  {"square",       L'■'},
  {"emptysquare",  L'□'},
  {"circle",       L'●'},
  {"emptycircle",  L'○'},
  {"diamond",      L'◆'},
  {"emptydiamond", L'◇'},
  {"up",           L'▲'},
  {"down",         L'▼'},
  {"left",         L'◀'},
  {"right",        L'▶'},
  {"arrowup",      L'↑'},
  {"arrowdown",    L'↓'},
  {"arrowleft",    L'←'},
  {"arrowright",   L'→'},
  {"infinity",     L'∞'},
  {"check",        L'✓'},
  {"xmark",        L'✗'},
  {"eighth",       L'♪'},
  {"beamed",       L'♫'},
  {"flat",         L'♭'},
  {"sharp",        L'♯'},
};

// The glyph of a symbol code, as ♥ for "heart"; an unknown code gives its first character, an empty one the space.
inline wchar_t get_symbol(const string & code) {
    auto it = symbol_codes.find(code);
    if (it != symbol_codes.end()) {return it->second;}
    return code.empty() ? L' ' : code[0];}


// Cell-kind tags: identify which marker kind produced a Matrix cell. marker_none = 0 so default-constructed cells (kind = 0) read as "no kind" naturally; real kinds start from 1.
constexpr uint8_t marker_none    = 0;
constexpr uint8_t marker_normal  = 1;
constexpr uint8_t marker_hd      = 2;
constexpr uint8_t marker_fhd     = 3;
constexpr uint8_t marker_braille = 4;
constexpr uint8_t marker_box     = 5;

// Representative model glyph per kind, used by Python's marker preview / docs.
const unordered_map<uint8_t, wchar_t> symbol_model = {
    {marker_normal,  L'?'},
    {marker_hd,      L'▚'},
#ifdef _WIN32
    {marker_fhd,     L' '},          // the sextant sample asks for more room than a windows character has, and fhd is not a code there anyway
#else
    {marker_fhd,     L'🬗'},
#endif
    {marker_braille, L'⢕'},
    {marker_box,     L'┼'}};

// The representative glyph of a marker kind, as ▚ for the high definition one; an unknown kind gives the question mark.
inline wchar_t get_symbol_model(uint8_t type) noexcept {
    auto it = symbol_model.find(type);
    return it != symbol_model.end() ? it->second : L'?'; }
