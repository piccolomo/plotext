# Command-line entry point. See docs/source/cli.rst for the user-facing syntax.

import sys

from plotext._cli.words import split_sentence_by_method, get_method_name
from plotext._cli.run import get_method_and_owner_tuple_from_name, run_methods
from plotext._cli.help import print_help, print_methods
from plotext._methods.string import note


# Run the given Python code. Used by `plotext -c "<code>"`.
def run_python_code(code):
    try:
        exec(code, {'__name__': '__main__'})
    except Exception as error:
        note("plotext", f"{error}", "error")
        sys.exit(1)


# Prints the docstring for 'plotext --method --doc'. The normal route would run the method first with no arguments, causing a crash.
def print_method_doc(method_name):
    import plotext as plotext_module
    pretty = getattr(plotext_module.doc, method_name, None)
    if callable(pretty):
        pretty()
        return
    from plotext._signal.signal import signal_class
    method, _ = get_method_and_owner_tuple_from_name(method_name, [signal_class, plotext_module.figure, plotext_module])
    if method is None:
        note("plotext", f"unknown method '{method_name}'", "error")
        sys.exit(1)
    print(method.__doc__ or f"(no docstring for --{method_name})")


# Command-line entry point: routes the typed sentence to the help page, the documentation menu, the methods list, the -c code runner, or the methods.
def main(sentence = None):
    # Drop sys.argv[0] (the program name); keep the rest, the words typed after plotext.
    sentence = sys.argv[1:] if sentence is None else sentence

    # Nothing typed, or --help / -h: print the help page.
    if not sentence or sentence[0] in ('--help', '-h'):
        print_help()
        return

    # --doc: open the interactive documentation menu.
    if sentence[0] == '--doc':
        import plotext as plt
        plt.doc()
        return

    # --methods: print the categorized list of CLI methods.
    if sentence[0] == '--methods':
        print_methods()
        return

    # -c "<code>": run the given Python code instead of the methods.
    if sentence[0] == '-c':
        if len(sentence) < 2:
            note("plotext", "-c needs a code string", "error")
            sys.exit(1)
        run_python_code(sentence[1])
        return

    # Otherwise: divide the sentence by --method and run the methods in order.
    methods_words = split_sentence_by_method(sentence)

    # Per-method doc shortcut: `plotext --signal --doc` prints signal's docstring.
    if len(methods_words) >= 2 and get_method_name(methods_words[-1][0]) == 'doc':
        print_method_doc(get_method_name(methods_words[-2][0]))
        return

    run_methods(methods_words)


if __name__ == '__main__':
    main()
