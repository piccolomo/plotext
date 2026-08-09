# Object utilities: hashing and type checks

import hashlib
import pickle


# The sha256 hash of any Python value, as a text of 64 characters; the pickle protocol is named, since the default one changes with the Python version and would give the same value two different hashes
def hash(value):
    return hashlib.sha256(pickle.dumps(value, protocol = 4)).hexdigest()


# The hash of a list of floats, each rounded to the given number of decimals first.
def hash_floats(data, decimals = 5):
    return hash([round(el, decimals) for el in data])


# True when the value behaves like a list, as [1, 2] does and "ab" does not.
def is_list_like(value):
    return (
        hasattr(value, "__iter__")
        and hasattr(value, "__len__")
        and hasattr(value, "__getitem__")
        and not isinstance(value, (str, bytes))
        and not callable(value))


# True when the value is a number, integers and booleans included.
def is_numerical(value):
    return isinstance(value, (int, float, bool))


# True when the value is a triplet of red, green and blue, as (255, 0, 0).
def is_rgb(value):
    return isinstance(value, (tuple, list)) and len(value) == 3
