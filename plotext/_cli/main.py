# Command-line entry point. See docs/source/cli.rst for the user-facing syntax.

import sys

from plotext._cli.arguments import group_by_method
from plotext._cli.run import find_method, run_methods
from plotext._cli.help import print_help, print_methods


# Exec arbitrary Python with `plt` and `plotext` pre-bound. Used by `plotext -c "<code>"`.
def run_c_code(code):
    import plotext as plotext_module
    try:
        exec(code, {'plt': plotext_module, 'plotext': plotext_module, '__name__': '__main__'})
    except Exception as error:
        print(f"plotext: {error}", file=sys.stderr)
        sys.exit(1)


# Print one method's docstring: styled prettydoc if registered, else raw __doc__.
# Used by `plotext --METHOD --doc`.
def print_method_doc(method_name):
    import plotext as plotext_module
    pretty = getattr(plotext_module.doc, method_name, None)
    if callable(pretty):
        pretty()
        return
    from plotext._signal.signal import signal_class
    method, _ = find_method(method_name, [signal_class, plotext_module.figure, plotext_module])
    if method is None:
        print(f"plotext: unknown method '{method_name}'", file=sys.stderr)
        sys.exit(1)
    print(method.__doc__ or f"(no docstring for --{method_name})")


# Command-line entry point. Recognises:
#   plotext                              -> print --help
#   plotext --help, -h                   -> print --help
#   plotext --doc                        -> open the interactive doc picker
#   plotext -c "<code>"                  -> exec arbitrary Python (plt is plotext)
#   plotext --METHOD ... --METHOD --help -> print one method's docstring
#   plotext --METHOD [args] ...          -> run the --METHOD chain
def main(arguments=None):
    # Drop sys.argv[0] (the program name); keep the rest as user-typed tokens.
    arguments = sys.argv[1:] if arguments is None else arguments

    # No args, or --help / -h: print the help page.
    if not arguments or arguments[0] in ('--help', '-h'):
        print_help()
        return

    # --doc: open the interactive doc picker grouped by section.
    if arguments[0] == '--doc':
        import plotext as plt
        plt.doc()
        return

    # -c "<code>": exec arbitrary Python instead of parsing the --METHOD chain.
    if arguments[0] == '-c':
        if len(arguments) < 2:
            print("plotext: -c needs a code string", file=sys.stderr)
            sys.exit(1)
        run_c_code(arguments[1])
        return

    # Otherwise: parse the chain of --METHODs and run them in order.
    methods = group_by_method(arguments)

    # Per-method doc shortcut: `plotext --signal --doc` prints signal's docstring.
    if len(methods) >= 2 and methods[-1][0] == 'doc':
        print_method_doc(methods[-2][0])
        return

    run_methods(methods)


if __name__ == '__main__':
    main()
