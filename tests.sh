#!/bin/bash
#choice of yes or no
fork(){
while true;
do
    #read -n 1 -r -p  "y/n? " response   
    read -n 1 -r -p "? " response  
    echo -e ""
    if [[ $response =~ ^([yY])$ ]]
    then
	out=1
      	break
    elif [[ $response =~ ^([nN][oO]|[nN])$ ]]
    then
	out=0
	break
    fi
done
}

echo -en "Command Line Tool: Scatter Plot"
fork
if test $out -eq 1
then
    plotext scatter --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Scatter Plot Test" --marker braille 
fi


echo -en "Command line: Line Plot"
fork
if test $out -eq 1
then
    plotext plot --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 2500 --color magenta+ --title "Line Plot Test" 
fi

echo -en "Command Line Tool: Plotter"
fork
if test $out -eq 1
then
    plotext plotter --path test --xcolumn 1 --ycolumns 2 --sleep 0.1 --lines 120 --marker hd --title "Plotter Test" 
fi

echo -en "Command Line Tool: Bar Plot"
fork
if test $out -eq 1
then
    plotext bar --path test --xcolumn 1 --title "Bar Plot Test" --xlabel Animals --ylabel Count 
fi

echo -en "Command Line Tool: Histogram Plot"
fork
if test $out -eq 1
then
    plotext hist --path test --xcolumn 1 --ycolumns 2 --lines 5000 --title "Histogram Test" 
fi

echo -en "Command Line Tool: Image Plot"
fork
if test $out -eq 1
then
    plotext image --path test 
fi

echo -en "Command Line Tool: GIF Plot"
fork
if test $out -eq 1
then
    plotext gif --path test 
fi

echo -en "Command Line Tool: Video Plot"
fork
if test $out -eq 1
then
    plotext video --path test --from_youtube True 
fi

echo -en "Command Line Tool: YouTube Plot"
fork
if test $out -eq 1
then
    plotext youtube --url test
fi

echo -en "Scatter"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Scatter Plot'); plt.show()"
fi

echo -en "Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y = plt.sin(); plt.plot(y); plt.title('Line Plot'); plt.show()"
fi

echo -en "Stem Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y = plt.sin(length = 100); plt.plot(y, fillx = True); plt.title('Stem Plot'); plt.show()"
fi

echo -en "Multiple Data Set"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(phase = -1); plt.plot(y1, label = 'plot'); plt.scatter(y2, label = 'scatter'); plt.title('Multiple Data Set'); plt.show()"
fi

echo -en "Multiple Axes Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y1 = plt.sin(); y2 = plt.sin(2, phase = -1); plt.plot(y1, xside= 'lower', yside = 'left', label = 'lower left'); plt.plot(y2, xside= 'upper', yside = 'right', label = 'upper right'); plt.title('Multiple Axes Plot'); plt.show()"
fi

echo -en "Logarithmic Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; l = 10 ** 4; y = plt.sin(periods = 2, length = l); plt.plot(y); plt.xscale('log'); plt.yscale('linear'); plt.grid(0, 1); plt.title('Logarithmic Plot'); plt.xlabel('logarithmic scale'); plt.ylabel('linear scale'); plt.show();"
fi

echo -en "Streaming Data"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; l = 1000; frames = 200; plt.title('Streaming Data'); [(plt.cld(), plt.clt(), plt.plot(plt.sin(periods = 2, length = l, phase = 2 * i / frames)), plt.sleep(0.00), plt.show()) for i in range(frames)]"
fi

echo -en "Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Most Favored Pizzas in the World'); plt.show()"
fi

echo -en "Horizontal Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages, orientation = 'h', width = 3 / 5); plt.title('Most Favored Pizzas in the World'); plt.show()"
fi

echo -en "Simple Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.simple_bar(pizzas, percentages, width = 100, title = 'Most Favored Pizzas in the World'); plt.show()"
fi

echo -en "Multiple Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.multiple_bar(pizzas, [male_percentages, female_percentages], labels = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
fi

echo -en "Simple Multiple Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.simple_multiple_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender'); plt.show()"
fi

echo -en "Stacked Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.stacked_bar(pizzas, [male_percentages, female_percentages], labels = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.show()"
fi

echo -en "Simple Stacked Bar Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; male_percentages = [14, 36, 11, 8, 7, 4]; female_percentages = [12, 20, 35, 15, 2, 1]; plt.simple_stacked_bar(pizzas, [male_percentages, female_percentages], width = 100, labels = ['men', 'women'], title = 'Most Favored Pizzas in the World by Gender'); plt.show()"
fi

