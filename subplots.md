# Multiple Subplots

To plot a grid of subplots, use the following main functions:

 - `plt.subplots(rows, cols)` to creates a matrix of subplots with the given number of rows and columns.

 - `plt.subplot(row, col)` to access the subplot at the given row and column, counting (from 1) from the upper left corner of the matrix of plots.

 - `plt.span(rowspan, colspan)` to set how many rows and/or columns the current subplot should span in the matrix of subplots.

Here is a coded example, where the [`maryling.jpg`](https://raw.githubusercontent.com/piccolomo/plotext/master/images/marylin.jpg) and [`mj.jpg`](https://raw.githubusercontent.com/piccolomo/plotext/master/images/mj.jpg) files should be placed in the script folder.

```
import plotext as plt
import random
import yfinance as yf

plt.subplots(3, 3)

plt.subplot(1, 1)
l = 256
plt.plot(plt.sin(length = l), marker = "fhd", color = list(range(l)))
plt.title("Plot Colors")
plt.canvas_color((200,200,200)) # rgb coloring
plt.axes_color("bright-black")
plt.ticks_color("bright-yellow")

plt.subplot(1, 2)
pizzas = ["Pepperoni", "Sausage", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 10, 11, 8, 7, 4]
female_percentages = [12, 35, 30, 15, 2, 1]
plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")

plt.subplot(1, 3)
l = 3 * 10 ** 4
data1 = [random.gauss(0, 1) for el in range(10 * l)]
data2 = [random.gauss(3, 1) for el in range(6 * l)]
data3 = [random.gauss(6, 1) for el in range(4 * l)]
bins = 60
plt.hist(data1, bins, label="mean 0")
plt.hist(data2, bins, label="mean 3")
plt.hist(data3, bins, label="mean 6")
plt.title("Histogram Plot")

plt.subplot(2, 1)
plt.span(1, 2)
path = plt.file.join_paths(plt.file.script_folder(), 'mj.jpg')
size = [68, 38]
size = plt.image_plot(path, size = size, keep_ratio = 0)
plt.plotsize(*size)
plt.frame(True)
plt.title("Michael Jackson")

plt.subplot(2, 2)
plt.datetime.set_datetime_form(date_form = '%d/%m/%Y')
start = plt.datetime.string_to_datetime("11/07/2020")
end = plt.datetime.today.datetime
data = yf.download('goog', start, end)
prices = list(data["Close"])
dates = [plt.datetime.datetime_to_string(el) for el in data.index]
plt.plot_date(dates, prices)
plt.title("Google Stock Price")
plt.ylabel("$ Stock Price")

plt.subplot(3, 2)
cols, rows = 68, 20
p = 1
matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]
plt.matrix_plot(matrix)
plt.plotsize(cols, rows)
plt.title("Matrix Plot")

plt.subplot(2, 3)
plt.span(1, 2)
path = plt.file.join_paths(plt.file.script_folder(), 'marylin.jpg')
size = [68, 38]
size = plt.image_plot(path, size = size, keep_ratio = 0)
plt.plotsize(*size)
plt.frame(True)
plt.title("Marilyn Monroe")

plt.show()
```
or directly on terminal:
```
python3 -c "import plotext as plt; import random; import yfinance as yf; plt.subplots(3, 3); plt.subplot(1, 1); l = 256; plt.plot(plt.sin(length = l), marker = 'fhd', color = list(range(l))); plt.title('Plot Colors'); plt.canvas_color((200,200,200)); plt.axes_color('bright-black'); plt.ticks_color('bright-yellow'); plt.subplot(1, 2); pizzas = ['Pepperoni', 'Sausage', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 10, 11, 8, 7, 4]; female_percentages = [12, 35, 30, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.subplot(1, 3); l = 3 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)]; data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.subplot(2, 1); plt.span(1, 2); path = plt.file.join_paths(plt.file.script_folder(), 'mj.jpg'); size = [68, 38]; size = plt.image_plot(path, size = size, keep_ratio = 0); plt.plotsize(*size); plt.frame(True); plt.title('Michael Jackson'); plt.subplot(2, 2); plt.datetime.set_datetime_form(date_form = '%d/%m/%Y'); start = plt.datetime.string_to_datetime('11/07/2020'); end = plt.datetime.today.datetime; data = yf.download('goog', start, end); prices = list(data['Close']); dates = [plt.datetime.datetime_to_string(el) for el in data.index]; plt.plot_date(dates, prices); plt.title('Google Stock Price'); plt.ylabel('$ Stock Price'); plt.subplot(3, 2); cols, rows = 68, 20; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.subplot(2, 3); plt.span(1, 2); path = plt.file.join_paths(plt.file.script_folder(), 'marylin.jpg'); size = [68, 38]; size = plt.image_plot(path, size = size, keep_ratio = 0); plt.plotsize(*size); plt.frame(True); plt.title('Marilyn Monroe'); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)


[ Main Menu ](https://github.com/piccolomo/plotext#main-menu)
