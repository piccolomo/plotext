# Everything about the words of the sentence: which ones name a method, and what value each one carries.

import os
import sys

from plotext._methods.file import csv_read
from plotext._methods.sequence import transpose
from plotext._methods.string import note


# A list whose items are meant to become separate arguments in the next function call.
class ListOfArguments(list):
    pass


# Return text as a float, or unchanged if it isn't numeric.
def to_float(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return text


# Translate a column selection like '1,3' into a list of ints.
def get_columns_from_string(columns_string):
    return [int(column) for column in columns_string.split(',')]


# Pick the selected columns, counted from 1, from the matrix of columns.
def select_columns(matrix, columns):
    return [matrix[column - 1] for column in columns]


# Transpose a csv table into its columns, each a list of floats.
def get_data_from_table(table):
    return [[to_float(value) for value in column] for column in transpose(table)]


# Use the first element of each column as the key for the rest.
def columns_to_dict(columns):
    return {column[0]: column[1:] for column in columns}


# Transpose a csv table to columns of floats, then use row 0 as keys.
def get_dict_from_table(table):
    return columns_to_dict(get_data_from_table(table))


# One column enters the next call directly; several enter as separate arguments.
def get_arguments_from_matrix(matrix):
    return matrix[0] if len(matrix) == 1 else ListOfArguments(matrix)


# Lookup table where any missing name resolves to itself as a string, so eval can
# read [a,b,c] as ['a','b','c'] and {a:1} as {'a':1} without requiring quotes.
class bare_names(dict):
    def __missing__(self, key): return key

bare_names_namespace = bare_names({'true': True, 'false': False, 'null': None,
                                   'True': True, 'False': False, 'None': None})


# Read a whole CSV file, returning the chosen columns of floats; no row is dropped, so a file carrying a header needs it taken off first, or read with the dict ending. columns_string = '' for all.
def get_columns_from_file(path, columns_string):
    matrix = get_data_from_table(csv_read(path))
    if columns_string:
        matrix = select_columns(matrix, get_columns_from_string(columns_string))
    return get_arguments_from_matrix(matrix)


# Read a CSV file and return {header: column} using row 0 as keys.
def get_dict_from_file(path):
    return get_dict_from_table(csv_read(path))


# Split '<path>[:columns|dict]' from the right, so a ':' inside a url stays in the path.
def get_path_and_ending(at_path_ending):
    path, _, ending = at_path_ending.rpartition(':')
    if path and (ending == 'dict' or ending.replace(',', '').isdigit()):
        return path, ending
    return at_path_ending, ''


# Turns an @ word into its value: @path:<path>[:ending] or @sample:<name>[:ending].
def get_value_from_at_word(at_word):
    prefix, _, at_path_ending = at_word.partition(':')
    if prefix == 'path':
        path, ending = get_path_and_ending(at_path_ending)
        if ending == 'dict': return get_dict_from_file(path)
        return get_columns_from_file(path, ending)
    if prefix == 'sample':
        name, ending = get_path_and_ending(at_path_ending)
        from plotext._methods.sequence import sample
        try:
            path = sample(name)
        except ValueError:
            note("plotext", f"unknown @sample:{name}", "error")
            sys.exit(1)
        if path.endswith('.csv'):
            if ending == 'dict': return get_dict_from_file(path)
            return get_columns_from_file(path, ending)
        return path
    note("plotext", f"@-syntax must start with @path: or @sample:, got '@{prefix}'", "error")
    sys.exit(1)


# Read piped stdin (comma- or whitespace-separated numbers). Used by `-`.
def read_input():
    rows = [line.replace(',', ' ').split() for line in sys.stdin.read().splitlines()]
    rows = [r for r in rows if r]
    # a single row of numbers is one data series, not one column per number
    rows = [[value] for value in rows[0]] if len(rows) == 1 else rows
    return get_arguments_from_matrix(get_data_from_table(rows))


# Turns one word into its value (see docs/source/cli.rst for the rules).
def get_value_from_word(word):
    if not isinstance(word, str): return word
    if word.startswith('@'): return get_value_from_at_word(word[1:])
    if word == '-': return read_input()
    try: return eval(word, {'__builtins__': {}}, bare_names_namespace)
    except Exception: return word


# True for a word naming a method, like '--signal'.
def is_method_word(word):
    return word.startswith('--')


# The method name inside a method word: the dashes dropped, hyphens turned to underscores.
def get_method_name(word):
    return word[2:].replace('-', '_')


# Divide the sentence into methods_words, one group per method: each starts at its --method word and holds the words that follow it; the words before any method are dropped.
def split_sentence_by_method(sentence):
    methods_words = []
    for word in sentence:
        if is_method_word(word):
            methods_words.append([word])
        elif methods_words:
            methods_words[-1].append(word)
    return methods_words