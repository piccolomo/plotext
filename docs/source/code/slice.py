import plotext as plt

matrix = plt.matrix(11, 3, plt.pixel())

matrix.insert(0, 0, "First Line")
matrix.insert(0, 1, "Second Line")
matrix.insert(0, 2, "Third Line")

print(matrix)
