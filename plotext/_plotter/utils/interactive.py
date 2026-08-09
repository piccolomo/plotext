# Interactive mode: with it on, every method changing the figure reprints it as soon as it ends, so the plot updates as you build it; the choice lives on the master figure, and one command reprints once, however many calls it makes inside.

import functools

from plotext._correct import bool as correct_bool


# Holds the interactive choice and the switch turning it on; the figure gains these methods, since plot_class is built on this class.
class interactive_class:

    def __init__(self):
        self._interactive = False        # the user choice, set by interactive(): with it on, every change reprints the figure
        self._outermost_call = False     # True while a user command is running, so the calls it makes inside stay quiet

    # Turn interactive mode on or off; with it on, every method changing the figure reprints it at once, the first reprint coming with the next such call.
    def interactive(self, active = True):
        self.master()._interactive = correct_bool.boolean(active, True)
        return self


# Give back the method with the reprint logic around it: while it runs, the calls it makes inside stay quiet, and at its end the figure is reprinted, when reprint_at_end is asked and interactive mode is on.
def _decorate(method, reprint_at_end):

    @functools.wraps(method)
    def run_method(self, *args, **kwargs):
        master = self.master()

        # A user command is already running, so this call is one of its inner ones: run it and say nothing.
        if master._outermost_call:
            return method(self, *args, **kwargs)

        # This call is the user command: raise the flag, run the method, lower the flag even when it fails.
        master._outermost_call = True
        try:
            result = method(self, *args, **kwargs)
        finally:
            master._outermost_call = False

        # The figure changed and the user asked to see it: print it once.
        if reprint_at_end and master._interactive:
            master.show()
        return result

    return run_method


# Gives back a method that reprints the figure when it ends.
# Input: one figure method, like title().
# Operation: builds a new function around it; each time that runs, it reads the _outermost_call flag on the master figure. With the flag already up, the method is one called from inside another, so it runs and prints nothing. With the flag down, this is the user command: the flag is raised, the method runs, the flag is lowered, and the figure is printed when interactive mode is on.
# In plain terms: the first method you call claims the job of printing and holds it until it is done, so you see the finished figure once, not the half built one many times.
# Output: that new function, which takes the place of the method, since the line @reprint_after sits above its definition.
def reprint_after(method):
    return _decorate(method, True)


# Gives back a method that reprints nothing.
# Input: one building method, like bar(), which returns a signal and puts nothing on the figure.
# Operation: the same construction, with one difference: the new function never prints, even when it is the user command; it only raises the flag while the builder runs.
# In plain terms: a builder has nothing to show yet, so it keeps its inner calls quiet and leaves the printing to the later draw().
# Output: that new function, taking the place of the method, since the line @no_reprint_after sits above its definition.
def no_reprint_after(method):
    return _decorate(method, False)
