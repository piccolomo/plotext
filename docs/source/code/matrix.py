import plotext as plt

m = plt.matrix(23, 9)
m1 = plt.matrix(10, 5, plt.pixel(background = 'red+'))
m2 = plt.colorize("some text", "magenta", "gray+", "bold")

m.insert(1, 1, m1)
m.insert(21, 1, m2, ha = "right")
m.insert(21, 3, "raw text", ha = "right")
m.insert(1, 7, m2)

m.print()