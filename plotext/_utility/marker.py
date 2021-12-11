from plotext._utility.color import color_sequence, colorize
from plotext._utility.data import join
from plotext._utility.platform import _platform
import sys

##############################################
############    Marker Codes     #############
##############################################

space_marker = ' ' # the default null character that appears as background to all plots

# special marker codes, easier to remember for special characters
marker_codes = {'sd'         :'█',
                'dot'        :'•',
                
                'dollar'     :'$',
                'euro'       :'€',
                'bitcoin'    :'฿',
                
                'at'         :'@',
                'heart'      :'♥',
                'smile'      :'☺',
                
                'gclef'      :'𝄞',
                'note'       :'𝅘𝅥',
                'shamrock'   :'☘',
                'atom'       :'⚛',
                'snowflake'  :'❄',
                'lightinig'  :'🌩',
                'queen'      :'♕',
                'king'       :'♔',
                
                'cross'      :'♰',
                'yinyang'    :'☯',
                'om'         :'ॐ',
                'osiris'     :'𓂀',
 
                'zero'       :'🯰',
                'one'        :'🯱',
                'two'        :'🯲',
                'three'      :'🯳',
                'four'       :'🯴',
                'five'       :'🯵',
                'six'        :'🯶',
                'seven'      :'🯷',
                'eight'      :'🯸',
                'nine'       :'🯹'}

hd_marker_codes = {'hd': '▞',
                   'fhd': '🬗'} # the markers that represents the higher definition characters  

marker_sequence = ['fhd', '•', 'x', 'y', 'z'] # the standard marker sequence for multiple data plots
marker_sequence += list(map(chr, range(97, 97 + len(color_sequence) - len(marker_sequence)))) # it continues with the alphabet letters
bar_marker = 'fhd'

side_symbols = {("lower", "left"): 'L', ("lower", "right"): '⅃', ("upper", "left"): 'Γ', ("upper", "right"): '⅂'} # symbols used in the legend to indentify the axes used for plot

grid_codes = {(1,1,0,0): '└', (1,0,1,0): '│', (1,1,1,0): '├', (0,0,1,1): '┐', (1,0,1,1): '┤', (0,1,0,1): '─', (1,1,1,1): '┼', (0,1,1,1): '┬', (1,1,0,1): '┴', (1,0,0,1):'┘', (0,1,1,0):'┌'} # codes for grid characters used to easily identify what happens when summed; eg: '─' + '│' = '┼'
grid_markers = {grid_codes[el]:el for el in grid_codes}

hd_codes = {(0,0,0,0): ' ', (1,0,0 ,0): '▘', (0,0,1,0): '▖', (0,0,0,1): '▗', (0,1,0,0): '▝', (1,0,1,0): '▌', (0,1,0,1): '▐', (0,0,1,1): '▄', (1,1,0,0):    '▀', (1,0,0,1): '▚',  (0,1,1,0): '▞', (1,1,1,0): '▛', (1,0,1,1): '▙', (0,1,1,1): '▟', (1,1,0,1): '▜', (1,1,1,1): '█'} # codes for high definition markers used to easily sum them; eg: '▘' + '▗' = '▚'
hd_markers = {hd_codes[el]:el for el in hd_codes}

fhd_codes = {(0,0,0,0,0,0): ' ', (1,0,1,0,1,0):'▌', (0,1,0,1,0,1): '▐', (1,1,1,1,1,1): '█', (1,0,0,0,0,0):'🬀', (0,1,0,0,0,0):'🬁', (1,1,0,0,0,0):'🬂', (0,0,1,0,0,0):'🬃', (1,0,1,0,0,0):'🬄', (0,1,1,0,0,0):'🬅', (1,1,1,0,0,0):'🬆', (0,0,0,1,0,0):'🬇', (1,0,0,1,0,0):'🬈', (0,1,0,1,0,0):'🬉', (1,1,0,1,0,0):'🬊', (0,0,1,1,0,0):'🬋', (1,0,1,1,0,0):'🬌', (0,1,1,1,0,0):'🬍', (1,1,1,1,0,0):'🬎', (0,0,0,0,1,0):'🬏', (1,0,0,0,1,0):'🬐', (0,1,0,0,1,0):'🬑', (1,1,0,0,1,0):'🬒', (0,0,1,0,1,0):'🬓', (0,1,1,0,1,0):'🬔', (1,1,1,0,1,0):'🬕', (0,0,0,1,1,0):'🬖', (1,0,0,1,1,0):'🬗', (0,1,0,1,1,0):'🬘', (1,1,0,1,1,0):'🬙', (0,0,1,1,1,0):'🬚', (1,0,1,1,1,0):'🬛', (0,1,1,1,1,0):'🬜', (1,1,1,1,1,0):'🬝', (0,0,0,0,0,1):'🬞', (1,0,0,0,0,1):'🬟', (0,1,0,0,0,1):'🬠', (1,1,0,0,0,1):'🬡', (0,0,1,0,0,1):'🬢', (1,0,1,0,0,1):'🬣', (0,1,1,0,0,1):'🬤', (1,1,1,0,0,1):'🬥', (0,0,0,1,0,1):'🬦', (1,0,0,1,0,1):'🬧', (1,1,0,1,0,1):'🬨', (0,0,1,1,0,1):'🬩', (1,0,1,1,0,1):'🬪', (0,1,1,1,0,1):'🬫', (1,1,1,1,0,1):'🬬', (0,0,0,0,1,1):'🬭', (1,0,0,0,1,1):'🬮', (0,1,0,0,1,1):'🬯', (1,1,0,0,1,1):'🬰', (0,0,1,0,1,1):'🬱', (1,0,1,0,1,1):'🬲', (0,1,1,0,1,1):'🬳', (1,1,1,0,1,1):'🬴', (0,0,0,1,1,1):'🬵', (1,0,0,1,1,1):'🬶', (0,1,0,1,1,1):'🬷', (1,1,0,1,1,1):'🬸', (0,0,1,1,1,1):'🬹', (1,0,1,1,1,1):'🬺', (0,1,1,1,1,1):'🬻'} # codes for full high definition markers used to easily sum them; eg: '🬐' + '🬇' = '🬗'
fhd_markers = {fhd_codes[el]:el for el in fhd_codes}

