# Propagator: the base of the plot components reachable from the figure, like the clear object and the rulers; it holds the plot owning the component and repeats a setting on the same component of every subplot.
# Each child class supplies _counterpart(subplot), giving the component of that subplot matching this one: the ruler of the same axis and side, the clear object, and so on.

class propagator_class:
    # Bind the component to the plot owning it.
    def __init__(self, plot):
        self._plot = plot

    # The master figure, asked to the owning plot; the reprint_after decorator needs it.
    def master(self):
        return self._plot.master()

    # The subplots of the owning plot, one per position of its grid, and none when it holds no grid.
    def _subplots(self):
        return [self._plot._get_subplot(*position) for position in self._plot._get_slots_range()] if self._plot._has_subplots() else []

    # Repeat a setting on every subplot.
    # Input: the name of a method of this component, as "lim", and the arguments to call it with.
    # Operation: for each direct subplot of the owning plot, it takes the matching component with _counterpart(subplot), then calls the named method on it with those arguments; each of those calls repeats the same on its own subplots, so the setting reaches the whole tree.
    # In plain terms: a setting written on the figure lands on every subplot too, without the caller walking the tree.
    # Output: nothing; the subplots are changed.
    def _propagate(self, method_name, *args):
        for subplot in self._subplots():
            getattr(self._counterpart(subplot), method_name)(*args)
