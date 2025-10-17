from plotext._clink import clink, wstring
from plotext._marker import marker as marker_class


# Point class representing a graphical point with coordinates and an associated marker
class point_class:
    # Initialize point with coordinates, marker, or existing pointer
    def __init__(self, x = 0, y = 0, marker = None, pointer = None):
        marker = marker_class() if marker is None else marker
        self._pointer = clink.point_new(x, y, marker._pointer) if pointer is None else pointer

    # Delete the point pointer on object destruction
    def __del__(self):
        clink.point_delete(self._pointer)

    # # Set fill properties for the point
    # def set_fill(self, bool = 0, x = 0, y = 0):
    #     print(x, y)
    #     clink.point_set_fill(self._pointer, bool, x, y)
    #     return self 

    # Get column (x-coordinate) 
    def get_x(self):
        return clink.point_get_x(self._pointer) 

    # Get row (y-coordinate)
    def get_y(self):
        return clink.point_get_y(self._pointer) 

    def get_marker(self):
        return marker_class(_pointer = point_get_marker(self._pointer))


    # Get column (x-coordinate) 
    def get_col(self):
        return clink.point_get_col(self._pointer) 

    # Get row (y-coordinate)
    def get_row(self):
        return clink.point_get_row(self._pointer) 

    # Get string representation of the point
    def get_string(self, fill):
        p = clink.point_get_wstring(self._pointer, fill)
        string = wstring.from_buffer(p).value
        clink.wstring_delete(p)
        return string

    # Get marker object associated with this point
    def get_marker(self):
        return marker_class(_pointer = clink.point_get_marker(self._pointer))

    def __repr__(self):
        return self.get_string(1)

    # Print the point string and return self
    def log(self, fill = True):
        print(self.get_string(fill))
        return self

