# Grid: fixed-size (cols x rows) backing grid used by points_class.squash for fast (col, row) → point-index lookup

from plotext._kernel.clink import clink


# Grid: fixed-size 2D grid mapping (col, row) → index in a points collection
class grid:
    # Initialize the grid with given cols and rows
    def __init__(self, cols, rows):
        self._pointer = clink.grid_new(cols, rows)
        self._cols = cols
        self._rows = rows

    # Destructor
    def __del__(self):
        clink.grid_delete(self._pointer)

    # Clear the grid
    def clear(self):
        clink.grid_clear(self._pointer)
        return self

    # Log the grid
    def log(self):
        clink.grid_log(self._pointer)
        return self

    # Get the number of stored points
    def length(self):
        return clink.grid_get_length(self._pointer)

    # Get number of columns
    def get_cols(self):
        return self._cols

    # Get number of rows
    def get_rows(self):
        return self._rows

    # String representation
    def __repr__(self):
        return f"PlotextGrid(cols {self._cols}, rows {self._rows}, length {self.length()})"
