def log_limits(limits):
    limits = ['None' if limit is None else str(round(limit, 2)) for limit in limits]
    return '[' + ', '.join(limits) + ']'

# Format axis and side for logging purposes

def log_axis(axis, side):
    return 'axis ' + str(axis) + ' side ' + str(side)