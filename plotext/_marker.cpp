#include <vector>

using namespace std;

vector<bool> sum_vectors(vector<bool> v1, vector<bool> v2){
  vector<bool> v;
  for (size_t i = 0; i < v1.size(); i++) {v.push_back(v1[i] or v2[i]);}
  return v;}


class HDmarker{
public:
  wchar_t marker;
  vector<bool> code;

  HDmarker() {marker = L'X'; code = {0};};
  
  HDmarker(vector<bool> c, wchar_t m) : marker(m), code(c) {}

  void log(){
    size_t l = code.size();
    cout << "(";
    for (size_t i = 0; i < l; i ++) {cout << code[i]; if (i != l - 1){cout << ", ";};}
    cout << "): "; wcout << marker << endl;}

  bool operator==(HDmarker M) const {return marker == M.marker;}
  bool operator==(wchar_t m) const {return marker == m;}
  bool operator==(vector<bool> c) const {return code == c;}
};


class HDmarkers{
public:
  vector<HDmarker> markers;

  ~HDmarkers() {markers.clear();}

  void append_marker(vector<bool> c, wchar_t m){
    markers.push_back(HDmarker(c, m));}

  HDmarker get(wchar_t m){
    HDmarker M;
    for(HDmarker marker : markers){if(marker == m){M = marker;}}
    return M;}

  HDmarker get(vector<bool> c){
    HDmarker M;
    for(HDmarker marker : markers){if (marker == c){M = marker;}}
    return M;}

  vector<bool> get_vector(wchar_t m){return get(m).code;}

  wchar_t get_marker(vector<bool> c){return get(c).marker;}

  wchar_t sum(wchar_t m1, wchar_t m2) {return get_marker(sum_vectors(get_vector(m1), get_vector(m2)));}

  bool in(wchar_t m){bool res = false; HDmarker M = get(m); if(not (M == HDmarker())){res = true;} return res;}

  void log(){cout << "size: " << markers.size() << endl;
    for(HDmarker marker : markers) {marker.log();}}};


int main(){


}
