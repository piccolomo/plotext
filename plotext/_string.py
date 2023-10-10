space = ' '

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return string == len(string) * space# and len(string) != 0

def correct_label(label = None): 
    return None if only_spaces(label) else str(label).strip()

def correct_position(position, alignment, label_length, string_length):
    l, ls = label_length, string_length
    center =  l // 2 # position of center in string counting from 0
    displacement = [0, - center, - l, - center][alignment + 1]
    position += displacement
    position = 0 if - (l - 1) <= position < 0 and alignment == 2 else ls - l if 0 < ls - position <= (l - 1) and alignment == 2 else position
    return position

# ls - l < position < ls


 
