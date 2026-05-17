# Internal file I/O implementation. The class at the bottom (`file`) is the public facade exposed as plotext.file.

import os, sys, inspect


# Expand "~/..." paths to the user's home folder
def correct(path):
    return os.path.expanduser(path)


# Return the lowercased file extension (no dot) from a path, e.g. "html" from "plot.html"
def _get_extension(path):
    return os.path.splitext(path)[1].lower().lstrip('.')


# Write text to a file. append=True appends instead of overwriting
def write(text, path, append=False):
    with open(correct(path), 'a' if append else 'w', encoding='utf-8') as f:
        f.write(text)


# Read text from a file
def read(path):
    with open(correct(path), 'r', encoding='utf-8') as f:
        return f.read()


# True if the path refers to an existing filesystem entry
def exists(path):
    return os.path.exists(correct(path))


# Remove the file at the given path (no-op if it doesn't exist)
def delete(path):
    path = correct(path)
    if os.path.isfile(path):
        os.remove(path)


# Parent directory. With no path argument, returns the caller's script folder. level>1 walks further up.
def parent(path=None, level=1):
    if path is None:
        path = inspect.getfile(sys._getframe(1))
    for _ in range(level):
        path = os.path.abspath(os.path.join(path, os.pardir))
    return path


# Join path components into an absolute path. The first part can be "~" to mean the home folder.
def join(*args):
    args = list(args)
    args[0] = correct(args[0])
    return os.path.abspath(os.path.join(*args))


# Public facade — re-exposes the module functions as static methods so the API is exposed as plotext.file
class file:
    """Basic file I/O helpers: path correction, text read/write, existence checks, deletion, parent/script-folder lookup and path joining."""
    correct = staticmethod(correct)
    read    = staticmethod(read)
    write   = staticmethod(write)
    exists  = staticmethod(exists)
    delete  = staticmethod(delete)
    parent  = staticmethod(parent)
    join    = staticmethod(join)
