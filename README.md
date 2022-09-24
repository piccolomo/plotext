<p align="left">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/data/logo.png" /></p>

`plotext` **plots directly on terminal**
- it allows for [scatter](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot), [line](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#line-plot), [bar](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#simple-bar-plot), [histogram](https://github.com/piccolomo/plotext/blob/master/readme/bar.md#histogram-plot) and [date-time](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#datetime-plot) plots (including [candlestick](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md#candlestick-plot)),
- it can also plot [error bars](https://github.com/piccolomo/plotext/blob/master/readme/other.md#error-plot), [confusion matrices](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md#confusion-matrix), and add extra [text](https://github.com/piccolomo/plotext/blob/master/readme/other.md#text-plot), [lines](https://github.com/piccolomo/plotext/blob/master/readme/other.md#line-plot) and [shapes](https://github.com/piccolomo/plotext/blob/master/readme/other.md#shape-plot) to the plot, 
- you could use it to [plot images](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plot) (including [GIFs](https://github.com/piccolomo/plotext/blob/master/readme/image.md#gif-plot)) and [stream video](https://github.com/piccolomo/plotext/blob/master/readme/video.md#video-plot) with audio (including [YouTube](https://github.com/piccolomo/plotext/blob/master/readme/video.md#play-youtube)),
- it has **no dependencies** (except for optional dependencies for image/video plotting),
- it provides a simple [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool),
- it can [save plots](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions) as text or as colored `html`,
- it provides a tool to [color strings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text).

![subplots](https://raw.githubusercontent.com/piccolomo/plotext/master/data/subplots.png)
image code [here](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md#subplots)


## Install
- `pip install plotext` for normal installation,
- `pip install plotext --upgrade` to upgrade to the latest PyPi version,
- `pip install "plotext[image]"` to install the optional dependency for **image plotting** (including GIFs),
- `pip install "plotext[video]"` to install the optional dependencies for **video rendering**, which will also allow to plot images,
- `pip install "plotext[completion]"` to allow TAB completion in the [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool) (under development),
- `pip install git+https://github.com/piccolomo/plotext`, to install the [GitHub version](https://github.com/piccolomo/plotext), if more updated and you feel courageous,
   - `pip install "plotext[image] @ git+https://github.com/piccolomo/plotext.git"` to include image plotting dependencies,
   - `pip install "plotext[video] @ git+https://github.com/piccolomo/plotext.git"` to include video plotting dependencies,
   - `pip install "plotext[completion] @ git+https://github.com/piccolomo/plotext.git"` to include the TAB completion dependency,
- the optional packages are `pillow` (for image plotting), `opencv-python` (for video rendering), `ffpyplayer` (to stream audio), `pafy` and `youtube-dl` (to stream YouTube), `shtab` (for TAB completion),
- use the function `test()` to quickly test (up to image rendering) your newly installed version of `plotext`: any issue report is very welcomed. This function will download and finally remove a test image.
- created and tested in Ubuntu 22.04 and Python 3.10,



## Guide


#### Main Plots
- [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md)
- [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
- [Datetime Plots](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
- [Other Plots](https://github.com/piccolomo/plotext/blob/master/readme/other.md)

#### Plotting Utilities
- [Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)
- [Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
- [Subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)

#### 2D Plots
- [Matrix Plots](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md)
- [Image Plots](https://github.com/piccolomo/plotext/blob/master/readme/image.md)
- [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)


#### Other Resources
- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md)
- [Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)
- [Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md)