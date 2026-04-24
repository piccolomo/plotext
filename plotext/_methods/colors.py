# Color-related helpers backed by the C kernel

from plotext._kernel.clink import clink


# Get color name as UTF-8 string for a given color code
def get_color_name(color):
    return clink.get_color_name(color).decode("utf-8")
