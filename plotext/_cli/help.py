# --help and --methods output: styled headers, categorized method lists.

import textwrap

from plotext._cli.run import media_methods


# Return obj's sorted public callable attribute names.
def get_public_method_names(obj):
    return sorted(n for n in dir(obj) if not n.startswith('_') and callable(getattr(obj, n, None)))


# Print comma-separated items, wrapping at max_width chars, with the given indent.
def print_items_in_rows(items, max_width=80, indent="  "):
    text = ", ".join(items)
    print(textwrap.fill(text, width=max_width, initial_indent=indent,
                        subsequent_indent=indent, break_long_words=False))


# Print a section title in bold bright cyan.
def header(text):
    print(f"\033[1;96m{text}\033[0m")


# Print the top --help title: yellow text inside a bold cyan double-line frame, slightly indented.
def title(text):
    pad = 6
    width = len(text) + pad * 2
    frame  = "\033[94m"    # bright blue, no bold
    accent = "\033[1;93m"  # bold bright yellow
    reset  = "\033[0m"
    margin = "  "
    print()
    print(f"{margin}{frame}╔{'═' * width}╗{reset}")
    print(f"{margin}{frame}║{' ' * pad}{accent}{text}{frame}{' ' * pad}║{reset}")
    print(f"{margin}{frame}╚{'═' * width}╝{reset}")


# Subcategories of figure methods, by source mixin class.
drawing_methods = {'signal', 'bar', 'multiple_bar', 'stacked_bar', 'hist', 'box',
                   'candlestick', 'error', 'event', 'rectangle', 'polygon',
                   'segment', 'text', 'heatmap', 'confusion_matrix', 'line', 'draw'}
subplot_methods = {'subplots', 'subplot', 'plot_size', 'size_direction', 'size_policy',
                   'get_parent', 'get_master', 'get_terminal', 'get_position', 'get_size',
                   'get_log', 'log'}
rendering_methods = {'show', 'save', 'build'}
clear_methods = {'clear', 'cld', 'clear_size', 'clear_subplots', 'clear_data',
                 'clear_settings', 'clear_pixels', 'clear_styles'}
# Print the categorized list of CLI methods (for --methods).
def print_methods():
    import plotext as plotext_module
    from plotext._signal.signal import signal_class
    fig = plotext_module.figure
    figure_set = set(get_public_method_names(fig))
    module_set = set(get_public_method_names(plotext_module))
    drawing = sorted(figure_set & drawing_methods)
    subplots = sorted(figure_set & subplot_methods)
    rendering = sorted(figure_set & rendering_methods)
    clear = sorted(figure_set & clear_methods)
    media = sorted((figure_set | module_set) & media_methods)
    settings = sorted(figure_set - drawing_methods - subplot_methods - rendering_methods
                      - clear_methods - media_methods)
    signal_methods = get_public_method_names(signal_class)
    module_helpers = [n for n in get_public_method_names(plotext_module)
                      if n not in figure_set and n not in media_methods and n not in ('figure', 'terminal')]
    print("plotext: available CLI methods\n")
    header("drawing (signal-creating)")
    print_items_in_rows(drawing)
    print()
    header("media")
    print_items_in_rows(media)
    print()
    header("subplots")
    print_items_in_rows(subplots)
    print()
    header("settings")
    print_items_in_rows(settings)
    print()
    header("rendering")
    print_items_in_rows(rendering)
    print()
    header("clear")
    print_items_in_rows(clear)
    print()
    header("signal configuration")
    print_items_in_rows(signal_methods)
    print()
    header("module helpers")
    print_items_in_rows(module_helpers)
    print()


# Print the --help text.
def print_help():
    title("Plotext Command Line Interface")
    print()
    header("usage")
    print("  plotext --METHOD [arg ...]                          # one method")
    print("  plotext --METHOD [arg ...] --METHOD [arg ...] ...   # chained")
    print("  plotext -c \"<code>\"                                 # run arbitrary Python; plotext is already loaded as plt\n")
    print("  this CLI mirrors plotext's Python API: same methods, same arguments, only the calling syntax differs.\n")
    header("methods")
    print("  each --METHOD calls one plotext function.")
    print("  --methods           lists all available methods, grouped by category.")
    print("  --METHOD --help     shows one method's docstring.\n")
    header("arguments")
    print("  words that follow a --METHOD (until the next --METHOD) are its positional argument values")
    print("  or parameter=value pairs (for non-positional arguments).\n")
    print("  formats:")
    print("    [1,2,3] or [a,b,c]    → list (bare words become strings)")
    print("    {a:1} or {a:b}        → dict")
    print("    5 or 3.14             → number")
    print("    true / false          → boolean")
    print("    -                     → read from a pipe (e.g. echo '1 2 3' | plotext --signal -)")
    print("    anything else         → string\n")
    header("@path")
    print("  use as an argument value to load data from a file path on disk;")
    print("  each column of the CSV becomes one positional argument:")
    print("    @path:<path>          → load all columns")
    print("    @path:<path>:2        → pick only column 2 (1-indexed)")
    print("    @path:<path>:1,3      → pick columns 1 and 3")
    print("    @path:<path>:dict     → load as {header: column} (use with --candlestick)")
    print()
    print("  examples of paths:")
    print("    linux:    data.csv, ./data.csv, /home/user/data.csv, ~/Downloads/data.csv")
    print("    windows:  data.csv, .\\data.csv, C:\\Users\\you\\data.csv")
    print()
    header("@sample")
    print("  use as an argument value to load a bundled sample shipped with plotext:")
    print("    @sample:<name>        → CSV columns (or media file path for image samples)")
    print("    @sample:<name>:2      → pick column 2 from the sample CSV")
    print("    @sample:<name>:dict   → load sample CSV as {header: column}")
    print()
    from plotext._cli.load import list_sample_names, get_sample_csv_path
    print("  available names:")
    import os
    for n in list_sample_names():
        csv = get_sample_csv_path(n)
        if csv:
            kind, use = "csv", "use with --signal, --bar, --hist"
        else:
            from plotext._cli.load import get_sample_media_path
            media = get_sample_media_path(n)
            ext = os.path.splitext(media)[1].lstrip('.') if media else "?"
            kind, use = ext, "use with --image" if ext in ('jpg', 'jpeg', 'png') else f"use with --{ext}"
        print(f"    {n:14s}{kind:8s}→ {use}")
    print()
    header("examples")
    print("  plotext --sin --signal --lines --label sine --show               # data helper feeds signal")
    print("  plotext --noise --hist bins=20 --show                            # gaussian noise into a histogram")
    print("  plotext --signal [1,4,9,16,25] --lines --label squares --show    # inline list of numbers")
    print("  plotext --bar [a,b,c] [10,25,18] --title Counts --show           # bare words become strings")
    print("  plotext --signal @path:data.csv:2 --lines --show                 # column 2 of an on-disk CSV")
    print("  plotext --bar @sample:pizzas --title 'Pizza popularity' --show   # bundled CSV sample")
    print("  plotext --date axis=x --activate --candlestick @sample:stock:dict --draw --show   # OHLC with dates")
    print("  plotext --image @sample:puppy                                    # bundled image (no --show)")
    print("  plotext --image https://picsum.photos/400/300                    # URL (downloaded once, cached)")
    print("  plotext --gif @sample:shaq                                       # animated; press q to exit")
    print("  plotext --video https://youtu.be/dQw4w9WgXcQ                     # YouTube URLs work too")
    print("  plotext -c \"plt.plot(plt.sin()); plt.show()\"                     # arbitrary Python via -c\n")
