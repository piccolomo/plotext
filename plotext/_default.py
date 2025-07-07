from plotext._pixel import pixel_class as pixel


# Default terminal size in characters (width, height)
default_terminal_width = 211 * 2 // 3
default_terminal_height = 53 * 2 // 3
default_terminal_prompt_height = 3


# Frequencies for grid lines on axes
default_xfrequency = 7
default_yfrequency = 5


# Default pixel colors for plot elements

default_labels_foreground = "blue+"
default_labels_background = "white"

default_axes_foreground = "black"
default_axes_background = "white"

default_ruler_foreground = "blue"
default_ruler_background = "white"

default_canvas_foreground = "default"
default_canvas_background = "white"

default_lines_foreground = "orange"
default_lines_background = "white"

default_legend_foreground = "black"
default_legend_background = "white"


# Default pixels

default_labels_pixel = pixel(default_labels_foreground, default_labels_background)
default_axis_pixel = pixel(default_axes_foreground, default_axes_background)
default_ruler_pixel = pixel(default_ruler_foreground, default_ruler_background)
default_canvas_pixel = pixel(default_canvas_foreground, default_canvas_background)
default_lines_pixel = pixel(default_lines_foreground, default_lines_background)
default_legend_pixel = pixel(default_legend_foreground, default_legend_background)


# Subplots default size direction
default_size_direction = 1
