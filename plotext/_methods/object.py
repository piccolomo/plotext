# Object utilities: hashing, type checks, and attribute handling

from copy import copy
import hashlib
import pickle
import inspect


# Generate SHA-256 hash of a Python object
def hash(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()


# Hash a list of floats after rounding to the given number of decimals
def hash_floats(data, decimals = 5):
    return hash([round(el, decimals) for el in data])


# Check if object is list-like
def is_list_like(obj):
    return (
        hasattr(obj, "__iter__")
        and hasattr(obj, "__len__")
        and hasattr(obj, "__getitem__")
        and not isinstance(obj, (str, bytes))
        and not callable(obj))


# Check if object is numerical type
def is_numerical(x):
    return isinstance(x, (int, float, bool))


# Check if object is an RGB triplet (tuple or list of length 3)
def is_rgb(obj):
    return isinstance(obj, (tuple, list)) and len(obj) == 3


# Set nested attribute on an object, creating intermediate attributes if missing
def set_attribute(obj, attribute, value):
    value_copy = copy(value)

    # Handle methods by wrapping execution
    if inspect.ismethod(value):
        def value_copy():
            getattr(value.__self__, value.__name__)()

    attributes = attribute.split('.')

    # Create intermediate attributes if missing
    for atr in attributes[:-1]:
        if not hasattr(obj, atr):
            setattr(obj, atr, type('', (), {})())
        obj = getattr(obj, atr)

    # Set final attribute
    setattr(obj, attributes[-1], value_copy)

    return obj
