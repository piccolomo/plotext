from plotext._utility.data import no_duplicates

##############################################
############     Style Codes    ##############
##############################################

no_style = 'default'

style_codes = {"bold": 1, "dim": 2, "italic": 3, "underline": 4, "double-underline": 21, "strike": 9, "inverted": 7, "flash": 5} # text styles and their ascii code

styles = list(style_codes.keys()) + [no_style]

info_style = 'dim'

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
    return styles[codes.index(code)] if code in codes else no_style

def clean_styles(style): # it returns a well written sequence of styles (separated by spaces) from a possible confused one
    codes = get_style_codes(style)
    return ' '.join([get_style_name(el) for el in codes])

def is_style(style):
    style = style.strip().split() if isinstance(style, str) else ['']
    return any([el in styles for el in style])

def styles_doc():
    from plotext._utility import styles, colorize, title_color
    c = [colorize(el, style = el) for el in styles]
    c = '\n'.join(c)
    print(c)
    mul = 'bold italic dim'
    print('\n' + colorize('multiple styles are accepted. ', title_color) + 'eg: ' + colorize(mul, style = mul))
