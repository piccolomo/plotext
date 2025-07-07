Change Log
==========


Version 6.0
-----------
- The kernel of the code has been rewritten in C++
- Added `prettydoc` module to generate colorful docstrings
- `colorize` is now a class, not a function
   - its `fullground` parameter has been renamed `foreground`
   - its `show` parameter has been removed and replace with its `print()` method


Version 5.3
-----------
Available on `Plotext GitHub 5.30 <https://github.com/piccolomo/plotext/releases/tag/5.3.0>`_ only.

- Documentation Updates
	- All docstrings updated.
	- The colored docstrings of all methods can now be easily printed using a dedicated `.doc()` internal method. For example, `plotext.scatter.doc()` will print the colorized docstring of the `scatter()` function.
- Function and Parameter Renaming
	- Renamed `text` parameter to `label` in the `text()` method.
	- Renamed `label` parameter to `labels` in the `multiple_bar()` and `stacked_bar()` functions.
	- Renamed `fullground` parameter to `color` in the `colorize()` method.
	- Renamed `datetimes_to_string()` method to `datetimes_to_strings()`.
- Function Modifications
	- Removed `trend` parameter from the `indicator()` function.
	- Added `log` and `header` parameters to the `read_data()` method.
	- Changed text default alignment to `'center'` in the `text()` method.
- New Feature: Added `boxplot` as requested in `Issue 169 <https://github.com/piccolomo/plotext/issues/169>`_ and proposed in `Pull Request 170 <https://github.com/piccolomo/plotext/pull/170>`_.


Version 5.2
-----------

version 5.2.8
^^^^^^^^^^^^^
Published on `PyPI <https://pypi.org/project/plotext/5.2.8/>`_

- **Bug Fixes**:
	- Solved `Issue 153 <https://github.com/piccolomo/plotext/issues/153>`_ allowing bar plots with zero datasets.
	- Solved `Issue 151 <https://github.com/piccolomo/plotext/issues/151>`_ regarding nested subplot inheritance.
	- Addressed `Issue 142 <https://github.com/piccolomo/plotext/issues/142>`_ by removing side symbols (e.g., ⅃) in legends for single datasets.
	- Fixed bar plot issue due to max number of subplots (`Issue 150 <https://github.com/piccolomo/plotext/issues/150>`_).
- **Enhancements**:
	- Added date-time support for ``xlim()`` and ``ylim()``, fixing `Issue 138 <https://github.com/piccolomo/plotext/issues/138>`_.
	- Added `marker` parameter to ``from_matplotlib()``, solving `Issue 134 <https://github.com/piccolomo/plotext/issues/134>`_.


versions < 5.2.8 
^^^^^^^^^^^^^^^^
- New Features
	- Added `indicator()` function as requested in `Issue 121 <https://github.com/piccolomo/plotext/issues/121>`_.
	- Added `interactive()` function as requested in `Issue 115 <https://github.com/piccolomo/plotext/issues/115>`_.
	- Added `confusion_matrix()` function as requested in `Issue 113 <https://github.com/piccolomo/plotext/issues/113>`_.
	- Added `square()` function as requested in `Issue 108 <https://github.com/piccolomo/plotext/issues/108>`_.
	- Added `simple_bar()`, `simple_multiple_bar()`, and `simple_stacked_bar()` functions as requested in `Issue 98 <https://github.com/piccolomo/plotext/issues/98>`_.
	- Added `xreverse()` and `yreverse()` functions as requested in `Issue 86 <https://github.com/piccolomo/plotext/issues/86>`_.
	- Added `polygon()` and `rectangle()` functions.
	- Added `append` parameter to the `save_fig()` function as requested in `Issue 109 <https://github.com/piccolomo/plotext/issues/109>`_.
	- Introduced `background` color option in the `text()` function.
	- Introduced `shtab` optional dependency as discussed in `Pull Request 118 <https://github.com/piccolomo/plotext/pull/118>`_.
- Improvements
	- Improved handling of `Nan` and `None` values in the data, as requested in `Issue 114 <https://github.com/piccolomo/plotext/issues/114>`_.
	- Simplified bar ticks creation and added `reset_ticks` parameter to optionally disable default ticks creation.
	- Enhanced functionality of `fillx` and `filly` parameters to accept `True`, `False`, numerical values, and `"internal"` for more flexible filling options.
