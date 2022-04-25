from plotext._utility.data import no_duplicates, join, round, mean, memorize

# A user could specify three types of colors 
  # an integer for 256 color codes
  # a tuple    for RGB color codes
  # a string   for 16 color codes or styles

# Along side the user needs to specify whatever it is for background / fullground / style
# which plotext calls 'character' = 0 / 1 / 2

##############################################
#########    String Color Codes    ###########
##############################################

no_color = "default" # the standard name of the color/ style that does nothing, but any other string which is not a style or color would do

color_codes = {"black": 0,   "white": 15,
               "gray": 8,    "gray+": 7,
               "red": 1,     "red+": 9,
               "green": 2,   "green+": 10,
               "orange": 3,  "orange+": 11,
               "blue": 4,    "blue+": 12,
               "magenta": 5, "magenta+": 13,
               "cyan": 6,    "cyan+": 14} # fullground colors and their ascii code

colors = list(color_codes.keys()) + [no_color]

def get_color_code(color): # the color number code from color string 
    color = color.strip()
    return color_codes[color]

def get_color_name(code): # the color string from color number code
    codes = list(color_codes.values())
    return colors[codes.index(code)] if code in codes else no_color

def is_string_color(color):
    return isinstance(color, str) and color.strip() in colors

color_sequence = ["blue+", "green+", "red+", "cyan+", "magenta+", "yellow", "gray", "blue", "green", "red", "cyan", "magenta", "gold", "black"] # standard color sequence for multiple data plots
color_sequence += [el for el in colors if el not in color_sequence] 

##############################################
############     Style Codes    ##############
##############################################

style_codes = {"bold": 1, "dim": 2, "italic": 3, "underline": 4, "double-underline": 21, "strike": 9, "inverted": 7, "flash": 5} # text styles and their ascii code

styles = list(style_codes.keys()) + [no_color]

def get_style_code(style): # from single style to style number code
    style = style.strip()
    return style_codes[style]

def get_style_codes(style): # from many styles (separated by space) to as many number codes
    style = style.strip().split()
    codes = [get_style_code(el) for el in style if el in styles]
    codes = no_duplicates(codes)
    return codes
    
def get_style_name(code): # from style number code to style name
    codes = list(style_codes.values())
    return styles[codes.index(code)] if code in codes else no_color

def clean_styles(style): # it returns a well written sequence of styles (separated by spaces) from a possible confused one
    codes = get_style_codes(style)
    return ' '.join([get_style_name(el) for el in codes])

def is_style(style):
    style = style.strip().split() if isinstance(style, str) else ['']
    return any([el in styles for el in style])

##############################################
#########    Other Color Types    ############
##############################################

def is_integer_color(color): 
    return isinstance(color, int) and 0 <= color <= 255

def is_rgb_color(color):
    is_rgb = isinstance(color, list) or isinstance(color, tuple)
    is_rgb = is_rgb and len(color) == 3
    is_rgb = is_rgb and all([is_integer_color(el) for el in color])
    return is_rgb

def is_color(color):
    return is_string_color(color) or is_integer_color(color) or is_rgb_color(color)

##############################################
###########    Color Themes    ###############
##############################################

themes = {}
ls = len(color_sequence)

themes["default"] = ["white", "white", "black", no_color, color_sequence]

sequence = [no_color] * ls
themes['clear'] = [no_color, no_color, no_color, no_color, sequence]

themes['pro'] = [no_color, no_color, no_color, no_color, color_sequence]

sequence = [(0, 255, 65), (0, 143, 17), (0, 59, 0)]
sequence += [el for el in color_sequence if el not in sequence]
themes['matrix'] = [(13,2,8), (13,2,8), sequence[0], 'bold', sequence]

blue = (0, 64, 239); red = (242,80,34); yellow = (255,185,0); green = (127,186,0)
sequence = [blue, red, green, yellow]
sequence += [el for el in color_sequence if el not in sequence]
themes['windows'] = ['gray+', 'gray+', 'black', no_color, sequence]

pink = (255, 200, 200)
sequence = [(86, 186, 236), 'green+']
sequence += [el for el in color_sequence if el not in sequence]
themes['girly'] = [pink, pink, 'blue+', no_color, sequence]

sequence = ['blue', 22, 54]
sequence += [el for el in color_sequence if el not in sequence]
themes['dark'] = ['black', 'black', 'orange', no_color, sequence]

sequence = [21, 41, 196]
sequence += [el for el in color_sequence if el not in sequence]
themes['retro'] = [250, 234, 186, no_color, sequence]
            
sequence = [111, 174, 186]
sequence += [el for el in color_sequence if el not in sequence]
themes['elegant'] = [66, 4, 216, "bold", sequence]

sequence = [27, 88, 11]
sequence += [el for el in color_sequence if el not in sequence]
themes['grandpa'] = [66, 94, 155, "bold", sequence]

sequence = [142, 124, 57]
sequence += [el for el in color_sequence if el not in sequence]
themes['salad'] = [95, 22, 221, "bold", sequence]

