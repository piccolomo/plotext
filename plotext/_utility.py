import math
import hashlib, pickle

###############################################
##########    List Manipulation     ###########
###############################################

def unique(data): # removes duplicates from a list
    return list(set(list(data)))

###############################################
###########    List Creation     ##############
###############################################

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * math.pi * periods / (length - 1)
    phase =  math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(- d * el) for el in range(length)]

###############################################
#########   String Manipulation     ###########
###############################################

def pad(string, length = None): # pad a number with spaces before to reach length
    string = str(string)
    l = len(string)
    length = l if length is None else int(length)
    return string + ' ' * (length - l)

#is_string = lambda el: isinstance(el, str)


#### not sure yet

def hash(object):
    return hashlib.sha256(pickle.dumps(object)).hexdigest()

def hash_floats(data, decimals = 5):
    return hash([round(el, decimals) for el in data])