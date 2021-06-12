### Scatter Plot
python3 -m plotext "import plotext as plt; y = plt.sin(100, 3); plt.scatter(y); plt.plotsize(100, 30); plt.title('Scatter Plot Example'); plt.show()"


### Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; y = plt.sin(100, 3); plt.plot(y); plt.plotsize(100, 30); plt.title('Plot Example'); plt.show()"


### Log Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; l = 10 ** 4; x = range(1, l + 1); y = plt.sin(l, 2); plt.plot(x, y); plt.plotsize(100, 30); plt.xscale('log'); plt.yscale('linear'); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.grid(1, 0); plt.show()"

### Stem Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; y = plt.sin(50, 2); plt.scatter(y, fillx = True); plt.plotsize(100, 30); plt.title('Stem Plot'); plt.show()"


### Multiple Data Set
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; y1 = plt.sin(1000, 3); y2 = plt.sin(1000, 3, 1.5, phase = 1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter', marker = 'small'); plt.plotsize(100, 30); plt.title('Multiple Data Set'); plt.show()"


### Double Y Axis
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; y1 = plt.sin(1000, 3); y2 = [2 * el for el in plt.sin(1000, 1, 0, phase = 1)]; plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter', marker = 'small', yaxis = 'right'); plt.plotsize(100, 30); plt.title('Double Y Axis'); plt.ylabel('left axis', 'right axis'); plt.show()"


### Bar Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; cities = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mexico City', 'Cairo', 'Mumbai', 'Beijing']; population = [37400068, 28514000, 25582000, 21650000, 21581000, 20076000, 19980000, 19618000]; plt.bar(cities, population); plt.plotsize(100, 30); plt.title('Bar Plot of the World Largest Cities'); plt.xlabel('City'); plt.ylabel('Population'); plt.show()"


### Hist Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; import random; l = 10 ** 3; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)]; data3 = [random.gauss(6, 1) for el in range(4 * l)]; plt.clp(); bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.xlabel('data bin'); plt.ylabel('frequency'); plt.plotsize(100, 30); plt.show()"


### Ticks
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; l, n = 1000, 3; y1 = plt.sin(l, n); y2 = plt.sin(l, n, 2); import numpy as np; xticks = np.arange(0, l + l / (2 * n), l / (2 * n)); xlabels = [str(i) + 'π' for i in range(2 * n + 1)]; plt.scatter(y1, label = 'periodic signal'); plt.scatter(y2, label = 'decaying signal', marker = 'small', color = 'gold'); plt.plotsize(100, 30); plt.ticks(None, 3); plt.xticks(xticks, xlabels); plt.show()"


### Date-Time Plot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; plt.clp(); dates = ['01/01/2021 12:20', '02/01/2021 15:40', '03/01/2021 15:10', '04/01/2021 15:24', '05/01/2021', '05/01/2021 18:10', '05/01/2021 23:20', '06/01/2021 12:10','07/01/2021']; prices = [100, 110, 130, 140, 150, 160, 170, 180]; dates_x = [plt.string_to_time(el) for el in dates]; plt.plot(dates_x, prices, marker = '.'); plt.scatter(dates_x, prices, marker = 'small'); plt.xticks(dates_x, dates); plt.title('Date-Time Plot'); plt.xlabel('Date-Time'); plt.ylabel('Stock Price $'); plt.plotsize(100, 30); plt.show()"


### Plot Limits
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; l, n = 1000, 2; x = range(1, l + 1); y = plt.sin(l, n); plt.scatter(x, y, color = 'indigo'); plt.xlim(x[0] - 101, x[-1] + 100); plt.ylim(-1.2, 1.2); plt.plotsize(100, 30); plt.show()"


### Plot Aspect
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; l, n = 1000, 2; x = range(1, l + 1); y = plt.sin(l, n); plt.plot(x, y, label = 'periodic signal', color = 'violet', marker = 'small'); plt.plotsize(100, 30); plt.grid(True); plt.title('Plot Style Example'); plt.xlabel('x axis label'); plt.ylabel('y axis label'); plt.canvas_color('white'); plt.axes_color('cloud'); plt.ticks_color('iron'); plt.xaxes(1, 0); plt.yaxes(1, 0); plt.ticks(10); plt.show()"


### Subplot
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; l, n = 1000, 5; y = plt.sin(l, n); plt.clf(); plt.subplots(2, 1); plt.subplot(1, 1); plt.plot(y, yaxis = 'right'); plt.plotsize(100, 27); plt.subplot(2, 1); plt.hist(y, color = 'indigo'); plt.plotsize(100, 27); plt.show()"


### Stream
python3 -m plotext "print('\npress for next text'); input()"
python3 -m plotext "import plotext as plt; import numpy as np; l, n = 1000, 2; x = np.arange(0, l); xticks = np.linspace(0, l - 1, 5); xlabels = [str(i) + 'pi' for i in range(5)]; frames = 100; plt.clf(); plt.ylim(-1, 1); plt.xticks(xticks, xlabels); plt.yticks([-1, 0, 1]); plt.plotsize(100, 30); plt.title('Streaming Data'); plt.colorless();  y = lambda i: plt.sin(l, n, 0, phase = i  / 100); [(plt.cld(), plt.clt(), plt.scatter(x, y(i), marker = 'dot'), plt.sleep(0.01), plt.show()) for i in range(frames)]"
