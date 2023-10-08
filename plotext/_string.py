from plotext._default import default_placement, correct_horizontal_alignment

space = ' '

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return string == len(string) * space# and len(string) != 0

def correct_label(label = None): 
    return None if only_spaces(label) else str(label).strip()

def get_displacement(string, alignment = None):
    l = len(string)
    alignment = correct_horizontal_alignment(alignment)
    index = default_placement.horizontal_alignments.index(alignment)
    displacements = [0, - l // 2 + 1, - l]
    return displacements[index]
