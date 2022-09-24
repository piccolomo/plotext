def decimal_characters(characters = 3):
    dec_characters = characters - 2
    return dec_characters

def decimal_points(characters = 3):
    dec_characters = decimal_characters(characters)
    if characters == 1 or characters == 2:
        dec_characters = 0
    return dec_characters

def delta(level = 0, characters = 3):
    dec_characters = decimal_characters(characters)
    if characters == 1:
        dec_characters = 0
    return 10 ** (level - dec_characters)

def levels(characters = 3):
    dec_characters = decimal_characters(characters)
    if characters == 1:
        dec_characters = 0
    return dec_characters + 1

def lower_bound(level = 0, characters = 3):
    dec_characters = decimal_characters(characters)
    if level == 0:
        return 0
    elif level >= 1:
        return 10 ** level

def upper_bound(level = 0, characters = 3):
    dec_characters = decimal_characters(characters)
    if level < dec_characters :
        return 10 ** (level + 1) - delta(level, dec_characters)
    elif level == dec_characters or characters == 1:
        return 10 ** (dec_characters + 2) - 1

def steps(level = 0, characters = 3):
    dec_characters = decimal_characters(characters)
    if characters == 1:
         dec_characters = 0
    if characters == 2:
         dec_characters = 1
    if level == 0:
        return 10 ** (dec_characters + 1)
    elif 0 < level < dec_characters:
        return 9 * 10 ** dec_characters
    elif level == dec_characters :
        return 99 * 10 ** dec_characters

def signature(data):
    sign = 1
    for i in range(len(data)):
        sign = int(sign and data[i] >= 0)
    if sign == 0:
        sign = -1
    return sign

def round_dec(num, decimal_points):
    num_rounded = round(num * 10 ** decimal_points) / 10 ** decimal_points
    if num_rounded - round(num_rounded) == 0.0:
        num_rounded = round(num_rounded) 
    return num_rounded

def numbers(characters = 3):
    tot = []
    dec_points = decimal_points(characters)
    for level in range(levels(characters)):
        new = [lower_bound(level, characters) + l * delta(level, characters) for l in range(steps(level, characters))]
        new = [round_dec(el, dec_points) for el in new]
        tot += new
    return tot



m, M = 1, 10
n = 2
data = [(M - m) / (n - 1) * k + m for k in range(n)]
print("data", data, "\n")

characters = 4
sign = signature(data)
# dec_characters = decimal_characters(characters, sign)
# #print(dec_characters)

x_first, x_last = min(data), max(data)

# n = len(data)
# for level in range(dec_characters + 1):
#     d = delta(level, characters, sign)
#     lower = lower_bound(level, characters, sign)
#     lvs = levels(level, characters, sign)
#     #m = delta * (n - 1) / (x_last - x_first)
#     #k0 = x_first  / delta
#     #print(delta, " ",k0)
#     #k0=(a * m - li) / dni
#     #    b = li - a * m + round(k0) * dni  
#     #    b_list.append(b)
#     e = 1
#     if x_first != 0 and lower != 0:
#         e = math.log(lower / x_first, 10)
#     e = round(e)
#     k0 = ((10 ** e) * x_first - lower) / d
#     t = ((10 ** e) * x_last - lower - d * k0) / (d * (n - 1))

#     m = (t * d) * (n - 1) / (x_last - x_first)
#     c = lower + d * k0 - m * x_first
#     test = lower +  d * (t * n + k0) < lower + d * (lvs - 1)
#     #if not test:
#     data_new = [cut(lower +  d * (t * k + k0))  for k in range(n)]
#     print(level, test, data_new, k0, t, " - ", 1/m, -c/m)
#     #    data_new = [round(a * el + b, 14) for el in data]
#     #print(i)
#     #print(data_new)
