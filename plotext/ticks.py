# /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script is focused on solving the problem of representing the each x or y tick number within a finite number of characters c.
# This is necessary for example for very long tick numbers, which could occupy too much space in the terminal.
# In general we want to limit each number to a maximum number of characters c, and transform it in case it surpass this limit. The transformation undergone would be clarified with a formula appearing underneath the plot.

# At first let's formalize the representation of a positive number n (>=0) within c characters. 
# If for example we use c = 4 number of characters, considering that one characters is dedicated to the comma ".", we can represent the following numbers:
# - from 0.00 to 9.99 with 0.01 spacing between each number
# - from 10.0 to 99.9 with 0.1 spacing
# - from 100. to 9999 with 1 spacing
# In this case we have 3 levels of representation with increasing spacing. This behavior can be generalized with the formula:
# n[k] = k * delta[l]
# where l is the level of representation, n the number represented with c characters, delta[l] is the spacing of level i, and k takes values from a lower to a upper bound dependent to the band, in other words k in the following set
# I[k] = [lower[l], upper[l]].
# For negative numbers the representation is the same with 1 initial characters dedicated to the "-" sign and c - 1 to the number representation. 
# The exact formulas are here evaluated:

# The numbers of representation levels correspondent to c characters.
# Eg: levels(4) = 3
def levels(c):
    if c == 1:
        c += 1
    return c - 1

# The spacing for level l and characters c. Note that l must be in [0, levels(c) - 1]. 
# Eg: delta(0, 4) = 0.01; delta(1, 4) = 0.1; delta(2, 4) = 1
def delta(l, c):
    if c == 1:
        c += 1
    return 10 ** (2 - c + l)

# The lower bound for level l and characters c. Note that l must be in [0, levels(c) - 1]. 
# Eg: lower(0, 4) * delta(0, 4) = 0; lower(1, 4) * delta(1, 4) = 10.0; lower(2, 4) * delta(2, 4) = 100.
def lower(l, c):
    if l == 0:
        return 0
    else:
        return 10 ** (c - 2)

# The upper bound for level l and characters c. Note that l must be in [0, levels(c) - 1]. 
# Eg: upper(0, 4) * delta(0, 4) = 9.99; upper(1, 4) * delta(1, 4) = 99.9; upper(2, 4) * delta(2, 4) = 9999
def upper(l, c):
    if c == 1:
        return 9
    if l !=  c - 2:
        return 10 * 10 ** (c - 2) - 1
    else:
        return 100 * 10 ** (c - 2) - 1
    
# This function evaluates the number of steps in each level l. Note: this function is not really necessary for the rest.  
# Eg: steps(0, 4) = 1000, steps(1, 4) = 900, steps(2, 4) = 9900
def steps(l, c):
    return upper(l, c) - lower(l, c) + 1

# This function round a number to c number of characters (regardless if they are decimal or not).
# Eg: _round(0.369, 4) = 0.37; _round(12345, 3) = 123
def _round(n, c):
    sign = +1
    if n < 0:
        if c > 1:
            c = c - 1
        sign = -1
    if n <=0:  
        n = abs(n)
    d = c - len(str(int(n))) - 1
    if d <= 0 or n == float(int(n)):
        return sign * round(float(str(n)[:c]))
    else:
        return sign * round(n, d)

# This function evaluates all possible numbers that can be represented using c number of characters.
def numbers(c):
    tot = []
    for l in range(levels(c)):
        new = [k * delta(l, c) for k in range(lower(l, c), upper(l, c) + 1)]
        new = [_round(el, c) for el in new]
        tot += new
    return tot

# This test function checks whatever all the numbers represented with c characters have in fact a number of characters <= c
def test_numbers(c):
    return all([len(str(el)) <= c for el in numbers(c)])

# And here is the test
# un-comment to run !
# for c in range(7):
#    pass
#    print(test_numbers(c))


# Let's formalize the representation of a data set within c number of characters. The solution would be different if the data set is positive (>=0), negative (<=0), or with mixed signs.
# These are the functions used to differentiate these cases:

