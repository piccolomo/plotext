Installation
============

|plotext| is a Python package with a small C++ kernel, compiled
*automatically* during installation: a **single** ``pip`` command is usually
all you need.


From PyPI
---------

Install the **stable** version::

   pip install plotext

Upgrade an existing installation::

   pip install plotext --upgrade

.. important::

   PyPI still hosts version 5: version 6 is available only from GitHub,
   until its official release.


From GitHub
-----------

Install the latest **development** version directly from the repository::

   pip install git+https://github.com/piccolomo/plotext


.. _extras:

Optional extras
---------------

|plotext| ships two **optional** feature sets: ``image`` for images and GIFs
(`Pillow <https://pillow.readthedocs.io/>`_), and ``video`` for video and
YouTube playback (Pillow, `ffpyplayer <https://pypi.org/project/ffpyplayer/>`_,
`yt-dlp <https://github.com/yt-dlp/yt-dlp>`_). Install either with the usual
extras syntax::

   pip install "plotext[image]"
   pip install "plotext[video]"

.. caution::

   The ``video`` extra needs Python 3.13 or older, since ``ffpyplayer``
   does not install on Python 3.14 yet; the ``image`` extra is unaffected.
   On a Python 3.14 system, create the environment with an older
   interpreter, for example with `uv <https://docs.astral.sh/uv/>`_::

      uv venv --python 3.13 --seed ~/envs/plotext
      source ~/envs/plotext/bin/activate
      pip install "plotext[video]"


C++ kernel
----------

Compiling the kernel requires a **C++ compiler**, whose installation depends
on the operating system:

- **Linux**: ``g++``, installed with ``sudo apt install build-essential``
  on Debian / Ubuntu
- **macOS**: ``g++``, installed with ``xcode-select --install``
- **Windows**: the MinGW-w64 toolchain, easiest via
  `MSYS2 <https://www.msys2.org/>`_

.. warning::

   If no compiler is found, the installation completes anyway, printing
   ``[plotext] WARNING: kernel compilation failed``: plotext then relies
   on the kernel file already included in the package, and fails to
   import if none matches your system. To solve it, install a compiler
   from the list above, then reinstall, or run ``python build_cpp.py``
   from a cloned repository.


Testing
-------

Verify the installation by running the built-in test function::

   import plotext as plt
   plt.test()

It runs the bundled unit test suite and prints a summary of the results.


Constants
---------

| ``plotext.version`` holds the installed |plotext| version, as a string.
| ``plotext.platform`` holds the system in use, ``"unix"`` or ``"windows"``, detected when the package is imported.


.. _contributing:

Contributing
------------

Bug reports and pull requests are welcome:

- `Issue tracker <https://github.com/piccolomo/plotext/issues>`_
- `Pull requests <https://github.com/piccolomo/plotext/pulls>`_
