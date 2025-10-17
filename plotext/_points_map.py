from plotext._clink import clink

class points_map:
    def __init__(self, cols, rows):
        self._pointer = clink.points_map_new(cols, rows)

    def __del__(self):
        clink.points_map_delete(self._pointer)

    def clear(self):
        clink.points_map_clear(self._pointer)
        return self

    def log(self):
        clink.points_map_log(self._pointer)
        return self

    def get_length(self):
        return clink.points_map_get_length(self._pointer)