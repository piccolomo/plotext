# Internal file I/O implementation. The class at the bottom (`file`) is the public facade exposed as plotext.file.

import os, sys, io, inspect, csv, tempfile

from plotext._methods.string import note


# Normalize a path-or-URL into a local filesystem path. URLs (http/https/ftp) get downloaded once into <tempdir>/plotext/<hash>_<basename> and reused on subsequent calls (so plt.gif("https://…/x.gif") behaves the same on second run). "~/..." paths expand to the user's home folder. Other strings pass through. Cross-platform, tempfile.gettempdir() lands in %TEMP% on Windows and /tmp on Unix.
def correct(path):
    if isinstance(path, str) and path.startswith(('http://', 'https://', 'ftp://')):
        return _fetch_url(path)
    return os.path.expanduser(path)


# Pull `url` down to <tempdir>/plotext/<hash>_<basename> on first use; on subsequent calls the saved file is already there, so we just return its path. Filename is prefixed with a short URL hash so two URLs that happen to end in the same basename don't trample each other. Forward-references download() (defined below), resolved at call time.
def _fetch_url(url):
    import hashlib, pathlib, urllib.parse
    parsed = urllib.parse.urlparse(url)
    name = pathlib.Path(parsed.path).name or 'download'
    key = hashlib.md5(url.encode()).hexdigest()[:8]
    cache_dir = pathlib.Path(tempfile.gettempdir()) / 'plotext'
    cache_dir.mkdir(parents = True, exist_ok = True)
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


# Write a string to a file
def write(text, path, append = False, log = False):
    path = correct(path)
    with open(path, 'a' if append else 'w', encoding = 'utf-8') as f:
        f.write(text)
    if log: note("plotext.file.write", f"{len(text)} characters written to {path}")


# Read a file as a string
def read(path, log = False):
    path = correct(path)
    with open(path, 'r', encoding = 'utf-8') as f:
        text = f.read()
    if log: note("plotext.file.read", f"{len(text)} characters read from {path}")
    return text


# Read a csv file as a table (a list of rows, each being a list of strings), reusing read()
# The empty rows are left out, a file ending with a new line otherwise giving a last row with no cells, which loses every column when the table is turned into columns
def csv_read(path, delimiter = ',', log = False):
    rows = [row for row in csv.reader(io.StringIO(read(path)), delimiter = delimiter) if row]
    if log: note("plotext.file.csv", f"{len(rows)} rows read from {correct(path)}")
    return rows


# Turn a table (a list of rows) into its csv text, ready for write()
def string(data, delimiter = ','):
    buffer = io.StringIO()
    csv.writer(buffer, delimiter = delimiter, lineterminator = '\n').writerows(data)
    return buffer.getvalue()


# True if the path refers to an existing filesystem entry
def exists(path):
    return os.path.exists(correct(path))


# True when the path sits inside the folder the program runs in, any shortcut followed first; on windows a path on another drive is never inside, which is what the raised error means
def _is_inside_working_folder(path):
    working = os.path.realpath(os.getcwd())
    try:
        return os.path.commonpath([os.path.realpath(path), working]) == working
    except ValueError:
        return False


# Remove the file at the given path (no-op if it doesn't exist). With safe left on, only files inside the folder the program runs in can be removed.
def delete(path, safe = True, log = False):
    path = correct(path)
    if safe and not _is_inside_working_folder(path):
        note("plotext.file.delete", f"{path} is outside the working folder; pass safe = False to delete it anyway", "warning")
        return
    if os.path.isfile(path):
        os.remove(path)
        if log: note("plotext.file.delete", f"{path} deleted")
    elif log:
        note("plotext.file.delete", f"nothing to delete at {path}")


# Parent directory. With no path argument, returns the caller's script folder. level>1 walks further up.
def parent(path = None, level = 1):
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
def download(url, path, log = False):
    from urllib.request import urlretrieve
    path = correct(path)
    urlretrieve(url, path)
    if log: note("plotext.file.download", f"{url} saved to {path}")


# Public facade, re-exposes the module functions as static methods so the API is exposed as plotext.file
class file_class:
    """Basic file I/O helpers: text read/write, csv table reading and serialization, URL download, existence checks, deletion, parent/script-folder lookup and path joining."""
    read     = staticmethod(read)
    write    = staticmethod(write)
    csv      = staticmethod(csv_read)
    string   = staticmethod(string)
    exists   = staticmethod(exists)
    delete   = staticmethod(delete)
    parent   = staticmethod(parent)
    join     = staticmethod(join)
    download = staticmethod(download)

    def __repr__(self):
        return "PlotextFileToolkit()"

file = file_class()   # singleton instance, so `plotext.file` is the live object (gives the repr) instead of the class
