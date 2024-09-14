ha = ['left', 'center', 'right']
va = ['top', 'center', 'bottom']
ha_short = [-1, 0, 1]

def correct_ha(alignement):
    return ha.index(alignement) - 1 if alignement in ha else alignement if alignement in ha_short else -1

def correct_va(alignement):
    return va.index(alignement) - 1 if alignement in va else alignement if alignement in ha_short else -1