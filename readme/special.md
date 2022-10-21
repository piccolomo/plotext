# Special Plots

- [Error Plot](https://github.com/piccolomo/plotext/blob/master/readme/special.md#error-plot)
- [Event Plot](https://github.com/piccolomo/plotext/blob/master/readme/special.md#event-plot)
- [Streaming Data](https://github.com/piccolomo/plotext/blob/master/readme/special.md#streaming-data)
- [Confusion Matrix](https://github.com/piccolomo/plotext/blob/master/readme/special.md#confusion-matrix)
- [Matrix Plot](https://github.com/piccolomo/plotext/blob/master/readme/special.md#matrix-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Error Plot

To plot data with error bars, along either or both the `x` and `y` axes use the `error()` function as in this example:

```python
import plotext as plt
from random import random 
l = 20
n = 1
ye = [random() * n for i in range(l)]; xe = [random() * n for i in range(l)]
y = plt.sin(length = l); 
plt.error(y, xerr = xe, yerr = ye)
plt.title('Error Plot')
plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; plt.clf();  from random import random; l = 20; n = 1; ye = [random() * n for i in range(l)]; xe = [random() * n for i in range(l)]; y = plt.sin(length = l); plt.error(y, xerr = xe, yerr = ye); plt.title('Error Plot'); plt.show();"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/error.png)

More documentation can be accessed with `doc.error()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Special Plots](https://github.com/piccolomo/plotext/blob/master/readme/special.md)

## Event Plot

To signal the timing of certain events the `event_plot()` function could be of use. Here is an example:

```python
import plotext as plt
from random import randint
from datetime import datetime, timedelta

plt.date_form("H:M") # also just "H" looks ok

times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)] # A random list of times during the day
times = plt.datetimes_to_string(times)

plt.plotsize(None, 20) # Set the preferred height or comment for maximum size 

plt.event_plot(times)

plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; from random import randint; from datetime import datetime, timedelta; plt.date_form('H:M'); times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)]; times = plt.datetimes_to_string(times); plt.plotsize(None, 20); plt.event_plot(times); plt.show()"
```

![datetime](https://raw.githubusercontent.com/piccolomo/plotext/master/data/eventplot.png)

More documentation can be accessed with `doc.event_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Special Plots](https://github.com/piccolomo/plotext/blob/master/readme/special.md)

## Streaming Data

When streaming a continuous flow of data, consider using the `sleep()` method, to reduce a possible screen flickering, and the clearing methods described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#clearing-functions).

Here is a coded example:

```python
import plotext as plt

l = 1000
frames = 200

plt.title("Streaming Data")
# plt.clc()

for i in range(frames):
    plt.clt() # to clear the terminal
    plt.cld() # to clear the data only

    y = plt.sin(periods = 2, length = l, phase = 2 * i  / frames)
    plt.scatter(y)

    #plt.sleep(0.001) # to add 
    plt.show()
```

or directly on terminal:

```console
python3 -c "import plotext as plt; l = 1000; frames = 200; plt.title('Streaming Data'); [(plt.cld(), plt.clt(), plt.plot(plt.sin(periods = 2, length = l, phase = 2 * i  / frames)), plt.sleep(0), plt.show()) for i in range(frames)]"
```

![example](https://raw.githubusercontent.com/piccolomo/plotext/master/data/stream.gif)

[Main Guide](https://github.com/piccolomo/plotext#guide), [Special Plots](https://github.com/piccolomo/plotext/blob/master/readme/special.md#basic-plots)

## Matrix Plot

To plot a 2D pixelled representation of a matrix, use the function `matrix_plot()`. 

- The intensity of the pixel (how light it is) is proportional to the correspondent element in the matrix.

- The parameter `fast`, if set to True, allows to plot much faster, but the plot final dimensions will be locked to the whatever size was previously chosen, and won't adapt to the terminal or subplot size; also any setting function which follows will not have any effect (like `xlabel()`, `frame()` and so on).

- The same function can **plot in colors**, if each pixel is an RGB tuple of three integers, between 0 and 255.

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

![matrix](https://raw.githubusercontent.com/piccolomo/plotext/master/data/matrix.png)

More documentation can be accessed with `doc.matrix_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Special Plots](https://github.com/piccolomo/plotext/blob/master/readme/special.md#matrix-plots)

## Confusion Matrix

To plot the [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) correspondent to certain actual and predicted observations, use the `confusion_matrix()` function - in short `cmatrix()` - as in this example:

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

More documentation can be accessed with `doc.confusion_matrix()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Special Plots](https://github.com/piccolomo/plotext/blob/master/readme/special.md#matrix-plots)
