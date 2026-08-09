// High-definition marker maps: HD (2x2), FHD (2x3), Braille (2x4) glyph lookups and Box-drawing line lookups

// HD codes

constexpr wchar_t hd_lookup[16] = {
    L' ',  // 0b0000
    L'▗',  // 0b0001
    L'▖',  // 0b0010
    L'▄',  // 0b0011
    L'▝',  // 0b0100
    L'▐',  // 0b0101
    L'▞',  // 0b0110
    L'▟',  // 0b0111
    L'▘',  // 0b1000
    L'▚',  // 0b1001
    L'▌',  // 0b1010
    L'▙',  // 0b1011
    L'▀',  // 0b1100
    L'▜',  // 0b1101
    L'▛',  // 0b1110
    L'█'   // 0b1111
};

// Retrieve the HD character for a given 4-bit code
constexpr inline wchar_t get_hd_symbol(unsigned char code) noexcept {return hd_lookup[code];}

// The single bit of the sub cell at (col, row) inside a cols by rows grid, the top left taking the highest bit and the bottom right bit 0; used by the hd, fhd and braille characters.
inline constexpr uint8_t get_dot_bit(uint8_t col, uint8_t row, uint8_t cols, uint8_t rows) noexcept { return 1u << (cols * rows - 1 - row * cols - col); }


// FHD codes: the characters of every 6 bit code, from 0 to 63
// These sextants ask for more room than a windows character has, so there the table holds blanks and is never read: fhd is not among the codes on windows, and the word is drawn as plain text instead.
#ifdef _WIN32
constexpr wchar_t fhd_lookup[64] = {};
#else
constexpr wchar_t fhd_lookup[64] = {
    U' ',    // 0b000000 = 0
    U'🬞',   // 0b000001 = 1
    U'🬏',   // 0b000010 = 2
    U'🬭',   // 0b000011 = 3
    U'🬇',   // 0b000100 = 4
    U'🬦',   // 0b000101 = 5
    U'🬖',   // 0b000110 = 6
    U'🬵',   // 0b000111 = 7
    U'🬃',   // 0b001000 = 8
    U'🬢',   // 0b001001 = 9
    U'🬓',   // 0b001010 = 10
    U'🬱',   // 0b001011 = 11
    U'🬋',   // 0b001100 = 12
    U'🬩',   // 0b001101 = 13
    U'🬚',   // 0b001110 = 14
    U'🬹',   // 0b001111 = 15
    U'🬁',   // 0b010000 = 16
    U'🬠',   // 0b010001 = 17
    U'🬑',   // 0b010010 = 18
    U'🬯',   // 0b010011 = 19
    U'🬉',   // 0b010100 = 20
    U'▐',    // 0b010101 = 21
    U'🬘',   // 0b010110 = 22
    U'🬷',   // 0b010111 = 23
    U'🬅',   // 0b011000 = 24
    U'🬤',   // 0b011001 = 25
    U'🬔',   // 0b011010 = 26
    U'🬳',   // 0b011011 = 27
    U'🬍',   // 0b011100 = 28
    U'🬫',   // 0b011101 = 29
    U'🬜',   // 0b011110 = 30
    U'🬻',   // 0b011111 = 31
    U'🬀',   // 0b100000 = 32
    U'🬟',   // 0b100001 = 33
    U'🬐',   // 0b100010 = 34
    U'🬮',   // 0b100011 = 35
    U'🬈',   // 0b100100 = 36
    U'🬧',   // 0b100101 = 37
    U'🬗',   // 0b100110 = 38
    U'🬶',   // 0b100111 = 39
    U'🬄',   // 0b101000 = 40
    U'🬣',   // 0b101001 = 41
    U'▌',    // 0b101010 = 42
    U'🬲',   // 0b101011 = 43
    U'🬌',   // 0b101100 = 44
    U'🬪',   // 0b101101 = 45
    U'🬛',   // 0b101110 = 46
    U'🬺',   // 0b101111 = 47
    U'🬂',   // 0b110000 = 48
    U'🬡',   // 0b110001 = 49
    U'🬒',   // 0b110010 = 50
    U'🬰',   // 0b110011 = 51
    U'🬊',   // 0b110100 = 52
    U'🬨',   // 0b110101 = 53
    U'🬙',   // 0b110110 = 54
    U'🬸',   // 0b110111 = 55
    U'🬆',   // 0b111000 = 56
    U'🬥',   // 0b111001 = 57
    U'🬕',   // 0b111010 = 58
    U'🬴',   // 0b111011 = 59
    U'🬎',   // 0b111100 = 60
    U'🬬',   // 0b111101 = 61
    U'🬝',   // 0b111110 = 62
    U'█',    // 0b111111 = 63
};
#endif


