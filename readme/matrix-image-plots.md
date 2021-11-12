# Matrix/Image Plots

- [ Matrix Plot ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md#matrix-plot)
- [ Image Plot ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md#image-plot)

[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)



## Matrix Plot

To plot a 2D pixelled representation of a matrix, use the function `plt.matrix_plot()`.

Here is a coded example:

```
import plotext as plt

cols, rows = 100, 30
matrix = range(rows * cols)
matrix = [[matrix[cols * r + c] for c in range(cols)] for r in range(rows)]


plt.matrix_plot(matrix)
plt.plotsize(cols, rows)
plt.show()
```
The intensity of the pixel (how white it is) is proportional to the correspondent element in the matrix. 

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/matrix.png)

[ Matrix/Image Menu ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md#matriximage-plots)



## Image Plot

To plot an image use `plt.image_plot(path)` with the following optional parameters:

- `marker`, to set the marker used to identify each pixel in the plot. The default value is `sd`. Note that since all canvas will be covered with pixels, using the higher resolution markers (`hd` and `fhd`) will not result in an improved spatial resolution.

- `grayscale`: to plot in gray-scale.

- `size`: to resize the image before plotting; recommended for faster computation, expecially for big pictures.

- `keep_ratio` to maintain (or not) the original image aspect ratio.

- `resample` to apply (or not) a smoothing algorithm during resizing (default is True).

The function returns the actual size of the image in unit of character pixels: it is recommended to use this size to later fix the plot size with `plt.plot_size()`.

Here is an example, where the image `maryling.jpg` is in the script folder:

```
import plotext as plt

path = plt.file.join_paths(plt.file.script_folder(), 'marylin.jpg')

size = [200, 60]
size = plt.image_plot(path, size = size, keep_ratio = True)

plt.plotsize(*size)
plt.show()
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/image.png)

[ Matrix/Image Menu ](https://github.com/piccolomo/plotext/blob/master/readme/matrix-image-plots.md#matriximage-plots)
