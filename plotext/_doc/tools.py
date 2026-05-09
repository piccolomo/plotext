# Docs tools: exposes short aliases for the prettydoc API and registers all shared data types

from plotext.prettydoc import docs


# Initialize docs
pd = docs(colorless = 1)
add, alias, doc = pd.add_function, pd.add_alias, pd.add_doc
par, spec, past = pd.add_parameter, pd.add_parameter_spec, pd.add_past_parameter
out, past_out = pd.add_output, pd.add_past_output
add_type = pd.register_type
type = pd.type


# Simple Data Types
add_type("float", "A floating-point number")
add_type("floats", "A list of floating-point numbers")
add_type("int", "An integer")
add_type("bool", "A boolean value")
add_type("string", "A text string")
add_type("strings", "A list of strings")
add_type("tuple", "A tuple of values")

# Internal data types
add_type("plot", "A plot object")
add_type("signal", "A plotext signal object")
add_type("marker", "A plotext marker object")
add_type("text", "A plotext text object")
add_type("terminal", "A plotext terminal object")
add_type("pixel", "A plotext pixel object")
add_type("colorize", "A plotext colorize object")
add_type("matrix", "A plotext matrix object")
add_type("couple", "A two-value tuple or list")
add_type("function", "A Python callable, or a list of callables")
add_type("docs", "A plotext.prettydoc docs manager object")

# Advanced or long explanation data types
add_type("axis", "'x' or 'y' (0 or 1 in short)")
add_type("side", "'lower' or 'upper' for x axis, 'left' or 'right' for y axis; 0 or 1 in short")

add_type("axis_multiple", type.axis + "; a list containing both axes is also allowed")
add_type("side_multiple", type.side + "; a list of both sides is also allowed")

add_type("xside", "Either 'lower' or 'upper'; 0 or 1 in short")
add_type("yside", "Either 'left' or 'right'; 0 or 1 in short")

add_type("label", "A string or a plotext.colorize object")
add_type("scale", "'linear' or 'log'")
add_type("alignment", "'center' or 'edge'")
add_type("direction", "1 or -1")
add_type("line_method", "'simple' or 'full'; 0 or 1 in short")
add_type("orientation", "'vertical' / 'v' or 'horizontal' / 'h'")
add_type("alignment_h", "'left', 'center' or 'right' (short 'l', 'c', 'r'; -1, 0, 1 in integer form)")
add_type("alignment_v", "'top', 'center' or 'bottom' (short 't', 'c', 'b'; -1, 0, 1 in integer form)")
add_type("alignment_text", "for horizontal text: 'left', 'center' or 'right' (short 'l', 'c', 'r'); for vertical text: 'top', 'center' or 'bottom' (short 't', 'c', 'b'); -1, 0 or 1 in integer form")
add_type("size_policy", "'minimum' or 'maximum'")
add_type("color_pair", "A list of two color strings")
add_type("ohlc_dict", "A dict with keys 'date', 'open', 'close', 'high', 'low'; each holding a sequence of values (date may be strings, timestamps, or datetime objects; the others are numeric)")
add_type("matrix_insertable", "A plotext.matrix, plotext.colorize, or raw string")
add_type("style", "A style code string")
add_type("date", "Dates may be provided as string, timestamp (float), or a Python/Pandas datetime object.")
add_type("value", "A numeric value or date; " + type.date)
add_type("data_single", "A sequence of numeric values or dates; " + type.date)
add_type("data_multiple", "One or two sequences of numeric values or dates; " + type.date)
add_type("data_bar", "One, two, or three sequences of numeric values or dates: one sets the bar heights, two set the bar coordinates and heights, three set the bar coordinates, baselines and heights. " + type.date)
add_type("data_multiple_bar", "One or two arguments: a list of height-sequences, or x and a list of height-sequences. " + type.date)
add_type("marker_par_draw", "A single character, a character code from plotext.markers(), an HD marker code ('hd', 'fhd', 'braille'), a plotext.marker() object, or a list of any of these (one per point)")
add_type("marker_par", "A single character, a character code from plotext.markers(), or an HD marker code ('hd', 'fhd', 'braille')")
add_type("pixel_par", "A plotext.pixel object, a foreground string or integer, or a tuple specifying (foreground, background, style)")
add_type("color", "A string color code, an integer (lower than 256), or a tuple of 3 integers (each lower than 256)")

# Time related
add_type("date_form", "Date format string using standard Python strftime directives")

add_type("date_single_time_par", "A date or time value: string, Python datetime object, float timestamp, or pandas Timestamp/DatetimeIndex")
add_type("date_time_par", type.date_single_time_par + " (a list thereof)")

add_type("convert_output_par", "'string', 'timestamp', or 'datetime'")
add_type("convert_output", "A string, Python datetime object, or float (a list thereof)")


# Messages
add_type("markers", "Available marker codes: 'hd', 'fhd', 'braille' (in addition to any single character).")
add_type("colors", "Use plotext.colors() for available color codes.")
add_type("styles", "Use plotext.styles() for available style codes.")
add_type("limits", "If not provided (None value), the limit is calculated automatically.")
add_type("dates_accepted", "Dates (as string, timestamp, or datetime) are allowed if the axis supports them via plotext.date().")
add_type("line_styles", "Available line styles: 'default' or 'double'.")
add_type("axis_styles", "Available axis styles: 'default', 'double', 'dotted', or 'rounded'.")
