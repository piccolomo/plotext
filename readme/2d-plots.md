[Plotext Guide](https://github.com/piccolomo/plotext#guide)

# 2D Plots

- [Matrix Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#matrix-plot)
- [Image Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#image-plot)



## Matrix Plot

To plot a 2D pixelled representation of a matrix, use the function `plt.matrix_plot()`.

Here is a coded example:

```python
import plotext as plt

cols, rows = 200, 45
p = 1
matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]

plt.matrix_plot(matrix)
plt.plotsize(cols, rows)
plt.title("Matrix Plot")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; cols, rows = 200, 45; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/matrix.png)

Access the function `plt.matrix_plot()` documentation with `plt.doc.matrix_plot()`.

**Note**: The intensity of the pixel (how light it is) is proportional to the correspondent element in the matrix. 

**Note**: The same function can plot in colors if each pixel is an RGB tuple of three integers between 0 and 255.

[2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)



## Image Plot

To plot an image use `plt.image_plot(file_path)` with the following optional parameters:

- `marker`, to set the marker used to identify each pixel in the image. The default value is `sd`. Note that since all canvas will be covered with pixels, using the higher resolution markers (`hd` and `fhd`) will not result in an improved spatial resolution.

- `grayscale`: to plot in gray-scale.

- `size`: to resize the image before plotting; recommended for faster computation, especially for big pictures.

- `keep_ratio` to maintain (or not) the original image aspect ratio.

- `resample` to apply (or not) a smoothing algorithm during resizing (as by default).

The function returns the actual size of the image in unit of character pixels: it is recommended to use this size to later fix the plot size with `plt.plot_size()`.

Here is an example, where the image [`monalisa.jpg`](https://raw.githubusercontent.com/piccolomo/plotext/master/images/monalisa.jpg) should be placed is in the script folder:

```python
import plotext as plt

path = plt.file.join_paths(plt.file.script_folder(), 'mj.jpg')

size = [200, 60]
size = plt.image_plot(path, size = size, keep_ratio = True)

plt.plotsize(*size)
plt.title("Mona Lisa")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; path = plt.file.join_paths(plt.file.script_folder(), 'monalisa.jpg'); size = [200, 60]; size = plt.image_plot(path, size = size, keep_ratio = True); plt.plotsize(*size); plt.title('Mona Lisa'); plt.show()"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/image.png)

Access the function `plt.image_plot()` documentation with `plt.doc.image_plot()`.

**Note**: To easily manipulate file paths use the tools recommended in [File Utilities](https://github.com/piccolomo/plotext/blob/master/readme/file.md)

**Note**: To save the result, in colors, as an html page, use the function `plt.savefig()`.

[2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)