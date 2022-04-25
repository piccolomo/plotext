# 2D Plots

- [Matrix Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#matrix-plot)
- [Image Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#image-plot)
- [GIF Plot](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#gif-plot)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)


## Matrix Plot

To plot a 2D pixelled representation of a matrix, use the function `matrix_plot()`. Here is a coded example:

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
![matrix](https://raw.githubusercontent.com/piccolomo/plotext/master/images/matrix.png)

- The intensity of the pixel (how light it is) is proportional to the correspondent element in the matrix. 

- The same function can **plot in colors** if each pixel is an RGB tuple of three integers, between 0 and 255.

- Future development (under request) may include a side bar to link the pixel intensity to its actual value in the matrix. 

- Access the full documentation of the function `plt.matrix_plot()` with `plt.doc.matrix_plot()`.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)



## Image Plot

To plot an image use the function `image_plot()` as in this example:

```python
import plotext as plt
plt.image_plot(plt.test_image_path)
plt.title("The Creation by Michelangelo")
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.image_plot(plt.test_image_path); plt.title('The Creation by Michelangelo'); plt.show()"
```

![image](https://raw.githubusercontent.com/piccolomo/plotext/master/images/image.png)

- It is recommended to use the function `plotsize()` before `image_plot()`, especially for larger images, to reduce the image size and so the computational load.

- The parameter `fast`, if `True`, allows to plot much faster, but the plot final dimensions will be locked to the whatever size was previously chosen, and won't adapt to the terminal or subplot size.

- A curious visual effect is obtained using for example `marker = list("Creation")` with `style = 'inverted'`: try it out!

- Use the parameter `grayscale` to plot in gray-scale.

- To easily manipulate file paths, use the tools recommended in [this section](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities).

- To save the result **in colors**, as an `html` page, use the function `plt.savefig()`.

- To plot images **beyond the terminal size** use the function `plt.limit_size()` or the app developed [here](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter), using `tkinter`.

- Access the full documentation of the function `plt.image_plot()` with `plt.doc.image_plot()`.


## Gif Plot

To plot a GIF image use the function `play_gif()` as in this example:

```python
import plotext as plt
plt.play_gif(plt.test_gif_path)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.play_gif(plt.test_gif_path); plt.show()"
```
which will play the following GIF:

![image](https://raw.githubusercontent.com/piccolomo/plotext/master/images/homer.gif)


[Plotext Guide](https://github.com/piccolomo/plotext#guide), [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)