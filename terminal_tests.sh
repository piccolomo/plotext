### Scatter
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"
### Line
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"
### Stem
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y, fillx = True); plt.title('Stem Plot'); plt.show()"
### Multiple Data
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(phase = -1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter'); plt.title('Multiple Data Set'); plt.show()"
### Multiple Axis
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside= 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside= 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"
### Log
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; l = 10 ** 4; x = range(1, l + 1); y = plt.sin(1, 2, l); plt.plot(x, y); plt.xscale('log'); plt.yscale('linear'); plt.grid(1, 0); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show()"
### Stream
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; l = 1000; x = range(1, l + 1); frames = 50; plt.title('Streaming Data'); plt.clc(); [(plt.cld(), plt.clt(), plt.plot(x, plt.sin(1, periods = 2, length = l, phase = 2 * i  / frames), marker = 'dot'), plt.sleep(0), plt.show()) for i in range(frames)]"
### Bar
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Most Favored Pizzas in the World'); plt.show()"
### Horizontal Bar
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h'); plt.title('Most Favored Pizzas in the World'); plt.show()"
### Multiple Bar
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
### Stacked Bar
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
### Hist Plot
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; import random; l = 7 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)];  data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.show()"
### Datetime
python3 -c "print('\npress for next text'); input()"
python3 -c "import yfinance as yf; import plotext as plt; plt.datetime.set_datetime_form(date_form='%d/%m/%Y'); start = plt.datetime.string_to_datetime('11/07/2020'); end = plt.datetime.today.datetime; data = yf.download('goog', start, end); prices = list(data['Close']); dates = [plt.datetime.datetime_to_string(el) for el in data.index]; plt.plot_date(dates, prices); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
### Limits
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; l = 1000; x = range(1, l + 1); y = plt.sin(lenfth = 1000); plt.scatter(x, y); plt.xlim(x[0] - 101, x[-1] + 100); plt.ylim(-1.2, 1.2); plt.show()"
### Ticks
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; l, p = 1000, 3; y = plt.sin(periods = p, length = l); plt.scatter(y); xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.show()"
### Labels
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; plt.plot(plt.sin()); plt.plot_size(150, 45); plt.frame(True); plt.grid(True); plt.title('Plot Title'); plt.xlabel('Lower'); plt.ylabel('Left'); plt.xlabel('Upper', xside = 'upper'); plt.ylabel('Right', yside = 'right'); plt.show()"
### Colors
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; l = 256; plt.plot(plt.sin(length = l), marker = 'fhd', color = list(range(l))); plt.title('Plot Colors'); plt.canvas_color(254); plt.axes_color((20, 40, 100)); plt.ticks_color('bright-yellow'); plt.plot_size(150, 45); plt.show()"
### Matrix
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; cols, rows = 200, 45; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.show()"
### Image
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; path = plt.file.join_paths(plt.file.script_folder(), 'monalisa.jpg'); size = [200, 60]; size = plt.image_plot(path, size = size, keep_ratio = True); plt.plotsize(*size); plt.title('Mona Lisa'); plt.show()"
### Subplots
python3 -c "print('\npress for next text'); input()"
python3 -c "import plotext as plt; import random; import yfinance as yf; plt.subplots(3, 3); plt.subplot(1, 1); l = 256; plt.plot(plt.sin(length = l), marker = 'fhd', color = list(range(l))); plt.title('Plot Colors'); plt.canvas_color(254); plt.axes_color((20, 40, 100)); plt.ticks_color('bright-yellow'); plt.subplot(1, 2); pizzas = ['Pepperoni', 'Sausage', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 10, 11, 8, 7, 4]; female_percentages = [12, 35, 30, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.subplot(1, 3); l = 3 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)]; data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.subplot(2, 1); plt.span(1, 2); path = plt.file.join_paths(plt.file.script_folder(), 'mj.jpg'); size = [68, 38]; size = plt.image_plot(path, size = size, keep_ratio = 0); plt.plotsize(*size); plt.frame(True); plt.title('Michael Jackson'); plt.subplot(2, 2); plt.datetime.set_datetime_form(date_form = '%d/%m/%Y'); start = plt.datetime.string_to_datetime('11/07/2020'); end = plt.datetime.today.datetime; data = yf.download('goog', start, end); prices = list(data['Close']); dates = [plt.datetime.datetime_to_string(el) for el in data.index]; plt.plot_date(dates, prices); plt.title('Google Stock Price'); plt.ylabel('$ Stock Price'); plt.subplot(3, 2); cols, rows = 68, 20; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.subplot(2, 3); plt.span(1, 2); path = plt.file.join_paths(plt.file.script_folder(), 'marylin.jpg'); size = [68, 38]; size = plt.image_plot(path, size = size, keep_ratio = 0); plt.plotsize(*size); plt.frame(True); plt.title('Marilyn Monroe'); plt.show()"
