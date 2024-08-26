import math

###############################################
###########    List Creation     ##############
###############################################

def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0): # sinusoidal data with given parameters
    f = 2 * math.pi * periods / (length - 1)
    phase =  math.pi * phase
    d = decay / length
    return [amplitude * math.sin(f * el + phase) * math.exp(- d * el) for el in range(length)]