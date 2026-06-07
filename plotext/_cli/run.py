# Method lookup, per-method argument resolution, and the main dispatch loop.

import inspect
import sys

from plotext._cli.arguments import ListOfArguments
from plotext._cli.load import get_value_from_argument


# Module-level data helpers (--sin, --square, ...) whose result feeds the next signal-creating method.
methods_that_create_signals = {'signal', 'bar', 'multiple_bar', 'stacked_bar', 'hist', 'box',
                                'candlestick', 'error', 'event', 'rectangle', 'polygon',
                                'segment', 'text', 'heatmap', 'confusion_matrix', 'image'}

# Media methods that always use the module-level helper (direct print, no figure pipeline).
media_methods = {'image', 'gif', 'video'}


# Get the method named `name` from one owner, or None.
def get_method(name, owner):
    if owner is None: return None
    method = getattr(owner, name, None)
    return method if callable(method) else None


# Find the first owner that has the method; return (method, owner) or (None, None).
def find_method(name, owners):
    for owner in owners:
        method = get_method(name, owner)
        if method: return method, owner
    return None, None


# Run the method; print a clear error and exit if it raises.
def call_method(method, positional_arguments, non_positional_arguments):
    try:
        return method(*positional_arguments, **non_positional_arguments)
    except Exception as error:
        print(f"plotext: error in --{method.__name__}: {error}", file=sys.stderr)
        sys.exit(1)


# Pick the "key=value" pairs whose key matches a parameter of the method.
def get_non_positional_arguments(arguments, parameter_names):
    non_positional_arguments = {}
    for arg in arguments:
        if '=' not in arg: continue
        key, raw_value = arg.split('=', 1)
        if key in parameter_names: non_positional_arguments[key] = get_value_from_argument(raw_value)
    return non_positional_arguments


# Pick everything that isn't a recognised "key=value" pair, spreading ListOfArguments.
def get_positional_arguments(arguments, parameter_names):
    positional_arguments = []
    for arg in arguments:
        if '=' in arg:
            key, _ = arg.split('=', 1)
            if key in parameter_names: continue
        value = get_value_from_argument(arg)
        if isinstance(value, ListOfArguments): positional_arguments.extend(value)
        else: positional_arguments.append(value)
    return positional_arguments


# Build (positional_arguments, non_positional_arguments) for `method` from the raw CLI argument strings.
def get_method_arguments(method, arguments):
    try: parameter_names = set(inspect.signature(method).parameters)
    except (TypeError, ValueError): parameter_names = set()
    return get_positional_arguments(arguments, parameter_names), get_non_positional_arguments(arguments, parameter_names)


# Execute methods left-to-right, threading state across them.
def run_methods(methods):
    import plotext as plotext_module
    from plotext._signal.signal import signal_class
    fig = plotext_module.figure
    fig.clear()
    signal_to_draw = None
    active_object = None
    data_for_next_signal = None    # plotext-module helper output waiting to feed the next signal-creating method

    def draw_signal():
        nonlocal signal_to_draw
        if signal_to_draw is not None:
            fig.draw(signal_to_draw)
            signal_to_draw = None

    for method_name, arguments in methods:
        if method_name == 'draw':
            draw_signal()
            active_object = None
            data_for_next_signal = None
            continue
        # --show always renders the master figure (never a subplot's local .show()).
        if method_name == 'show':
            draw_signal()
            call_method(fig.show, *get_method_arguments(fig.show, arguments))
            continue
        # --subplot always navigates from the figure (never from a previously-selected
        # subplot's nested grid). Nested subplots aren't reachable through the chain;
        # use `plotext -c "<code>"` for those.
        if method_name == 'subplot':
            method, source = fig.subplot, fig
            positional_arguments, non_positional_arguments = get_method_arguments(method, arguments)
            result = call_method(method, positional_arguments, non_positional_arguments)
            active_object = result if result is not None else None
            signal_to_draw = None
            data_for_next_signal = None
            continue
        # Media methods: use the module-level helper and print directly.
        if method_name in media_methods:
            module_method = getattr(plotext_module, method_name, None)
            if module_method is None:
                print(f"plotext: unknown method '{method_name}'", file=sys.stderr)
                sys.exit(1)
            positional_arguments, non_positional_arguments = get_method_arguments(module_method, arguments)
            result = call_method(module_method, positional_arguments, non_positional_arguments)
            if hasattr(result, 'print'):
                result.print()
            continue
        method, source = find_method(method_name, [active_object, signal_to_draw, fig, plotext_module])
        if method is None:
            print(f"plotext: unknown method '{method_name}'", file=sys.stderr)
            sys.exit(1)
        positional_arguments, non_positional_arguments = get_method_arguments(method, arguments)
        # Absorb-next: data-helper output feeds the next signal-creating method.
        if (source is fig and method_name in methods_that_create_signals
                and data_for_next_signal is not None):
            positional_arguments = [data_for_next_signal] + positional_arguments
            data_for_next_signal = None
        result = call_method(method, positional_arguments, non_positional_arguments)
        # Update state based on result + which owner the method came from.
        if source is fig and isinstance(result, signal_class):
            draw_signal()
            signal_to_draw = result
            active_object = None
        elif source is plotext_module and result is not None and not isinstance(result, type(fig)):
            data_for_next_signal = result
        elif result is not None and result is not fig:
            active_object = result
