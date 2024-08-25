class MarkerType {
private:
	marker_type type;

public:
	inline MarkerType(const marker_type & t = normal) noexcept : type(t) {}

	inline MarkerType(const MarkerType & other) noexcept : type(other.type) {}
	inline MarkerType(MarkerType && other) noexcept : type(other.type) {}
	inline MarkerType & operator=(const MarkerType & m) noexcept {type = m.type; return *this;}

	inline void clear() noexcept {type = normal;}

	inline void set_normal(const marker_type & t) noexcept {type = t;}

	inline constexpr marker_type get_type() const noexcept {return type;}

	inline size_t get_rows() const noexcept {return get_marker_rows(type);}
	inline size_t get_cols() const noexcept {return get_marker_cols(type);}
	inline size_t get_resolution() const noexcept {return get_cols() * get_rows();}

    inline constexpr bool is_normal() const noexcept {return type == normal;}
	inline constexpr bool is_not_normal() const noexcept {return not is_normal();}

	inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
		string str = get_marker_label(type); 
		cstring_to_buffer(string_to_wstring(str).c_str(), buffer, length_buffer);}
};