# This function evaluates the signature of a data set (already sorted in ascending order).
# Eg: _signature([1, 2, 3]) = 1; _signature([-3, -2, -1]) = -1; _signature([-1, 0, 1]) = 0
def _signature(data):
    if data[0] >=0:
        sign = 1
    elif data[-1] <= 0:
        sign = -1
    elif data[-1] > 0:
        sign = 0
    return sign

# We represent the data points using the formula:
# m[j] = dm * j + m0 for j in [0, M - 1]
# where dm is the spacing between each data point, m0 the initial value and M the number of points.
# In general, the transformed point n[j] would be connected to m[j] using the linear formula:
# m[j] = a * n[j] + b
# where a is the slope and b the intercept. The goal is to find a and b for all cases. 

# This function redirecting the solution to the problem (of representing a data set within c characters) for each case (depending on the signature of the data).
# Note: if each data point of the original data is already within c characters, no transformation is necessary, and so a = 1 and b = 0.
# The solution for negative numbers can be easily found using the solution for positive numbers, while for mixed signs a different solution is necessary. 

def _round_data(data, c):
    data = sorted([round(el, 13) for el in data])
    data_c = [_round(el, c) for el in data]  
    if data_c == data:
        return data_c, (1, 0)
    #print("rounding ...")
    sign = _signature(data)
    if sign == 1:
        return _round_positive_data(data, c)
    elif sign == - 1:
        return _round_negative_data(data, c)
    else:
        return _round_mixed_data(data, c - 1)
    
# Let's consider first the simpler case of positive data (m[j] >= 0). We want each data point to be represented by c characters.
# A note: the data may need some initial optional re-scaling if it is either too big or too small for c characters representation. More specifically, if the last value m[M - 1] is either bigger then the biggest number (that can be represented by c characters) or smaller then the smallest number (that can be represented by c characters), then the data is multiplied by the minimum power of 10 such that m[M - 1] can be represented by c characters. The reason a power of 10 is chosen is that the re-scaled value would contain the same digits as the original values, just shifted left or right with respect to the comma, making their reading more straightforward. So the first transformation would be from m[j] to 10 ** exp * m[j] where exp = 0 if no initial transformation takes place.  
# Extending the formula for a number represented by c characters n[k] = k * dn[l], allowing k to be linearly dependent on j:
# k = k0 + dk * j
# we get n[j] = (k0 + dk * j) * delta[l]
# and we require that m[j] ~ n[j] which gives rise to the following 2 conditions:
# k0 * delta[l] ~ m0
# dk * delta[l] ~  dm
# The solution is k0 = int[m0 / dn[l]] and dk = int[dm / dn[l]]
# An important extra condition is that k0 + dk * (M - 1) is in [lower[l], upper[l]]. 
# A way to solve this is to find the solution of those 2 equations (plus the extra condition) for all levels l and to chose the one with smallest overall error err = sum_j abs[m_j - n_j] for j in [0, M - 1]
# In order to find a and b, we see that:
# a * n[j] + b = a * dk * delta[l] * j + (a * k0 * delta[l] + b)
# comparing to 10 ** -exp * m[j] = 10 ** -exp * dm * j + 10 ** -exp * m0 we get:
# a = 10 ** -exp * dm / (dk * delta[l])
# b = 10 ** -exp * m0 - a * k0 * delta[l]

# The following functions are necessary to represent positive data points (>=0) using c characters.

from math import log10, ceil # necessary for the initial optional re-scaling

