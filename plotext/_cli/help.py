# --help output: styled headers and categorized usage hints.

import textwrap

from plotext._cli.run import media_methods
from plotext._primitives.colorize import colorize
from plotext.prettydoc._defaults.pixels import default_pixels


# Return obj's sorted public callable attribute names.
def get_public_method_names(obj):
    return sorted(n for n in dir(obj) if not n.startswith('_') and callable(getattr(obj, n, None)))


# Print comma-separated items, wrapping at max_width chars, with the given indent.
def print_items_in_rows(items, max_width = 80, indent = "  "):
    text = ", ".join(items)
    print(textwrap.fill(text, width = max_width, initial_indent = indent,
                        subsequent_indent = indent, break_long_words = False))


# Print a section header, styled like the documentation menu sections, with one blank line above.
def header(text):
    print()
    print(colorize(text, pixel = default_pixels["section"]))


# Print the top title, styled like the documentation menu title, with no blank line above.
def title(text):
    print(colorize(text, pixel = default_pixels["title"]))


# Sections of the documentation menu whose entries the CLI cannot invoke.
sections_not_reachable = {'primitives', 'pixel', 'colorize', 'matrix', 'text', 'marker', 'point',
                          'plotext components', 'file', 'terminal', 'prettydoc', 'prettydoc registry'}

# Menu sections joined into another group in the CLI listing.
sections_joined = {'simulate': 'tools'}


# Print the list of CLI methods, grouped and ordered as the documentation menu sections (for --methods).
def print_methods():
    import plotext as plotext_module
    from plotext._signal.signal import signal_class
    from plotext._doc.doc import pd
    fig = plotext_module.figure
    reachable = (set(get_public_method_names(fig))
                 | set(get_public_method_names(plotext_module))
                 | set(get_public_method_names(signal_class))
                 | set(get_public_method_names(fig.clear))
                 | set(get_public_method_names(fig.ruler('x')))
                 | set(get_public_method_names(fig.date('x'))))
    reachable -= {'figure', 'terminal', 'file', 'prettydoc', 'doc', 'matplotlib'}
    title("Plotext CLI Methods")
    groups = {}
    for section_name, functions in pd._get_section():
        if section_name in sections_not_reachable:
            continue
        names = {fn._get_listed_name() for fn in functions
                 if fn._get_listed_name() in reachable and not isinstance(fn._function[0], type)}
        target = sections_joined.get(section_name, section_name)
        groups.setdefault(target, set()).update(names)
    for section_name, names in groups.items():
        if names:
            header(section_name)
            print_items_in_rows(sorted(names))
    print()


# Print the --help text.
# The bundled sample names, each with its kind and the methods it suits, one per line.
def get_sample_names_text():
    import os
    from plotext._methods.sequence import sample, sample_names
    lines = []
    for name in sample_names():
        extension = os.path.splitext(sample(name))[1].lstrip('.')
        if extension == 'csv':
            kind, use = "csv", "use with --signal, --bar, --hist"
        else:
            kind, use = extension, "use with --image" if extension in ('jpg', 'jpeg', 'png') else f"use with --{extension}"
        lines.append(f"    {name:14s}{kind:8s}\u2192 {use}")
    return "\n".join(lines)


def print_help():
    title("Plotext Command Line Interface")

    header("usage")
    print("  plotext --figure --METHOD [arg ...]                          # one figure method\n"
          "  plotext --figure --METHOD [arg ...] --METHOD [arg ...] ...   # chained\n"
          "  plotext -c \"<code>\"                                          # run arbitrary Python code\n"
          "  this CLI mirrors plotext's Python API: same methods, same arguments, only the calling syntax differs.")

    header("methods")
    print("  each --METHOD calls one plotext function.\n"
          "  --doc               opens the interactive documentation menu (sections + per-method docstrings).\n"
          "  --METHOD --doc      shows one method's docstring.\n"
          "  --methods           prints the categorized list of available methods.")

    header("arguments")
    print("  words that follow a --METHOD (until the next --METHOD) are its positional argument values\n"
          "  or parameter=value pairs (for named arguments).\n"
          "  formats:\n"
          "    [1,2,3] or [a,b,c]    \u2192 list (bare words become strings)\n"
          "    {a:1} or {a:b}        \u2192 dict\n"
          "    5 or 3.14             \u2192 number\n"
          "    true / false          \u2192 boolean\n"
          "    -                     \u2192 read from a pipe (e.g. echo '1 2 3' | plotext --figure --signal - --draw --show)\n"
          "    anything else         \u2192 string")

    header("@path")
    print("  use as an argument value to load data from a file path on disk;\n"
          "  each column of the CSV becomes one positional argument:\n"
          "    @path:<path>          \u2192 load all columns\n"
          "    @path:<path>:2        \u2192 pick only column 2 (1-indexed)\n"
          "    @path:<path>:1,3      \u2192 pick columns 1 and 3\n"
          "    @path:<path>:dict     \u2192 load as {header: column} (use with --candlestick)\n"
          "\n"
          "  examples of paths:\n"
          "    linux:    data.csv, ./data.csv, /home/user/data.csv, ~/Downloads/data.csv\n"
          "    windows:  data.csv, .\\data.csv, C:\\Users\\you\\data.csv")

    header("@sample")
    print("  use as an argument value to load a bundled sample shipped with plotext:\n"
          "    @sample:<name>        \u2192 CSV columns (or media file path for image samples)\n"
          "    @sample:<name>:2      \u2192 pick column 2 from the sample CSV\n"
          "    @sample:<name>:dict   \u2192 load sample CSV as {header: column}\n"
          "\n"
          "  available names:\n" + get_sample_names_text())

    header("examples")
    print("  plotext --figure --signal [1,4,9,16,25] --lines --label squares --draw --show                       # inline list of numbers\n"
          "  plotext --figure --signal @path:data.csv:2 --lines --draw --show                                    # column 2 of an on-disk CSV\n"
          "  plotext --figure --sin --signal --lines --label sine --draw --show                                  # data helper feeds signal\n"
          "  plotext --figure --bar [a,b,c] [10,25,18] --draw --title Counts --show                              # bare words become strings\n"
          "  plotext --figure --bar @sample:pizzas --draw --title 'Pizza popularity' --show                      # bundled CSV sample\n"
          "  plotext --figure --noise --hist bins=20 --draw --show                                               # gaussian noise into a histogram\n"
          "  plotext --figure --date axis=x --activate --candlestick @sample:stock:dict --draw --show            # OHLC with dates\n"
          "  plotext --image @sample:puppy                                                                       # bundled image (no --show)\n"
          "  plotext --image https://picsum.photos/400/300                                                       # URL (downloaded once, cached)\n"
          "  plotext --gif @sample:shaq seconds=3                                                                # animated; stops after 3s, or on q\n"
          "  plotext --video https://youtu.be/dQw4w9WgXcQ                                                        # YouTube URLs work too\n"
          "  plotext --figure --ruler axis=y --lim -1 1 --sin --signal --draw --show                             # y axis limits\n"
          "  plotext --figure --theme dark --sin --signal --draw --show                                          # themed plot\n"
          "  plotext -c \"import plotext as plt; fig = plt.figure; fig.draw(fig.signal(plt.sin())); fig.show()\"   # arbitrary Python via -c\n")