- Updated code structure:
	  - Introduced `_global.py` and `_matrix.py` files.
	  - Changed `_utility` folder to a single file.
	  - Introduced `_dict.py` file containing long dictionaries related to markers, colors, styles, and themes.
	  - Introduced `_build.py` to handle the long `build_plot()` function separately.
- Fixes
	- Fixed legend symbol for braille markers, merging `Pull Request 135 <https://github.com/piccolomo/plotext/pull/135>`_.
	- Allowed compatibility with Python 3.7, resolving `Issue 130 <https://github.com/piccolomo/plotext/issues/130>`_.
	- Enabled new line `'\n'` in `text()` to properly plot, addressing `Issue 127 <https://github.com/piccolomo/plotext/issues/127>`_.
	- Enabled TAB completion in command line tool, as discussed in `Pull Request 126 <https://github.com/piccolomo/plotext/pull/126>`_.
	- Solved incorrect definitions of `xlim()` and `ylim()`, fixing `Issue 112 <https://github.com/piccolomo/plotext/issues/112>`_ and `Issue 123 <https://github.com/piccolomo/plotext/issues/123>`_.
	- Removed `version()` function; it is now represented as simply `version` value.
- Other Changes
	- Integrated changes from `Pull Request 107 <https://github.com/piccolomo/plotext/pull/107>`_ related to allowing `plotext` with `python -m` flag.
	- Removed memory of past plotted bars in bar functions; bars can now have negative values.
	- Code reorganized for improved maintainability.


Version 5.1
-----------
This version is available on `Plotext GitHub 5.1.0 <https://github.com/piccolomo/plotext/releases/tag/5.1.0>`_ only.

- New Features
	- Added `error()` function as requested in `Issue 91 <https://github.com/piccolomo/plotext/issues/91>`_.
	- Added `--lines` flag in the command line tool to handle large data sets.
	- Added `--xcolumn` and `--ycolumns` flags to easily set the `x` and `y` data from the data table.
	- Added `log` parameter to most of the `file functions <https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities>`_.
	- Introduced 4 x 2 `braille` markers, as requested in `Issue 89 <https://github.com/piccolomo/plotext/issues/89>`_.
- Improvements
	- Corrected and integrated all `.md` files.
	- Test files are now available online rather than being downloaded during installation, reducing package size.
	- Added `--path` flag to the command line tool, replacing the `--file` flag.
	- Improved handling of small axis numerical ticks in exponential form and in `log` scale, solving `Issue 90 <https://github.com/piccolomo/plotext/issues/90>`_.
	- Changed default bar marker to `hd`, addressing `Issue 96 <https://github.com/piccolomo/plotext/issues/96>`_.
- Fixes
   - Solved issue with consecutive calls to `show()` function causing problems with text plots, as detailed in `Issue 94 <https://github.com/piccolomo/plotext/issues/94>`_.


Version 5.0
-----------
- Improvements
	- Added ``play_gif()``, ``play_video()``, ``play_youtube()``, ``download()``, and ``get_youtube()`` functions to play GIFs and videos.
	- Rewritten command line tool for enhanced functionality.
	- Added ``candlestick()`` plot function.
	- Introduced new logic for creating a matrix of subplots, allowing nested sub-matrices and settings propagation from top to bottom levels.
	- Added ``take_min()`` function.
	- Improved plotting performance, up to 5 times faster for small data and 2 times faster for long data (performance varies by machine).
	- Replaced ``xaxis()`` with ``xaxes()`` and ``yaxis()`` with ``yaxes()`` to set the presence of both axes simultaneously without needing the ``xside`` parameter.
	- Added ``ticks_style()`` function to customize tick styles.
	- Added ``theme()`` function for setting plot themes.
	- Introduced ``fast`` parameter in ``matrix_plot()`` and ``image_plot()`` for faster plotting.
	- Added ``text()`` function to add string labels to the plot.
	- Added ``keep_colors`` parameter in ``save_fig()`` to retain ANSI color codes in ``txt`` files (viewable with ``less -R file_path.txt``).
	- Introduced ``event_plot()`` inspired by `Issue 83 <https://github.com/piccolomo/plotext/issues/83>`_.
	- Simplified string color codes.
	- ``xside`` and ``yside`` parameters can now accept 1 and 2 for simplified usage.
	- Larger plots are now handled outside of ``ipython``, which prints an extra line or two.