def _round_positive_data(data, c):
    m = len(data)
    ml = data[-1] # the last data point
    levs = list(range(levels(c))) # all possible levels
    if levs == []:
        return [], [1, 0]
    lo = [lower(l, c) for l in levs] # the lower bound for each level
    up = [upper(l, c) for l in levs] # the upper bound for each level
    dn = [delta(l, c) for l in levs] # the spacing for each level

    # the optional re-scaling
    exp = 0
    if ml > up[-1] * dn[-1]:
        exp = log10(ml / (up[-1] * dn[-1]))
        exp = -ceil(exp)
    if ml < dn[0]:
        exp = log10(dn[0] / ml)
        exp = ceil(exp)
    data = [el * 10 ** ceil(exp) for el in data]

    m0 = data[0] # the smallest value in the data set
    dm = data[1] - data[0] # the spacing of the data set
    
    k0 = [int(m0 / dn[l]) for l in levs] # the solution for k0 for all levels
    dk = [max(1, int(dm / dn[l])) for l in levs] #  the solution for dk for all levels
    sol = [[(k0[l] + dk[l] * j) * dn[l] for j in range(m)] for l in levs] # all possible solutions n[j]
    err = [sum([abs(data[j] - sol[l][j]) for j in range(m)]) for l in levs] # the error for all levels
    lim = [k0[l] + dk[l] * (m - 1) <= up[l] for l in levs] # the extra condition for each level
    for l in levs: # modify the errors so that only when the extra condition is verified, the solution is considered
        if not lim[l]:
            err[l] = 2 * abs(max(err)) + 1
    l = position(err, min(err))[0] # the level where the error is minimum
    data = sol[l]
    a = 10 ** (-exp) * dm / (dk[l] * dn[l])
    b = 10 ** -exp * m0 - a * k0[l] * dn[l]
    for l in levs:
        pass
        #print(" ", l, "-", sol[l])
    return [data, (a, b)]

# This function finds the positions in a data set of certain value.
def position(data, value):
    res = []
    for i in range(len(data)):
        if data[i] == value:
            res.append(i)
    return res

# In the case of negative data values (<=0), it is easy to find a solution using the results for positive values.
# All it takes is a proper sign inversion.
# Note that the number of characters is one less then c because the first character is assigned to the "-" sign.
# Note also that in this case a * n[j] + b = -m[j] and so a * (-n[j]) -b = m[j], and so only b changes sign.
def _round_negative_data(data, c):
    data = sorted([-el for el in data])
    data, (a, b) = _round_positive_data(data, c - 1)
    data = sorted([-el for el in data], key = lambda x: x)
    return [data, (a, -b)]

# In the case of mixed data, the formula n[k] = k * delta[l] can be extended to negative numbers if k is in the set
# I[k] = [- upper[l], -lower[l]] + [lower[l], upper[l]]
# The main problem with this set is that going from k = -lower[l] to k = lower[l] there is a jump of 2 * lower[l] while for all other values a regular jump of 1.
# A way to deal with this is to introduce this new variable k[t] such that:
# k[t] = t for l = 0
# k[t] = (2 * t + 1) * lower[l] for l != 0
# For l = 0 there is no jump problem since +- lower[l] = 0
# For l!= 0, k = -lower[l], implies t = -1, while k = lower[l] implies t = 0 with a regular jump of 1 in t.
# The upper limiting condition for t is that:
# abs[t] <= upper[0] for l = 0
# - 0.5 * (upper[l] / lower[l] + 1)  <= t <= 0.5 * (upper[l] / lower[l] - 1) for l != 0
# In conclusion with the definitions given, we consider numbers n[t] written as:
# n[t] = k[t] * delta[l]
# which are both positive and negative. Let's write k[t] in a single formula as:
# k[t] = (s[l] * t + i[l]) * low[l]
# where s[0] = 1, s[l!=0] = 2; i[0] = 0, i[l!=0] = 1; low[0] = 1, low[l!=0] = lower[l]
# The initial optional re-scaling of the data is similar to the positive case with the difference that one needs to check whatever m[0] OR m[M-1] are bigger then the biggest number (that can be represented by c characters) or smaller then the smallest number (that can be represented by c characters) before re-scaling by the minimum 10 ** exp. 
# If we want to apply this to a data set m[j], then we allow t to be:
# t = t0 + dt * j
# so that n[j] = (s[l] * (t0 + dt * j) + i[l]) * low[l] * delta[l] = t0 * s[l] * low[l] * delta[l] + dt * s[l] * low[l] * delta[l] * j
# and equating with m[j] = m0 + dm * j we get the 2 following conditions:
# t0 * s[l] * low[l] * delta[l] ~ m0
# dt * s[l] * low[l] * delta[l] ~ dm
# with solutions given by t0 = int(m0 / (s[l] * low[l] * delta[l])) and dt = int(dm / (s[l] * low[l] * delta[l])).
# The extra condition is that k[t0 + dt * (M - 1)] is in [lower[l], upper[l]]. 
# Similarly to the positive case, the way to solve this is to find the solution of those 2 equations (plus the extra condition) for all levels l and to chose the one with smallest overall error err = sum_j abs[m_j - n_j] for j in [0, M - 1]
# In order to find a and b in this case, we see that:
# a * n[j] + b = a * dt * s[l] * low[l] * delta[l] * j + a * t0 * s[l] * low[l] * delta[l] + b
# comparing to 10 ** -exp * m[j] = 10 ** -exp * dm * j + 10 ** -exp * m0 we get:
# a = 10 ** -exp * dm / (dt * s[l] * low[l] * delta[l])
# b = 10 ** -exp * m0 - a * t0 * s[l] * low[l] * delta[l])

