# Takes the (method, arguments) tuples built by words.py and runs them in order: finds each method, turns its arguments into values, calls it.

import inspect
import sys

from plotext._cli.words import get_method_name, ListOfArguments, get_value_from_word
from plotext._methods.string import note


# Module-level data helpers (--sin, --square, ...) whose results accumulate, in order, and feed the next signal-creating method.
methods_that_create_signals = ['signal', 'bar', 'hist', 'box',
                               'candlestick', 'error', 'event', 'rectangle', 'polygon',
                               'segment', 'text', 'heatmap', 'cmatrix', 'image']

# Media methods that always use the module-level helper (direct print, no figure pipeline).
media_methods = ['image', 'gif', 'video']


# The method called method_name inside owner, or None when there is none.
def get_method_in_owner_from_name(method_name, owner):
    if owner is None: return None
    method = getattr(owner, method_name, None)
    return method if callable(method) else None


# The (method, owner) tuple of the first owner holding a method called method_name, the owners tried in order; (None, None) when no owner has it.
def get_method_and_owner_tuple_from_name(method_name, owners):
    for owner in owners:
        method = get_method_in_owner_from_name(method_name, owner)
        if method: return method, owner
    return None, None


# Calls the method with the values of its arguments, the leading values placed before them, printing a clear error and stopping the program when the call fails: hist() with ['1', '2', '3', 'bins=20'] calls hist(1, 2, 3, bins = 20).
def call_method_from_arguments(method, arguments, leading_values = []):
    named_parameters = get_named_parameters_from_method(method)
    positional_arguments = leading_values + get_positional_arguments(arguments, named_parameters)
    named_arguments_dict = get_named_arguments_dict(arguments, named_parameters)
    try:
        return method(*positional_arguments, **named_arguments_dict)
    except Exception as error:
        note("plotext", f"error in --{getattr(method, '__name__', type(method).__name__)}: {error}", "error")
        sys.exit(1)


# True when the argument contains an equal symbol: 'bins=20' gives true, '1' gives false.
def contains_equal_symbol(argument):
    return '=' in argument


# Splits the argument at its first equal symbol, into the named parameter before it and the value text after it: 'bins=20' gives 'bins' and '20'.
def split_argument_into_named_parameter_and_value(argument):
    named_parameter, _, value_text = argument.partition('=')
    return named_parameter, value_text


# True when the argument holds an equal symbol and the parameter name before it is one the method accepts: for hist(), 'bins=20' gives true, 'wrong=20' false.
def argument_contains_named_parameter(argument, named_parameters):
    if not contains_equal_symbol(argument):
        return False
    named_parameter, _ = split_argument_into_named_parameter_and_value(argument)
    return named_parameter in named_parameters


# Splits the argument, then turns the value text into its real value: 'bins=20' gives 'bins' and the number 20.
def get_name_and_value_tuple(argument):
    named_parameter, value_text = split_argument_into_named_parameter_and_value(argument)
    return named_parameter, get_value_from_word(value_text)


# Keeps the arguments naming a parameter of the method, and collects their name and value pairs: ['1', 'bins=20'] gives {'bins': 20}.
def get_named_arguments_dict(arguments, named_parameters):
    return dict(get_name_and_value_tuple(argument) for argument in arguments
                if argument_contains_named_parameter(argument, named_parameters))


# Keeps only the arguments that are not named parameters of the method: ['1', '2', 'bins=20'] gives ['1', '2'].
def get_arguments_not_in_named_parameters(arguments, named_parameters):
    return [argument for argument in arguments if not argument_contains_named_parameter(argument, named_parameters)]


# Turns each argument into its value, a file content entering as one value per column: ['1', '2'] gives [1, 2].
def get_values_from_arguments(arguments):
    values = []
    for word in arguments:
        value = get_value_from_word(word)
        values += list(value) if isinstance(value, ListOfArguments) else [value]
    return values


# The values of the arguments that are not named parameters, in the order typed: ['1', '2', 'bins=20'] gives [1, 2].
def get_positional_arguments(arguments, named_parameters):
    return get_values_from_arguments(get_arguments_not_in_named_parameters(arguments, named_parameters))


# The named parameters the method accepts: for hist(), ['data', 'bins', 'marker', ...]; an empty list when the method cannot be asked.
def get_named_parameters_from_method(method):
    try:
        return list(inspect.signature(method).parameters)
    except (TypeError, ValueError):
        return []


# The memory carried while running the methods: which object they act on, the signal waiting to be drawn, the plot it was created on, the object a method returned, and the test data waiting for the next plotting method.
class chain_state:
    def __init__(self, figure, terminal):
        self.figure = figure
        self.terminal = terminal
        self.selected = None
        self.signal_to_draw = None
        self.plot_of_signal_to_draw = figure
        self.active_object = None
        self.data_for_next_signal = []


