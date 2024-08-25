class Marker: public Character, public MarkerType {
public:
	inline Marker() noexcept : Character(), MarkerType() {}
	inline Marker(const wchar_t & c, const Pixel & p = Pixel()) noexcept : Character(c, p), MarkerType(normal) {}
	inline Marker(const marker_type & t, const Pixel & p = Pixel()) noexcept : MarkerType(t), Character(space, p) {}

	inline Marker(const Marker & m) noexcept : Character(m), MarkerType(m) {};
	inline Marker & operator=(const Marker & m) noexcept {Character::operator=(m); MarkerType::operator=(m); return *this;}

	inline void clear() noexcept {Character::clear(); MarkerType::clear();}

	virtual inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    	pixel_to_buffer(buffer, length_buffer);
    	if (is_normal()) {character_to_buffer(buffer, length_buffer);}
    	else {MarkerType::to_buffer(buffer, length_buffer);}
    	cstring_to_buffer(ansi_end, buffer, length_buffer);}

    inline void log() const noexcept {
    	wchar_t buffer[marker_size_max + 1]; buffer[0] = '\0'; size_t length = 0;
   	 	to_buffer(buffer, length);
   	 	wcout << buffer;}
};