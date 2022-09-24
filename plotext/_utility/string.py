from plotext._utility.marker import space_marker

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or '' 
    return (type(string) == str) and (string == len(string) * " ") #and len(string) != 0
    
def insert_label(string, label, coord, alignment): # it inserts a string label inside a string, at a given coordinate and alignment
    s, l = len(string), len(label)
    a = -int(l / 2) if alignment == 'center' else 0 if alignment == 'left' else -l + 1
    b = max(coord + a, 0)
    e = b + l
    if e >= s:
        b = max(0, s - l)
        e = b + l
    string = string[:b] + label[:s] + string[e:]
    return string, b, e # b, e are also returned for xticks

def pad_label(label, d): # it adds 0s at the end of a label if necessary
    zeros = len(label) - 1 - label.index('.')
    if zeros < d:
        label += '0' * (d - zeros)
    return label

def pad_labels(labels, side): # it adds empty spaces before or after the labels if necessary
    length = 0 if labels == [] else max(list(map(len, labels)))
    if side == "left":
        labels = [space_marker * (length - len(el)) + el for el in labels]
    if side == "right":
        labels = [el + space_marker * (length - len(el)) for el in labels]
    return labels
