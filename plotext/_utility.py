import math
import hashlib, pickle
from copy import copy
from ._link import rescale_value

###############################################
##########    List Manipulation     ###########
###############################################

def unique(data): # removes duplicates from a list
    return list(set(list(data)))

def repeat(data, length): 
    original = data.copy()
    make_copy = lambda: [copy(el) for el in original]
    l = (length + 1) // len(data);  L = range(l)
    [data.extend(make_copy()) for i in L]
    return data[ : length]

def replace_none(data, alternative): # replace None elements in data with correspondent in alternative
    return [d if d is not None else a for (d, a) in zip(data, alternative)]


def log(data): # it apply log function to the data
    return [math.log10(el) for el in data] #if isinstance(data, list) else math.log10(data)

def power10(data): # it reverse the effect of log function to the data
    return [10 ** el for el in data]

def apply_scale(data, scale): 
    return log(data) if scale == "log" else data

def reverse_scale(data, scale):
    return power10(data) if scale == "log" else data

###############################################
###########    List Creation     ##############
###############################################

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * math.pi * periods / (length - 1)
    phase =  math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(- d * el) for el in range(length)]

def linspace(lower, upper, length = 10): # it returns a lists of numbers from lower to upper, with given length, equally distanced
    slope = (upper - lower) / (length - 1) if length > 1 else 0
    return [lower + x * slope for x in range(length)]

def rescale(value, minimum, maximum, bins, delta):
    #[value, minimum, maximum] = apply_scale([value, minimum, maximum], scale)
    return int(rescale_value(value, minimum, maximum, bins, delta))

###############################################
#########   String Manipulation     ###########
###############################################

space = ' '

def pad(string, length = None): # pad a number with spaces before to reach length
    string = str(string)
    l = len(string)
    length = l if length is None else int(length)
    return string + ' ' * (length - l)

def only_spaces(string): # it returns True if string is made of only empty spaces or is None or ''
    return string == len(string) * space

###############################################
##############   Hashing     ##################
###############################################

def hash(object):
    return hashlib.sha256(pickle.dumps(object)).hexdigest()

def hash_floats(data, decimals = 5):
    return hash([round(el, decimals) for el in data])