sequence = [27, 34, 52]
sequence += [el for el in color_sequence if el not in sequence]
themes['serious'] = [95, 52, 190, "bold", sequence]

sequence = [26, 85, 124]
sequence += [el for el in color_sequence if el not in sequence]
themes['scream'] = [130,88,227, "bold", sequence]

sequence = [6, 125, 190]
sequence += [el for el in color_sequence if el not in sequence]
themes['dreamland'] = [180, 2, 221, "bold", sequence]

sequence = [39, 202, 228]
sequence += [el for el in color_sequence if el not in sequence]
themes['sand'] = [180, 172, 192, "bold", sequence]

sequence = [39, 202, 228]
sequence += [el for el in color_sequence if el not in sequence]
themes['mature'] = [180, 24, 184, "bold", sequence]

##############################################
#########    Colorizing Strings    ###########
##############################################

def colorize(string, fullground = None, style = None, background = None, show = False): # it paints a text with given fullground and background color
    string = apply_ansi(string, background, 0)
    string = apply_ansi(string, fullground, 1)
    string = apply_ansi(string, style, 2)
    if show:
        print(string)
    return string

def uncolorize(string): # remove color codes from colored string
    colored = lambda: ansi_begin in string
    while colored():
        b = string.index(ansi_begin)
        e = string[b : ].index('m') + b + 1
        string = string.replace(string[b : e], '')
    return string

def apply_ansi(string, color, character):
    begin, end = ansi(color, character)
    return begin + string + end

###############################################
##############    Utilities    ################
###############################################

#ansi_begin = '\033['
ansi_begin = '\x1b['
ansi_end = ansi_begin + '0m'

def all_ansi(background, fullground, style):
    color = [background, fullground, style]
    return ''.join([ansi(color[i], i)[0] for i in range(3)])

def turn_gray(matrix): # it takes a standard matrix and turns it into an grayscale one
    M, m = max(join(matrix), default = 0), min(join(matrix), default = 0)
    to_gray = lambda el: tuple([int(255 * (el - m) / (M - m))] * 3) if M != m else (127, 127, 127) 
    return [[to_gray(el) for el in l] for l in matrix]

#@memorize
def ansi(color, character):
    if color == no_color:
        return ['', '']
    col, fg, tp = '', '', ''
    if character == 2 and is_style(color):
        col = get_style_codes(color)
        col = ';'.join([str(el) for el in col])
    elif character != 2:
        fg = '38;' if character == 1 else '48;'
        tp = '5;'
        if is_string_color(color):
            col = str(get_color_code(color))
        elif is_integer_color(color):
            col = str(color)
        elif is_rgb_color(color):
            col = ';'.join([str(el) for el in color])
            tp = '2;'
    is_color = col != ''
    begin = ansi_begin + fg + tp + col + 'm' if is_color else ''
    end = ansi_end if is_color else ''
    return [begin, end]

###############################################
#######    Color Types Conversion     #########
###############################################
## This section is usefull to produce html colored version of the plot and to translate all color types (types 0 and 1) in rgb (type 2 in plotext) and avoid confusion. the match is almost exact and it depends on the terminal i suppose

def to_rgb(color):
    if is_string_color(color): # from 0 to 1
        color = get_color_code(color)
        #color = type0_to_type1_codes[code]
    if is_integer_color(color): # from 0 or 1 to 2
        return type1_to_type2_codes[color]
    return color

type0_to_type1_codes = {0: 40, 1: 41, 2: 42, 3: 43, 4: 44, 5: 45, 6: 46, 7: 47, 8: 100, 9: 101, 10: 102, 11: 103, 12: 104, 13: 105, 14: 106, 15: 107}

