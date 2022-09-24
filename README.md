<p align="left">  <img src="https://raw.githubusercontent.com/piccolomo/plotext/master/images/logo.png" /></p>

`plotext` plots directly on terminal: the syntax is very similar to `matplotlib`, it has no dependencies (except for an optional dependency required for image plotting) and can [save plots](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#other-functions) as text or as colored `html`.

It also provides a simple [command line tool](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool) and a function to [color strings](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text).

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)
Image code [here](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md).


## Guide

- [Basic Plots](https://github.com/piccolomo/plotext/blob/master/readme/basic.md) 
- [Bar Plots](https://github.com/piccolomo/plotext/blob/master/readme/bar.md)
- [Datetime Plots](https://github.com/piccolomo/plotext/blob/master/readme/datetime.md)
- [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md)
- [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md)
- [Multiple Subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md)
- [Utilities](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md)
- [Other Environments](https://github.com/piccolomo/plotext/blob/master/readme/environments.md)
- [Project Notes](https://github.com/piccolomo/plotext/blob/master/readme/notes.md)


## Install

As usual, with:
```console
pip install plotext
```
To upgrade to the latest version, with ```pip install plotext --upgrade```.

To install the optional dependency necessary to plot images, use:
```console
pip install "plotext[image]"
``` 
which will make sure that the package `pillow` is installed.