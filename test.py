import plotext as plt

w = 15
m = plt.matrix(w, 5)
mi = plt.colorize("ciao", "red").get_matrix()
m2 = plt.colorize("ciao", "green")

[m.insert(i, 0, str(i)[-1]) for i in range(w)]

b1 = m.insert(w - 1, 1, mi, 1)

b2 = m._insert_colorize_dynamically(11, 1, m2)

b3 = m._insert_colorize(8, 1, plt.colorize("ciao", "blue+"), -1, 1)

m.print()

