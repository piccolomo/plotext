from plotext._clink import clink, wstring


class points_class:
    # Initialize points with new or existing pointer
    def __init__(self, size):
        self._pointer = clink.points_new(size)


    # Clean up pointer on deletion
    def __del__(self): clink.points_delete(self._pointer); self._pointer = None

    # Clear all points 
    def log(self): clink.points_log(self._pointer)

    def get_length(self): return clink.points_get_length(self._pointer)
    def get_capacity(self): return clink.points_get_capacity(self._pointer)