# Stops the program when the figure was not selected, as --title needs --figure before it.
def require_figure(state, method_name):
    if state.selected != 'figure':
        note("plotext", f"--{method_name} acts on the figure: write --figure before the figure methods", "error")
        sys.exit(1)


# Stops the program naming the method plotext does not know.
def exit_on_unknown_method(method_name, owner_name = ''):
    note("plotext", f"unknown {owner_name}method '{method_name}'".replace("  ", " "), "error")
    sys.exit(1)


# --figure and --terminal: the following methods act on the named object.
def select_object(state, object_name):
    state.selected = object_name
    state.active_object = None


# --draw: puts the waiting signal on the plot it was created on, and the following methods act on that plot.
def draw_waiting_signal(state):
    require_figure(state, 'draw')
    plot = state.plot_of_signal_to_draw
    if state.signal_to_draw is not None:
        plot.draw(state.signal_to_draw)
    state.signal_to_draw = None
    state.plot_of_signal_to_draw = state.figure
    state.active_object = plot if plot is not state.figure else None
    state.data_for_next_signal = []


# --show: renders the whole figure, never a single subplot.
def show_figure(state, arguments):
    require_figure(state, 'show')
    call_method_from_arguments(state.figure.show, arguments)


# --subplot: the following methods act on the chosen subplot, always counted from the figure.
def move_to_subplot(state, arguments):
    require_figure(state, 'subplot')
    state.active_object = call_method_from_arguments(state.figure.subplot, arguments)
    state.signal_to_draw = None
    state.data_for_next_signal = []


# --image, --gif and --video: run directly and display, with no figure involved.
def run_media_method(method_name, arguments):
    import plotext as plotext_module
    method = get_method_in_owner_from_name(method_name, plotext_module)
    if method is None:
        exit_on_unknown_method(method_name)
    result = call_method_from_arguments(method, arguments)
    if hasattr(result, 'print'):
        result.print()


# A terminal method, like --size: its plain result, when there is one, is printed.
def run_terminal_method(state, method_name, arguments):
    method = get_method_in_owner_from_name(method_name, state.terminal)
    if method is None:
        exit_on_unknown_method(method_name, 'terminal ')
    result = call_method_from_arguments(method, arguments)
    if result is not None and result is not state.terminal:
        print(result)


# The owners searched for a method, in order: the object a method returned, the waiting signal, the figure, its clear attribute, and the plotext module.
def get_owners(state):
    import plotext as plotext_module
    if state.selected is None:
        return [plotext_module]
    return [state.active_object, state.signal_to_draw, state.figure, state.figure.clear, plotext_module]


# The test data waiting for a plotting method, taken out of the memory; an empty list when the method takes none.
def take_data_for_next_signal(state, method_name, owner):
    if isinstance(owner, type(state.figure)) and method_name in methods_that_create_signals and state.data_for_next_signal:
        data = state.data_for_next_signal
        state.data_for_next_signal = []
        return data
    return []


# Remembers what the method returned: a signal waits for --draw, a test data result joins the queue, any other object is where the following methods act.
def remember_result(state, result, owner):
    from plotext._signal.signal import signal_class
    import plotext as plotext_module
    if isinstance(owner, type(state.figure)) and isinstance(result, signal_class):
        state.signal_to_draw = result
        state.plot_of_signal_to_draw = owner
        state.active_object = None
    elif owner is plotext_module and result is not None and not isinstance(result, type(state.figure)):
        state.data_for_next_signal.append(result)
    elif result is not None and result is not state.figure:
        state.active_object = result


# Any other method: found on the first owner holding it, then called, its result remembered.
def run_method(state, method_name, arguments):
    method, owner = get_method_and_owner_tuple_from_name(method_name, get_owners(state))
    if method is None:
        if state.selected is None and (get_method_in_owner_from_name(method_name, state.figure) or get_method_in_owner_from_name(method_name, state.figure.clear)):
            require_figure(state, method_name)
        exit_on_unknown_method(method_name)
    leading_values = take_data_for_next_signal(state, method_name, owner)
    result = call_method_from_arguments(method, arguments, leading_values)
    remember_result(state, result, owner)


# Runs the methods of the sentence in order, each acting on the figure, on the terminal or on its own.
def run_methods(methods_words):
    import plotext as plotext_module
    state = chain_state(plotext_module.figure, plotext_module.terminal)
    state.figure.clear()

    for method_words in methods_words:
        method_name, arguments = get_method_name(method_words[0]), method_words[1:]

        if method_name in ('figure', 'terminal'):
            select_object(state, method_name)

        elif method_name == 'draw':
            draw_waiting_signal(state)

        elif method_name == 'show':
            show_figure(state, arguments)

        elif method_name == 'subplot':
            move_to_subplot(state, arguments)

        elif method_name in media_methods:
            run_media_method(method_name, arguments)

        elif state.selected == 'terminal':
            run_terminal_method(state, method_name, arguments)

        else:
            run_method(state, method_name, arguments)
