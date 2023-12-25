color_codes = {"black":   0,    "white": 15,
               "gray":    8,    "gray+": 7,
               "red":     1,     "red+": 9,
               "green":   2,   "green+": 10,
               "orange":  3,  "orange+": 11,
               "blue":    4,    "blue+": 12,
               "magenta": 5, "magenta+": 13,
               "cyan":    6,    "cyan+": 14}

def color_to_integer(color):
    color = color.strip()
    valid = color in color_codes
    return color_codes[color] if valid else None

# self.color_sequence = ["blue+", "green+", "red+", "cyan+"]

