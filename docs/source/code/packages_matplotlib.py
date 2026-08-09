import matplotlib.pyplot as mpl
import plotext as plt

y = plt.sin()
y_down = [-value for value in y]
x = range(len(y))

mpl.clf()
mpl.subplot(211)
mpl.plot(x, y, color = 'red', label = 'up')
mpl.plot(x, y_down, color = 'green', label = 'down')
mpl.legend()
mpl.title('Some Smart Title')
mpl.xlabel('here is a label')

mpl.subplot(212)
mpl.scatter(x[::10], y[::10], color = 'blue', label = 'sampled')
mpl.bar([40, 100, 160], [0.4, 0.8, 0.6], width = 20, color = 'orange', label = 'bars')
mpl.legend()
mpl.ylabel('the y axis')

fig = plt.matplotlib(mpl.gcf())
fig.plot_size(120, 45)
fig.legend()
fig.show()