// Retrieve the FHD character for a given 6-bit code
constexpr inline wchar_t get_fhd_symbol(unsigned char code) noexcept {return fhd_lookup[code];}


// Braille codes: the characters of every 8 bit code, from 0 to 255
constexpr wchar_t braille_lookup[256] = {
    L' ',    // 0b00000000 (0)
    L'⢀',   // 0b00000001 (1)
    L'⡀',   // 0b00000010 (2)
    L'⣀',   // 0b00000011 (3)
    L'⠠',   // 0b00000100 (4)
    L'⢠',   // 0b00000101 (5)
    L'⡠',   // 0b00000110 (6)
    L'⣠',   // 0b00000111 (7)
    L'⠄',   // 0b00001000 (8)
    L'⢄',   // 0b00001001 (9)
    L'⡄',   // 0b00001010 (10)
    L'⣄',   // 0b00001011 (11)
    L'⠤',   // 0b00001100 (12)
    L'⢤',   // 0b00001101 (13)
    L'⡤',   // 0b00001110 (14)
    L'⣤',   // 0b00001111 (15)
    L'⠐',   // 0b00010000 (16)
    L'⢐',   // 0b00010001 (17)
    L'⡐',   // 0b00010010 (18)
    L'⣐',   // 0b00010011 (19)
    L'⠰',   // 0b00010100 (20)
    L'⢰',   // 0b00010101 (21)
    L'⡰',   // 0b00010110 (22)
    L'⣰',   // 0b00010111 (23)
    L'⠔',   // 0b00011000 (24)
    L'⢔',   // 0b00011001 (25)
    L'⡔',   // 0b00011010 (26)
    L'⣔',   // 0b00011011 (27)
    L'⠴',   // 0b00011100 (28)
    L'⢴',   // 0b00011101 (29)
    L'⡴',   // 0b00011110 (30)
    L'⣴',   // 0b00011111 (31)
    L'⠂',   // 0b00100000 (32)
    L'⢂',   // 0b00100001 (33)
    L'⡂',   // 0b00100010 (34)
    L'⣂',   // 0b00100011 (35)
    L'⠢',   // 0b00100100 (36)
    L'⢢',   // 0b00100101 (37)
    L'⡢',   // 0b00100110 (38)
    L'⣢',   // 0b00100111 (39)
    L'⠆',   // 0b00101000 (40)
    L'⢆',   // 0b00101001 (41)
    L'⡆',   // 0b00101010 (42)
    L'⣆',   // 0b00101011 (43)
    L'⠦',   // 0b00101100 (44)
    L'⢦',   // 0b00101101 (45)
    L'⡦',   // 0b00101110 (46)
    L'⣦',   // 0b00101111 (47)
    L'⠒',   // 0b00110000 (48)
    L'⢒',   // 0b00110001 (49)
    L'⡒',   // 0b00110010 (50)
    L'⣒',   // 0b00110011 (51)
    L'⠲',   // 0b00110100 (52)
    L'⢲',   // 0b00110101 (53)
    L'⡲',   // 0b00110110 (54)
    L'⣲',   // 0b00110111 (55)
    L'⠖',   // 0b00111000 (56)
    L'⢖',   // 0b00111001 (57)
    L'⡖',   // 0b00111010 (58)
    L'⣖',   // 0b00111011 (59)
    L'⠶',   // 0b00111100 (60)
    L'⢶',   // 0b00111101 (61)
    L'⡶',   // 0b00111110 (62)
    L'⣶',   // 0b00111111 (63)
    L'⠈',   // 0b01000000 (64)
    L'⢈',   // 0b01000001 (65)
    L'⡈',   // 0b01000010 (66)
    L'⣈',   // 0b01000011 (67)
    L'⠨',   // 0b01000100 (68)
    L'⢨',   // 0b01000101 (69)
    L'⡨',   // 0b01000110 (70)
    L'⣨',   // 0b01000111 (71)
    L'⠌',   // 0b01001000 (72)
    L'⢌',   // 0b01001001 (73)
    L'⡌',   // 0b01001010 (74)
    L'⣌',   // 0b01001011 (75)
    L'⠬',   // 0b01001100 (76)
    L'⢬',   // 0b01001101 (77)
    L'⡬',   // 0b01001110 (78)
    L'⣬',   // 0b01001111 (79)
    L'⠘',   // 0b01010000 (80)
    L'⢘',   // 0b01010001 (81)
    L'⡘',   // 0b01010010 (82)
    L'⣘',   // 0b01010011 (83)
    L'⠸',   // 0b01010100 (84)
    L'⢸',   // 0b01010101 (85)
    L'⡸',   // 0b01010110 (86)
    L'⣸',   // 0b01010111 (87)
    L'⠜',   // 0b01011000 (88)
    L'⢜',   // 0b01011001 (89)
    L'⡜',   // 0b01011010 (90)
    L'⣜',   // 0b01011011 (91)
    L'⠼',   // 0b01011100 (92)
    L'⢼',   // 0b01011101 (93)
    L'⡼',   // 0b01011110 (94)
    L'⣼',   // 0b01011111 (95)
    L'⠊',   // 0b01100000 (96)
    L'⢊',   // 0b01100001 (97)
    L'⡊',   // 0b01100010 (98)
    L'⣊',   // 0b01100011 (99)
    L'⠪',   // 0b01100100 (100)
    L'⢪',   // 0b01100101 (101)
    L'⡪',   // 0b01100110 (102)
    L'⣪',   // 0b01100111 (103)
    L'⠎',   // 0b01101000 (104)
    L'⢎',   // 0b01101001 (105)
    L'⡎',   // 0b01101010 (106)
    L'⣎',   // 0b01101011 (107)
    L'⠮',   // 0b01101100 (108)
    L'⢮',   // 0b01101101 (109)
    L'⡮',   // 0b01101110 (110)
    L'⣮',   // 0b01101111 (111)
    L'⠚',   // 0b01110000 (112)
    L'⢚',   // 0b01110001 (113)
    L'⡚',   // 0b01110010 (114)
    L'⣚',   // 0b01110011 (115)
    L'⠺',   // 0b01110100 (116)
    L'⢺',   // 0b01110101 (117)
    L'⡺',   // 0b01110110 (118)
    L'⣺',   // 0b01110111 (119)
    L'⠞',   // 0b01111000 (120)
    L'⢞',   // 0b01111001 (121)
    L'⡞',   // 0b01111010 (122)
    L'⣞',   // 0b01111011 (123)
    L'⠾',   // 0b01111100 (124)
    L'⢾',   // 0b01111101 (125)
    L'⡾',   // 0b01111110 (126)
    L'⣾',   // 0b01111111 (127)
    L'⠁',   // 0b10000000 (128)
    L'⢁',   // 0b10000001 (129)
    L'⡁',   // 0b10000010 (130)
    L'⣁',   // 0b10000011 (131)
    L'⠡',   // 0b10000100 (132)
    L'⢡',   // 0b10000101 (133)
    L'⡡',   // 0b10000110 (134)
    L'⣡',   // 0b10000111 (135)
    L'⠅',   // 0b10001000 (136)
    L'⢅',   // 0b10001001 (137)
    L'⡅',   // 0b10001010 (138)
    L'⣅',   // 0b10001011 (139)
    L'⠥',   // 0b10001100 (140)
    L'⢥',   // 0b10001101 (141)
    L'⡥',   // 0b10001110 (142)
    L'⣥',   // 0b10001111 (143)
    L'⠑',   // 0b10010000 (144)
    L'⢑',   // 0b10010001 (145)
    L'⡑',   // 0b10010010 (146)
    L'⣑',   // 0b10010011 (147)
    L'⠱',   // 0b10010100 (148)
    L'⢱',   // 0b10010101 (149)
    L'⡱',   // 0b10010110 (150)
    L'⣱',   // 0b10010111 (151)
    L'⠕',   // 0b10011000 (152)
    L'⢕',   // 0b10011001 (153)
    L'⡕',   // 0b10011010 (154)
    L'⣕',   // 0b10011011 (155)
    L'⠵',   // 0b10011100 (156)
    L'⢵',   // 0b10011101 (157)
    L'⡵',   // 0b10011110 (158)
    L'⣵',   // 0b10011111 (159)
    L'⠃',   // 0b10100000 (160)
    L'⢃',   // 0b10100001 (161)
    L'⡃',   // 0b10100010 (162)
    L'⣃',   // 0b10100011 (163)
    L'⠣',   // 0b10100100 (164)
    L'⢣',   // 0b10100101 (165)
    L'⡣',   // 0b10100110 (166)
    L'⣣',   // 0b10100111 (167)
    L'⠇',   // 0b10101000 (168)
    L'⢇',   // 0b10101001 (169)
    L'⡇',   // 0b10101010 (170)
    L'⣇',   // 0b10101011 (171)
    L'⠧',   // 0b10101100 (172)
    L'⢧',   // 0b10101101 (173)
    L'⡧',   // 0b10101110 (174)
    L'⣧',   // 0b10101111 (175)
    L'⠓',   // 0b10110000 (176)
    L'⢓',   // 0b10110001 (177)
    L'⡓',   // 0b10110010 (178)
    L'⣓',   // 0b10110011 (179)
    L'⠳',   // 0b10110100 (180)
    L'⢳',   // 0b10110101 (181)
    L'⡳',   // 0b10110110 (182)
    L'⣳',   // 0b10110111 (183)
    L'⠗',   // 0b10111000 (184)
    L'⢗',   // 0b10111001 (185)
    L'⡗',   // 0b10111010 (186)
    L'⣗',   // 0b10111011 (187)
    L'⠷',   // 0b10111100 (188)
    L'⢷',   // 0b10111101 (189)
    L'⡷',   // 0b10111110 (190)
    L'⣷',   // 0b10111111 (191)
    L'⠉',   // 0b11000000 (192)
    L'⢉',   // 0b11000001 (193)
    L'⡉',   // 0b11000010 (194)
    L'⣉',   // 0b11000011 (195)
    L'⠩',   // 0b11000100 (196)
    L'⢩',   // 0b11000101 (197)
    L'⡩',   // 0b11000110 (198)
    L'⣩',   // 0b11000111 (199)
    L'⠍',   // 0b11001000 (200)
    L'⢍',   // 0b11001001 (201)
    L'⡍',   // 0b11001010 (202)
    L'⣍',   // 0b11001011 (203)
    L'⠭',   // 0b11001100 (204)
    L'⢭',   // 0b11001101 (205)
    L'⡭',   // 0b11001110 (206)
    L'⣭',   // 0b11001111 (207)
    L'⠙',   // 0b11010000 (208)
    L'⢙',   // 0b11010001 (209)
    L'⡙',   // 0b11010010 (210)
    L'⣙',   // 0b11010011 (211)
    L'⠹',   // 0b11010100 (212)
    L'⢹',   // 0b11010101 (213)
    L'⡹',   // 0b11010110 (214)
    L'⣹',   // 0b11010111 (215)
    L'⠝',   // 0b11011000 (216)
    L'⢝',   // 0b11011001 (217)
    L'⡝',   // 0b11011010 (218)
    L'⣝',   // 0b11011011 (219)
    L'⠽',   // 0b11011100 (220)
    L'⢽',   // 0b11011101 (221)
    L'⡽',   // 0b11011110 (222)
    L'⣽',   // 0b11011111 (223)
    L'⠋',   // 0b11100000 (224)
    L'⢋',   // 0b11100001 (225)
    L'⡋',   // 0b11100010 (226)
    L'⣋',   // 0b11100011 (227)
    L'⠫',   // 0b11100100 (228)
    L'⢫',   // 0b11100101 (229)
    L'⡫',   // 0b11100110 (230)
    L'⣫',   // 0b11100111 (231)
    L'⠏',   // 0b11101000 (232)
    L'⢏',   // 0b11101001 (233)
    L'⡏',   // 0b11101010 (234)
    L'⣏',   // 0b11101011 (235)
    L'⠯',   // 0b11101100 (236)
    L'⢯',   // 0b11101101 (237)
    L'⡯',   // 0b11101110 (238)
    L'⣯',   // 0b11101111 (239)
    L'⠛',   // 0b11110000 (240)
    L'⢛',   // 0b11110001 (241)
    L'⡛',   // 0b11110010 (242)
    L'⣛',   // 0b11110011 (243)
    L'⠻',   // 0b11110100 (244)
    L'⢻',   // 0b11110101 (245)
    L'⡻',   // 0b11110110 (246)
    L'⣻',   // 0b11110111 (247)
    L'⠟',   // 0b11111000 (248)
    L'⢟',   // 0b11111001 (249)
    L'⡟',   // 0b11111010 (250)
    L'⣟',   // 0b11111011 (251)
    L'⠿',   // 0b11111100 (252)
    L'⢿',   // 0b11111101 (253)
    L'⡿',   // 0b11111110 (254)
    L'⣿'    // 0b11111111 (255)
};

