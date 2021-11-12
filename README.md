<p align="center">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png" /></p>

`plotext` plots directly on terminal, it has no dependencies and the syntax is very similar to `matplotlib`. It also provide a simple command line tool.

Here is an example of what you could output with `plotext`:
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)

Follow this menu for details on how to actually use this package.

## Main Menu

- [ Basic Plots ](https://github.com/piccolomo/plotext/blob/master/readme/basic.md) 
- [ Bar Plots ](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
- [ Datetime Plots ](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
- [ Plot Aspect ](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
- [ Matrix/Image Plots ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md)
- [ Multiple Subplots ](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)
- [ Other Utilities ](https://github.com/piccolomo/plotext/blob/master/readme/other.md)


## How to Installx
To install the latest version of `plotext` you could use:
```
pip install plotext --upgrade
```

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)




## Main Updates:
Note: there are many new features from the previous version, any bug report is useful and very welcomed.

  - entire code re-written
  - faster plotting
  - higher resolution 3 x 2 unicode mosaics markers (not available in windows)
  - new color codes which include 256 color codes and full RGB colors
  - multiple and stacked bar charts
  - datetime plot and scatter functions
  - datetime class added to better handle datetime object of most types
  - matrix plot
  - image plot
  - save plots also in color in html
  - file class added to better handle files and file paths
  - data can also be plotted on the upper x axis
  - unittest file added 
  - `xside` and `yside` parameters introduced for many functions
  - columns and rows span in subplots matrix
  - more clear functions added
  - option to limit or not the plot dimensions in both directions 
  - bar chart log scale solved on both axes
  - bar chart 0 value issue solved
  - legend extra character to identify on which axes each data is plotted
  - time() function added to check plotting computational time
  - xfreq() is now xfrequency(), yfreq() is yfrequency()
  - doc class added to easily access all functions doc-strings 
  - get_canvas() is not build()


[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)


## Future Plans
By request:

 - mosaic markers available on windows (not sure how)
 - remove grid span areas intersection problems
 - bar alignment 
 - finance function 
 - text widget to add labels to plot (not as easy as it sounds)
 - using numpy to handle the matrix of characters and colors (not sure if it will make a difference)
 - title styles
 - clear only printed lines done properly
 - hist plot log scale on y axes  
 - `hd` and `fhd` label ticks that adapts to plot or scatter function

Any help or new ideas are welcomed.


## Credits and Sources of Inspiration
 - user `jtplaarj` for the great ideas and codes regarding multiple and stacked bar plots [Issue #48]
 - user `ethack` for  requiring log scale on bar plot [Issue #37]
 - user `gregwa1953` for  inspiring `plt.limit_size()` [Issue #33]
 - user `rbanffy` for suggestion of using 3 x 2 unicode mosaic box characters [Issue #29].
 - user `henryiii` for unittest suggestion [Issue #32]
 - user `whisller` and `willmcgugan` for integration with `Rich` package [Issue #26]
 - user `garid3000` for the idea of a function that returns the plot canvas [Issue #20]
 - user `robintw` and `Sauci` for horizontal bar plot idea and code, respectively [Issue #16]
 - user `Zaneo` for multiple data set idea [Issue #13] 
 - user `Zaneo` for double axes idea [Issue #12] 
 - users `geoffrey-eisenbarth` and  `matthewhanson` for requesting datetime support [Issue #7]
 - user `kris927b` for requesting histogram plot [Issue #6]

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)


