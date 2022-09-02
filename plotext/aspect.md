# Plot Aspect
- [Plot Labels](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-labels)
- [Plot Lines](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-lines)
- [Markers](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#markers)
- [Colors](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors)
- [Styles](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#styles)
- [Themes](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#themes)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Plot Labels
You could easily add the following text labels to the plot:

- a **title** on the top of the active plot with `title(label)`,
- the **x axes labels** with `xlabel(label)`: its parameter `xside` is used to address a specific `x` axis, `lower` or `upper` - in short `1` or `2`,
- analogously the **y axes labels** with `ylabel(label)`: `yside` parameter, is used to address a specific `y` axis , `left` or `right` - in short `1` or `2`,
- the axes labels will all appear at the bottom of the plot, with the exception of the upper `x` axis label, which will appear on the top center of the plot, moving the plot title to the top left, if present,
- to change the labels colors and styles, use the functions `ticks_colors()` and `ticks_style()`, as explained in [this section](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#colors).

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Plot Lines
Here are the main functions used to alter the plot lines:
- `xaxes(lower, upper)` to set whatever or not to show the `x` axes; it accepts two Boolean inputs, one for each `x` axis,
- `yaxes(left, right)` to set whatever or not to show the `y` axes; it accepts two Boolean inputs, one for each `y` axis,
- to control all axes simultaneously, use the function `frame(frame)` instead, which will show or remove the **plot frame** (composed of all 4 axes); it require a single Boolean,
- the function `grid(horizontal, vertical)` is used to add or remove the horizontal and vertical grid lines and requires two Boolean inputs,
- to add extra lines at some specific coordinates use the functions `vertical_line()` and `horizontal_line()`, as explained in [this section](https://github.com/piccolomo/plotext/blob/master/readme/other.md#line-plot).


[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Markers
To specify which marker to use, for a data point, use the parameter `marker`, available for most plotting functions, eg: `scatter(data, marker = "x")`. You could provide the following:

- a **single character**; if the space character, the plot will be invisible,
- a **list of specific markers**, one for each data point: its length will automatically adapt to the data set,
- one of the following **marker codes** which will translate in the marker specified (some may not be available in Windows): 
  ![markers](https://raw.githubusercontent.com/piccolomo/plotext/master/data/markers.png)
- the marker code `sd` stands for *standard definition*,
- **`hd`** stands for *high definition*, which uses the 2 x 2 unicode block characters, such as ▞,
- **`fhd`** stands for *full high definition*, which uses the 3 x 2 unicode block characters, such as 🬗; this marker works only in Unix systems and only in some terminals,
- **`braille`** uses the 4 x 2 unicode braille characters, such as ⢕, this marker should works in Unix systems (tested only in few terminals),
- it is possible to have markers of different resolutions in the same canvas, but it is recommended not to mix them when using line plots (i.e. using the function `plot()`) in the same signal, while it is safe to mix them with a normal scatter plot,
- access the function `markers()` for the available marker codes.

   - the default `hd` marker (the 2 x 2 higher definition marker) is available only in `Unix` systems, as it doesn't seem to render well in Windows,
   - the 3 x 2 higher definition marker, named `fhd`, works only in `Unix` systems and only in some terminals,
   - the 4 x 2 highest definition marker, named `braille`, is now available (from version 5.1) and should work in Unix systems.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Colors
Colors could easily applied to the entire plot, using the following functions:

- `canvas_color(color)` to set the background color of the plot canvas alone (the area where the data is plotted),
- `axes_color(color)` to sets the background color of the axes, axes numerical ticks, axes labels and plot title,
- `ticks_color(color)` sets the (fullground) color of the axes ticks, the grid lines, title, and legend labels, if present,
- `ticks_style(style)` sets the style of the axes ticks, title, and legend labels, if present.

Here are the types of color codes that could be provided to the `color` parameter of the previous functions, as well as the `fullground` or `background` parameter of the function `colorize()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text):
- the following **color string codes**:\
![color-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/color-codes.png)
   - note: `default` will use the default terminal color,
- an **integer between 0 and 255**, resulting in the following colors:
![integer-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/integer-codes.png)
   - note: the first 16 integer color codes produce the same results as the string color codes,
- an **RGB color** consisting of a tuple of three values (red, green, blue), each between 0 and 255, to obtain the most realistic color rendering,
- a **list of color codes** to give a different color to each plot marker: the length of the list of colors will adapt to the length of the data set; each color could be of a different kind (string, integer or rgb),
- access the function `colors()` for the available string and integer codes.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Styles
These are the available **style codes** that could be provided to the `style` parameter of any plotting function, including `colorize()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#colored-text):

![style-codes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/styles.png)
- any combination of styles could be used at the same time, provided they are separated by a space,
- using `flash` will result in an actual white flashing marker,
- access the function `styles()` for the available style codes.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)


## Themes
To quickly chose a favoured color combination, for the entire figure or one of its subplot, use the function `theme()`. The available themes could be displayed with the function `themes()`; here is its output: 
![themes](https://raw.githubusercontent.com/piccolomo/plotext/master/data/themes.png)
- to remove all plot colors and styles from the current subplot, use the function `clear_color()`, in short `clc()`, which is equivalent to `theme('clear')`,
- to add, tweak, rename any theme presented, please feel free to open an issue, dropping your favourite combination of canvas, axes, ticks color and style together with 3 signal colors in sequence: any idea is welcomed,

[Main Guide](https://github.com/piccolomo/plotext#guide), [Plot Aspect](https://github.com/piccolomo/plotext/blob/master/readme/aspect.md#plot-aspect)
