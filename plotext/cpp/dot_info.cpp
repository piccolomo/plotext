class DotInfo : public FillInfo, public MiniDot {
public:
  inline DotInfo() noexcept : FillInfo(), MiniDot() {}; 
  inline DotInfo operator|(const DotInfo & di) const noexcept {DotInfo r; static_cast<FillInfo&>(r) = FillInfo::operator|(di); static_cast<MiniDot&>(r) = MiniDot::operator|(di); return r;}
  inline DotInfo operator|(const FillInfo & fi) const noexcept {DotInfo r; static_cast<FillInfo&>(r) = FillInfo::operator|(fi); return r;}
  inline DotInfo & operator=(const DotInfo & r) noexcept {FillInfo::operator=(r); MiniDot::operator=(r); return *this;}

  inline constexpr FillInfo get_fill_info() const noexcept {return *this;}

  inline void log() const noexcept {FillInfo::log(); wcout << L", "; MiniDot::log();}
};