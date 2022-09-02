# Matrix Plots
- [Matrix Plot](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md#matrix-plot)
- [Confusion Matrix](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md#confusion-matrix)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Matrix Plot
To plot a 2D pixelled representation of a matrix, use the function `matrix_plot(matrix)`. Here is a coded example:
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
![matrix](https://raw.githubusercontent.com/piccolomo/plotext/master/data/matrix.png)

- The intensity of the pixel (how light it is) is proportional to the correspondent element in the matrix,
- the parameter `fast`, if set to True, allows to plot much faster, but the plot final dimensions will be locked to the whatever size was previously chosen, and won't adapt to the terminal or subplot size; also any setting function which follows will not have any effect (like `xlabel()`, `frame()` and so on),
- the same function can **plot in colors**, if each pixel is an RGB tuple of three integers, between 0 and 255,
- access the full documentation of the function `plt.matrix_plot()` with `plt.doc.matrix_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Matrix Plots](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md#matrix-plots)


## Confusion Matrix
To plot the confusion matrix correspondent to certain actual and predicted observations, use the `confusion_matrix()` function - `cmatrix()` in short - as in this example:

```python
import plotext as plt; plt.clf()
from random import randrange
l = 300
actual = [randrange(0, 4) for i in range(l)]
predicted = [randrange(0,4) for i in range(l)]
labels = ['Autumn', 'Spring', 'Summer', 'Winter']

plt.cmatrix(actual, predicted, labels)
plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; from random import randrange; l = 300; actual = [randrange(0, 4) for i in range(l)]; predicted = [randrange(0,4) for i in range(l)]; labels = ['Autumn', 'Spring', 'Summer', 'Winter']; plt.cmatrix(actual, predicted, labels); plt.show()"
```
![cmatrix](https://raw.githubusercontent.com/piccolomo/plotext/master/data/cmatrix.png)

Access the full documentation of the function `plt.confusion_matrix()` with `plt.doc.confusion_matrix()`.


[Main Guide](https://github.com/piccolomo/plotext#guide), [Matrix Plots](https://github.com/piccolomo/plotext/blob/master/readme/matrix.md#matrix-plots)