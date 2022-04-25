from plotext._utility.marker import space
from plotext._utility.color import colorize

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or '' 
    return (type(string) == str) and (string == len(string) * space) #and len(string) != 0

def format_time(name, time): # it properly formats the computational time 
    t = time if time is not None else 0
    unit = 's' if t >= 1 else 'ms' if t >= 10 ** -3 else 'µs'
    p = 0 if unit == 's' else 3 if unit == 'ms' else 6
    t = round(10 ** p * t, 1)
    l = len(str(int(t)))
    t = str(t)
    t = ' ' * (3 - l) + t
    return colorize(name + ': ', "", "dim") + colorize(t + ' ' + unit, "cyan", "bold")

def insert_string(string, label, coord, alignment = "center", extra_space = 0): # it inserts label inside string, at a given coordinate and alignment
    s, l = len(string), len(label)
    if l + extra_space > s:
        return string, None, None
    a = -int(l / 2) if alignment == 'center' else 0 if alignment == 'left' else -l + 1 
    b = max(coord + a, 0) 
    e = b + l 
    if e >= s: 
        b = max(0, s - l) 
        e = b + l 
    string = string[:b] + label[:s] + string[e:]
    return string, b, e

def insert_strings(string, labels, coords, extra = 0): # it inserts a string label inside a string, at a given coordinate and alignment
    string_length = len(string)
    coords_length = len(coords)
    #alignments = ["center"] * coords_length if alignments == None else alignments
    occupied = []
    used = []
    for i in range(coords_length):
        string_temp, b, e = insert_string(string, labels[i], coords[i], extra_space = extra)
        if b is not None and b not in occupied and 0 <= coords[i] < string_length:
            string = string_temp
            occupied += list(range(b, e + extra))
            used.append(coords[i])
    return string, used

def pad_string(num, length): # pad a number with spaces before to reach length 
    num = str(num)
    l = len(num)
    return num + ' ' * (length - l)
    