- Bug Fixes
	- Added the back-end function ``from_matplotlib()``, as requested in `Issue 75 <https://github.com/piccolomo/plotext/issues/75>`_.
	- Solved `Issue 90 <https://github.com/piccolomo/plotext/issues/90>`_ to plot small axis numerical ticks in exponential form and in `log` scale.
	- Solved `Issue 94 <https://github.com/piccolomo/plotext/issues/94>`_ caused by consecutive calls to the ``show()`` function with text plots.
	- Changed the default bar marker to ``hd`` to address `Issue 96 <https://github.com/piccolomo/plotext/issues/96>`_.
- Deprecations and Removals
	- Removed ``span()`` function.
	- Removed ``clear_plot()`` function; ``clear_figure()`` now handles its functionality based on the subplot matrix level.
	- Removed ``colorless()`` function; ``clear_color()`` now handles its functionality based on the subplot matrix level.
	- Removed ``size``, ``keep_ratio``, and ``resample`` parameters from ``image_plot()``.
	- Removed ``plot_date()`` and ``scatter_date()`` functions; date/time plots are now handled by ``plot()`` and ``scatter()``.
	- Removed file class; all related tools have been moved to a normal level.
	- Removed date-time class; all tools rewritten and moved to a normal level.
- Refactoring
	- Rewritten entire code for improved performance and maintainability.
	- Introduced `input_form` and `output_form` for handling date/time string objects.
	- Introduced `test()` function for improved testing capabilities.


Version 4.3
-----------
- Accounted for exponential float notation as requested in `Pull 82 <https://github.com/piccolomo/plotext/pull/82>`_.
- Added functionality to properly read `numpy` data as requested in `Issue 84 <https://github.com/piccolomo/plotext/issues/84>`_ and `Issue 85 <https://github.com/piccolomo/plotext/issues/85>`_.


Version 4.2
-----------
- Added `norm` parameter in ``hist()`` function as requested in `Issue 76 <https://github.com/piccolomo/plotext/issues/76>`_ and incorporated changes from `Pull 79 <https://github.com/piccolomo/plotext/pull/79>`_.


Version 4.1
-----------
**Improvements**
	- Added ``horizontal_line`` and ``vertical_line`` functions, as requested in `Issue 65 <https://github.com/piccolomo/plotext/issues/65>`_.
	- The plotting functions now handle non-numerical values by excluding them from plots, as requested in `Issue 65 <https://github.com/piccolomo/plotext/issues/65>`_.
	- Added command line tool discussed in `Issue 47 <https://github.com/piccolomo/plotext/issues/47>`_, `Pull 57 <https://github.com/piccolomo/plotext/pull/57>`_, `Pull 52 <https://github.com/piccolomo/plotext/pull/52>`_, and `Pull 51 <https://github.com/piccolomo/plotext/pull/51>`_.
	- Added guide for integration with package `rich`, as discussed in `Issue 26 <https://github.com/piccolomo/plotext/issues/26>`_.
	- Added guide for integration with `tkinter`, as discussed in `Issue 33 <https://github.com/piccolomo/plotext/issues/33>`_.
**Bug Fixes**
	- Solved single bar plot error discussed in `Issue 63 <https://github.com/piccolomo/plotext/issues/63>`_.
	- Fixed bar error reported in `Issue 61 <https://github.com/piccolomo/plotext/issues/61>`_.
	- Added exception handling when subplot size exceeds default, as noted in `Issue 60 <https://github.com/piccolomo/plotext/issues/60>`_.
	- Removed `shell` function and parameter as they were deemed useless.
**Miscellaneous**
	- Set default marker to ``hd`` to avoid complications with ``fhd`` marker in some terminals, as noted in `Issue 62 <https://github.com/piccolomo/plotext/issues/62>`_.
	- Changed default canvas background color back to ``bright-white``.
	- Made `pillow` an optional dependency, as requested in `Issue 56 <https://github.com/piccolomo/plotext/issues/56>`_.
	- Removed `numpy` as a dependency (not even optional).
	- Changed `platform` function as recommended in `Issue 55 <https://github.com/piccolomo/plotext/issues/55>`_.
	- Corrected and integrated all `.md` files.


