# Container: the object update() gives back, holding one printing method per documented entry, reached by name as plotext.doc.bar(); calling the container itself opens the interactive menu.

from plotext.prettydoc._primitives.source import source_class


class docs_output:

    # Start empty; update() then fills it with one printing method per entry.
    def __init__(self):
        self._function_dict = {}
        self._path_dict = {}

    # Every entry name with its printing method, in the order they were documented.
    def _get_functions(self):
        return self._function_dict

    # How many entries the container holds.
    def _get_length(self):
        return len(self._function_dict)

    # Reaching a name gives its printing method, as doc.gif; a name holding further ones gives a step instead, so that doc.pixel.copy reaches the copy() method of the pixel.
    def __getattr__(self, name):
        return self._resolve(name)

    # The name of an entry without its parentheses, as "plotext.figure.signal.get" for "plotext.figure.signal().get".
    def _plain(self, key):
        plain = key.replace('()', '')
        return plain

    # Every way of reaching an entry, one per source path it was given.
    def _paths(self, key):
        paths = self._path_dict.get(key) or [self._plain(key)]
        return paths

    # What a dotted path gives: the printing method of the entry ending there, or a step, when other entries continue past it.
    def _resolve(self, path):
        final = [key for key in self._function_dict if any(('.' + full).endswith('.' + path) for full in self._paths(key))]
        deeper = [key for key in self._function_dict if any('.' + path + '.' in '.' + full for full in self._paths(key))]
        if not final and not deeper: raise AttributeError("no documented function named " + path)
        out = source_class(self, path) if deeper else self._function_dict[min(final, key = len)]
        return out

    # The printing method of the entry ending at the given path; when several do, the shortest name wins, the one closest to the top.
    def _printer(self, path):
        final = [key for key in self._function_dict if any(('.' + full).endswith('.' + path) for full in self._paths(key))]
        if not final: raise AttributeError("no documented function named " + path)
        return self._function_dict[min(final, key = len)]

    # The names documented right after the given path, as "copy" for "plotext.pixel".
    def _next_names(self, path):
        names = []
        for key in self._function_dict:
            for full in self._paths(key):
                if '.' + path + '.' in '.' + full:
                    names.append(('.' + full).split('.' + path + '.', 1)[1].split('.')[0])
        return names

    # Every entry name without its path, offered when pressing the tab key.
    def __dir__(self):
        return [key.split('.')[-1] for key in self._function_dict]

    # Representation
    def __repr__(self):
        return f"PrettyDoc({self._get_length()} functions)"

    # Calling the container, as plotext.doc(), opens the interactive menu.
    def __call__(self):
        self._call()
