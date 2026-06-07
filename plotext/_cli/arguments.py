# Argument-parsing primitives: floats, list/dict transformations, --method grouping.

from plotext._methods.sequence import transpose


# A list whose items are meant to become separate arguments in the next function call.
class ListOfArguments(list):
    pass


# Return text as a float, or unchanged if it isn't numeric.
def to_float(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return text


# Pick a subset of columns by a 1-indexed comma-separated string like '1,3'.
def select_columns(columns, mode):
    indices = [int(c) - 1 for c in mode.split(',')]
    return [columns[i] for i in indices]


# Use the first element of each column as the key for the rest.
def columns_to_dict(columns):
    return {column[0]: column[1:] for column in columns}


# Transpose a CSV table to columns of floats. columns = '' for all, '1,3' to keep only those.
def get_columns_from_table(table, columns):
    data = [[to_float(x) for x in c] for c in transpose(table)]
    if columns:
        data = select_columns(data, columns)
    return data[0] if len(data) == 1 else ListOfArguments(data)


# Transpose a CSV table to columns of floats, then use row 0 as keys.
def get_dict_from_table(table):
    columns = [[to_float(x) for x in c] for c in transpose(table)]
    return columns_to_dict(columns)


# Group arguments into [(method_name, [arg_strings]), ...], one entry per --method.
def group_by_method(arguments):
    groups = []
    for arg in arguments:
        if arg.startswith('--'): groups.append((arg[2:].replace('-', '_'), []))
        elif groups: groups[-1][1].append(arg)
    return groups
