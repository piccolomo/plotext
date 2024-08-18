class Marker: public Character {
private:
	MarkerType type;
	
public:
	inline Marker() noexcept : Character() {type = normal;}
	inline Marker(const wchar_t & c, const Pixel & p = Pixel()) noexcept : Marker(normal, p) {set_char(c);}
	inline Marker(const MarkerType & t, const Pixel & p = Pixel()) noexcept : type(t), Character(space, p) {}
	inline Marker(const Marker & m) noexcept : type(m.type), Character(m) {};

	inline void clear() noexcept {type = normal; Character::clear();}

	inline void set_type(const MarkerType & t) noexcept {type = t;}

	inline constexpr MarkerType get_type() const noexcept {return type;}
	inline size_t get_rows() const noexcept {return get_marker_rows(type);}
	inline size_t get_cols() const noexcept {return get_marker_cols(type);}
	inline size_t get_resolution() const noexcept {return get_cols() * get_rows();}

    inline constexpr bool is_normal() const noexcept {return type == normal;}
	inline constexpr bool is_hd() const noexcept {return not is_normal();}

	inline void type_to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {string str = get_marker_label(type); cstring_to_buffer(string_to_wstring(str).c_str(), buffer, length_buffer);}

	virtual inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    	pixel_to_buffer(buffer, length_buffer);
    	if (is_normal()) {character_to_buffer(buffer, length_buffer);}
    	else {type_to_buffer(buffer, length_buffer);}
    	cstring_to_buffer(ansi_end, buffer, length_buffer);
    }
};