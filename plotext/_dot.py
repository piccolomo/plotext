from plotext._cimport import *


# Dot class representing a graphical dot with coordinates and an associated marker
class dot_class:
    # Initialize dot with a point or an existing pointer
    def __init__(self, point = point_class(), pointer = None):
        self._pointer = clink.dot_new(point._pointer) if pointer is None else pointer


    # Delete the underlying dot pointer
    def __del__(self):
        clink.dot_delete(self._pointer)


    # Get string representation of the dot
    def get_string(self):
        p = clink.dot_get_wstring(self._pointer)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string


    def __repr__(self):
        return self.get_string()


    # Print the dot's string representation and return self
    def log(self):
        print(self.get_string())
        return self
