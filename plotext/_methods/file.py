# Internal file I/O implementation. The class at the bottom (`file`) is the public facade exposed as plotext.file.

import os, sys, inspect, csv, tempfile


# Normalize a path-or-URL into a local filesystem path. URLs (http/https/ftp) get downloaded once into <tempdir>/plotext/<hash>_<basename> and reused on subsequent calls (so plt.gif("https://…/x.gif") behaves the same on second run). "~/..." paths expand to the user's home folder. Other strings pass through. Cross-platform — tempfile.gettempdir() lands in %TEMP% on Windows and /tmp on Unix.
def correct(path):
    if isinstance(path, str) and path.startswith(('http://', 'https://', 'ftp://')):
        return _fetch_url(path)
    return os.path.expanduser(path)


# Pull `url` down to <tempdir>/plotext/<hash>_<basename> on first use; on subsequent calls the saved file is already there, so we just return its path. Filename is prefixed with a short URL hash so two URLs that happen to end in the same basename don't trample each other. Forward-references download() (defined below) — resolved at call time.
def _fetch_url(url):
    import hashlib, pathlib, urllib.parse
    parsed = urllib.parse.urlparse(url)
    name = pathlib.Path(parsed.path).name or 'download'
    key = hashlib.md5(url.encode()).hexdigest()[:8]
    cache_dir = pathlib.Path(tempfile.gettempdir()) / 'plotext'
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / f'{key}_{name}'
    if not dest.exists():
        try:
            download(url, str(dest))
        except Exception:
            raise FileNotFoundError(f"could not fetch URL {url!r}")
    return str(dest)


# Return the lowercased file extension (no dot) from a path, e.g. "html" from "plot.html"
def _get_extension(path):
    return os.path.splitext(path)[1].lower().lstrip('.')


# CSV → list of rows. Uses the stdlib csv module so quoting/escaping/commas-in-values work correctly.
def _read_csv(path):
    with open(correct(path), 'r', encoding='utf-8', newline='') as f:
        return list(csv.reader(f))


# List of rows → CSV. Mirrors _read_csv.
def _write_csv(data, path, append=False):
    with open(correct(path), 'a' if append else 'w', encoding='utf-8', newline='') as f:
        csv.writer(f).writerows(data)


# Write to a file. Dispatches by extension: .csv expects a list of rows (csv module handles quoting); any other extension expects a string.
def write(data, path, append=False):
    if _get_extension(path) == 'csv':
        _write_csv(data, path, append)
        return
    with open(correct(path), 'a' if append else 'w', encoding='utf-8') as f:
        f.write(data)


# Read from a file. Dispatches by extension: .csv returns a list of rows; any other extension returns the file's text.
def read(path):
    if _get_extension(path) == 'csv':
        return _read_csv(path)
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


# Download a URL to path (urllib.urlretrieve).
def download(url, path):
    from urllib.request import urlretrieve
    urlretrieve(url, correct(path))


# Public facade — re-exposes the module functions as static methods so the API is exposed as plotext.file
class file:
    """Basic file I/O helpers: path correction, text/csv read/write (extension-dispatched), URL download, existence checks, deletion, parent/script-folder lookup and path joining."""
    correct  = staticmethod(correct)
    read     = staticmethod(read)
    write    = staticmethod(write)
    exists   = staticmethod(exists)
    delete   = staticmethod(delete)
    parent   = staticmethod(parent)
    join     = staticmethod(join)
    download = staticmethod(download)

    def __repr__(self):
        return "Plotext File Toolkit"

file = file()   # singleton instance — so `plotext.file` is the live object (gives the repr) instead of the class