echo -en "Histogram Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; import random; l = 7 * 10 ** 4; data1 = [random.gauss(0, 1) for el in range(10 * l)]; data2 = [random.gauss(3, 1) for el in range(6 * l)]; data3 = [random.gauss(6, 1) for el in range(4 * l)]; bins = 60; plt.hist(data1, bins, label='mean 0'); plt.hist(data2, bins, label='mean 3'); plt.hist(data3, bins, label='mean 6'); plt.title('Histogram Plot'); plt.show()"
fi

echo -en "Datetime Plot"
fork
if test $out -eq 1
then
    python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/04/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); prices = list(data['Close']); dates = plt.datetimes_to_strings(data.index); plt.plot(dates, prices); plt.title('Google Stock Price'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
fi

echo -en "Candlestick Plot"
fork
if test $out -eq 1
then
    python3 -c "import yfinance as yf; import plotext as plt; plt.date_form('d/m/Y'); start = plt.string_to_datetime('11/04/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_strings(data.index); plt.candlestick(dates, data); plt.title('Google Stock Price Candlesticks'); plt.xlabel('Date'); plt.ylabel('Stock Price $'); plt.show()"
fi


echo -en "Box Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; labels = ['apple', 'orange', 'banana', 'pear']; weights = [[1,2,3,5,10,8], [4,9,6,12,20,13], [1,2,3,4,5,6], [3,9,12,16,9,8,3,7,2]]; plt.box(labels, weights, width = 0.3); plt.title('The Weight of the Fruits'); plt.show();"
fi

echo -en "Error Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.clf(); from random import random; l = 20; n = 1; ye = [random() * n for i in range(l)]; xe = [random() * n for i in range(l)]; y = plt.sin(length = l); plt.error(y, xerr = xe, yerr = ye); plt.title('Error Plot'); plt.show();"
fi

echo -en "Event Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; from random import randint; from datetime import datetime, timedelta; plt.date_form('H:M'); times = [datetime(2022, 3, 27, randint(0, 23), randint(0, 59), randint(0, 59)) for i in range(100)]; times = plt.datetimes_to_strings(times); plt.plotsize(None, 20); plt.eventplot(times); plt.show()"
fi

echo -en "Extra Lines"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; y = plt.sin(); plt.scatter(y); plt.title('Extra Lines'); plt.vline(100, 'magenta'); plt.hline(0.5, 'blue+'); plt.plotsize(100, 30); plt.show()"
fi

echo -en "Text Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; pizzas = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; percentages = [14, 36, 11, 8, 7, 4]; plt.bar(pizzas, percentages); plt.title('Labelled Bar Plot using Text()'); [plt.text(pizzas[i], i + 1, y = percentages[i] + 1.5, alignment = 'center', color = 'red') for i in range(len(pizzas))]; plt.ylim(0, 38); plt.plotsize(100, 30); plt.show()"
fi

echo -en "Shapes"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.clf(); plt.title('Shapes'); plt.polygon(); plt.rectangle(); plt.polygon(sides = 100); plt.show()"
fi

echo -en "Indicator"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.indicator(45.3, 'Price'); plt.plotsize(30, 10); plt.show()"
fi

    
echo -en "Settings Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; l, p = 300, 2; plt.plot(plt.sin(length = l, periods = p), label = 'My Signal'); plt.plotsize(100, 30); plt.title('Some Smart Title'); plt.xlabel('Time'); plt.ylabel('Movement'); plt.ticks_color('red'); plt.ticks_style('bold'); plt.xlim(-l//10, l + l//10); plt.ylim(-1.5, 1.5); xticks = [l * i / (2 * p) for i in range(2 * p + 1)]; xlabels = [str(i) + 'π' for i in range(2 * p + 1)]; plt.xticks(xticks, xlabels); plt.yfrequency(5); plt.show()"
fi


echo -en "Matrix Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; cols, rows = 200, 45; p = 1; matrix = [[(abs(r - rows / 2) + abs(c - cols / 2)) ** p for c in range(cols)] for r in range(rows)]; plt.matrix_plot(matrix); plt.plotsize(cols, rows); plt.title('Matrix Plot'); plt.show()"
fi

echo -en "Confusion Matrix"
fork
if test $out -eq 1
then
python3 -c "import plotext as plt; from random import randrange; l = 300; actual = [randrange(0, 4) for i in range(l)]; predicted = [randrange(0,4) for i in range(l)]; labels = ['Autumn', 'Spring', 'Summer', 'Winter']; plt.cmatrix(actual, predicted, labels); plt.show()"
fi

echo -en "Image Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; path = 'cat.jpg'; plt.download(plt.test_image_url, path); plt.image_plot(path); plt.title('A very Cute Cat'); plt.show(); plt.delete_file(path)"
fi

echo -en "GIF plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; path = 'homer.gif'; plt.download(plt.test_gif_url, path); plt.play_gif(path); plt.show(); plt.delete_file(path)"
fi

echo -en "Video Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; path = 'moonwalk.mp4'; plt.download(plt.test_video_url, path); plt.play_video(path, from_youtube = True); plt.delete_file(path)"
fi

echo -en "YouTube Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.play_youtube(plt.test_youtube_url)"
fi

echo -en "Subplots"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; import random; import yfinance as yf; plt.date_form('d/m/Y'); start = plt.string_to_datetime('28/03/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_strings(data.index); p = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; mp = [14, 36, 11, 8, 7, 4]; fp = [12, 20, 35, 15, 2, 1]; hd = [random.gauss(1, 1) for el in range(3 * 10 ** 5)]; path = 'cat.jpg'; plt.download(plt.test_image_url, path); plt.clf(); plt.subplots(1, 2); plt.subplot(1, 1).plotsize(plt.tw() // 2, None); plt.subplot(1, 1).subplots(3, 1); plt.subplot(1, 2).subplots(2, 1); plt.subplot(1, 1).ticks_style('bold'); plt.subplot(1, 1).subplot(1, 1); plt.theme('windows'); plt.candlestick(dates, data); plt.title('Google Stock Price CandleSticks'); plt.subplot(1, 1).subplot(2, 1); plt.theme('dreamland'); plt.stacked_bar(p, [mp, fp], labels = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.subplot(1, 1).subplot(3, 1); plt.theme('matrix'); bins = 18; plt.hist(hd, bins, label = 'Gaussian Noise Distribution', marker = 'fhd'); plt.yfrequency(0); plt.title('Histogram Plot'); plt.subplot(1, 2).subplot(1, 1).title('Default Theme'); plt.plot(plt.sin(periods = 3), marker = 'fhd', label = '3 periods'); plt.plot(plt.sin(periods = 2), marker = 'fhd', label = '2 periods'); plt.plot(plt.sin(periods = 1), marker = 'fhd', label = '1 period'); plt.subplot(1, 2).subplot(2, 1); plt.plotsize(2 * plt.tw() // 3, plt.th() // 2); plt.image_plot(path); plt.title('A very Cute Cat'); plt.show(); plt.delete_file(path);"
fi

echo -en "Test Plot"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.test()"
fi

echo -en "Markers"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.markers()"
fi

echo -en "Colors"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.colors()"
fi

echo -en "Styles"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.styles()"
fi

echo -en "Themes"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.themes()"
fi


echo -en "Extreme Cases"
fork
if test $out -eq 1
then
    python3 -c "import plotext as plt; plt.clf(); plt.subplots(5, 5); plt.subplot(1,1); plt.scatter(); plt.title('scatter()'); plt.subplot(1, 2); plt.scatter([]); plt.title('scatter([])'); plt.subplot(1, 3); plt.plot(); plt.title('plot()'); plt.subplot(1,4); plt.scatter([]); plt.title('scatter([])'); plt.subplot(1, 5); plt.candlestick([], []); plt.title('candlestick([], [])');
plt.subplot(2, 1); plt.bar(); plt.title('bar()'); plt.subplot(2, 2); plt.bar([]); plt.title('bar([])'); plt.subplot(2, 3); plt.bar([],[]); plt.title('bar([],[])'); plt.subplot(2, 4); plt.bar([0, 1]); plt.title('bar([0, 1])'); plt.subplot(2, 5); plt.bar([0,0]); plt.title('bar([0,0])'); plt.subplot(3, 1); plt.multiple_bar(); plt.title('multiple_bar()'); plt.subplot(3, 2); plt.multiple_bar([]); plt.title('multiple_bar([])'); plt.subplot(3, 3); plt.multiple_bar([], []); plt.title('multiple_bar([], [])');
plt.subplot(3, 4); plt.multiple_bar([[0,1],[0,1]]); plt.title('multiple_bar([[0,1],[0,1]])'); plt.subplot(3, 5); plt.multiple_bar([[0,0],[0,0]]); plt.title('multiple_bar([[0,0],[0,0]])'); plt.subplot(4, 1); plt.hist([]); plt.title('hist([])'); plt.subplot(4, 2); plt.error(); plt.title('error()'); plt.subplot(4, 3); plt.error([]); plt.title('error([])'); plt.subplot(4, 4); plt.event_plot([]); plt.title('event_plot([])'); plt.subplot(4, 5); plt.vline(0); plt.title('vline(0)'); plt.subplot(5, 1); plt.text('ciao bello!', 0, 0); plt.title('text(..., 0, 0)'); plt.subplot(5, 2); plt.rectangle(); plt.title('rectangle()'); plt.subplot(5, 3); plt.rectangle([], []); plt.title('rectangle([], [])'); plt.subplot(5, 4); plt.polygon(); plt.title('polygon()'); plt.subplot(5, 5); plt.matrix_plot([[]]); plt.title('matrix_plot([[]])'); plt.show()"
fi

