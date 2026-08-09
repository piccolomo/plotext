# Selection: base for objects holding several same-kind items (rulers, date converters); repeats a method on every item.

class selection_class:
    # Bind the selection to its items: the same-kind objects it was built from
    def __init__(self, items):
        self._items = items

    # Repeat a method, given its name and arguments, on every selected item
    def _repeat(self, method_name, *args):
        for item in self._items:
            getattr(item, method_name)(*args)

    # Print as the selected items, one per line
    def __repr__(self):
        return "\n".join([repr(item) for item in self._items])
