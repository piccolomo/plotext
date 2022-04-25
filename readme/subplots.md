[Plotext Guide](https://github.com/piccolomo/plotext#guide)


# Multiple Subplots

To plot a grid of subplots, use the following main functions:

- `plt.subplots()` to creates a matrix of subplots with the given number of rows and columns.

- `plt.subplot()` to access the subplot at the given row and column, counting (from 1) from the upper left corner of the matrix of plots. 
    
   - Most of the commands referring to the active subplot, could be alternatively passed directly. Eg: subplot(1, 3); plotsize(100, 30) becomes subplot(1, 3).plotsize(300, 30).
    
   - Each subplot could creates its own matrix of subplots. Eg: subplots(2, 2); subplot(1, 1); subplots(3, 4) or directly subplots(2, 2).subplot(1, 1).subplots(3, 4) which will create a 2 by 2 matrix where the first subplot is a 3 by 4 matrix
   
   - If the active figure contains further subplots, any plotting or settings functions will apply to any of is subplots as well. This is useful to avoid rewriting the same code for each subplot. 

- `main()` returns the main figure at the uppermost level, and sets the active figure to it. Any further commands will refer to the entire figure and to any of its subplots.

- `plot_size()` to set the plot size - width and height - of the active subplot (in units of character size). 

- If the plot is part of a matrix of subplots, the final widths/heights will be the same for each column/row: by default the maximum is taken, use `take_min()` to take the minimum instead.

Here is a coded example, which requires the package `yfinance`.

```python
import plotext as plt
import random
import yfinance as yf

plt.date_form('d/m/Y')
start = plt.string_to_datetime("15/03/2022")
end = plt.today_datetime()
data = yf.download('goog', start, end)
dates = plt.datetimes_to_string(data.index)
p = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
mp = [14, 36, 11, 8, 7, 4]
fp = [12, 20, 35, 15, 2, 1]
hd1 = [random.gauss(1, 1) for el in range(3 * 10 ** 5)]
hd2 = [random.gauss(4, 1) for el in range(2 * 10 ** 5)]

plt.clf()
plt.subplots(1, 2)
plt.subplot(1, 1).plotsize(plt.tw() // 2, None)
plt.subplot(1, 1).subplots(3, 1)
plt.subplot(1, 2).subplots(2, 1)
plt.subplot(1, 1).ticks_style('bold')
plt.subplot(1, 2).theme('elegant')

plt.subplot(1, 1).subplot(1, 1)
plt.candlestick(dates, data)
plt.title("Google Stock Price CandleSticks")

plt.subplot(1, 1).subplot(2, 1)
plt.stacked_bar(p, [mp, fp], label = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")

plt.subplot(1, 1).subplot(3, 1)
bins = 18
plt.hist(hd1, bins, label="mean 1", marker = 'fhd')
plt.yfrequency(0)
plt.title('Histogram Plot')

plt.subplot(1, 2).subplot(1, 1)
plt.plot(plt.sin(periods = 3), marker = "fhd", label = "3 periods")
plt.plot(plt.sin(periods = 2), marker = "fhd", label = "2 periods")
plt.plot(plt.sin(periods = 1), marker = "fhd", label = "1 periods")

plt.subplot(1, 2).subplot(2, 1)
plt.plotsize(2 * plt.tw() // 3, plt.th() // 2)
plt.image_plot(plt.test_image_path)
plt.title('Creation of Michelangelo')

plt.show()
```
or directly on terminal:
```console
python3 -c "import plotext as plt; import random; import yfinance as yf; plt.date_form('d/m/Y'); start = plt.string_to_datetime('15/03/2022'); end = plt.today_datetime(); data = yf.download('goog', start, end); dates = plt.datetimes_to_string(data.index); p = ['Sausage', 'Pepperoni', 'Mushrooms', 'Cheese', 'Chicken', 'Beef']; mp = [14, 36, 11, 8, 7, 4]; fp = [12, 20, 35, 15, 2, 1]; hd1 = [random.gauss(1, 1) for el in range(3 * 10 ** 5)]; hd2 = [random.gauss(4, 1) for el in range(2 * 10 ** 5)]; plt.clf(); plt.subplots(1, 2); plt.subplot(1, 1).plotsize(plt.tw() // 2, None); plt.subplot(1, 1).subplots(3, 1); plt.subplot(1, 2).subplots(2, 1); plt.subplot(1, 1).ticks_style('bold'); plt.subplot(1, 2).theme('elegant'); plt.subplot(1, 1).subplot(1, 1); plt.candlestick(dates, data); plt.title('Google Stock Price CandleSticks'); plt.subplot(1, 1).subplot(2, 1); plt.stacked_bar(p, [mp, fp], label = ['men', 'women']); plt.title('Most Favored Pizzas in the World by Gender'); plt.subplot(1, 1).subplot(3, 1); bins = 18; plt.hist(hd1, bins, label='mean 1', marker = 'fhd'); plt.yfrequency(0); plt.title('Histogram Plot'); plt.subplot(1, 2).subplot(1, 1); plt.plot(plt.sin(periods = 3), marker = 'fhd', label = '3 periods'); plt.plot(plt.sin(periods = 2), marker = 'fhd', label = '2 periods'); plt.plot(plt.sin(periods = 1), marker = 'fhd', label = '1 periods'); plt.subplot(1, 2).subplot(2, 1); plt.plotsize(2 * plt.tw() // 3, plt.th() // 2); plt.image_plot(plt.test_image_path); plt.title('Creation of Michelangelo'); plt.show()"
```
![example](https://raw.githubusercontent.com/piccolomo/plotext/master/images/subplots.png)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)