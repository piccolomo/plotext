class DotMap {
private:
	size_t index;
	size_t row;

public:
	inline DotMap(const size_t & r, const size_t & i) noexcept : row(r), index(i) {}

	inline bool operator==(const DotMap & ei) noexcept {return ei.index == index;}

	inline void set_index(const size_t & i) noexcept {index = i;}

	inline size_t get_index() const {return index;}
	inline size_t get_row() const noexcept {return row;}

	inline void log() const noexcept {wcout << "(row " << row << ", index " << get_index() << ")";}
};



class ColMap {
private:
	size_t col;
	vector<DotMap> map;

public:
	inline ColMap(const size_t & c) noexcept : col(c) {};
	inline ColMap(const size_t & col, const size_t & row, const size_t & index) noexcept : ColMap(col) {map.emplace_back(row, index);};

	inline bool operator==(const ColMap & cm) noexcept {return col == cm.col;}
	
	inline size_t get_length() const noexcept {return map.size();}
	inline size_t get_col() const noexcept {return col;}
	inline size_t get_map_index(const size_t & row) noexcept {size_t length = get_length(); for(size_t j = 0; j < length; j++) {if(map.at(j).get_row() == row) {return j;}} return size_max;}
	inline size_t get_index(const size_t & row) noexcept {size_t map_index = get_map_index(row); if (map_index != size_max) {return map.at(map_index).get_index();} return size_max;}

	inline void add_index(const size_t & row, const size_t & index) noexcept {
		size_t map_index = get_map_index(row); 
		if (map_index != size_max) {return map.at(map_index).set_index(index);} 
		else {map.emplace_back(row, index);} }

	inline void log() const noexcept {wcout << "[col " << col << " "; for (auto d: map) {d.log();} wcout << "]";}
};


class MatrixMap{
private:
	vector<ColMap> map;

public:
	inline size_t get_length() const noexcept {return map.size();}
	inline size_t get_map_index(const size_t & col) noexcept {size_t length = get_length(); for(size_t j = 0; j < length; j++) {if(map.at(j).get_col() == col){return j;}} return size_max;}
	inline size_t get_index(const size_t & col, const size_t & row) noexcept {size_t map_index = get_map_index(col); if (map_index != size_max) {return map.at(map_index).get_index(row);} return size_max;}
	
	inline void add_index(const size_t & col, const size_t & row, const size_t & index) noexcept {
		size_t map_index = get_map_index(col); 
		if (map_index != size_max) {return map.at(map_index).add_index(row, index);} 
		else {map.emplace_back(col, row, index);} }
	
	inline void log() const noexcept {for (auto r: map) {r.log();}}
};