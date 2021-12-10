<p align="left">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png" /></p>

`plotext` plots directly on terminal and the syntax is very similar to `matplotlib`. It has no dependencies (except for an optional dependency required for image plotting).
It also provide a simple command line tool.

This is what you could output on terminal with `plotext`:
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)

For details on how to use the package, follow this menu.


## How to Install
To install the latest version of `plotext` you can use:
```
pip install plotext
```
and to upgrade to the latest version `pip install plotext --upgrade`.

In order to install the optional dependency necessary to plot images, use:

```
pip install plotext[image]
```

Which will make sure that the package `pillow` is installed. 


[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Main Menu

- [ Basic Plots ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md) 
- [ Bar Plots ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
- [ Datetime Plots ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
- [ Plot Aspect ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
- [ Matrix/Image Plots ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md)
- [ Multiple Subplots ](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)
- [ Other Utilities ](https://github.com/piccolomo/plotext/blob/master/readme/other.md)



## Main Updates:
Note: there are many new features from the previous version, any bug report is useful and very welcomed.

From version 4.0.0:

 - fixed bar error reported in [ Issue 61 ](https://github.com/piccolomo/plotext/issues/61) by user `SoyBison`
 - added exception when subplots size is bigger then default ([ Issue 60 ](https://github.com/piccolomo/plotext/issues/60))
 - `pillow` is now an optional dependency [ Issue 56 ](https://github.com/piccolomo/plotext/issues/56)
 - `numpy` is no longer a dependency (not even optional)
 - `platform` function changed, as recommended by user `crisluengo` in [ Issue 55 ](https://github.com/piccolomo/plotext/issues/55)
 - `shell` function and parameter removed as found to be useless
 - all `.md` files corrected and integrated

From versions 3:

  - entire code re-written
  - faster plotting
  - 2 x 2 marker is now called `hd` (as for *high resolution*) instead of `small`
  - added higher resolution 3 x 2 unicode mosaics markers (not available in windows), called `fhd` (as for *full high resolution*)
  - added new color codes, which include 256 color codes and full RGB colors
  - added multiple and stacked bar charts
  - added datetime scatter and plot functions
  - added datetime class to better handle most datetime objects
  - added `matrix_plot()` function
  - added `image_plot()` to plot images from file path
  - plots now can also be saved in color using `.html` extension
  - added file class to better handle files and file paths
  - data can now also be plotted on the upper x axis
  - `unittest` file added called `test.py`
  - `xside` and `yside` parameters introduced for many related functions
  - `span()` function added to span columns and rows in the matrix of subplots
  - added more `clear` functions
  - added function `limit_size()` to limit or not the plot dimensions to the terminal size
  - bar chart log scale issue solved on both axes
  - bar chart 0 value issue solved
  - added optional legend extra characters to identify on which axes each data is plotted
  - `time()` function added to check plotting computational time
  - `xfreq()` is now `xfrequency()`, `yfreq()` is `yfrequency()`
  - added doc class to easily access all functions doc-strings 
  - `get_canvas()` is now `build()`


[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)


## Future Plans

 - finalize the command tool created by `asartori86` and discussed in [ Issue 47 ](https://github.com/piccolomo/plotext/issues/47) to handle more options, settings and funtions
 - guide for integration with package `rich`, as discussed in [ Issue 26 ](https://github.com/piccolomo/plotext/issues/26)
 - guide for `tkinter` integration, as discussed in [ Issue 33 ](https://github.com/piccolomo/plotext/issues/33)
 - mosaic markers available on windows (not sure how)
 - remove grid span areas intersection problems
 - bar alignment option
 - finance function (?)
 - text widget to add labels to plot (not as easy as it sounds)
 - using `numpy` to make plotting faster (not sure if it will make a difference)
 - title styles
 - clear only printed lines, done properly
 - `hist` plot log scale on y axes 
 - `hd` and `fhd` label ticks that adapts to plot or scatter function

Any help or new ideas are welcomed.

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)


## Credits and Sources of Inspiration
 - user `asartori86` for the awesome command line tool [ Issue 47 ](https://github.com/piccolomo/plotext/issues/47)
 - user `jtplaarj` for the great ideas and codes regarding multiple and stacked b⎄ar plots: [ Issue 48 ](https://github.com/piccolomo/plotext/issues/48)
 - user `ethack` for  requiring log scale on bar plot: [ Issue 37 ](https://github.com/piccolomo/plotext/issues/37)
 - user `gregwa1953` for  inspiring `plt.limit_size()`: [ Issue 33 ](https://github.com/piccolomo/plotext/issues/33)
 - user `rbanffy` for suggestion of using 3 x 2 unicode mosaic box characters: [ Issue 29 ](https://github.com/piccolomo/plotext/issues/29).
 - user `henryiii` for unittest suggestion: [ Issue 32 ](https://github.com/piccolomo/plotext/issues/32)
 - user `whisller` and `willmcgugan` for integration with `Rich` package: [ Issue 26 ](https://github.com/piccolomo/plotext/issues/26)
 - user `garid3000` for the idea of a function that returns the plot canvas: [ Issue 20 ](https://github.com/piccolomo/plotext/issues/20)
 - user `robintw` and `Sauci` for horizontal bar plot idea and code, respectively: [ Issue 16 ](https://github.com/piccolomo/plotext/issues/16)
 - user `Zaneo` for multiple data set idea: [ Issue 13 ](https://github.com/piccolomo/plotext/issues/13)
 - user `Zaneo` for double axes idea: [ Issue 12 ](https://github.com/piccolomo/plotext/issues/12)
 - users `geoffrey-eisenbarth` and  `matthewhanson` for requesting datetime support: [ Issue 7 ](https://github.com/piccolomo/plotext/issues/7)
 - user `kris927b` for requesting histogram plot: [ Issue 6 ](https://github.com/piccolomo/plotext/issues/6)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)