// Retrieve the braille character for a given 8-bit code
constexpr inline wchar_t get_braille_symbol(unsigned char code) noexcept {return braille_lookup[code];}


// Box-drawing line lookups: one 16-entry table per style. 4-bit arm code (N/E/S/W = bits 3/2/1/0) indexes each table. Style is selected externally by the caller (e.g. BoxCharacter::style_bits).
constexpr uint8_t box_n = 0b1000;   // bit 3
constexpr uint8_t box_e = 0b0100;   // bit 2
constexpr uint8_t box_s = 0b0010;   // bit 1
constexpr uint8_t box_w = 0b0001;   // bit 0

// Style indices (used to pick which lookup table; not encoded in the bit pattern)
constexpr uint8_t box_normal  = 0;
constexpr uint8_t box_double  = 1;
constexpr uint8_t box_heavy   = 2;
constexpr uint8_t box_dotted  = 3;
constexpr uint8_t box_rounded = 4;

// Normal style: edges, corners, T-junctions, cross + 4 half-arm stubs
constexpr wchar_t box_normal_lookup[16] = {
    0,        // 0b0000  0
    L'╴',     // 0b0001  1
    L'╷',     // 0b0010  2
    L'┐',     // 0b0011  3
    L'╶',     // 0b0100  4
    L'─',     // 0b0101  5
    L'┌',     // 0b0110  6
    L'┬',     // 0b0111  7
    L'╵',     // 0b1000  8
    L'┘',     // 0b1001  9
    L'│',     // 0b1010 10
    L'┤',     // 0b1011 11
    L'└',     // 0b1100 12
    L'┴',     // 0b1101 13
    L'├',     // 0b1110 14
    L'┼',     // 0b1111 15
};

