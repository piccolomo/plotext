<p align="left">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png" /></p>

`plotext` plots directly on terminal: the syntax is very similar to `matplotlib`, it has no dependencies (except for optional dependencies for image/video plotting) and can [save plots](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions) as text or as colored `html`.

It also provides a simple [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool) and a function to [color strings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text).

![subplots](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)
Image code [here](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md).

## Install

As usual, with:
```console
pip install plotext
```
To upgrade to the latest version, with ```pip install plotext --upgrade```.

To install the optional dependency necessary (`pillow`) to plot images (including GIFs), use:
```console
pip install "plotext[image]"
```
To install the optional dependencies (`pillow`, `pafy`, `opencv-python`, `ffpyplayer`) necessary to play videos, use:
```console
pip install "plotext[video]"
```
which will also allow to plot images. 
The command `pip install youtube-dl==2020.12.2` has helped me with youtube video rendering problems.


## Guide

- [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md) 
    - [Scatter Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
    - [Line Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot)
    - [Stem Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#stem-plot)
    - [Multiple Data Sets](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-data-sets)
    - [Multiple Axes Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#multiple-axes-plot)
    - [Log Plot](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#log-plot)
    - [Streaming Data](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#streaming-data)
    
- [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
    - [Simple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#simple-bar-plot)
    - [Horizontal Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#horizontal-bar-plot)
    - [Sketchy Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#sketchy-bar-plot)
    - [Multiple Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#multiple-bar-plot)
    - [Stacked Bar Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#stacked-bar-plot)
    - [Histogram Plot](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot)

- [Datetime Plots](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
    - [Datetime Utilities](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-utilities)
    - [Basic Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#basic-plot)
    - [Candlestick Plot](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#candlestick-plot)

- [Plot Tools](https://github.com/piccolomo/plotext/blob/master/readme/tools.md)
    - [Event Plot](https://github.com/piccolomo/plotext/blob/master/readme/tools.md#event-plot)
    - [Extra Lines](https://github.com/piccolomo/plotext/blob/master/readme/tools.md#extra-lines)
    - [Text Plot](https://github.com/piccolomo/plotext/blob/master/readme/tools.md#text-plot)

- [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
    - [Plot Size](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-size)
    - [Plot Labels](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels)
    - [Plot Limits](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-limits)
    - [Axes Ticks](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#axes-ticks)
    - [Plot Lines](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines)
    - [Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors)
    - [Markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers)

- [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md)
    - [Matrix Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#matrix-plot)
    - [Image Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#image-plot)
    - [GIF Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#gif-plot)

- [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)
    - [Video Plot](https://github.com/piccolomo/plotext/blob/master/readme/video.md#video-plot)
    - [Play YouTube](https://github.com/piccolomo/plotext/blob/master/readme/video.md#play-youtube)

- [Multiple Subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)

- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md)
    - [Command Line Tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool)
    - [Colored Text](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text)
    - [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities)
    - [Clear Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clear-functions)
    - [Other Functions](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions)
    - [Docstrings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#docstrings)

- [Other Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)
    - [Rich](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#rich)
    - [Tkinter](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter)

- [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md)
    - [Main Updates](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#main-updates)
    - [Future Plans](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#future-plans)
    - [Credits](https://github.com/piccolomo/plotext/blob/master/readme/notes.md#credits)