Version 4.0
-----------
**Improvements**
	- Entire code re-written for better performance.
	- Improved plotting speed.
	- Changed 2 x 2 marker to ``hd`` (high resolution) instead of ``small``.
	- Added higher resolution 3 x 2 Unicode mosaic markers (not available in Windows), called ``fhd`` (full high resolution).
	- Added new color codes, including 256 color codes and full RGB colors.
	- Introduced multiple and stacked bar charts.
	- Added date-time scatter and plot functions.
	- Added date-time class for better handling of date-time objects.
	- Added ``matrix_plot()`` and ``image_plot()`` functions.
	- Plots can now be saved in color using `.html` extension.
	- Added file class for better file and path handling.
	- Data can now be plotted on the upper x axis.
	- Added `unittest` file named `test.py`.
	- Introduced `xside` and `yside` parameters for many related functions.
	- Added `span()` function to span columns and rows in the matrix of subplots.
	- Added more `clear` functions.
	- Added `limit_size()` function to control plot dimensions relative to terminal size, inspired by `Issue 33 <https://github.com/piccolomo/plotext/issues/33>`_.
	- Added optional legend extra characters for axis identification.
	- Added `time()` function to check plotting computational time.
	- Renamed `xfreq()` to `xfrequency()` and `yfreq()` to `yfrequency()`.
	- Added doc class for easy access to function docstrings.
	- Renamed `get_canvas()` to `build()`.
	- Reinstated `frame()` function.
**Bug Fixes**
	- Solved bar chart log scale issue on both axes.
	- Solved bar chart zero value issue.


Version 3.1
-----------
- Fixed plot resizing issue discussed in `Issue 23 <https://github.com/piccolomo/plotext/issues/23>`_.
- Added `clear_data()` and `test()` functions.


Version 3.0
-----------
- Re-written most of the code.
- Added direct terminal command line tool (first type).
- Introduced `"small"` marker with improved resolution, and new marker codes.
- Added matrix of subplots.
- Added log plots, stem plot, and double `y` axes plot.
- Added bar plot and date/time plot functions.
- Added `get_canvas()` and `sin()` functions.
- Added `clear_figure()` function.
- Changed `figsize()` to `plotsize()`.
- Renamed `nocolor()` to `colorless()`.
- Replaced `frame()` function with `xaxes()` and `yaxes()`.


Version 2.3
-----------
- Solved histogram error reported in `Issue 15 <https://github.com/piccolomo/plotext/issues/15>`_.
- Added histogram plot and `fillx` and `filly` parameters.


Version 2.2
-----------
- Updated `readme.md` description file.
- Changed `fig_size()` to `figsize()`, `facecolor()` to `axes_color()`, and `canvas_size()` to `fig_size()`.
- Slightly modified behavior under Windows.
- Introduced new Windows-friendly markers.
- Default color combination for plots instead of colorless.
- Removed `force_size` parameter.
- Added `grid()` function for optional grid lines.
- Added `frame()` function (present by default).
- Streamlined parameters in `plot` and `scatter` functions.
- Added `nocolor()` function and improved line-filling algorithm.
- Added `clp()` and `clt()` functions for `clear_plot()` and `clear_terminal()`.
- Updated color codes and added `parameters()` and `docstrings()` functions.


Version 2.1
-----------
- Plot now shows actual data ticks using a simpler algorithm.
- Changed `ticks_number` to `ticks`.
- Updated set functions like `set_title()` to `title()`.
- Added optional grid and `fill` parameter.
- Changed `axes_color()` to `facecolor()` to align with `matplotlib`.
- Improved legend positioning and introduced new color codes.
- Code restructured and revised.


Version 2.0
-----------
- Plot now shows actual data ticks with improved adaptability.
- Added `set_xticks()` and `set_yticks()` functions.
- Added labels to axes, titles, and legends for multiple data sets.
- Updated set functions for list parameters to accept different formats.
- Changed `spacing` to `ticks_number`.
- Removed `equations` and `decimals` parameters.
- Code restructured and revised.


Version 1.0
-----------
- `plotext` now works in Windows with colors and Python IDLE3 (without colors and adaptive dimensions).
- Added new color codes with background codes.
- Introduced `force_size` parameter.
- Added `savefig()`, `get_version()`, and `run_test()` functions.
- Removed dependency on `numpy` and `time` packages.
- Updated code for improved readability and documentation.
- Set `equations` parameter to `False` by default.
- Removed `get` functions for plot parameters.