// Double style: edges, corners, T-junctions, cross. No half-arm stubs in Unicode.
constexpr wchar_t box_double_lookup[16] = {
    0,        // 0b0000  0
    0,        // 0b0001  1
    0,        // 0b0010  2
    L'╗',     // 0b0011  3
    0,        // 0b0100  4
    L'═',     // 0b0101  5
    L'╔',     // 0b0110  6
    L'╦',     // 0b0111  7
    0,        // 0b1000  8
    L'╝',     // 0b1001  9
    L'║',     // 0b1010 10
    L'╣',     // 0b1011 11
    L'╚',     // 0b1100 12
    L'╩',     // 0b1101 13
    L'╠',     // 0b1110 14
    L'╬',     // 0b1111 15
};

// Heavy (thick) style: edges, corners, T-junctions, cross + 4 half-arm stubs.
constexpr wchar_t box_heavy_lookup[16] = {
    0,        // 0b0000  0
    L'╸',     // 0b0001  1
    L'╻',     // 0b0010  2
    L'┓',     // 0b0011  3
    L'╺',     // 0b0100  4
    L'━',     // 0b0101  5
    L'┏',     // 0b0110  6
    L'┳',     // 0b0111  7
    L'╹',     // 0b1000  8
    L'┛',     // 0b1001  9
    L'┃',     // 0b1010 10
    L'┫',     // 0b1011 11
    L'┗',     // 0b1100 12
    L'┻',     // 0b1101 13
    L'┣',     // 0b1110 14
    L'╋',     // 0b1111 15
};

