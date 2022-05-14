<p align="left">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png" /></p>

- `plotext` plots **directly on terminal**,
- it allows for bar, histogram and date-time plots (including candlesticks),
- it can also plot images (including GIF) and stream videos (including YouTube) with audio,
- it has **no dependencies** (except for optional dependencies for image/video plotting),
- it provides a simple [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool),
- it can [save plots](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions) as text or as colored `html`,
- it provides a tool to [color strings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text).

![subplots](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)
Image code [here](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md).

## Install
- `pip install plotext` for normal installation, with `pip install plotext`,
- `pip install plotext --upgrade` to upgrade to the latest version,
- `pip install "plotext[image]"` to install the optional dependency for **image plotting** (including GIFs)
- `pip install "plotext[video]"` to install the optional dependencies for **video rendering**, which will also allow to plot images. 

Notes:

- the optional packages are `pillow` (for image plotting), `opencv-python` (for video rendering), `pafy` (to stream YouTube) and `ffpyplayer` (to stream audio).
- The command `pip install youtube-dl==2020.12.2` has helped with YouTube video rendering problems.


## Guide

#### Main Plots
- [Basic](https://github.com/piccolomo/plotext/blob/master/readme/basic.md) 
- [Bar](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
- [Datetime](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
- [Other](https://github.com/piccolomo/plotext/blob/master/readme/other.md)

#### Plotting Utilities
- [Settings](https://github.com/piccolomo/plotext/blob/master/readme/settings.md)
- [Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
- [Subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)

#### Image and Video Rendering
- [Image](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md)
- [Video](https://github.com/piccolomo/plotext/blob/master/readme/video.md)

#### Other
- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md)
- [Other Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)
-- [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md)