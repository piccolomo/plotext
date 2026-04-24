Installation
============

``plotext`` is a pure Python package backed by a small C++ kernel loaded
via ``ctypes``. The kernel is compiled automatically during installation,
so a single ``pip`` command is usually all you need.


From PyPI
---------

Install the stable version::

   pip install plotext

Upgrade an existing installation::

   pip install plotext --upgrade


From GitHub
-----------

Install the latest development version directly from the repository::

   pip install git+https://github.com/piccolomo/plotext


Optional extras
---------------

``plotext`` ships a handful of optional feature sets: ``image`` for image
plotting (Pillow), ``video`` for video rendering (Pillow, OpenCV,
ffpyplayer, pafy, youtube-dl), and ``completion`` for shell TAB
completion (shtab). Install any combination with the usual extras
syntax, e.g.::

   pip install "plotext[image]"
   pip install "plotext[video]"
   pip install "plotext[completion]"


C++ kernel
----------

``plotext`` includes a small C++ kernel that is compiled during source
installs. You need a working C++ compiler: ``g++`` on Linux or macOS
(``sudo apt install build-essential`` on Debian/Ubuntu,
``xcode-select --install`` on macOS), or the MinGW-w64 toolchain on
Windows (easiest via `MSYS2 <https://www.msys2.org/>`_).

If no compiler is found the install still completes with a warning;
you can build the kernel later by running ``python build_cpp.py`` from
a cloned repository.

PyPI wheels ship a pre-built kernel, so no compiler is needed in that
case.


Testing
-------

Verify the installation by running the built-in test function::

   import plotext as plt
   plt.test()

It exercises the public API up to image rendering (a test image is
downloaded to your home folder and removed afterwards).


Contributing
------------

Bug reports and pull requests are welcome:

- `Issue tracker <https://github.com/piccolomo/plotext/issues>`_
- `Pull requests <https://github.com/piccolomo/plotext/pulls>`_
