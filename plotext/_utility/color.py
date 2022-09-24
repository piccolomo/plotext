from plotext._utility.data import mean
import sys

##############################################
###########    Standard Colors    ############
##############################################

no_color_name = "default" # the name of the color that does... nothing

fullground_codes = {no_color_name: 0, "black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35, "cyan": 36, "white": 37, "bright-black": 90, "bright-red": 91, "bright-green": 92, "bright-yellow": 93, "bright-blue": 94, "bright-magenta": 95, "bright-cyan": 96, "bright-white": 97} # fullground colors and their ascii code

style_codes = {"bold": 1, "dim": 2, "italic": 3, "underline": 4, "double-underline": 21, "strike": 9, "inverted": 7, "flash": 5} # text styles and their ascii code

all_codes = {**fullground_codes, **style_codes} # used for color type

background_codes = {no_color_name: 0, "black": 40, "red": 41, "green": 42, "yellow": 43, "blue": 44, "magenta": 45, "cyan": 46, "white": 47, "bright-black": 100, "bright-red": 101, "bright-green": 102, "bright-yellow": 103, "bright-blue": 104, "bright-magenta": 105, "bright-cyan": 106, "bright-white": 107} # background colors and their ascii code

fullground_colors = list(fullground_codes.keys())
background_colors = list(background_codes.keys())
styles = list(style_codes.keys())

color_sequence = ["bright-blue", "bright-green", "bright-red", "bright-cyan", "bright-magenta", "bright-yellow", "bright-black", "blue", "green", "red", "cyan", "magenta", "yellow", "black"] # standard color sequence for multiple data plots

color_sequence += [el for el in fullground_colors if el not in color_sequence]  # it continues with the remaining fullground colors

def color_name(code, fullground = 1): # it returns the color name from code used
    codes = all_codes if fullground else background_codes
    return list(codes.keys())[list(codes.values()).index(code)]

##############################################
########    Color Representation    ##########
##############################################

# internally to plotext a tuple represents a color this way:
#   first digit for color type regular/ 256 colors / rgb / not recognised: 0 / 1 / 2 / 3
#   second digit for fullground / background: 1 / 0
#   integer color codes following (including styles for regular fullground representation)

def color_type(color = None): # color type: 0 = standard, 1 = 256 colors, 2 = rgb tuple
    t = 3 # not recognised
    if type(color) == str: # default
        color = color.split(' ')
        t = 0 if any([el in all_codes for el in color]) else 3
    elif type(color) == int and 0 <= color <= 255:
        t = 1
    elif (type(color) == tuple or type(color) == list) and all([0 <= el <= 255 for el in color]):
        t = 2
    return t

def color_code(color = None, fullground = True): # given a color, an integer or a tuple, it returns the internal to plotext color code and bool which is True if the color is unrecognised
    color = "" if color is None else color
    t = color_type(color) # color type
    code = [t] + [int(fullground)]
    if t == 0:
        color = color.split(' ')
        codes = all_codes if fullground == 1 else background_codes
        code += [codes[el] for el in color if el in codes]
    elif t == 1: 
        code += [color] 
    elif t == 2:
        code += list(color)
    return tuple(code)

##############################################
########    Apply Color to Text     ##########
##############################################

def begin_escape(color_code): # it takes the internal color code and returns the correspondent ascii code
    if color_code[0] == 3 or (color_code[0] == 0 and color_code[2] == 0): 
        return ''
    escape = '\x1b['
    escape = '\033['
    if color_code[0] != 0:
        escape += '38;' if color_code[1] == 1 else '48;'
    type_code = ['', '5;', '2;']
    escape += type_code[color_code[0]]
    escape += ';'.join(map(str, color_code[2:])) + 'm'
    return escape

def end_escape(color_code = None): # the closing ascii sequence, dependent on the color code as for no_color_name the end sequence is ''
    return '' if color_code[0] == 3 or (color_code[0] == 0 and color_code[2] == 0) else '\033[0m' #'\x1b[0m'
    
def colorize(string, fullground = None, background = None, show = False): # it paints a text with given fullground and background color
    string = string if fullground is None else begin_escape(color_code(fullground, 1)) + string + end_escape(color_code(fullground, 1))
    string = string if background is None else begin_escape(color_code(background, 0)) + string + end_escape(color_code(background, -1))
    if show:
        print(string)
    else:
        return string

def uncolorize(string): # remove color codes from colored string
    asci = '\x1b['
    asci = '\033['
    colored = lambda: asci in string
    while colored():
        b = string.index(asci)
        e = string[b:].index('m') + b + 1
        string = string.replace(string[b:e], '')
    return string

##############################################
#############    Sum Colors     ##############
##############################################

def sum_colors(color1, color2): # it sums colors, when they are rgb
    if color1[1] != color2[1]: # different fullground colors
        print("fatal error: the universe will collapse soon. good luck ...")
    else:
        fg = color1[1]
    if color1[0] == 2 and color2[0] == 2: # if rgb
        color1, color2 = color1[2:], color2[2:]
        color = color2 if color1 == color2 else [round(mean(color1[i], color2[i], 2)) for i in range(3)]
        color = (2, fg) + tuple(color)
    else:
        color = color2
    return color

def to_gray_rgb(matrix): # it takes a standard matrix and turns it into an grayscale rgb one
    M, m = max([max(el) for el in matrix]), min([min(el) for el in matrix])
    gray_rgb = lambda el: tuple([int(255 * (el - m) / (M - m))] * 3)
    matrix = [[gray_rgb(el) for el in l] for l in matrix]
    return matrix

##############################################
#######    Color Type Conversion     #########
##############################################
# This section is usefull to produce html colored version of the plot and to translate all color types (types 0 and 1) in rgb (type 2 in plotext) and avoid confusion. the match is almost exact and it depends on the terminal i suppose

def to_rgb(color_code):
    t, fg = color_code[0:2]
    color = color_code[2] if t<=1 else color_code[2:]
    if t == 0: # from 0 to 1
        color = 30 if color == 0 and fg else 107 if color == 0 else color
        color = type0_to_type1_codes[color]
    if t <= 1: # from 0 or 1 to 2
        return type1_to_type2_codes[color]
    else: #  if color is already rgb or type 2
        return color

type0_to_type1_codes = {30: 0, 31: 1, 32: 2, 33: 3, 34: 4, 35: 5, 36: 6, 37: 7, 90: 8, 91: 9, 92: 10, 93: 11, 94: 12, 95: 13, 96: 14, 97: 15, 40: 0, 41: 1, 42: 2, 43: 3, 44: 4, 45: 5, 46: 6, 47: 7, 100: 8, 101: 9, 102: 10, 103: 11, 104: 12, 105: 13, 106: 14, 107: 15}

type1_to_type2_codes = {0:(0,0,0), 1:(205,49,49), 2:(13,188,121), 3:(229,229,16), 4:(36, 114, 200), 5:(188,63,188), 6:(17,168,205), 7:(229,229,229), 8:(102,102,102), 9:(241,76,76), 10:(35,209,139), 11:(245,245,67), 12:(59,142,234), 13: (214,112,214), 14:(41,184,219), 15:(229,229,229), 16:(0,0,0), 17:(0,0,95), 18:(0,0,135), 19:(0,0,175), 20:(0,0,215), 21:(0,0,255), 22:(0,95,0), 23:(0,95,95), 24:(0,95,135), 25:(0,95,175), 26:(0,95,215), 27:(0,95,255), 28:(0,135,0), 29:(0,135,95), 30:(0,135,135), 31:(0,135,175), 32:(0,135,215), 33:(0,135,255), 34:(0,175,0), 35:(0,175,95), 36:(0,175,135), 37:(0,175,175), 38:(0,175,215), 39:(0,175,255), 40:(0,215,0), 41:(0,215,95), 42:(0,215,135), 43:(0,215,175), 44:(0,215,215), 45:(0,215,255), 46:(0,255,0), 47:(0,255,95), 48:(0,255,135), 49:(0,255,175), 50:(0,255,215), 51:(0,255,255), 52:(95,0,0), 53:(95,0,95), 54:(95,0,135), 55:(95,0,175), 56:(95,0,215), 57:(95,0,255), 58:(95,95,0), 59:(95,95,95), 60:(95,95,135), 61:(95,95,175), 62:(95,95,215), 63:(95,95,255), 64:(95,135,0), 65:(95,135,95), 66:(95,135,135), 67:(95,135,175), 68:(95,135,215), 69:(95,135,255), 70:(95,175,0), 71:(95,175,95), 72:(95,175,135), 73:(95,175,175), 74:(95,175,215), 75:(95,175,255), 76:(95,215,0), 77:(95,215,95), 78:(95,215,135), 79:(95,215,175), 80:(95,215,215), 81:(95,215,255), 82:(95,255,0), 83:(95,255,95), 84:(95,255,135), 85:(95,255,175), 86:(95,255,215), 87:(95,255,255), 88:(135,0,0), 89:(135,0,95), 90:(135,0,135), 91:(135,0,175), 92:(135,0,215), 93:(135,0,255), 94:(135,95,0), 95:(135,95,95), 96:(135,95,135), 97:(135,95,175), 98:(135,95,215), 99:(135,95,255), 100:(135,135,0), 101:(135,135,95), 102:(135,135,135), 103:(135,135,175), 104:(135,135,215), 105:(135,135,255), 106:(135,175,0), 107:(135,175,95), 108:(135,175,135), 109:(135,175,175), 110:(135,175,215), 111:(135,175,255), 112:(135,215,0), 113:(135,215,95), 114:(135,215,135), 115:(135,215,175), 116:(135,215,215), 117:(135,215,255), 118:(135,255,0), 119:(135,255,95), 120:(135,255,135), 121:(135,255,175), 122:(135,255,215), 123:(135,255,255), 124:(175,0,0), 125:(175,0,95), 126:(175,0,135), 127:(175,0,175), 128:(175,0,215), 129:(175,0,255), 130:(175,95,0), 131:(175,95,95), 132:(175,95,135), 133:(175,95,175), 134:(175,95,215), 135:(175,95,255), 136:(175,135,0), 137:(175,135,95), 138:(175,135,135), 139:(175,135,175), 140:(175,135,215), 141:(175,135,255), 142:(175,175,0), 143:(175,175,95), 144:(175,175,135), 145:(175,175,175), 146:(175,175,215), 147:(175,175,255), 148:(175,215,0), 149:(175,215,95), 150:(175,215,135), 151:(175,215,175), 152:(175,215,215), 153:(175,215,255), 154:(175,255,0), 155:(175,255,95), 156:(175,255,135), 157:(175,255,175), 158:(175,255,215), 159:(175,255,255), 160:(215,0,0), 161:(215,0,95), 162:(215,0,135), 163:(215,0,175), 164:(215,0,215), 165:(215,0,255), 166:(215,95,0), 167:(215,95,95), 168:(215,95,135), 169:(215,95,175), 170:(215,95,215), 171:(215,95,255), 172:(215,135,0), 173:(215,135,95), 174:(215,135,135), 175:(215,135,175), 176:(215,135,215), 177:(215,135,255), 178:(215,175,0), 179:(215,175,95), 180:(215,175,135), 181:(215,175,175), 182:(215,175,215), 183:(215,175,255), 184:(215,215,0), 185:(215,215,95), 186:(215,215,135), 187:(215,215,175), 188:(215,215,215), 189:(215,215,255), 190:(215,255,0), 191:(215,255,95), 192:(215,255,135), 193:(215,255,175), 194:(215,255,215), 195:(215,255,255), 196:(255,0,0), 197:(255,0,95), 198:(255,0,135), 199:(255,0,175), 200:(255,0,215), 201:(255,0,255), 202:(255,95,0), 203:(255,95,95), 204:(255,95,135), 205:(255,95,175), 206:(255,95,215), 207:(255,95,255), 208:(255,135,0), 209:(255,135,95), 210:(255,135,135), 211:(255,135,175), 212:(255,135,215), 213:(255,135,255), 214:(255,175,0), 215:(255,175,95), 216:(255,175,135), 217:(255,175,175), 218:(255,175,215), 219:(255,175,255), 220:(255,215,0), 221:(255,215,95), 222:(255,215,135), 223:(255,215,175), 224:(255,215,215), 225:(255,215,255), 226:(255,255,0), 227:(255,255,95), 228:(255,255,135), 229:(255,255,175), 230:(255,255,215), 231:(255,255,255), 232:(8,8,8), 233:(18,18,18), 234:(28,28,28), 235:(38,38,38), 236:(48,48,48), 237:(58,58,58), 238:(68,68,68), 239:(78,78,78), 240:(88,88,88), 241:(98,98,98), 242:(108,108,108), 243:(118,118,118), 244:(128,128,128), 245:(138,138,138), 246:(148,148,148), 247:(158,158,158), 248:(168,168,168), 249:(178,178,178), 250:(188,188,188), 251:(198,198,198), 252:(208,208,208), 253:(218,218,218), 254:(228,228,228), 255:(238,238,238)}
# source for conversion to rgb: https://jonasjacek.github.io/colors/ 

#[print(colorize("test", color, "white"), colorize("test", to_rgb(color_code(color,1)), "white")) for color in range(16)]; # used to test the conversion

def colors():
    out  = "These are the types of color codes that could be provided to the 'color' parameter of any plotting function, as well as the 'fullground' parameter of the function 'plt.colorize()', or as input for the functions 'plt.canvas_color()', 'plt.axes_color()' and 'plt.ticks_color()':\n\n"

    color = "bold underline"
    
    out += "• 'None' (as by default), to set the color automatically.  \n\n"
    
    out += "• The following " + colorize("color string codes", color) + ": "
    c = [colorize(el, el, background = "black" if el == "bright-white" else None) for el in fullground_codes]
    c = "\n   ".join(c)
    out += "\n\n   " + c + "\n\n"
    
    out += "• Along side the previous string color codes, one can add as many styles as desired among the following " + colorize("string style codes", color) + ": "
    c = [colorize(el, el) for el in style_codes]
    c = "\n   ".join(c)
    out += "\n\n   " + c + "\n\n"
    out += """The color and style codes must be separated by a space. Using 'flash' will result in an actual white flashing marker (therefore it will not work with 'bright-white' canvas background color). Naturally those style won't work as background colors.\n\n"""

    out += "• An " + colorize("integer between 0 and 255", color) + ", resulting in the following colors: "
    c = [colorize(str(i), i) for i in range(256)]
    c = ", ".join(c)
    out += "\n\n" + c + ". "
    out += "\n\nNote that the first 16 produce the same results as the previous string color codes.\n\n"
    
    out += "• An " + colorize("RGB color", color) + " consisting of a tuple of three values (red, green, blue), each between 0 and 255, to obtain the most realistic color rendering.\n\n"

    out += "• A " + colorize("list of color codes", color) + " to give a different color to each plot marker: the length of the list of colors will adapt to the length of the data set.\n\n"

    out += colorize("Background Colors", color) + ": all color codes above are valid also as background color, if provided to the 'background' parameter of the function 'plt.colorize()' or input as for the functions 'plt.canvas_color()', and 'plt.axes_color()'. For example, here is the effect of the string color codes above intended as background color: "
    c = [colorize(el, fullground = ("bright-white" if el == "black" else None), background = el) for el in fullground_codes]
    c = "\n   ".join(c)
    out += "\n\n   " + c + "\n"
    sys.stdout.write(out)