// Dotted style: only the two plain edges exist in Unicode (no dotted corners or junctions).
constexpr wchar_t box_dotted_lookup[16] = {
    0,        // 0b0000  0
    0,        // 0b0001  1
    0,        // 0b0010  2
    0,        // 0b0011  3
    0,        // 0b0100  4
    L'┈',     // 0b0101  5
    0,        // 0b0110  6
    0,        // 0b0111  7
    0,        // 0b1000  8
    0,        // 0b1001  9
    L'┊',     // 0b1010 10
    0,        // 0b1011 11
    0,        // 0b1100 12
    0,        // 0b1101 13
    0,        // 0b1110 14
    0,        // 0b1111 15
};

// Rounded style: only the four corners exist in Unicode (no rounded edges, T-junctions or cross).
constexpr wchar_t box_rounded_lookup[16] = {
    0,        // 0b0000  0
    0,        // 0b0001  1
    0,        // 0b0010  2
    L'╮',     // 0b0011  3
    0,        // 0b0100  4
    0,        // 0b0101  5
    L'╭',     // 0b0110  6
    0,        // 0b0111  7
    0,        // 0b1000  8
    L'╯',     // 0b1001  9
    0,        // 0b1010 10
    0,        // 0b1011 11
    L'╰',     // 0b1100 12
    0,        // 0b1101 13
    0,        // 0b1110 14
    0,        // 0b1111 15
};

