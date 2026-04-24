Future Ideas
============

Any new idea is welcomed by opening an `issue report <https://github.com/piccolomo/plotext/issues/new>`_ or a `pull request <https://github.com/piccolomo/plotext/compare>`_.

Here are some of the possible ways to improve `plotext` in the future (any help is welcomed):

Bug Fixes
---------
- Solve issue with `clear_color()` method not working properly, as presented in `Issue 156 <https://github.com/piccolomo/plotext/issues/156>`_.
- Fix simple stacked and multiple bar plot not working with a single data set, as presented in `Issue 155 <https://github.com/piccolomo/plotext/issues/155>`_.
- Resolve Chinese text bug, as presented in `Issue 158 <https://github.com/piccolomo/plotext/issues/158>`_.
- Address `frame()` method's behavior changes if called before `subplots()`; e.g., `import plotext as plt plt.clf() plt.subplots(2,2) plt.subplot(1,2) plt.frame(0) plt.subplots(2,2) plt.show()` versus `import plotext as plt plt.clf() plt.frame(0) plt.subplots(2,2) plt.show()` 
- Fix issue with `labels` parameter in `confusion_matrix()` (for non-boolean data) which doesn't seem to work properly.
- Resolve weekends time gap issue in datetime plots, as presented in `Issue 148 <https://github.com/piccolomo/plotext/issues/148>`_.

New Features
-------------
- Add custom lines, as requested in `Issue 145 <https://github.com/piccolomo/plotext/issues/145>`_.
- Support datetime integration, as requested in `Issue 154 <https://github.com/piccolomo/plotext/issues/154>`_.
- Add command line arguments to set plot limits, as requested in `Issue 173 <https://github.com/piccolomo/plotext/issues/173>`_.
- Allow plot and scatter to start from 0 and not 1 (optionally), as requested in `Issue 176 <https://github.com/piccolomo/plotext/issues/176>`_.
- Add heatmap plot, as requested in `Issue 143 <https://github.com/piccolomo/plotext/issues/143>`_.
- Add OHLC datetime plot, as requested in `Issue 149 <https://github.com/piccolomo/plotext/issues/149>`_.
- Add network graphs, as requested in `Issue 160 <https://github.com/piccolomo/plotext/issues/160>`_.
- Integrate `colorize()` in `text()` and `indicator()` or any string `label` parameter, as requested in `Issue 144 <https://github.com/piccolomo/plotext/issues/144>`_; possible idea: `colorize()` to output a `matrix_class()` object.
- Allow simple bar plots in a matrix of subplots, as requested in `Issue 171 <https://github.com/piccolomo/plotext/issues/171>`_; this could be extended to allow images also, rendered with the `fast` parameter set to `True`.
- Allow users to decide plot legend position and frame.
- Allow clickable plots, as requested in `Issue 175 <https://github.com/piccolomo/plotext/issues/175>`_; this might be challenging!
- Add text table feature with nice formatting (?).

New Functions
--------------
- Add `bold()` function to make a string bold.
- Add `plotter()` function to scatter and plot simultaneously.
- Add `clear_settings()` method to clear only the plot settings (labels, title, etc.) and not the data or colors.
- Add `simple_hist()` function, analogous to `simple_bar()`.

General Improvements
--------------------
- Add uppercase, lowercase, and title styles.
- Add `log` parameter to `save_fig()` and similar functions.
- Avoid float in axes labels if ticks are all integers.
- Catch errors in video reproduction and get YouTube.
- In read data, default folder should be the script folder.
- Allow simple bar plots to handle negative values.
- Allow `limit_size()` to be used also after `plot_size()`.
- Add bar `alignment` and `style` parameters.
- Add matrix plot side bar to connect intensity level with the actual matrix value.
- High-resolution markers available on Windows and other rarer terminals (under request and not sure how).
- Add method to optionally set the sizes of a matrix of subplots giving priority to the subplots closer to the bottom right edge, instead of upper left ones (as by default).
- Convert the class `matrix_class()`, the engine running the plots, to C++ and connect it to the Python code (not sure how and would appreciate some help on this).

Internal Conventions
---------------------
- Change candlestick data name conventions, as requested in `Issue 148 <https://github.com/piccolomo/plotext/issues/148>`_.
- Add parameter on bar plot methods for custom texts above bars, as proposed in `Pull Request 164 <https://github.com/piccolomo/plotext/pull/164>`_.
- Unify names for `color` and `colors` parameters in `candlestick()`, `multiple_bar()`, etc.
- Change `coordinate` parameter to `x` and `y` in `hline()` and `vline()`.
- Change `strings_to_time()` to `strings_to_times()`.
- Decide on a general convention for method aliases.
- Change `frame` parameter to `show` in `frame()` method.
- Change count from 0 in command line tool `xcol` and `ycols` parameters for uniformity.

Documentation and Testing
-------------------------
- Add docstring for `string_to_time()` and `strings_to_times()`.
- Add unit testing, as suggested in `Issue 130 <https://github.com/piccolomo/plotext/issues/130>`_.
- Extend command line tool so that `man plotext` and `whatis plotext` are allowed.