def _round_mixed_data(data, c):
    m = len(data)
    m0 = data[0]
    ml = data[-1] # the last data point
    levs = list(range(levels(c))) # all possible levels
    if levs == []:
        return [], [1, 0]
    s = [1 if l == 0 else 2 for l in levs] # the slope in k[t] for each level
    i = [0 if l == 0 else 1 for l in levs] # the slope in k[t] for each level
    lo = [1 if l == 0 else lower(l, c) for l in levs] # the lower bound for each level
    up = [upper(l, c) for l in levs] # the upper bound for each level
    dn = [delta(l, c) for l in levs] # the spacing for each level

    # the optional re-scaling
    exp = 0
    m_max = max(-m0, ml)
    #m_min = min(-m0, ml)
    if m_max > up[-1] * dn[-1]:
        exp = log10(m_max / (up[-1] * dn[-1]))
        exp = -ceil(exp)
    if m_max < dn[0]:
        exp = log10(dn[0] / m_max)
        exp = ceil(exp)
    data = [el * 10 ** ceil(exp) for el in data]

    m0 = data[0] # the smallest value in the data set
    dm = data[1] - data[0] # the spacing of the data set
    
    t0 = [int(m0 / (s[l] * lo[l] * dn[l])) for l in levs] # the solution for t0 for all levels
    dt = [max(1, int(dm / (s[l] * lo[l] * dn[l]))) for l in levs] #  the solution for dt for all levels
    #print("dt", dt)
    sol = [[(s[l] * (t0[l] + dt[l] * j) + i[l]) * lo[l] * dn[l] for j in range(m)] for l in levs] # all possible solutions n[j]
    err = [sum([abs(data[j] - sol[l][j]) for j in range(m)]) for l in levs] # the error for all levels
    lim = [(s[l] * (m - 1) + i[l]) * lo[l] <= up[l] for l in levs] # the extra condition for each level
    for l in levs: # modify the errors so that only when the extra condition is verified, the solution is considered
        if not lim[l]:
            err[l] = 2 * abs(max(err)) + 1
    l = position(err, min(err))[0] # the level where the error is minimum
    #print("l", l)
    data = sol[l]
    a = 10 ** (-exp) * dm / (dt[l] * s[l] * lo[l] * dn[l])
    b = 10 ** -exp * m0 - a * t0[l] * s[l] * lo[l] * dn[l]
    for l in levs:
        pass
        #print(" ", l, "-", sol[l])
    return [data, (a, b)]

if __name__=="__main__":
    data = sorted([-0, 1.5, 3, 4.5])
    c = 2
    data_r, (a, b) = _round_data(data, c)
    data_n = [a * el + b for el in data_r]
    print(data, data_r)
    if data_n != data:
        print(data_n)
