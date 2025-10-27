def set_none_sizes(sizes, size_max):
    bins = len(sizes)
    for s in range(bins):
        size_set = sum([el for el in sizes[0:s] + sizes[s + 1:] if el is not None])
        available = max(size_max - size_set, 0)
        to_set = len([el for el in sizes[s:] if el is None])
        sizes[s] = available // to_set if sizes[s] is None else sizes[s]
    return sizes

# Fit sizes so they do not exceed size_max, respecting direction

def fit_sizes(sizes, size_max, direction = 1):
    sizes = sizes[::direction]
    l = len(sizes)
    for i in range(l):
        m = size_max - sum(sizes[:i])
        sizes[i] = min(sizes[i], m) if i != l - 1 else m
    return sizes[::direction]