# Per-argument value resolution: @-syntax (file loading), stdin pipe, and literal parsing.

import os
import sys

from plotext._methods.file import read
from plotext._cli.arguments import get_columns_from_table, get_dict_from_table


# Folder bundled with plotext holding sample CSVs and media files for @sample:<name>.
sample_data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_examples', 'data')


# Return sorted unique sample names available in the bundled data folder.
def list_sample_names():
    if not os.path.isdir(sample_data_folder):
        return []
    return sorted({os.path.splitext(f)[0] for f in os.listdir(sample_data_folder) if os.path.splitext(f)[0]})


# Find a bundled CSV sample by name; return its full path or None.
def get_sample_csv_path(name):
    path = os.path.join(sample_data_folder, f'{name}.csv')
    return path if os.path.exists(path) else None


# Find a bundled image/video sample by name; return its full path or None.
def get_sample_media_path(name):
    for extension in ('jpg', 'jpeg', 'png', 'gif', 'mp4', 'webm'):
        path = os.path.join(sample_data_folder, f'{name}.{extension}')
        if os.path.exists(path):
            return path
    return None


# Lookup table where any missing name resolves to itself as a string, so eval can
# parse [a,b,c] as ['a','b','c'] and {a:1} as {'a':1} without requiring quotes.
class bare_names(dict):
    def __missing__(self, key): return key

bare_names_namespace = bare_names({'true': True, 'false': False, 'null': None,
                                   'True': True, 'False': False, 'None': None})


# Read a CSV file, drop the header row, return chosen columns of floats. columns = '' for all.
def get_columns_from_file(path, columns):
    return get_columns_from_table(read(path)[1:], columns)


# Read a CSV file and return {header: column} using row 0 as keys.
def get_dict_from_file(path):
    return get_dict_from_table(read(path))


# Dispatcher for @-prefixed CLI arguments: @path:<path>[:cols|dict] or @sample:<name>[:cols|dict].
def at_dispatcher(at_string):
    prefix, _, rest = at_string.partition(':')
    if prefix == 'path':
        path, _, mode = rest.partition(':')
        if mode == 'dict': return get_dict_from_file(path)
        return get_columns_from_file(path, mode)
    if prefix == 'sample':
        name, _, mode = rest.partition(':')
        csv_path = get_sample_csv_path(name)
        if csv_path:
            if mode == 'dict': return get_dict_from_file(csv_path)
            return get_columns_from_file(csv_path, mode)
        media_path = get_sample_media_path(name)
        if media_path:
            return media_path
        print(f"plotext: unknown @sample:{name}", file=sys.stderr)
        sys.exit(1)
    print(f"plotext: @-syntax must start with @path: or @sample:, got '@{prefix}'", file=sys.stderr)
    sys.exit(1)


# Read piped stdin (comma- or whitespace-separated numbers). Used by `-`.
def read_input():
    rows = [line.replace(',', ' ').split() for line in sys.stdin.read().splitlines()]
    return get_columns_from_table([r for r in rows if r], '')


# Parse one CLI argument into a Python value (see docs/source/cli.rst for the rules).
def get_value_from_argument(argument):
    if not isinstance(argument, str): return argument
    if argument.startswith('@'): return at_dispatcher(argument[1:])
    if argument == '-': return read_input()
    try: return eval(argument, {'__builtins__': {}}, bare_names_namespace)
    except Exception: return argument
