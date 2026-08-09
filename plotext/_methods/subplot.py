# Utilities for fitting and distributing subplot sizes within constraints

# Distribute None values proportionally so total does not exceed max size
def set_none_sizes(sizes, size_max):
    bins = len(sizes)
    for s in range(bins):
        size_set = sum([el for el in sizes[0:s] + sizes[s + 1:] if el is not None])
        available = max(size_max - size_set, 0)
        to_set = len([el for el in sizes[s:] if el is None])
        sizes[s] = available // to_set if sizes[s] is None else sizes[s]
    return sizes


# Fit sizes so cumulative sum does not exceed max, with optional direction. Each entry is clamped to the remaining budget; if the budget runs out a slot becomes 0; if there's leftover budget after every slot has its requested size, the leftover is left unused (the last slot is no longer forced to absorb it).
def fit_sizes(sizes, size_max, direction = 1):
    sizes = sizes[::direction]
    l = len(sizes)
    for i in range(l):
        m = max(size_max - sum(sizes[:i]), 0)
        sizes[i] = min(sizes[i], m)
    return sizes[::direction]