from math import log10, ceil

def get_labels(ticks): # it returns the approximated string version of the data ticks
    d = get_distinguishing_digit(ticks)
    formatting_string = "{:." + str(d + 1) + "f}"
    labels = [formatting_string.format(el) for el in ticks]
    pos = [el.index('.') + d + 2 for el in labels]
    labels = [labels[i][: pos[i]] for i in range(len(labels))]
    all_integers = all(map(lambda el: el == int(el), ticks))
    labels = [str(int(el)) for el in ticks] if all_integers else labels
    add_zeros = not all_integers and len(labels) > 1
    labels = [add_extra_zeros(el, d) for el in labels] if add_zeros else labels
    return labels

def get_distinguishing_digit(data): # it return the minimum amount of decimal digits necessary to distinguish all elements of a list
    d = [_get_distinguishing_digit(data[i], data[i + 1]) for i in range(len(data) - 1)]
    return max(d, default = 1)

def _get_distinguishing_digit(a, b): # it return the minimum amount of decimal digits necessary to distinguish a from b
    d = abs(a - b)
    d = 0 if d == 0 else - log10(2 * d)
    d = 0 if d < 0 else ceil(d)
    #d = d + 1 if round(a, d) == round(b, d) else d
    return d

def add_extra_zeros(label, ndigits): # it adds 0s at the end of a label if necessary
    zeros = len(label) - 1 - label.index('.' if 'e' not in label else 'e')
    return (label + '0' * (ndigits - zeros)) if zeros < ndigits else label

def brush(*lists): # remove duplicates from lists x, y, z ...
    l = min(map(len, lists)) 
    lists = [el[:l] for el in lists] 
    z = transpose(lists, len(lists))
    z = no_duplicates(z)
    #z = sorted(z) #, key = lambda x: x[0])
    lists = transpose(z, len(lists))
    return lists

def transpose(data, length = 1): # it needs no explanation
    return list(map(list, zip(*data))) if len(data) != 0 else [[]] * length

def no_duplicates(data): # removes duplicates from a list
    new = []
    [new.append(item) for item in data if item not in new]
    return new


# def add_extra_spaces(labels, side): # it adds empty spaces before or after the labels if necessary
#     length = 0 if labels == [] else max_length(labels)
#     if side == "left":
#         labels = [space * (length - len(el)) + el for el in labels]
#     if side == "right":
#         labels = [el + space * (length - len(el)) for el in labels]
#     return labels
