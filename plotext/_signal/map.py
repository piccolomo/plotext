# PointsMap: fixed-size (cols x rows) backing map used by points_class.squash

from plotext._kernel.clink import clink


# Points map: fixed-size grid used to squash points during rendering
class points_map:
    # Initialize the points map with given cols and rows
    def __init__(self, cols, rows):
        self._pointer = clink.points_map_new(cols, rows)
        self._cols = cols
        self._rows = rows

    # Destructor
    def __del__(self):
        clink.points_map_delete(self._pointer)

    # Clear the points map
    def clear(self):
        clink.points_map_clear(self._pointer)
        return self

    # Log the points map
    def log(self):
        clink.points_map_log(self._pointer)
        return self

    # Get the number of stored points
    def get_length(self):
        return clink.points_map_get_length(self._pointer)

    # Get number of columns
    def get_cols(self):
        return self._cols

    # Get number of rows
    def get_rows(self):
        return self._rows

    # String representation
    def __repr__(self):
        return f"Plotext PointsMap: Cols {self._cols}, Rows {self._rows}, Length {self.get_length()}"
