# Interactive mode: when enabled (interactive()), every figure-mutating method reprints the whole figure once it finishes — matching matplotlib's interactive semantics, where any modification shows immediately. interactive_class is a mixin of plot_class; its state lives on the master plot only and the decorators always read it via get_master(). A re-entrancy guard (_outermost_call) collapses nested calls (clear -> clear_data, frame -> axis, a builder's internal ticks(), propagation to subplots) into a single reprint: only the outermost call shows.

import functools

from plotext._correct import bool as correct_bool


# Interactive-mode mixin: holds the per-figure state and the public toggle. Composed into plot_class alongside subplot_class / draw_class / plot_build_class.
class interactive_class:

    def __init__(self):
        self._interactive = False        # user-facing on/off (set via interactive()); when True, mutating calls reprint
        self._outermost_call = False     # re-entrancy guard: True while a top-level mutation runs, so nested calls stay silent

    # Toggle interactive mode. When on, every figure-mutating call (draw, title, lim, theme, ...) reprints the whole figure immediately, matplotlib-style. State is kept on the master and read by the @refresh decorator; enabling is silent, the next mutating call produces the first reprint.
    def interactive(self, active = True):
        self.get_master()._interactive = correct_bool.boolean(active, True)
        return self


# show_after=True: mutating setters (title, lim, theme, draw, ...) reprint once done. show_after=False: builders (bar, box, ...) only hold the guard so their internal setter calls stay quiet; the eventual draw() does the reprint.
def _wrap(method, show_after):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        master = self.get_master()
        if master._outermost_call:                 # an outermost call is already running → this one is nested, run silently
            return method(self, *args, **kwargs)
        master._outermost_call = True
        try:
            result = method(self, *args, **kwargs)
        finally:
            master._outermost_call = False
        if show_after and master._interactive:
            master.show()
        return result
    return wrapper


# Mutating setter: reprint the figure after it runs when interactive.
def refresh(method):
    return _wrap(method, True)


# Builder that internally calls decorated setters: hold the guard while building, don't reprint on its own.
def silent(method):
    return _wrap(method, False)
