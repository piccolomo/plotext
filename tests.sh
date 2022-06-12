plotext scatter --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Scatter Plot Test"

read -p ""
plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 230 --clear_terminal True --color magenta+ --title "Plot Test"

read -p ""
plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 2500 --clear_terminal True --marker braille --title "Plotter Test"

read -p ""
plotext bar --path test --xcolumn 1 --title "Bar Plot Test" --xlabel "Animals" --ylabel "Count"

read -p ""
plotext hist --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Histogram Test"

read -p ""
plotext image --path test

read -p ""
plotext gif --path test

read -p ""
plotext video --path test --from_youtube True

read -p ""
plotext youtube --url test

read -p ""
python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"

read -p ""
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"

read -p ""
python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y, fillx = True); plt.title('Stem Plot'); plt.show()"

python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(phase = -1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter'); plt.title('Multiple Data Set'); plt.show()"

python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside= 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside= 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"

python3 -c "import plotext as plt; l = 10 ** 4; y = plt.sin(periods = 2, length = l); plt.plot(y); plt.xscale('log'); plt.yscale('linear'); plt.grid(0, 1); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show();"


python3 -c "import plotext as plt; l = 1000; frames = 200; plt.title('Streaming Data'); [(plt.cld(), plt.clt(), plt.plot(plt.sin(periods = 2, length = l, phase = 2 * i  / frames)), plt.sleep(0), plt.show()) for i in range(frames)]"

python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Most Favored Pizzas in the World'); plt.show()"


python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 3 / 5); plt.title('Most Favored Pizzas in the World'); plt.show()"


python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 0.3, marker = 'fhd'); plt.title('Most Favoured Pizzas in the World'); plt.clc(); plt.plotsize(100, 2 * len(pizzas) + 4); plt.show()"

python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"

python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.stacked_bar(pizzas, [male_percentages, female_percentages], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"


python3 -c "import plotext as plt; import random; l = 7 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)];  data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.show()"

python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/07/2020'); end = plt.today_datetime(); data = yf.download('goog', start, end); prices = list(data['Close']); dates = plt.datetimes_to_string(data.index); plt.plot(dates, prices); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"


python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('01/02/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_string(data.index); plt.candlestick(dates, data); plt.title('Google Stock Price Candlesticks'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"


python3 -c "import plotext as plt; from random import randint; from datetime import datetime, timedelta; plt.date_form('H:M'); times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)]; times = plt.datetimes_to_string(times); plt.plotsize(None, 20); plt.eventplot(times); plt.show()"

python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Extra Lines'); plt.vline(100, 'magenta'); plt.hline(0.5, 'blue+'); plt.plotsize(100, 30); plt.show()"


python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Labelled Bar Plot using Text()'); [plt.text(pizzas[i], x = pizzas[i], y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]; plt.ylim(0, 38); plt.plotsize(100, 30); plt.show()"


python3 -c "import plotext as plt; cols, rows = 200, 45; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.show()"


python3 -c "import plotext as plt; path = 'cat.jpg'; plt.download(plt.test_image_url, path); plt.image_plot(path); plt.title('A very Cute Cat'); plt.show(); plt.delete_file(path)"

python3 -c "import plotext as plt; path = 'homer.gif'; plt.download(plt.test_gif_url, path); plt.play_gif(path); plt.show(); plt.delete_file(path)"


python3 -c "import plotext as plt; path = 'moonwalk.mp4'; plt.download(plt.test_video_url, path); plt.play_video(path, from_youtube = True); plt.delete_file(path)"


python3 -c "import plotext as plt; plt.play_youtube(plt.test_youtube_url)"

python3 -c "import plotext as plt; l, p = 300, 2; plt.plot(plt.sin(length = l, periods = p), label = 'My Signal'); plt.plotsize(100, 30); plt.title('Some Smart Title'); plt.xlabel('Time'); plt.ylabel('Movement'); plt.ticks_color('red'); plt.ticks_style('bold'); plt.xlim(-l//10, l + l//10); plt.ylim(-1.5, 1.5); xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.yfrequency(5); plt.show()"

python3 -c "import plotext as plt; import random; import yfinance as yf; plt.date_form('d/m/Y'); start = plt.string_to_datetime('28/03/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_string(data.index); p = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; mp = [14, 36, 11, 8, 7, 4]; fp = [12, 20, 35, 15, 2, 1]; hd = [random.gauss(1, 1) for el in range(3 * 10 ** 5)]; path = 'cat.jpg'; plt.download(plt.test_image_url, path); plt.clf(); plt.subplots(1, 2); plt.subplot(1, 1).plotsize(plt.tw() // 2, None); plt.subplot(1, 1).subplots(3, 1); plt.subplot(1, 2).subplots(2, 1); plt.subplot(1, 1).ticks_style('bold'); plt.subplot(1, 1).subplot(1, 1); plt.theme('windows'); plt.candlestick(dates, data); plt.title('Google Stock Price CandleSticks'); plt.subplot(1, 1).subplot(2, 1); plt.theme('dreamland'); plt.stacked_bar(p, [mp, fp], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.subplot(1, 1).subplot(3, 1); plt.theme('matrix'); bins = 18; plt.hist(hd, bins, label = 'Gaussian Noise Distribution', marker = 'fhd'); plt.yfrequency(0); plt.title('Histogram Plot'); plt.subplot(1, 2).subplot(1, 1).title('Default Theme'); plt.plot(plt.sin(periods = 3), marker = 'fhd', label = '3 periods'); plt.plot(plt.sin(periods = 2), marker = 'fhd', label = '2 periods'); plt.plot(plt.sin(periods = 1), marker = 'fhd', label = '1 period'); plt.subplot(1, 2).subplot(2, 1); plt.plotsize(2 * plt.tw() // 3, plt.th() // 2); plt.image_plot(path); plt.title('A very Cute Cat'); plt.show(); plt.delete_file(path);"


python 3 -c "import plotext as plt; plt.markers()"

python 3 -c "import plotext as plt; plt.colors()"

python 3 -c "import plotext as plt; plt.styles()"

python 3 -c "import plotext as plt; plt.themes()"