type1_to_type2_codes = {0:(0,0,0), 1:(205,49,49), 2:(13,188,121), 3:(229,229,16), 4:(36, 114, 200), 5:(188,63,188), 6:(17,168,205), 7:(229,229,229), 8:(102,102,102), 9:(241,76,76), 10:(35,209,139), 11:(245,245,67), 12:(59,142,234), 13: (214,112,214), 14:(41,184,219), 15:(229,229,229), 16:(0,0,0), 17:(0,0,95), 18:(0,0,135), 19:(0,0,175), 20:(0,0,215), 21:(0,0,255), 22:(0,95,0), 23:(0,95,95), 24:(0,95,135), 25:(0,95,175), 26:(0,95,215), 27:(0,95,255), 28:(0,135,0), 29:(0,135,95), 30:(0,135,135), 31:(0,135,175), 32:(0,135,215), 33:(0,135,255), 34:(0,175,0), 35:(0,175,95), 36:(0,175,135), 37:(0,175,175), 38:(0,175,215), 39:(0,175,255), 40:(0,215,0), 41:(0,215,95), 42:(0,215,135), 43:(0,215,175), 44:(0,215,215), 45:(0,215,255), 46:(0,255,0), 47:(0,255,95), 48:(0,255,135), 49:(0,255,175), 50:(0,255,215), 51:(0,255,255), 52:(95,0,0), 53:(95,0,95), 54:(95,0,135), 55:(95,0,175), 56:(95,0,215), 57:(95,0,255), 58:(95,95,0), 59:(95,95,95), 60:(95,95,135), 61:(95,95,175), 62:(95,95,215), 63:(95,95,255), 64:(95,135,0), 65:(95,135,95), 66:(95,135,135), 67:(95,135,175), 68:(95,135,215), 69:(95,135,255), 70:(95,175,0), 71:(95,175,95), 72:(95,175,135), 73:(95,175,175), 74:(95,175,215), 75:(95,175,255), 76:(95,215,0), 77:(95,215,95), 78:(95,215,135), 79:(95,215,175), 80:(95,215,215), 81:(95,215,255), 82:(95,255,0), 83:(95,255,95), 84:(95,255,135), 85:(95,255,175), 86:(95,255,215), 87:(95,255,255), 88:(135,0,0), 89:(135,0,95), 90:(135,0,135), 91:(135,0,175), 92:(135,0,215), 93:(135,0,255), 94:(135,95,0), 95:(135,95,95), 96:(135,95,135), 97:(135,95,175), 98:(135,95,215), 99:(135,95,255), 100:(135,135,0), 101:(135,135,95), 102:(135,135,135), 103:(135,135,175), 104:(135,135,215), 105:(135,135,255), 106:(135,175,0), 107:(135,175,95), 108:(135,175,135), 109:(135,175,175), 110:(135,175,215), 111:(135,175,255), 112:(135,215,0), 113:(135,215,95), 114:(135,215,135), 115:(135,215,175), 116:(135,215,215), 117:(135,215,255), 118:(135,255,0), 119:(135,255,95), 120:(135,255,135), 121:(135,255,175), 122:(135,255,215), 123:(135,255,255), 124:(175,0,0), 125:(175,0,95), 126:(175,0,135), 127:(175,0,175), 128:(175,0,215), 129:(175,0,255), 130:(175,95,0), 131:(175,95,95), 132:(175,95,135), 133:(175,95,175), 134:(175,95,215), 135:(175,95,255), 136:(175,135,0), 137:(175,135,95), 138:(175,135,135), 139:(175,135,175), 140:(175,135,215), 141:(175,135,255), 142:(175,175,0), 143:(175,175,95), 144:(175,175,135), 145:(175,175,175), 146:(175,175,215), 147:(175,175,255), 148:(175,215,0), 149:(175,215,95), 150:(175,215,135), 151:(175,215,175), 152:(175,215,215), 153:(175,215,255), 154:(175,255,0), 155:(175,255,95), 156:(175,255,135), 157:(175,255,175), 158:(175,255,215), 159:(175,255,255), 160:(215,0,0), 161:(215,0,95), 162:(215,0,135), 163:(215,0,175), 164:(215,0,215), 165:(215,0,255), 166:(215,95,0), 167:(215,95,95), 168:(215,95,135), 169:(215,95,175), 170:(215,95,215), 171:(215,95,255), 172:(215,135,0), 173:(215,135,95), 174:(215,135,135), 175:(215,135,175), 176:(215,135,215), 177:(215,135,255), 178:(215,175,0), 179:(215,175,95), 180:(215,175,135), 181:(215,175,175), 182:(215,175,215), 183:(215,175,255), 184:(215,215,0), 185:(215,215,95), 186:(215,215,135), 187:(215,215,175), 188:(215,215,215), 189:(215,215,255), 190:(215,255,0), 191:(215,255,95), 192:(215,255,135), 193:(215,255,175), 194:(215,255,215), 195:(215,255,255), 196:(255,0,0), 197:(255,0,95), 198:(255,0,135), 199:(255,0,175), 200:(255,0,215), 201:(255,0,255), 202:(255,95,0), 203:(255,95,95), 204:(255,95,135), 205:(255,95,175), 206:(255,95,215), 207:(255,95,255), 208:(255,135,0), 209:(255,135,95), 210:(255,135,135), 211:(255,135,175), 212:(255,135,215), 213:(255,135,255), 214:(255,175,0), 215:(255,175,95), 216:(255,175,135), 217:(255,175,175), 218:(255,175,215), 219:(255,175,255), 220:(255,215,0), 221:(255,215,95), 222:(255,215,135), 223:(255,215,175), 224:(255,215,215), 225:(255,215,255), 226:(255,255,0), 227:(255,255,95), 228:(255,255,135), 229:(255,255,175), 230:(255,255,215), 231:(255,255,255), 232:(8,8,8), 233:(18,18,18), 234:(28,28,28), 235:(38,38,38), 236:(48,48,48), 237:(58,58,58), 238:(68,68,68), 239:(78,78,78), 240:(88,88,88), 241:(98,98,98), 242:(108,108,108), 243:(118,118,118), 244:(128,128,128), 245:(138,138,138), 246:(148,148,148), 247:(158,158,158), 248:(168,168,168), 249:(178,178,178), 250:(188,188,188), 251:(198,198,198), 252:(208,208,208), 253:(218,218,218), 254:(228,228,228), 255:(238,238,238)}
## source for conversion to rgb: https://jonasjacek.github.io/colors/ 

