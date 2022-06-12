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