// Pack / unpack helpers for BoxCharacter's single-byte line code.
// Layout:
//   bits 0..3 (low 4 bits)  = arms (N=0b1000, E=0b0100, S=0b0010, W=0b0001)
//   bits 4..6 (next 3 bits) = style index (0..4)
//   bit  7                  = unused
inline constexpr uint8_t get_box_code (uint8_t arms, uint8_t style) noexcept { return (arms & 0b00001111) | ((style & 0b00000111) << 4); }
inline constexpr uint8_t get_box_arms (uint8_t code) noexcept { return  code       & 0b00001111; }
inline constexpr uint8_t get_box_style(uint8_t code) noexcept { return (code >> 4) & 0b00000111; }

// Retrieves the glyph for a packed line code; arm combinations missing from a style's table fall back to the normal style glyph, so no cell ever renders empty.
inline wchar_t get_box_glyph(uint8_t code) noexcept {
    const uint8_t arms  = get_box_arms (code);
    const uint8_t style = get_box_style(code);
    wchar_t glyph = 0;
    if      (style == box_double)  glyph = box_double_lookup [arms];
    else if (style == box_heavy)   glyph = box_heavy_lookup  [arms];
    else if (style == box_dotted)  glyph = box_dotted_lookup [arms];
    else if (style == box_rounded) glyph = box_rounded_lookup[arms];
    else                           glyph = box_normal_lookup [arms];
    return glyph ? glyph : box_normal_lookup[arms];}
