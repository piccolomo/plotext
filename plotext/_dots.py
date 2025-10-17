from plotext._clink import clink


class dots_class:
    def __init__(self, length):
        self._pointer = clink.dots_new(length)

    def __del__(self):
        clink.dots_delete(self._pointer)

    # Add a point to dots
    def add(self, signal, map):
        clink.dots_add(self._pointer, signal._pointer, map._pointer)

    # Log dots state
    def log(self):
        clink.dots_log(self._pointer)

    # Log dots state
    def log_map(self):
        clink.dots_log_map(self._pointer)


    # Add offset to all points
    def add_offset(self, dx, dy):
        clink.dots_add_offset(self._pointer, dx, dy)


    # Fix background pixel for dots
    def fix_background(self, pixel):
        return clink.dots_fix_background(self._pointer, pixel._pointer)

