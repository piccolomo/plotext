from copy import copy
import math, inspect, hashlib, pickle, sys


def hash(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

# Hash list of floats after rounding to specified decimals

def hash_floats(data, decimals = 5):
    return object_methods.hash([round(el, decimals) for el in data])

# Check if object is numerical type

def is_numerical(x):
    return isinstance(x, (int, float, bool))

# Set nested attribute on an object, creating intermediate attributes if missing

def set_attribute(obj, attribute, value):
    value_copy = copy(value)
    if inspect.ismethod(value):
        def value_copy():
            getattr(value.__self__, value.__name__)()
    attributes = attribute.split('.')
    for atr in attributes[:-1]:
        if not hasattr(obj, atr):
            setattr(obj, atr, type('', (), {})())
        obj = getattr(obj, atr)
    setattr(obj, attributes[-1], value_copy)
    return obj