##############################################
##########    Marker Functions     ###########
##############################################

def sum_markers(past, present): # properly sums markers depending on their type
    if past in hd_markers and present in hd_markers:
        return hd_codes[sum_tuples(hd_markers[past], hd_markers[present])]
   
    elif past in fhd_markers and present in fhd_markers:
        return fhd_codes[sum_tuples(fhd_markers[past], fhd_markers[present])]

    elif past in grid_markers and present in grid_markers:
        return grid_codes[sum_tuples(grid_markers[past], grid_markers[present])]
    else:
        return present

def refine_marker(marker, x, y): # used to identify the actual hd or fhd marker depending on the data coordinates
    if marker not in marker_codes and marker not in hd_marker_codes:
        return marker
    if marker in marker_codes:
        return marker_codes[marker]
    xfactor = 2
    yfactor = 3 if 'fhd' in marker else 2
    xcode = marker_code(x, xfactor)
    ycode = marker_code(y, yfactor)[::-1]
    code = tuple(join([[int(x and y) for x in xcode] for y in ycode]))
    marker = hd_codes[code] if marker == 'hd' else fhd_codes[code]
    return marker
        
def marker_code(x, factor): # the marker one dimensional tuple coordinates dependent on the coordinate and factor
    x = int((factor * x) % factor) 
    code = [x == i for i in range(factor)]
    return code
    
def marker_factor(markers, hd, fhd): # usefull to improve the resolution of the canvas for higher resolution markers
    if 'fhd' in markers:
        return fhd
    elif 'hd' in markers:
        return hd
    else:
        return 1

def sum_tuples(a, b): # it summs two tuples into one
    return tuple([int(a[i] or b[i]) for i in range(len(a))])

def markers():
    out = """A single character could be provided to the 'marker' parameter of any plotting function. \n
If 'None' is provided (as by default), the marker is set automatically. \n
If the space character " " is provided, the plot will be invisible. \n
A list of markers could also be provided: in this case the length of the list of markers will adapt to the length of the data set.

Here are the extra available marker codes: \n"""
    
    m = [el for el in marker_codes]
    v = [marker_codes[el]  for el in m]
    l = max([len(str(el)) for el in m])
    m = [el + " " * (l - len(str(el))) for el in m]
    out += "\n" + colorize("Code" + " " * (l - 4), "bright-blue bold") + "\t" + colorize("Marker", "bright-blue bold")
    for i in range(len(m)):
        out += "\n" + m[i] + "\t" + v[i]
    out += "\n"
    if _platform != "windows":
        out += """\nThe marker code "sd" stands for "standard resolution". To plot in higher resolutions use one of following two extra codes:\n"""
    
        m = [el for el in hd_marker_codes]
        v = [hd_marker_codes[el] for el in m]
        m = [el + " " * (l - len(str(el))) for el in m]
        m = [colorize(el, "bright-blue bold") for el in m]
        c = [2, 3]
        r = ["high resolution", "full high resolution"]
        r = [colorize(el, "bright-blue bold") for el in r]
    
        for i in range(len(m)):
            out += "\n" + m[i] + "\t" + v[i] + "\t" + r[i] + ": " + str(c[i]) + " x 2 unicode block characters" + "\n"

    sys.stdout.write(out)
    
##############################################
#########    Windows Exception     ###########
##############################################
if _platform == "windows":
    marker_codes = {'sd'         :'█',
                    'dot'        :'•',
                
                    'dollar'     :'$',
                    'euro'       :'€',
                    'bitcoin'    :'฿',
                
                    'at'         :'@',
                    'heart'      :'♥',
                    'smile'      :'☺'}
    hd_marker_codes = {}
    marker_sequence.pop(marker_sequence.index("fhd"))
    bar_marker = 'sd'
